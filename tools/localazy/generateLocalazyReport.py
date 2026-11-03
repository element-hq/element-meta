#!/usr/bin/env python3

# Copyright (c) 2026 Element Creations Ltd.
#
# SPDX-License-Identifier: AGPL-3.0-only OR LicenseRef-Element-Commercial.
# Please see LICENSE files in the repository root for full details.

# Generate a Markdown report of the Localazy strings which are not used by Element X Android and/or by Element X iOS.
# The latest develop branch of the Element X Android and Element X iOS projects is cloned (or updated) in the build/repos folder,
# with its full history, to know when each string was added.
# Requires git, and the Localazy CLI to get the actual Localazy keys.
# Usage: ./tools/localazy/generateLocalazyReport.py [--output tools/localazy/LocalazyReport.md]

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

META_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPOS_DIR = os.path.join(META_ROOT, "build", "repos")
DEFAULT_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LocalazyReport.md")
BRANCH = "develop"
RECENT_DAYS = 90
LOCALAZY_READ_KEY = "a7876306080832595063-aa37154bb3772f6146890fca868d155b2228b492c56c91f67abdcdfb74d6142d"
PLURAL_QUANTITIES = ("zero", "one", "two", "few", "many", "other")
IOS_LOCALIZATIONS = "ElementX/Resources/Localizations/en.lproj"
IOS_GENERATED_STRINGS = "ElementX/Sources/Generated/Strings.swift"
IOS_SKIPPED_ROOT_DIRS = ("UnitTests", "UITests", "PreviewTests", "IntegrationTests", "AccessibilityTests")


# Clone the latest develop branch of the element-hq project in the build/repos folder, or update it if already cloned,
# and return its path. The full history is needed to know when each string was added (see getKeyAddedDates()).
# LFS files are not downloaded, they are not needed.
def checkoutProject(name):
    path = os.path.join(REPOS_DIR, name)
    env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1")
    if os.path.isdir(os.path.join(path, ".git")):
        print(f"Updating {name}…", file=sys.stderr)
        isShallow = subprocess.check_output(["git", "-C", path, "rev-parse", "--is-shallow-repository"], text=True).strip() == "true"
        unshallow = ["--unshallow"] if isShallow else []
        subprocess.run(["git", "-C", path, "fetch", "--quiet", *unshallow, "origin", BRANCH], check=True, env=env)
        subprocess.run(["git", "-C", path, "reset", "--quiet", "--hard", "FETCH_HEAD"], check=True, env=env)
        subprocess.run(["git", "-C", path, "clean", "-fdx", "--quiet"], check=True, env=env)
    else:
        print(f"Cloning {name}…", file=sys.stderr)
        subprocess.run([
            "git", "clone", "--quiet", "--branch", BRANCH, "--single-branch",
            f"https://github.com/element-hq/{name}.git", path,
        ], check=True, env=env)
    return path


# Yield the paths of the files under root with one of the given extensions, ignoring hidden and build folders,
# and the folders for which isSkipped(path relative to root) returns True.
def walk(root, extensions, isSkipped):
    for directory, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "build"]
        if isSkipped(os.path.relpath(directory, root)):
            continue
        for file in files:
            if file.endswith(extensions):
                yield os.path.join(directory, file)


# Return the set of words and the set of string literals found in the files.
# Example: the line `Text(stringResource(CommonStrings.action_copy), tag = "a11y.copy")`
# gives the words {"Text", "stringResource", "CommonStrings", "action_copy", "tag", "a11y", "copy"}
# and the literals {"a11y.copy"}.
def readWords(files):
    words = set()
    literals = set()
    for path in files:
        with open(path, encoding="utf-8", errors="ignore") as f:
            content = f.read()
        words.update(re.findall(r"\w+", content))
        literals.update(re.findall(r'"([\w.]+)"', content))
    return words, literals


