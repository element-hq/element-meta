# Key backup and recovery in EX/EW

| Status | Last updated |
|--|--|
| Draft | Aug 28, 2023 |

This document aims to describe product requirements for key backup and recovery and its user-facing components in EX/EW.

**Table of contents**

**Figma designs**

## General guidelines, context, use cases

1. As a user I want to have message history across all my devices for that I can continue communication and use the history independent of the device.
2. As a user/organization I want to have key backup enabled automatically if my server has it enabled for that I cannot accidentally lose history.
3. As a user I want that key backup is enabled right away and independent of the recovery for that all keys are being backed-up and I can set up recovery at a later point in time when it suits me.
4. As a user I want to opt-out from key backup for that I have control over my data and what the server is allowed to store.
5. As a user I want to be able to change my recovery when I still have signed-in devices for that I can use it in case of a loss.

## Concept

### General requirements

- Key backup will always be enabled if the server enables it
- On a new device, key backup will be enabled even if the recovery isn't yet set up
- If recovery has not been set up and the user tries to sign out their last device there should be a warning and guidance to set it up

### Recovery setup
When a user has no signed-in devices, it is necessary to use recovery in order to regain access to 4S and key backup. This section describes the requirements to set up recovery.

- Recovery set up should not be part of [FTUE](https://github.com/vector-im/element-meta/blob/develop/docs/FTUE.md) to keep the experience slick and reduce the amount of steps.
- If recovery isn't yet set up, there should be a notice to the user to inform and guide to recovery setup. This notice should be visible until the user has completed recovery setup.

#### Recovery setup steps
- Currently there are two methods for a user to set up recovery
  - Generate a recovery key
  - Enter a recovery passphrase
- Both can be used in parallel but one method is mandatory to enable recovery
- For both, the user should be informed that they
  - need this recovery key in order to get access to their encryption identity and message history if they logout (or lose) all of their devices
  - should store the recovery key in a safe location (e.g., password manager or safe)

**1. Generate a recovery key**
- A suitable recovery key will be generated for the user
- The user can copy or download the key as file

**2. Enter a recovery phrase**
- The user can choose an own phrase
- There is validation to ensure sufficient entropy
- The text input should be visible

### Backup settings
- Set up recovery
  -  Allows the user to set up recovery
  -  Only shown if recovery isn't yet set up
- Change backup recovery key
  - Invalidates the previous recovery key(s)
  - Starts a new recovery set up
- Disable key backup
  - Removes existing key backup
  - Disables further key backup
  - Informs the user about consequences in a confirmation dialogue
