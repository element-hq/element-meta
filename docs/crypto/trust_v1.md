# Trust & decorations v1

| Status | Last updated |
|--|--|
| Draft | March 29, 2023 |

This document aims to describe the user-facing changes on the classic Element clients that will be made with the introduction of TOFU.

**Table of contents**

## General guidelines, context, use cases

1. As a security-aware user I want to notice when the identity of users I'm communication with changes so that I can make sure that the authenticity is still intact via other means.
2. As a user I want to know when an identity change has happened to be able to determine impact based on the messages before and after the change.
3. As a user I want a suitable behavior for identity changes depending on how sensitive I am towards security to make a sensible trade-off between security and usability. Therefore an identity change of a verified user should get more attention than an identity change of an automatically trusted user (TOFU).
4. As an organization/user, untrusted devices of other users always pose a threat to information security as it is impossible to determine the authenticity of the logged-in user.

## Indicators

For the first iteration in the classic Element clients, only the room indicators are relevant.

### Room

- Indicator for room encryption (on/off)
- Indicator for room integrity (currently part of the 'room encryption' indicator)
  - Shows information on an individual user's view
  - Use cases
    - Do I trust the identities of all other users in the room? Yes/No
    - Is there an identity mismatch with a verified user?
  - States (**currently**)
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

## Behavior for identity mismatch

An identity mismatch can occur due to key reset or malicious activity. This scenario **can't be fixed by the affected user**. 
The default behavior should be different depending on how trust has been established in the first place.

### TOFU-trusted user

- Other users will see a room notice informing them about the identity change and giving some further information on possible reasons and what to do
- The room notice allows to determine the point in time when the identity change has occured (or at least which messages were sent before/after)
- The new identity is automatically trusted via TOFU again
- Users can communicate as before

### Verified user

- Other users will see the indicator for bad room integrity is shown (red shield) => lists the users who are violating it and allows to resolve it
- Other users will be asked to verify the new identity to resolve the situation (manual verification)
- Messages from an untrusted identity show a warning until the identity is verified manually again
- Users can communicate as before (unless they use the setting _Never send encrypted messages to unverified sessions from this session_)

## Behavior for untrusted devices

When a user has a logged-in device that has not been verified with the identity of the user (using another device or a recovery method + key backup), the device will be untrusted and it is not possible to ensure that the device belongs to the actual user. This scenario **can be fixed by the affected user** by verifying the device. 

To keep security and integrity intact, the following measures will be taken
- Isolate untrusted devices in encrypted rooms (can't send/receive messages) so that no information is accidentally leaked

### Isolation of untrusted devices

If users deviate from the regular processes or there is a malicious homeserver inserting new devices, unverified devices can appear.

To cover for the risk of information leakage, users on untrusted devices cannot send or receive messages in encrypted rooms. 

- For now, the application will **block user interaction** for users on untrusted devices in encrypted rooms.
- Public rooms will still be accessible and usable from unverified devices
- Users on untrusted devices are informed about this state and guided to device verification to resolve it
- Key/secret exchange should be prevented until the situation is resolved
- Other users do not explicitly have to be informed about this (since there is no bad impact for them and they anyway have no means to resolve the situation)

## Settings

- `Never send encrypted messages to unverified sessions from this session (global / per room)` should be changed to `Never send encrypted messages to unverified users from this session (global / per room)` to reflect the new behavior of isolating unverified devices
