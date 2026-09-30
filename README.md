# Element meta

element-meta is the shared home of the Element apps: [Web and Desktop](https://github.com/element-hq/element-web),
[Android](https://github.com/element-hq/element-x-android) and [iOS](https://github.com/element-hq/element-x-ios).
It holds what is common to all of them: feature requests, the processes the app teams follow, and
product documentation.

## Feature requests

**This is the place to request a feature or a change for the Element apps**, whatever the platform.
[Open an enhancement request](https://github.com/element-hq/element-meta/issues/new?template=enhancement.yml).

The product team answers every request within a week, on the
[Feature Request Triage board](https://github.com/orgs/element-hq/projects/168). The answer also
says whether we would accept a PR for it. [How feature requests are triaged](docs/process/feature-requests.md)
explains what each answer means.

We no longer take feature requests in [Discussions](https://github.com/element-hq/element-meta/discussions),
and they will be closed. Please open an issue instead.

## Where else to go

- **A bug:** the app repository where it reproduces:
  [element-web](https://github.com/element-hq/element-web/issues),
  [element-x-android](https://github.com/element-hq/element-x-android/issues) or
  [element-x-ios](https://github.com/element-hq/element-x-ios/issues).
- **A request that only makes sense on one platform:** that app repository. If you are not sure,
  use it anyway; we will move the issue here if it concerns other platforms too.
- **An SDK API, protocol, performance or crypto concern:**
  [matrix-rust-sdk](https://github.com/matrix-org/matrix-rust-sdk/issues) for Element X on Android
  and iOS, [matrix-js-sdk](https://github.com/matrix-org/matrix-js-sdk/issues) for Element Web and
  Desktop.
- **Calls:** [element-call](https://github.com/element-hq/element-call/issues), which provides
  calls in all three apps.
- **The rich text composer:**
  [matrix-rich-text-editor](https://github.com/element-hq/matrix-rich-text-editor/issues), shared
  by all three apps.
- **Signing in, signing up or managing your account** in the web pages your homeserver opens for
  it: [matrix-authentication-service](https://github.com/element-hq/matrix-authentication-service/issues).
- **A security issue:** email security@element.io, not a public issue. See the
  [security disclosure policy](https://element.io/security/security-disclosure-policy).
- **A question or support request:** the app's Matrix room:
  [#element-web:matrix.org](https://matrix.to/#/#element-web:matrix.org),
  [#element-x-android:matrix.org](https://matrix.to/#/#element-x-android:matrix.org) or
  [#element-x-ios:matrix.org](https://matrix.to/#/#element-x-ios:matrix.org).

## Contributing

A PR for a feature or an enhancement must link an issue that carries the `X-Accepting-PRs` or
`X-Accepting-PoC-PRs` label. Get agreement on the change before writing the code. Bug fixes are
welcome without a prior decision. Each app repository's `CONTRIBUTING.md` has the details for its
codebase.

## Process docs

- [Feature requests](docs/process/feature-requests.md): where to file them, how they are answered,
  when to write a PR.
- [Label sync](docs/process/label-sync.md): the reusable workflow that syncs labels across
  repositories.

The app teams' other processes (issue triage, labelling, reviews) are being moved here from the
[wiki](https://github.com/element-hq/element-meta/wiki), which is out of date.

## Product documentation

- [`docs/`](docs): how some Element features are meant to behave. Many of these pages date from
  2022–2024, and some describe the legacy Element apps. Treat them as reference material, not as a
  description of the current apps.
- [`spec/`](spec/index.md): the non-standard Matrix event types used by Element.
