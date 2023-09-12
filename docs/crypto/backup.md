# Key backup and recovery in EX/EW

| Status | Last updated |
|--|--|
| Draft | Aug 28, 2023 |

This document aims to describe product requirements for key backup and recovery and its user-facing components in EX/EW.

- **Key backup** refers to the server-side encryption key backup. Devices can upload encrypted copies of their megolm keys (room history decryption keys) to the server.
- **Recovery** refers to secret storage (4S) that allows the user to securely store a remote encrypted backup of their devices' local secrets to their homeserver. The recovery restores the key backup secret as well as the cross-signing secrets.

**Table of contents**

- [General guidelines, context, use cases](#general-guidelines-context-use-cases)
- [Concept](#concept)
  * [General requirements](#general-requirements)
  * [Recovery setup](#recovery-setup)
    + [Recovery setup steps](#recovery-setup-steps)
  * [Recovery settings](#recovery-settings)
  * [Recovery](#recovery)

**Figma designs**

## General guidelines, context, use cases

1. As a user I want to have message history across all my devices for that I can continue communication and use the history independent of the device.
2. As a user/organization I want to have key backup enabled automatically if my server has it enabled for that I cannot accidentally lose history.
3. As a user I want that key backup is enabled right away and independent of the recovery for that all keys are being backed-up and I can set up recovery at a later point in time when it suits me.
4. As a user I want to opt-out from key backup for that I have control over my data and what the server is allowed to store.
5. As a user I will use classic clients and new clients. The key backup mechanism needs to compatible between them.
6. As a user I want to be able to change my recovery when I still have signed-in devices for that I can use it in case of a loss.

## Concept

### General requirements

- Key backup will always be enabled by default
- On a new device, key backup will be enabled even if the recovery isn't yet set up
- If recovery has not been set up and the user tries to sign out their last device there should be a warning and guidance to set it up
- Key backup on EX/EW must be compatible with backup implementations on classic / 3rd party client implementation such that users have a seamless experience when they use both in parallel
- Key backup must only contain safe keys such that the server cannot inject keys and the client can verify the keys' authenticity.

### Recovery setup
When a user has no signed-in devices, it is necessary to use recovery in order to regain access to their crypto identity (4S and key backup). The recovery key can also be used to verify devices (in a single device use case it's mandatory). This section describes the requirements to set up recovery.

- Recovery setup should not be part of [FTUE](https://github.com/vector-im/element-meta/blob/develop/docs/FTUE.md) to keep the experience slick and reduce the amount of steps.
- If recovery isn't yet set up, there should be a notice to the user to inform and guide to recovery setup. This notice should be visible until the user has completed it.

#### Recovery setup steps
- As a foundation, the app generates a recovery key for the user (there can be other mechanisms in the future)
- The user should be informed that they
  - need this recovery key in order to get access to their encryption identity. This allows to verify new devices and to get access to message history. If they logout (or lose) all of their devices, this key is mandatory.
  - should store the recovery key in a safe location (e.g., password manager or a safe)

**Generate a recovery key**
- A suitable recovery key will be generated for the user
- The user can copy or save the key as file

### Recovery settings
- Set up recovery
  -  Allows the user to set up recovery (see [Recovery setup](#recovery-setup))
  -  Only shown if recovery isn't yet set up
- Change recovery key
  - Requires the device to be trusted. Otherwise an existing recovery key is required.
  - If a user has lost their recovery key (or has other reasons to change it) but still has logged-in devices, they can create a new recovery key
  - Invalidates the previous recovery key(s)
  - Starts a new recovery set up
- Disable recovery
  - Removes existing key backup and 4S
  - Disables further key backup
  - Informs the user about consequences in a confirmation dialogue
    - On a new device, the user will not be able to retrieve their message history from the server (there might still be other clients forwarding keys for message history)
    - If the user loses all of their devices, they'll not be able to get access to their crypto identity.
      - They will need to rotate it which will be noticeable by other users they communicate with
      - They will lose access to their message history
      - They will need to re-verify users they have verified before to establish trust again
 - Troubleshooting
   - Only shown if something is wrong (some keys not available, etc.)
   - Asks the user to enter the recovery key to re-initialize the backup

### Recovery
The recovery process is handled in the [FTUE](https://github.com/vector-im/element-meta/blob/develop/docs/FTUE.md) concept.
