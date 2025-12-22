# EX Performance metrics

| Status | Last updated |
|--|--|
| In progress | December 22, 2025 |

<hr />

## Objective
Crashes are already tracked on Sentry. Performance metrics are also useful health metrics to check. They can be tracked by Sentry too.

This document specifies what metrics we track and how we measure them. It focuses on EX but it could be extended (and renamed) to track any matrix client app performance.

## Sentry semantics
As we use Sentry, we need to adopt its naming conventions for `Transaction(name: String, operation: String)` and `Span(operation: String, description: String)`. 
More information can be found in the Sentry documentation about [Transaction Name](https://docs.sentry.io/platforms/native/enriching-events/transaction-name/) and [Span Operations](https://develop.sentry.dev/sdk/performance/span-operations/).

## UX metrics

There are tracked using Sentry transactions. `Transaction.operation` is `ux` to reflect high-level, user journey metrics.

| Metric (Sentry Transaction Name) | Description | What is it measuring? | Initial and final conditions | Tech metrics | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Cold start | Cold start until the cached room list is displayed | How long it takes from launching the app to displaying cached data on the screen | From:<ul><li>The user is already connected</li><li>The app is not running in background</li><li> The user taps on the app icon</li></ul> To:<ul><li>The room list is fully loaded from the permanent cached and displayed to the end user | <ul><li>First rooms displayed after login or restoration (**TBD**) </li></ul> | The clock starts after the Sentry is initialised. |
| Catch-up | The app syncs and the room list becomes up-to-date | How long until the room list is up-to-date | From:<ul><li>The app was inactive in background and get debackgrounded</li><li>Or the app just finished its cold start</li></ul> To:<ul><li>The room list service state becomes [`Running`](https://github.com/matrix-org/matrix-rust-sdk/blob/matrix-sdk-ui-0.14.0/bindings/matrix-sdk-ffi/src/sync_service.rs#L36)</li><li>No more Syncing spinner |  | The expected final conditions should be:<ul><li>The room list is updated</li><li>Properly sorted</li><li>Last messages are up-to-date</li></ul> But we need more work to compute this metric.  |
| Notification to message | A notification was tapped and it opened a timeline | How long it takes from taping the notification to the message becoming visible in the app | From:<ul><li>The app is in background or active</li><li>The notification is for a message in the main timeline</li><li>The user taps on the notification</li></ul> To:<ul><li>The message is visible in the timeline</li><li>The timeline around this message is fully loaded | <ul><li>Timeline load</li></ul> |  |
| Open a room | Open a room and see loaded items in the timeline | How long it takes from tapping a room in the room list to displaying a full page of messages | From:<ul><li>User taps a room from the room list</li></ul> To:<ul><li>The timeline is fully loaded with first items loaded  | <ul><li>Timeline load</li></ul> |  |
| Send a message | Send to sent state in timeline  | How long it takes from tapping send to the message appearing in the timeline as sent | From:<ul><li>User hits the send button</li></ul> To:<ul><li>The timeline shows it as sent |  | **TODO**: We need to experiment the feasibility of this metric |

## Additional data

We need to add some data to the metrics so that we can better characterise them:

| Data | Why is it useful? | Notes |
| :---- | :---- | :---- |
| Device information | <ul><li>To detect specific device problem, especially on the fragmented Android ecosystem</li></ul> | It is provided by Sentry |
| Homeserver | <ul><li>To compare matrix.org and element.io homeservers speed</li><li>To measure the impact of a slow homeserver</li></ul> | **We use SHA-512 to compute the hash of the homeserve domain**, ie matrix.org or element.io.  |
| DB files size:<ul><li>Crypto store</li><li>State store</li><li>Event cache store</li><li>Media store</li></ul> | <ul><li>To check the impact of growing DB on speed performance</li><li>To check disk space used by the app</li></ul> | Expressed in MB. |

We'd want to add this data too, but it's not possible at the moment given the info we have in the SDK:

| Data | Why is it useful? | Notes |
| :---- | :---- | :---- |
| Account size | <ul><li>To check the impact on speed performance</li><li>To check the impact on \`/sync\` response size</li></ul> | Expressed in number of joined rooms.</br>**TODO**: Add the Rust SDK API for reference<br/>**TODO**: We need to experiment the feasibility of this metric |
| Catch-up /sync size | <ul><li>To check network usage stays as low as possible</li></ul> | The response size in kB of the first `/sync` request made during catch-up.</br>**TODO**: Add the Rust SDK API for reference</br>**TODO**: We need to experiment the feasibility of this metric |

## Tech metrics

They are tracked as Senty spans. `Span.operation` follows the [Span Operations](https://develop.sentry.dev/sdk/performance/span-operations/) convention like `http.client`. `Span.description` is the metric name.

| Metric (Sentry Span Description) | Category (Sentry Span Operation) | Description  | Notes |
| :---- | :---- | :---- | :---- |
| Timeline load | `function` | `sdkRoom.timelineWithConfiguration ()` | |

**TODO: Add more**


## Future considerations
Later, we could add the following UX metrics.

### UX starting from outside of the app
* Call answer to call
* Permalink to message
* Notification to threaded message
* Notification to invite (room or space)

And maybe all the variants:
* Permalink to room
* Permalink to space
* Permalink to threaded message
* Permalink to profile
* Permalink to Element Call

### UX inside the app
* Make a call
* QR code login
* Open member list
* Open a permalink (of all sorts)
* Open a thread

