# Feature requests

This page explains how feature requests for the Element apps (Web/Desktop, Android and iOS) are
filed, how the product team answers them, and when it makes sense to write code.

The short version: **open an issue, wait for an answer, and only write a PR once the issue says we
want one.**

## Where to file

Element is one product on three platforms. Features are managed in a single place so they stay
consistent.

| What you want | Where |
| --- | --- |
| A new feature, or a change to how an existing feature behaves: anything a user would notice | [element-meta](https://github.com/element-hq/element-meta/issues/new?template=enhancement.yml) |
| Something that only makes sense on one platform: OS integration, platform UI conventions, that platform's accessibility APIs, that repository's build or CI | the app repository: [element-web](https://github.com/element-hq/element-web/issues/new/choose), [element-x-android](https://github.com/element-hq/element-x-android/issues/new/choose) or [element-x-ios](https://github.com/element-hq/element-x-ios/issues/new/choose) |
| A bug | the repository where it reproduces |
| An SDK API, protocol, performance or crypto concern | [matrix-rust-sdk](https://github.com/matrix-org/matrix-rust-sdk/issues) (Element X on Android and iOS) or [matrix-js-sdk](https://github.com/matrix-org/matrix-js-sdk/issues) (Element Web and Desktop) |
| Calls | [element-call](https://github.com/element-hq/element-call/issues) |
| The rich text composer | [matrix-rich-text-editor](https://github.com/element-hq/matrix-rich-text-editor/issues) |
| The sign-in, sign-up and account management pages opened by your homeserver | [matrix-authentication-service](https://github.com/element-hq/matrix-authentication-service/issues) |

**If you are not sure, open it in the app repository you use.** We will move it to element-meta if
it concerns other platforms too. The templates ask the same questions in the same order, so a moved
issue still reads as if it had been filed in the right place.

The SDK, calls, composer and authentication repositories are not on the triage board described
below: requests there are agreed with their maintainers and do not go through the process on this
page.

Please report security issues by email to security@element.io, not in a public issue. See the
[security disclosure policy](https://element.io/security/security-disclosure-policy).

## Who decides

Accepting a feature is a **product decision**, made by the Element product managers. It means the
feature fits the direction of the product, the design is agreed, and we want it.

The decision depends on the problem, so the templates start from the problem rather than the
solution: what you are trying to do, who has this problem, and how often.

## How we answer

Feature requests are triaged on the
[Feature Request Triage board](https://github.com/orgs/element-hq/projects/168). It collects open
issues labelled `T-Enhancement` (or `T-Feature`) from element-meta, element-web, element-x-android
and element-x-ios. **Every request gets an answer within a week.**

The answer is the issue's `Status` on the board. It is shown in the Projects panel of the issue
page:

```
Projects
  Feature Request Triage
    Status   🧪 Let's try
```

| Status | What it means | Should I write a PR? |
| --- | --- | --- |
| 📥 Untriaged | Nobody has looked at it yet. | Not yet. Wait for an answer. |
| ❓ Needs info | We need more from you before we can answer. | Not yet. |
| 💬 In discussion | Product, design or engineering is working out an answer. | Not yet. |
| 🚫 Don't do | It does not fit the direction of the product. The issue is closed as "not planned", with the reason in a comment. | No. |
| ⏸️ Maybe later | It does not fit now. We may reconsider it. No promise, no date. | No. If you disagree, say so on the issue and we can look at it again. |
| 🧪 Let's try | We are open to a PR and will evaluate it as a proof of concept. We may still decide not to ship it. | Yes, knowing the risk. See below. |
| ✅ Do it | We want this. The core team will support integrating a PR that meets our quality bar. | Yes. |
| 🏗️ Coming soon | The core team is working on it, or will start soon. | No. Please don't duplicate the work. |

Every answer is explained in a comment on the issue. On the board, the assignee of an issue is the
person who owns its triage, not the person who will implement it.

These answers are not a priority order. They say how much *we* commit to, not when anything will
ship: most of the work behind 🧪 and ✅ is done by contributors, on their own schedule.

### About 🧪 Let's try

We are interested enough to look at an implementation, but a PR here is a proof of concept that
helps us evaluate the feature. **We may still decide not to ship it, and that is a possible
outcome.** If that is not a risk you want to take, wait for ✅ Do it.

### About ⏸️ Maybe later

There is no scheduled review of these issues. They stay open, and if someone still cares about one,
a comment on the issue brings it back to our attention.

## Labels

Only the two answers that invite you to write code also get a label, so you can find them in any
issue list without opening the board:

| Label | Meaning |
| --- | --- |
| `X-Accepting-PRs` | Same as ✅ Do it. We want this. The core team will support integrating a PR that meets our quality bar. |
| `X-Accepting-PoC-PRs` | Same as 🧪 Let's try. PR welcome as a proof of concept to evaluate the feature. No warranty it is merged. |

For example:
[issues accepting PRs in element-meta](https://github.com/element-hq/element-meta/issues?q=is%3Aissue%20is%3Aopen%20label%3AX-Accepting-PRs%2CX-Accepting-PoC-PRs).

## Before you write code

1. **Say whether you want to implement it.** The issue template asks.
2. **Wait for ✅ Do it or 🧪 Let's try** (or their labels) before you start. This rule protects your
   time more than ours: a PR with no agreed intent behind it is a design conversation held after
   the code was written.
3. **Link the issue from your PR.** A feature PR whose issue has neither label may be closed with a
   pointer back to the issue.
4. **If a week goes by without an answer**, comment on the issue and say so.

This applies to features and enhancements only. Bug fixes are welcome without a prior decision.