# Return a dict of the English Android strings, from all the `src/main/res/values/localazy.xml` files.
# Example:
#   <string name="action_copy">"Copy"</string>
#   <plurals name="common_member_count">
#     <item quantity="one">"%1$d member"</item>
#     <item quantity="other">"%1$d members"</item>
#   </plurals>
# gives {"action_copy": "\"Copy\"", "common_member_count": "\"%1$d members\""}.
# For plurals, the "other" form is used.
def getAndroidStrings(androidRoot):
    result = {}
    for directory, dirs, files in os.walk(androidRoot):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "build"]
        if directory.endswith("/src/main/res/values") and "localazy.xml" in files:
            for element in ET.parse(os.path.join(directory, "localazy.xml")).getroot():
                name = element.get("name")
                if element.tag == "string":
                    result[name] = "".join(element.itertext())
                elif element.tag == "plurals":
                    items = {item.get("quantity"): "".join(item.itertext()) for item in element}
                    result[name] = items.get("other") or next(iter(items.values()), "")
    return result


# Return a dict of the English iOS strings, from the files `Localizable.strings` and `Localizable.stringsdict`.
# Example: the line `"a11y.encryption_details" = "Encryption details";` of `Localizable.strings`
# gives {"a11y.encryption_details": "Encryption details"}. See getIosPluralValue() for `Localizable.stringsdict`.
def getIosStrings(iosRoot):
    result = {}
    localizations = os.path.join(iosRoot, IOS_LOCALIZATIONS)
    with open(os.path.join(localizations, "Localizable.strings"), encoding="utf-8") as f:
        for match in re.finditer(r'^"((?:[^"\\]|\\.)+)"\s*=\s*"((?:[^"\\]|\\.)*)";', f.read(), re.M):
            result[match.group(1)] = match.group(2)
    children = list(ET.parse(os.path.join(localizations, "Localizable.stringsdict")).getroot().find("dict"))
    for i in range(0, len(children), 2):
        result.setdefault(children[i].text, getIosPluralValue(children[i + 1]))
    return result


# Return the "other" form of a plural from `Localizable.stringsdict`, ignoring the `NSString*` entries.
# Example: for the key `a11y_digits_entered`, element is:
#   <dict>
#     <key>COUNT</key>
#     <dict>
#       <key>NSStringFormatSpecTypeKey</key>
#       <string>NSStringPluralRuleType</string>
#       <key>NSStringFormatValueTypeKey</key>
#       <string>d</string>
#       <key>one</key>
#       <string>%1$d digit entered</string>
#       <key>other</key>
#       <string>%1$d digits entered</string>
#     </dict>
#     <key>NSStringLocalizedFormatKey</key>
#     <string>%#@COUNT@</string>
#   </dict>
# and the result is "%1$d digits entered".
def getIosPluralValue(element):
    for variable in element.findall("dict"):
        entries = list(variable)
        forms = {entries[j].text: entries[j + 1].text for j in range(0, len(entries) - 1, 2) if entries[j].tag == "key"}
        forms = {quantity: value for quantity, value in forms.items() if not quantity.startswith("NSString")}
        if forms:
            return forms.get("other") or next(iter(forms.values()), "")
    return ""


# Return a dict mapping each iOS key to its SwiftGen accessor, from the generated file `Strings.swift`.
# Example: the lines
#   internal static var actionCopy: String { return L10n.tr("Localizable", "action_copy") }
#   internal static func a11yDigitsEntered(_ p1: Int) -> String {
#     return L10n.tr("Localizable", "a11y_digits_entered", p1)
# give {"action_copy": "actionCopy", "a11y_digits_entered": "a11yDigitsEntered"}.
def getIosAccessors(iosRoot):
    with open(os.path.join(iosRoot, IOS_GENERATED_STRINGS), encoding="utf-8") as f:
        content = f.read()
    result = {}
    for match in re.finditer(r'static (?:var|func) (\w+)[^\n]*?\n?[^\n]*?L10n\.tr\("Localizable", "([^"]+)"', content):
        result.setdefault(match.group(2), match.group(1))
    return result


# Return the set of words found in the Android production code (`.kt`, `.kts` and `.xml` files), excluding the
# string resource files, the test code and the tools folder. A key is used if it is in this set.
def getAndroidUsedWords(androidRoot):
    def isSkipped(path):
        return (
            re.search(r"(^|/)src/(test|androidTest)(/|$)", path) is not None
            or re.search(r"/res/values[^/]*$", path) is not None
            or path == "tools"
            or path.startswith("tools/")
        )

    words, _ = readWords(walk(androidRoot, (".kt", ".kts", ".xml"), isSkipped))
    return words


