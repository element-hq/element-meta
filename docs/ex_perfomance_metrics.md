# EX Performance metrics

| Status | Last updated |
|--|--|
| In progress | December 3, 2025 |

<hr />

## Objective
Crashes are already tracked on Sentry. Performance metrics are also useful health metrics to check. This can be tracked by Sentry too.

This document specifies what metrics we track and how we measure them. It has a focus on EX but it could be extended (and renamed) to track any matrix client app performance.

## UX metrics


| Title | Android name / Description | What it is measuring | Initial and final conditions | Tech metrics | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Cold start time | Cold start until cached room list is displayed | How long it takes from launching the app to displaying cached data on the screen | From:<ul><li>The user is already connected</li><li>The app is not running in background User taps on the app icon</li></ul> To:<ul><li>The room list is fully loaded from the permanent cached and displayed to the end user | <ul><li>First rooms displayed after login or restoration (TBD) </li></ul> | It does not consider Sentry init time and the check that the user has consented from disk. |
| Catch-up | Room list says it is resumed and running | How long until the room list is up-to-date | From:<ul><li>The app was inactive in background and get debackgrounded</li><li>Or the app just finished its cold start</li></ul> To:<ul><li>The room list service turns into `Running` No more Syncing spinner |  | The expected final conditions should be:<ul><li>The room list is updated</li><li>Properly sorted</li><li>Last messages are up-to-date</li></ul> But we need more work to get it |
| Notification to message | A notification was tapped and it opened a timeline | How long it takes from taping the notification to the message becoming visible in the app | From:<ul><li>The app is in background or active The user taps on a notification</li></ul> To:<ul><li>The message is visible in the timeline The timeline around this message is fully loaded |  |  |
| Open a room | Open a room and see loaded items in the timeline | How long it takes from tapping a room in the room list to displaying a full page of messages | From:<ul><li>User taps a room from the room list</li></ul> To:<ul><li>The timeline is fully loaded with first items loaded  | <ul><li>Get and display first timeline items</li></ul> |  |
| Send a message | ? | How long it takes from tapping send to the message appearing in the timeline as sent | From:<ul><li>User hits the send button</li></ul> To:<ul><li>The timeline shows it as sent |  | Needs to be tested for validation |


## Additional data

We need to add some data to the metrics so that we can better characterise them:

| Data | Why it is useful | Notes |
| :---- | :---- | :---- |
| Device information | <ul><li>It helps to detect specific device problem, especially on the fragmented Android ecosystem</li></ul> | It is provided by Sentry. No additional work |
| Homeserver URL hash | <ul><li>To compare matrix.org and element.io homeservers speeds</li><li>Measure the impact of a slow server</li></ul> | We use SHA-512 for the hash |
| DBs file size | <ul><li>Check the impact of growing DB on speed performance</li><li>Check disk space used by the app</li></ul> | We have 4 DBs: state, event, media, crypto |
| Account size | <ul><li>Check the impact on speed performance</li><li>Check the impact on \`/sync\` response size</li></ul> | It should be part of a new stats FFI API |
| First /sync response size | <ul><li>Check it stays as small as possible</li></ul> | It should be part of a new stats FFI API |