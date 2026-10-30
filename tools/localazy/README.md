# Localazy report

[generateLocalazyReport.py](generateLocalazyReport.py) generates a Markdown report of the usage of the [Localazy](https://localazy.com/p/element) strings by [Element X Android](https://github.com/element-hq/element-x-android) and [Element X iOS](https://github.com/element-hq/element-x-ios), with a link to Localazy for each string. The report can be linked from a GitHub issue to track the work to do. It contains 3 sections:
- the strings used by neither project;
- the strings used by Element X iOS but not by Element X Android;
- the strings used by Element X Android but not by Element X iOS.

Keys with the `_android` suffix are not imported in the iOS project, and keys with the `_ios` suffix are not imported in the Android project, so they are only checked on their platform.

The script clones the latest `develop` branch of both projects in the `build/repos` folder of this repository (git ignored), or updates them if they are already there. The report is written to [LocalazyReport.md](LocalazyReport.md), next to the script, by default. It is committed so that it can be read on GitHub, since it is too large for a GitHub issue. To refresh it, run the script again and commit the result. It requires `git`, and the [Localazy CLI](https://localazy.com/docs/cli/installation) to get the actual Localazy keys. From the root of this repository, run:

```shell
./tools/localazy/generateLocalazyReport.py [--output tools/localazy/LocalazyReport.md]
```
