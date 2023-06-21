# Device management (OIDC)

| Status | Last updated |
|--|--|
| Draft | June 21, 2023 |

This document outlines the use cases and concept for a device manager in EX/EW that is compatible with OpenID Connect (OIDC).

**Table of contents**

TBC

**Figma designs**

TBC

## Use cases / scenarios

1. As a user I want to have overview of my logged-in/authenticated devices for that I can manage access security of my account.
2. As a user I want to have the ability to disconnect remote devices selectively for that I can disconnect unused/lost devices or for that I can prevent harm from unknown devices (attackers), e.g., if my credentials have been compromised.
3. As a user I want to see the verification/trust state of all my devices for that I can identify untrusted devices. 
4. As a user I want to be explicitly notified if I have an untrusted device for that I can take an appropriate action (verify/disconnect).
5. As a user I want to be able to rename a device to give it a meaningful name (e.g., "iPad").

## Concept

In essence, device management consists of two areas, device authentication and device verification (cross-signing; crypto). In an OIDC world, device authentication is handled by the OIDC protocol in a dedicated IdP / OIDC provider (OP). Device verification must be handled in the Element clients as only those have the required encryption keys to determine trust reliably.

The concept for OIDC-based device management in EX/EW therefore is split in two parts:

**1. Device authentication management in the OIDC provider** (web-based; Matrix Authentication Service or third party upstream IdP)
  - If Matrix Authentication Service is used without an upstream IdP, there is an integrated, web-based device authentication manager
  - If an upstream IdP is used in addition, device authentication management relies on its capabilities

**2. Device verification management in the Element clients**
  - Element clients provide a (read-only) list of devices showing their verification/trust state
  - Element clients will notify users on login / opening the app if they have unverified devices

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
- Change push notifications behavior for devices (TBD - why is this needed here?)

### Device verification management in the Element clients (EW/EX)

This section outlines the requirements/features for an integrated device verification manager in the Element clients (EW/EX). 

- The user must be informed about unverified devices in the clients  (on login / when opening the app)
- List all devices logged-in to a user’s account
	- Verified devices
	- Unverified devices
- Mark current session
- Display verification state of all devices, see unverified sessions
- Display information about the devices (name, app version, session ID) => TBD
	- Display IP address of devices
	- Display last seen time (when was the device last online)
- Button "Manage devices" that guides the user to 'Session management in OP' (web view)
- Start verification of devices (TBD - why is this needed here?)
