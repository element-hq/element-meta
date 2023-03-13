# First Time User Experience

This document aims to make first time user experience as simple as possible. FTUE refers to either the first registration/login of a user or to linking additional devices. All FTUE scenarios need to be covered within the initial setup of Element clients.

| Status | Last updated |
|--|--|
| Draft | March 13, 2023 |

## Use cases / scenarios

### 1. A new employee of an organization is onboarded to Element

#### Conditions
- User account exists in IDM
- Homeserver is known
- User attributes can be obtained from IDM and should not be changed by users in most cases

### 2. An existing regular user wants to onboard another regular user

#### Conditions
- User account does not exist
- Existing user can make a homeserver proposal
	- Same homeserver
	- Propose another one ("Element Connect")
- User attributes are unknown

### 3. A regular user just downloads the app or opens the web app

#### Conditions
- User account is unknown
- Homeserver preference is unknown
- User attributes are unknown

## Flows

### 0. MDM (not in scope)

### 1. Invitation via link

### 1a) Enterprise / organizational invitation

1. User receives an invite link and clicks it
2. Browser opens and loads Element Web or the mobile app is opened (platform-dependent)
	1. User doesn't have the app => Open app store and allow to install, then launch it
	2. User has the app => Launch it
3. [homeserver and/or other information are imported via clipboard in the background ]
4. Welcome screen
5. Open web view overlay for login (or redirect to IdP on Web/Desktop; OIDC flow; requires consent on iOS; see [Login](#login) for more details)
6. User authenticates, web view closes (or redirect back to Web/Desktop app), user is back in the app
7. [user is logged in]
8. [user attributes are pulled from the server, if possible]
9. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
10. [if we don't get user attributes from the server or user is allowed to change them] Additional user attributes (user can skip; see [Additional user attributes](#additional-user-attributes) for more details)
11. Ask to allow notifications
12. Ask for consent to analytics
13. User account summary (your name, avatar, MXID, etc.)
14. Element is set up, user sees their 'All chats' list 


### 1b) Regular user invitation

1. User receives an invite link and clicks it
2. Browser opens and loads Element Web or the mobile app is opened (platform-dependent)
	1. User doesn't have the app => Open app store and allow to install, then launch it
	2. User has the app => Launch it
3. [homeserver, inviting user MXID and/or other information are imported via clipboard in the background ]
4. Welcome screen
5. Simplified homeserver choice ("You are about to register on homeserver.tld"; continue/change)
6. Open web view overlay for registration (or redirect to IDM registration on Web/Desktop; OIDC flow; requires consent on iOS; see [Registration](#registration) for more details)
7. User creates account
8. Web view closes (or redirect back to Web/Desktop app), user is back in the app
9. [user is logged in]
10. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
11. Additional user attributes (user can skip; see [Additional user attributes](#additional-user-attributes) for more details)
12. Ask to allow notifications
13. Ask for consent to analytics
14. User account summary (your name, avatar, MXID?, etc.)
15. Element is set up, user sees their 'All chats' list
16. A DM room with the inviting user is automatically set up

### 2. Manual login / registration

1. Welcome screen
2. Let's get you set up (options)
	1.  Log in with another device (highlighted prominently; A)
	2.  Log in manually (email / username; B)
	3.  Register new account (C)
3. Different flows depending on user choice

**A)  Log in with another device (QR code flow)**

1.  ‘Scan QR code’ view is shown with camera view and advice => "open Element on another logged-in device and click ‘Link additional device’"; QR code is shown
2.  User scans QR code
3.  [user/homeserver information and recovery key are imported in the background]
4.  [user is logged in]
5.  [message history and key backup are fetched from server, device is cross-signed]
6.  Ask to allow notifications
7.  Ask for consent to analytics
8.  Element is fully set up, user sees their 'All chats' list

**B) Log in manually (email / username)**

1. Simplified homeserver choice ("You are about to sign in to your account on matrix.org"; continue/change)
2. Open web view overlay for login (or redirect to IdP on Web/Desktop; OIDC flow; requires consent on iOS; see [Login](#login) for more details)
3. User authenticates, web view closes (or redirect back to Web/Desktop app), user is back in the app
4. [user is logged in]
5. [ask server if single device or additional device] Secure Messaging
	1. If no encryption or secure backup enabled => skip this step
	2. Single device => Ask for recovery method to obtain 4S (offer to reset?) => can't be skipped
	3. Additional device => Ask for cross-signing with another device (QR code or 6-digit code comparison) or recovery method => can't be skipped
4. [message history and key backup are fetched from server, device is cross-signed (if applicable)]
5. Ask to allow notifications
6. Ask for consent to analytics
7. Element is fully set up, user sees their 'All chats' list

**C) Register new account**

1. Simplified homeserver choice ("You are about to register on matrix.org"; continue/change)
2. Open web view overlay for registration (or redirect to IDM registration on Web/Desktop; OIDC flow; requires consent on iOS; see [Registration](#registration) for more details)
3. User creates account
4. Web view closes (or redirect back to Web/Desktop app), user is back in the app
5. [user is logged in]
6. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
7. Additional user attributes (user can skip; see [Additional user attributes](#additional-user-attributes) for more details)
8. Ask to allow notifications
9. Ask for consent to analytics
10. User account summary (your name, avatar, MXID?, etc.)
11. Element is fully set up, user sees their (empty) 'All chats' list
12. User gets hints on how to get started (start a conversation, join a public room, etc.)

## Related solution concepts

### Design for MAS-served components as part of OIDC flow
#### Login

For all login flows, the first entry point for a user is a web page served by MAS. There are different scenarios depending on the type of deployment:

- Using **integrated MAS-based login provider** (IdP) => users authenticate directly on the web page served by MAS
- Providing a **single upstream login provider** (IdP; e.g., Google) => MAS will transparently redirect the user to the upstream login provider to authenticate there
- Providing **multiple upstream login providers** (IdP; e.g., Google and Keycloak) => MAS will provide a list of login providers and redirects depending on user choice to the respective upstream login provider to authenticate there

As part of the flows involving upstream login providers, more sophisticated authentication security measures like 2FA, MFA, Brute-force protection, etc., can be employed, depending on the capabilities and configuration of the upstream login provider.

#### Registration

The options for registering a new user account depend on the respective user backend and the homeserver configuration.

- For a **MAS-backed** deployment (only using the internal user directory), the user creates their account directly on a web page served by MAS.
	- UserID
	- Password
	- E-Mail
	- E-Mail verification
	- Accept T&Cs (configurable)
	- Consent to share account data with the client
	
- For a deployment **backed by LDAP or another external user backend**, we don't have direct access to account creation. We can provide a configurable link to a web page served by the external user backend which allows account creation.
- The homeserver can be configured to disallow registration. In this case Element should inform the user after the homeserver choice.

### Additional user attributes

- Display name
- Mail address
- Avatar
- Phone number
- etc.

### How do you want others to find you?

We could make a difference by giving the user choice over which identifiers they want to associate with their MXID to allow others to find them by. **For enterprise use cases** there should be a way to pre-configure/enforce this so that the user does not have the choice and does not see the screen during FTUE.

- Name
- Mail address
- Phone number
- etc.

As part of this process they might also need to accept T&C's for identity servers.

### Settings
- User registration enabled/disabled
- Restrict user invitations to administrators
- Allow/disallow users to change user attributes
