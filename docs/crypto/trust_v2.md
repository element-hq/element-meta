# Trust & decorations v2

| Status | Last updated |
|--|--|
| Draft | May 3, 2023 |

This document aims to describe the concepts for user-facing crypto-trust components and related decorations in the Element X clients.

## General guidelines, context, use cases

1. As a security-aware user I want to notice when the identity of users I'm communication with changes so that I can make sure that the authenticity is still intact via other means.
2. As a user I want to know when an identity change has happened to be able to determine impact based on the messages before and after the change.
3. As a user I want a suitable behavior for identity changes depending on how sensitive I am towards security to make a sensible trade-off between security and usability. Therefore an identity change of a verified user should get more attention than an identity change of an automatically trusted user (TOFU).
3. As a user I want to know whether a room is encrypted for that I can use the room accordingly.
4. As a security-aware organization/user I want to ensure user authenticity/trust (make sure that users actually are who they appear to be) in order to prevent information leakage to unauthorized third parties.
5. As a user I want to know when a message has been sent in clear text in an encrypted room for that I can identify potential information leakage.
6. As an organization I want to be able to decide which level of trust is suited for users/rooms (TOFU vs. manual trust)
7. As an organization I want that the options to trust a new identity depend on desired trust level (simple confirmation vs. manual verification)
8. As a user I don't want to be bothered with technical information I do not need to understand in order to securely use the app. The app should only show crypto-related indications when it is necessary for the user to understand or for cases where they are able to act upon it.
9. As an organization/user, unverified devices of other users always pose a threat to information security as it is impossible to determine the authenticity of the logged-in user.
10. As were making FTUE a lot slicker we need tooltips for certain things like setting up recovery


## Indicator analysis & background
Gathering and analysis: https://docs.google.com/spreadsheets/d/19z9NQtfehwTETIOqA7SbXgaNqXR8xHE54ryUy2YOAzc/edit#gid=0

The following sections outline the encryption-related indicators from an Element Classic point of view. Quite a couple of them can be dropped in EX as we either do not need them anymore for UX reasons or can find solutions on the protocol level that make them obsolete.

### Timeline

The following refers to different states of the 'shield' indicator that can appear next to each message in the timeline.

- Message sent in clear text in an encrypted room => required for certain cases, might change iconography/color (needs design input)
- ~~Message sent by an unverified device of a verified user~~ => legacy and not required anymore as
	- a) users will not have unverified devices anymore in normal operations (we force verification during FTUE)
	- b) unverified devices will be isolated in encrypted rooms (can't send/receive messages)
- ~~Message sent by a deleted device~~ => legacy and not required anymore as we'll find a solution for this case on the protocol level
- ~~Authenticity of a message cannot be guaranteed~~ => legacy and not required anymore as unsafe keys will disappear (solved by symmetric backup and trusted key forwards)

### Other user's profiles

- ~~Indicator for device verification~~ => legacy and not required anymore as device verification will be forced during FTUE and there will be other handling for unverified devices, making this information redundant for other users
	- ~~One of the user's devices is unverified~~ (red shield with exclamation mark)
	- ~~All devices of the user are verified~~ (green shield with checkmark)

### Room

- Indicator for public rooms
- Indicator for room encryption (on/off)
- Indicator for room integrity (currently part of the 'room encryption' indicator)
  - Shows information on an individual user's view
  - Use cases
    - Do I trust the identities of all other users in the room? Yes/No
    - Is there an identity mismatch with a verified user?
  - States (Element Classic)
    - Room is encrypted but not all users have been verified, and those that have (if any) still have the verified identity (grey shield)
    - Room is encrypted but at least one user violates trust (identity mismatch; red shield with exclamation mark)
    - Room is encrypted and the user trusts all users (green shield with checkmark)
	    - The set of “all users” depends on the type of room:
		    - For regular / topic rooms, all users including yourself, are considered when decorating a room
		    - For 1:1 and group DM rooms, all other users (i.e. excluding yourself) are considered when decorating a room
  - States (**with TOFU**)
    - Room is encrypted and other users are TOFU-trusted or manually verified (grey shield)
    - Room is encrypted but at least one user violates its **verified** identity (identity mismatch; red shield with exclamation mark)
    - Room is encrypted and the user has **verified** the identity of all other users in the room (green shield with checkmark)

## Indicators in EX

TBC

## Behavior for identity mismatch

An identity mismatch can occur due to key reset or malicious activity. This scenario **can't be fixed by the affected user**. 
The default behavior should be different depending on how trust has been established in the first place.

### TOFU-trusted user

- Other users will see a room notice informing them about the identity change and giving some further information on possible reasons and what to do
- The new identity is automatically trusted via TOFU again
- Users can communicate as before

### Verified user

- Other users will see a room notice informing them about the identity change and giving some further information on possible reasons and what to do
- The indicator for bad room integrity is shown (red shield) => lists the users who are violating it and allows to resolve it
- Other users will be asked to verify the new identity to resolve the situation (manual verification)
- Messages from an untrusted identity show a warning until the identity is verified manually again
- Users can communicate as before (unless they use the setting _Never send encrypted messages to unverified sessions from this session_)

## Behavior for untrusted devices

When a user has a logged-in device that has not been verified with the identity of the user (using another device or a recovery method + key backup), the device will be untrusted and it is not possible to ensure that the device belongs to the actual user. This scenario **can be fixed by the affected user** by verifying the device. 

To keep security and integrity intact, the following measures will be taken
1. Force device verification during FTUE to prevent this scenario from occuring in normal operations (see FTUE product spec)
2. Isolate untrusted devices in encrypted rooms (can't send/receive messages) so that no information is accidentally leaked

### Isolation of untrusted devices

If users deviate from the regular processes or there is a malicious homeserver inserting new devices, unverified devices can still appear.

To cover for the risk of information leakage, users on untrusted devices cannot send nor receive messages in encrypted rooms. 

- For now, the application will **block user interaction** for users on untrusted devices in encrypted rooms.
- Public rooms will still be accessible and usable from unverified devices
- Users on untrusted devices are informed about this state and guided to device verification to resolve it
- Key/secret exchange should be prevented until the situation is resolved
- Other users do not explicitly have to be informed about this (since there is no bad impact for them and they anyway have no means to resolve the situation)