# Return the sets of words and of string literals found in the iOS production code (`.swift` files), excluding the
# generated code and the test code. A key is used if its accessor is in the words, or if the key is in the literals.
def getIosUsedWordsAndLiterals(iosRoot):
    def isSkipped(path):
        return path.split("/")[0] in IOS_SKIPPED_ROOT_DIRS or "Sources/Generated" in path

    return readWords(walk(iosRoot, (".swift",), isSkipped))


# Return a dict mapping each flattened key to the actual Localazy key, by downloading the English source strings.
# The keys are flattened with underscores by both platforms, but Localazy keys can contain dots.
# Example: the downloaded JSON
#   {"action": {"copy_link": "Copy link"}, "a11y.encryption_details": "Encryption details",
#    "a11y": {"digits_entered": {"one": "%1$d digit entered", "other": "%1$d digits entered"}}}
# gives {"action_copy_link": "action.copy_link", "a11y_encryption_details": "a11y.encryption_details",
#        "a11y_digits_entered": "a11y.digits_entered", "action": "action", "a11y": "a11y"}.
# The intermediate nodes are kept, because a key can also be the parent of other keys, e.g.
# `screen.custom_recovery_key.input.strength` and `screen.custom_recovery_key.input.strength.weak`,
# and in this case, the JSON only contains the children.
# Also return the set of the flattened keys of the plurals, e.g. {"a11y_digits_entered"}, since Localazy needs a `p:` prefix
# to find them.
# Return an empty dict and an empty set if the Localazy CLI is not available.
def getLocalazyKeys():
    result = {}
    plurals = set()

    def collect(node, path):
        if path:
            result.setdefault("_".join(path).replace(".", "_"), ".".join(path))
        isPlural = isinstance(node, dict) and node and all(quantity in PLURAL_QUANTITIES for quantity in node)
        if isPlural:
            plurals.add("_".join(path).replace(".", "_"))
        elif isinstance(node, dict):
            for key, value in node.items():
                collect(value, path + [key])

    with tempfile.TemporaryDirectory() as directory:
        with open(os.path.join(directory, "localazy.json"), "w") as f:
            json.dump({
                "readKey": LOCALAZY_READ_KEY,
                "download": {"files": [{"conditions": ["equals: ${languageCode}, en"], "output": "en_${file}"}]},
            }, f)
        try:
            subprocess.run(["localazy", "download"], cwd=directory, check=True, capture_output=True)
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"Warning: cannot download the keys from Localazy ({e}), the links may use wrong keys", file=sys.stderr)
            return result, plurals
        with open(os.path.join(directory, "en_content.json"), encoding="utf-8") as f:
            collect(json.load(f), [])
    return result, plurals


# Return a Markdown link to the current commit of the element-hq project cloned by checkoutProject(), on GitHub.
# Example: [`58dd508c`](https://github.com/element-hq/element-x-android/commit/58dd508c...).
def getCommitLink(repo):
    sha = subprocess.check_output(["git", "-C", repo, "rev-parse", "HEAD"], text=True).strip()
    shortSha = subprocess.check_output(["git", "-C", repo, "rev-parse", "--short", "HEAD"], text=True).strip()
    return f"[`{shortSha}`](https://github.com/element-hq/{os.path.basename(repo)}/commit/{sha})"


# Return a dict mapping each flattened key to the date (YYYY-MM-DD) of the first commit which added it to the files
# matching pathspecs, by going through the git history from the oldest commit. Only the keys in knownKeys are kept.
# Example: for Android, the diff line `+    <string name="action_copy">"Copy"</string>` of a commit of 2023-05-12,
# in any `localazy.xml` file, gives {"action_copy": "2023-05-12"}, even if the key was later moved to another module.
def getKeyAddedDates(repo, pathspecs, pattern, knownKeys):
    result = {}
    log = subprocess.run(
        ["git", "-C", repo, "log", "--reverse", "--format=commit %cs", "-p", "--no-color", "--", *pathspecs],
        check=True, capture_output=True, text=True, encoding="utf-8", errors="ignore",
    ).stdout
    date = None
    for line in log.splitlines():
        if line.startswith("commit "):
            date = line[len("commit "):]
        elif line.startswith("+"):
            match = re.match(pattern, line)
            if match:
                key = next(group for group in match.groups() if group)
                if key in knownKeys:
                    result.setdefault(key.replace(".", "_"), date)
    return result


