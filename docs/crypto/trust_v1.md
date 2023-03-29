# Trust & decorations v1

| Status | Last updated |
|--|--|
| Draft | March 29, 2023 |

This document aims to describe the user-facing changes on the classic Element clients that will be made with the introduction of TOFU.

**Table of contents**

## General guidelines, context, use cases

1. As a security-aware user I want to notice when the identity of users I'm communication with changes so that I can make sure that the authenticity is still intact via other means.
2. 
x. As an organization/user, untrusted devices of other users always pose a threat to information security as it is impossible to determine the authenticity of the logged-in user.

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
    - Room is encrypted but the user trusts no other user (grey shield)
    - Room is encrypted but at least one user violates trust (identity mismatch; red shield with exclamation mark)
    - Room is encrypted and the user trusts all other users (green shield with checkmark)
  - States (**with TOFU**)
    - Room is encrypted and other users are TOFU-trusted (grey shield)
    - Room is encrypted but at least one user violates **manual** trust (identity mismatch; red shield with exclamation mark)
    - Room is encrypted and the user has **manual** trust with all other users

## Behavior for identity mismatch

An identity mismatch can occur due to key reset or malicious activity. This scenario **can't be fixed by the user**. 
The default behavior should be different depending on how trust has been established in the first place.

### TOFU-trusted user

- Other users will see a room event informing them about the identity change and giving some further information on possible reasons and what to do
- The new identity is automatically trusted via TOFU again
- Users can communicate as before

### Manually trusted user (!WIP!)

- Other users will see the indicator for bad room integrity is shown (red shield) => lists the users who are violating it and allows to resolve it
- Other users will be asked to verify the new identity to resolve the situation (manual verification)
- Users can communicate as before (unless they use the setting _Never send encrypted messages to unverified sessions from this session_)

## Behavior for untrusted devices

When a user has a logged-in device that has not been verified with the identity of the user (using another device or a recovery method + key backup), the device will be untrusted and it is not possible to ensure that the device belongs to the actual user. This scenario **can be fixed by the respective user** by verifying the device. 

To keep security and integrity intact, the following measures will be taken
- Isolate untrusted devices in encrypted rooms (can't send/receive messages) so that no information is accidentally leaked

### Isolation of untrusted devices

If users deviate from the regular processes or there is a malicious homeserver inserting new devices, unverified devices can appear.

To cover for the risk of information leakage, the following steps will be taken
1. Users on unverified devices cannot send or receive messages in encrypted rooms
2. Users on unverified devices are informed about this state and guided to device verification to resolve it

## Settings

- Never send encrypted messages to unverified sessions from this session (global / per room)
