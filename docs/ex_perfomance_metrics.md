# EX Performance metrics

| Status | Last updated |
|--|--|
| In progress | December 3, 2025 |

<hr />

## Objective
Crashes are already tracked on Sentry. Performance metrics are also useful health metrics to check. They can be tracked by Sentry too.

This document specifies what metrics we track and how we measure them. It focuses on EX but it could be extended (and renamed) to track any matrix client app performance.

## UX metrics

| Title | Android name / Description | What is it measuring? | Initial and final conditions | Tech metrics | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Cold start | Cold start until the cached room list is displayed | How long it takes from launching the app to displaying cached data on the screen | From:<ul><li>The user is already connected</li><li>The app is not running in background</li><li> The user taps on the app icon</li></ul> To:<ul><li>The room list is fully loaded from the permanent cached and displayed to the end user | <ul><li>First rooms displayed after login or restoration (**TBD**) </li></ul> | The clock starts after the Sentry is initialised. |
| Catch-up | The app syncs and the room list becomes up-to-date | How long until the room list is up-to-date | From:<ul><li>The app was inactive in background and get debackgrounded</li><li>Or the app just finished its cold start</li></ul> To:<ul><li>The room list service state becomes [`Running`](https://github.com/matrix-org/matrix-rust-sdk/blob/matrix-sdk-ui-0.14.0/bindings/matrix-sdk-ffi/src/sync_service.rs#L36)</li><li>No more Syncing spinner |  | The expected final conditions should be:<ul><li>The room list is updated</li><li>Properly sorted</li><li>Last messages are up-to-date</li></ul> But we need more work to compute this metric  |
| Notification to message | A notification was tapped and it opened a timeline | How long it takes from taping the notification to the message becoming visible in the app | From:<ul><li>The app is in background or active</li><li>The notification is for a message in the main timeline</li><li>The user taps on the notification</li></ul> To:<ul><li>The message is visible in the timeline</li><li>The timeline around this message is fully loaded |  |  |
| Open a room | Open a room and see loaded items in the timeline | How long it takes from tapping a room in the room list to displaying a full page of messages | From:<ul><li>User taps a room from the room list</li></ul> To:<ul><li>The timeline is fully loaded with first items loaded  | <ul><li>Get and display first timeline items</li></ul> |  |
| Send a message | Send to sent state in timeline  | How long it takes from tapping send to the message appearing in the timeline as sent | From:<ul><li>User hits the send button</li></ul> To:<ul><li>The timeline shows it as sent |  | **TODO**: We need to experiment the feasibility of this metric |

## Additional data

We need to add some data to the metrics so that we can better characterise them:

| Data | Why is it useful? | Notes |
| :---- | :---- | :---- |
| Device information | <ul><li>To detect specific device problem, especially on the fragmented Android ecosystem</li></ul> | It is provided by Sentry |
| Homeserver URL hash | <ul><li>To compare matrix.org and element.io homeservers speed</li><li>To measure the impact of a slow homeserver</li></ul> | We use SHA-512 to compute the hash. </br>**TBD:** Define the input string (`https://matrix.org`, `matrix.org`() or `https://matrix-client.matrix.org` (`base_url`) or something else) |
| DBs file size | <ul><li>To check the impact of growing DB on speed performance</li><li>To check disk space used by the app</li></ul> | We have 4 DBs: state, event, media, crypto.</br>**TODO**: Add here names from the new Rust SDK API |
| Account size | <ul><li>To check the impact on speed performance</li><li>To check the impact on \`/sync\` response size</li></ul> | It is the number of rooms joined by the user.</br>**TODO**: Add the Rust SDK API for reference |
| First /sync response size | <ul><li>To check network usage stays as low as possible</li></ul> | **TODO**: Add the Rust SDK API for reference |