# Format a string value so that it fits in a Markdown table cell: remove the surrounding quotes, replace the line breaks
# with spaces, escape the pipes, unescape the quotes and truncate to 120 characters.
# Example: `"Don\'t | stop\nnow"` gives `Don't \| stop now`.
def formatValue(value):
    value = (value or "").strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        value = value[1:-1]
    value = value.replace("\\n", " ").replace("\n", " ").replace("|", "\\|").strip()
    value = value.replace("\\\"", "\"").replace("\\'", "'")
    return value if len(value) <= 120 else value[:117] + "…"


# Find the keys unused on Android and/or on iOS, and write the Markdown report.
def main():
    parser = argparse.ArgumentParser(description="Generate a report of the Localazy strings unused by Element X Android and/or Element X iOS.")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Path to the generated Markdown file")
    args = parser.parse_args()
    androidRoot = checkoutProject("element-x-android")
    iosRoot = checkoutProject("element-x-ios")

    androidStrings = getAndroidStrings(androidRoot)
    iosStrings = getIosStrings(iosRoot)
    iosAccessors = getIosAccessors(iosRoot)
    androidWords = getAndroidUsedWords(androidRoot)
    iosWords, iosLiterals = getIosUsedWordsAndLiterals(iosRoot)
    localazyKeys, localazyPlurals = getLocalazyKeys()
    androidAddedDates = getKeyAddedDates(
        androidRoot, [":(glob)**/src/main/res/values/localazy.xml"],
        r'^\+\s*<(?:string|plurals) name="([^"]+)"', androidStrings,
    )
    iosAddedDates = getKeyAddedDates(
        iosRoot, [":(glob)**/en.lproj/Localizable.strings", ":(glob)**/en.lproj/Localizable.stringsdict"],
        r'^\+"((?:[^"\\]|\\.)+)"\s*=|^\+\s*<key>([^<]+)</key>', iosStrings,
    )

    missingAccessors = [key for key in iosStrings if key not in iosAccessors]
    if missingAccessors:
        print(f"Warning: {len(missingAccessors)} iOS keys without SwiftGen accessor, e.g. {missingAccessors[:5]}", file=sys.stderr)

    def isUsedOnIos(key):
        accessor = iosAccessors.get(key)
        return (accessor is not None and accessor in iosWords) or key in iosLiterals

    # iOS keeps nested Localazy keys dotted (a11y.foo), Android flattens them (a11y_foo)
    iosKeysByNormalizedKey = {key.replace(".", "_"): key for key in iosStrings}
    displayKeys = {key: key for key in androidStrings}
    displayKeys.update(iosKeysByNormalizedKey)
    allKeys = sorted(displayKeys)

    # Keys with a platform suffix are only imported by that platform, so they count as used on the other one
    def isUsedOnAndroidOrIgnored(key):
        return key.endswith("_ios") or (key in androidStrings and key in androidWords)

    def isUsedOnIosOrIgnored(key):
        return key.endswith("_android") or (key in iosKeysByNormalizedKey and isUsedOnIos(iosKeysByNormalizedKey[key]))

    def englishValue(key):
        return androidStrings[key] if key in androidStrings else iosStrings.get(displayKeys[key])

    # Short strings are generic enough to be reused in the future
    def isShort(key):
        return len(formatValue(englishValue(key)).split()) <= 3

    # The key was added to Localazy a bit before it was first synced to one of the projects
    def addedDate(key):
        dates = [d for d in (androidAddedDates.get(key), iosAddedDates.get(key)) if d]
        return min(dates) if dates else None

    recentLimit = (datetime.date.today() - datetime.timedelta(days=RECENT_DAYS)).isoformat()

    def isRecent(key):
        date = addedDate(key)
        return date is not None and date >= recentLimit

    unusedKeys = [key for key in allKeys if not isUsedOnAndroidOrIgnored(key) and not isUsedOnIosOrIgnored(key)]
    sections = [
        (
            "Unused strings",
            "Strings with more than 3 words, used neither by Element X Android nor by Element X iOS. "
            "They can probably be removed from Localazy, unless they are for a feature not merged yet.",
            [key for key in unusedKeys if not isShort(key)],
        ),
        (
            "Short unused strings",
            "Strings with at most 3 words, used neither by Element X Android nor by Element X iOS. "
            "They could be reused in the future, so check them before removing them from Localazy.",
            [key for key in unusedKeys if isShort(key)],
        ),
        (
            "Strings not used on Android",
            "Strings used by Element X iOS but not by Element X Android. Keys with the `_android` suffix can probably be removed. "
            "For the other keys, this can be a difference between the implementations of both projects, or a feature not implemented "
            "yet on Android. If the difference is expected, the key can be renamed with the `_ios` suffix.",
            [key for key in allKeys if isUsedOnIosOrIgnored(key) and not isUsedOnAndroidOrIgnored(key)],
        ),
        (
            "Strings not used on iOS",
            "Strings used by Element X Android but not by Element X iOS. Keys with the `_ios` suffix can probably be removed. "
            "For the other keys, this can be a difference between the implementations of both projects, or a feature not implemented "
            "yet on iOS. If the difference is expected, the key can be renamed with the `_android` suffix.",
            [key for key in allKeys if isUsedOnAndroidOrIgnored(key) and not isUsedOnIosOrIgnored(key)],
        ),
    ]

    def tableLines(keys):
        lines = ["| Key | English value | Added | Localazy |", "|---|---|---|---|"]
        # Keys with a platform suffix first, the sort is stable so the keys stay sorted in each group
        for key in sorted(keys, key=lambda k: not k.endswith(("_android", "_ios"))):
            displayKey = localazyKeys.get(key, displayKeys[key])
            added = (addedDate(key) or "?") + (" 🆕" if isRecent(key) else "")
            # Localazy only finds the plurals with the `p:` prefix
            searchKey = ("p:" if key in localazyPlurals else "") + displayKey
            lines.append(
                f"| `{displayKey}` | {formatValue(englishValue(key))} | {added} "
                f"| [link](https://localazy.com/p/element/source-language?search={searchKey}&searchOptions=KEY,EXACT_MATCH) |"
            )
        return lines

    lines = [
        "# Localazy report",
        "",
        f"Usage of the Localazy strings by Element X Android (`{BRANCH}` at {getCommitLink(androidRoot)}) "
        f"and Element X iOS (`{BRANCH}` at {getCommitLink(iosRoot)}), generated on {datetime.date.today().isoformat()}, "
        f"out of {len(allKeys)} keys found in the English string files of both projects:",
        "",
    ]
    lines += [f"- [{title}](#{title.lower().replace(' ', '-')}): **{len(keys)}** keys" for title, _, keys in sections]
    lines += [
        "",
        "How this was computed:",
        "- Android: a key counts as used when it appears as a word in production `.kt`, `.kts` or `.xml` files "
        "(excluding `res/values*/`, `src/test`, `src/androidTest` and `tools/`).",
        "- iOS: a key counts as used when its SwiftGen accessor (`L10n.xxx`) or the raw key literal appears in production `.swift` files "
        "(excluding `Sources/Generated`, `UnitTests`, `UITests`, `PreviewTests`, `IntegrationTests` and `AccessibilityTests`).",
        "- Keys with the `_android` suffix are not imported in the iOS project, and keys with the `_ios` suffix are not imported "
        "in the Android project, so they are only checked on their platform.",
        "",
        "Caveats: keys built dynamically at runtime are not detected, so check each key before you change it. "
        "A string used only in tests counts as unused. Only the `develop` branch of both projects is analysed, "
        "so a string added to Localazy for a feature not merged yet (still in a pull request or in a branch) counts as unused.",
        "",
        "The *Added* column is the date of the first commit adding the key to the English string files of either project, "
        f"which is close to the date the key was added to Localazy. 🆕 marks the keys added in the last {RECENT_DAYS} days, "
        "which may be used by a feature still in development.",
    ]
    for title, description, keys in sections:
        lines += ["", f"## {title}", "", f"{description} **{len(keys)}** keys.", ""]
        # The blank line after the summary is required by GitHub to render the Markdown table
        lines += ["<details>", f"<summary>Show the {len(keys)} keys</summary>", ""]
        lines += tableLines(keys)
        lines += ["", "</details>"]
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    counts = ", ".join(f"{len(keys)} {title[0].lower() + title[1:]}" for title, _, keys in sections)
    recentUnusedCount = sum(1 for key in unusedKeys if isRecent(key))
    print(f"{counts}, out of {len(allKeys)} keys ({recentUnusedCount} unused keys added in the last {RECENT_DAYS} days), "
          f"report written to {args.output}")

if __name__ == "__main__":
    main()
