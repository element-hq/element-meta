# Device management

## Description

## Use cases / scenarios

## Concept

### Session management in MAS (web view)

- List all devices logged-in to a user’s account
- Mark inactive sessions (no activity since 90+ days)
- Display information about the devices (name, app version, session ID)
	- Display IP address of devices
	- Display last seen time (when was the device last online)
- Rename a device
- Logout single existing devices
- Logout multiple existing devices at once
- Change push notifications behavior for devices (why is this needed here?)

### Device verification in the Element clients

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
- Start verification of devices (why is this needed here?)
