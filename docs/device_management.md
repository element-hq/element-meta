# Device management (OIDC)

| Status | Last updated |
|--|--|
| Draft | July 11, 2023 |

This document outlines the use cases and concept for a device manager in EX/EW that is compatible with OpenID Connect (OIDC).

**Table of contents**

* [Use cases / scenarios](#use-cases--scenarios)
* [Concept](#concept)
  + [Device authentication management in Matrix Authentication Service (web view)](#device-authentication-management-in-matrix-authentication-service-web-view)
  + [Device management entry points in the Element clients (EW/EX)](#device-management-entry-points-in-the-element-clients-ewex)

**Figma designs**

https://www.figma.com/file/40ucfibvabgbB1nXvAqxxz/Device-Management-for-EX-%26-MAS?type=design&node-id=183-10284&mode=design&t=OpxkRa0wtbfZKAeM-0

## Use cases / scenarios

1. As a user I want to have overview of my logged-in/authenticated devices for that I can manage access security of my account.
2. As a user I want to have the ability to disconnect remote devices selectively for that I can disconnect unused/lost devices or for that I can prevent harm from unknown devices (attackers), e.g., if my credentials have been compromised.
3. As a user I want to be explicitly notified if I have a new login/device for that I can take an appropriate action (verify/disconnect).
4. As a user I want to be able to rename a device to give it a meaningful name (e.g., "iPad").

## Concept

In essence, device management used to consist of two areas, device authentication and device verification (cross-signing; crypto). In an OIDC world, device authentication is handled by the OIDC protocol in a dedicated IdP / OIDC provider (OP). Device verification generally must be handled in the Element clients as only those have the required encryption keys to determine trust reliably. With the introduction of the [Trust & decorations v2 / TOFU](https://github.com/vector-im/element-meta/blob/develop/docs/crypto/trust_v2.md) concept, [untrusted devices will be isolated](https://github.com/vector-im/element-meta/blob/develop/docs/crypto/trust_v2.md#behavior-for-untrusted-devices). For this reason, device verification state in the device manager has become less important and will be **dropped for simplicity and usability**.

The concept for OIDC-based device management in EX/EW is split in two parts:

**1. Device authentication management in the OIDC provider** (web-based; Matrix Authentication Service or third party upstream IdP)
  - If Matrix Authentication Service is used without an upstream IdP, there is an integrated, web-based device authentication manager
  - If an upstream IdP is used in addition, device authentication management relies on its capabilities

**2. Device management entry points in the Element clients (EX/EW)**
  - Element clients provide a settings entry _Devices_ which shows information about the current device and guides users to 1. via a link _Manage devices_
  - Element clients will notify users about new logins/devices (based on device verification state as a proxy for whether the device belongs to the user) guiding them to 1. to allow disconnecting potentially malicious devices

### Device authentication management in Matrix Authentication Service (web view)

This section outlines the requirements/features for a web-based device authentication manager in the Matrix Authentication Service (MAS). If a deployment uses an external upstream IdP in addition, this will be replaced by the upstream IdP's capabilities.

- List all devices logged-in to a user’s account
- Mark inactive sessions (no activity since 90+ days)
- Display information about the devices (name, app version, session ID)
	- Display IP address of devices
	- Display last seen time (when was the device last online)
- Rename a device
- Logout single existing devices
- Logout multiple existing devices at once
- Change push notifications behavior for devices

### Device management entry points in the Element clients (EW/EX)

This section outlines the requirements/features around device management entry points in the Element clients (EW/EX). 

- The user must be informed about new logins/devices in their account as long as they are untrusted  (via push notification / when opening the app)
- Display information about the current device (name, app version, session ID)
	- Display IP address of devices
	- Display last seen time (when was the device last online)
- Button _Manage devices_ that guides the user to 'Device authentication management in the OIDC Provider' (web view)
