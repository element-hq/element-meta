# First Time User Experience

| Status | Last updated |
|--|--|
| Draft | March 15, 2023 |

This document aims to make first time user experience as simple as possible. FTUE refers to either the first registration/login of a user or to linking additional devices. All FTUE scenarios need to be covered within the initial setup of Element clients.

**Table of contents**

- [General guidelines](#general-guidelines)
- [Use cases / scenarios](#use-cases--scenarios)
  * [1. A new employee of an organization is onboarded to Element](#1-a-new-employee-of-an-organization-is-onboarded-to-element)
  * [2. An existing regular user wants to onboard another regular user](#2-an-existing-regular-user-wants-to-onboard-another-regular-user)
  * [3. A regular user just downloads the app or opens the web app](#3-a-regular-user-just-downloads-the-app-or-opens-the-web-app)
- [Flows](#flows)
  * [0. MDM (not in scope)](#0-mdm-not-in-scope)
  * [1. Invitation via link](#1-invitation-via-link)
    + [1a) Enterprise / organizational invitation](#1a-enterprise--organizational-invitation)
    + [1b) Regular user invitation](#1b-regular-user-invitation)
  * [2. Manual login / registration](#2-manual-login--registration)
- [Related solution concepts](#related-solution-concepts)
  * [Design for MAS-served components as part of OIDC flow](#design-for-mas-served-components-as-part-of-oidc-flow)
    + [Login](#login)
    + [Registration](#registration)
    + [Branding](#branding)
  * [Additional user attributes](#additional-user-attributes)
  * [How do you want others to find you?](#how-do-you-want-others-to-find-you)
  * [Homeserver settings to consider](#homeserver-settings-to-consider)

## General guidelines

1. The user onboarding process should be as **simple** and **require as few steps as possible** so that users can start using the app and reach their goals quickly, preventing churn.
2. Many end-users do not understand or know about **federation and other technical topics**. Therefore the app should **not bother the end-user with it** but make them reach their goals at least as easily as with a centralized service. It must not be necessary to educate users about technical backgrounds in order to allow them to use the app.
3. **Technical wording** should be avoided wherever possible.
4. In order to simplify FTUE, the app should prominently advertise **invitation-based onboarding flows** that improve UX by providing information the user might not know or could be confusing (e.g., homeserver choice). See [Use cases / scenarios](#use-cases--scenarios).
5. The invitation flows should automatically **assist the user to reach their goals**. An invitation from a regular user should therefore end with the new user having a conversation with the inviting user. An invitation to a particular room should end with the new user joining that room.
6. Users should never end up having **unverified devices** as these are a threat to integrity/security and the user needs to follow a couple of steps to recover from this situation. Therefore FTUE flows should ensure that additionally linked devices will be verified.
7. **User discovery** is not trivial in a federated environment. The app should therefore allow the user to make a conscious decision on which identifiers they want to share for other users to find them by. This way the user has choice over which data to share with the provider and simultaneously gets awareness on how others can find them.
8. Homeserver deployments will move fully to **native OIDC**. This needs to be respected in the FTUE flows.

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
8. [ask server if single device or additional device] Secure Messaging
	1. If no encryption or secure backup enabled => skip this step or set up secure messaging if first login
	2. Single device (and not first login) => Ask for recovery method to obtain 4S (offer to reset?) => can't be skipped
	3. Additional device => Ask for cross-signing with another device (QR code or 6-digit code comparison) or recovery method => can't be skipped
9. [message history and key backup are fetched from server, device is cross-signed (if applicable)]
10. [user attributes are pulled from the server, if possible]
11. [only on first login] How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
12. Ask to allow notifications
13. Ask for consent to analytics
14. User account summary (your name, avatar, MXID, etc.)
15. Element is set up, user sees their 'All chats' list 


### 1b) Regular user invitation

1. User receives an invite link and clicks it
2. Browser opens and loads Element Web or the mobile app is opened (platform-dependent)
	1. User doesn't have the app => Open app store and allow to install, then launch it
	2. User has the app => Launch it
3. [homeserver, inviting user MXID and/or other information are imported via clipboard in the background ]
4. Welcome screen
5. Simplified homeserver choice ("You are about to register on homeserver.tld"; continue/change)
6. Open web view overlay for registration (or redirect to IDM registration on Web/Desktop; OIDC flow; requires consent on iOS; see [Registration](#registration) for more details)
7. User creates account (including optional additional attributes; see [Additional user attributes](#additional-user-attributes) for more details)
8. Web view closes (or redirect back to Web/Desktop app), user is back in the app
9. [user is logged in]
10. [only on first login] How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
11. Ask to allow notifications
12. Ask for consent to analytics
13. User account summary (your name, avatar, MXID?, etc.)
14. Element is set up, user sees their 'All chats' list
15. A DM room with the inviting user (or a room join for the room/space invitation) is automatically set up

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
	1. If no encryption or secure backup enabled => skip this step or set up secure messaging if first login
	2. Single device => Ask for recovery method to obtain 4S (offer to reset?) => can't be skipped
	3. Additional device => Ask for cross-signing with another device (QR code or 6-digit code comparison) or recovery method => can't be skipped
6. [message history and key backup are fetched from server, device is cross-signed (if applicable)]
7. [only on first login] How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
8. Ask to allow notifications
9. Ask for consent to analytics
10. [only on first login] User account summary (your name, avatar, MXID?, etc.)
11. Element is fully set up, user sees their 'All chats' list

**C) Register new account**

1. Simplified homeserver choice ("You are about to register on matrix.org"; continue/change)
2. Open web view overlay for registration (or redirect to IDM registration on Web/Desktop; OIDC flow; requires consent on iOS; see [Registration](#registration) for more details)
3. User creates account (including optional additional attributes; see [Additional user attributes](#additional-user-attributes) for more details)
4. Web view closes (or redirect back to Web/Desktop app), user is back in the app
5. [user is logged in]
6. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs; see [How do you want others to find you?](#how-do-you-want-others-to-find-you) for more details)
7. Ask to allow notifications
8. Ask for consent to analytics
9. User account summary (your name, avatar, MXID?, etc.)
10. Element is fully set up, user sees their (empty) 'All chats' list
11. User gets hints on how to get started (start a conversation, join a public room, etc.)

## Related solution concepts

### Design for MAS-served components as part of OIDC flow
#### Login

For all login flows, the first entry point for a user is a web page served by MAS. There are different scenarios depending on the type of deployment:

- Using **integrated MAS-based login provider** (IdP) => users authenticate directly on the web page served by MAS
- Providing a **single upstream login provider** (IdP; e.g., Google) => MAS will ask for the user's mail address to determine the right login provider automatically and will redirect accordingly. If there is no internal user directory, MAS will transparently redirect the user to the upstream login provider to authenticate there (most common case for this scenario).
- Providing **multiple upstream login providers** (IdP; e.g., Google and Keycloak) => MAS will ask for the user's mail address to determine the right login provider automatically and will redirect accordingly. Additionally, MAS will provide a list of login providers and redirects depending on user choice to the respective upstream login provider to authenticate there.

As part of the flows involving upstream login providers, more sophisticated authentication security measures like 2FA, MFA, Brute-force protection, etc., can be employed, depending on the capabilities and configuration of the upstream login provider.

#### Registration

The options for registering a new user account depend on the respective user backend and the homeserver configuration.

- For a **MAS-backed** deployment (only using the internal user directory), the user creates their account directly on a web page served by MAS.
	- UserID
	- Password
	- E-Mail
	- E-Mail verification
	- Optional additional user attributes (see [Additional user attributes](#additional-user-attributes) for more details)
	- Captcha (configurable)
	- Accept T&Cs (configurable)
	- Consent to share account data with the client
	
- For a deployment **backed by LDAP or another external user backend**, we don't have direct access to account creation. We can provide a configurable link to a web page served by the external user backend which allows account creation.
- The homeserver can be configured to disallow registration. In this case Element should inform the user after the homeserver choice.

#### Branding

MAS should offer different branding capabilities based on the branding of the respective client connecting to it. This capability is part of the OIDC specification and will be used by different clients to give users identification and recognition during login/registration. Apart from that, the general MAS design will provide a 'powered by Matrix' logo to build the bridge to the Matrix protocol.

### Additional user attributes

- Display name
- Avatar
- Phone number
- etc.

The availability of additional user attributes depend on the deployment scenario and/or whether the user has supplied them. When asking for optional user attributes, the app should clarify what they can be used for.

### How do you want others to find you?

We can make a difference by giving the user choice over which identifiers they want to associate with their MXID to allow others to find them by. **For enterprise use cases** there should be a way to pre-configure/enforce this so that the user does not have the choice and does not see the screen during FTUE.

- Name
- Mail address
- Phone number
- etc.

As part of this process they might also need to accept T&C's for identity servers.

The identifiers to choose have to be available either by obtaining them automatically from IDM or by the user supplying them in a prior step. If the user didn't supply certain identifiers, those will be listed but disabled. The user can later supply them in their settings and 'manage account' views, respectively. Furthermore, the user can change the available identifiers for user discovery at any point in time.

### Homeserver settings to consider
- User registration enabled/disabled
- Restrict user invitations to administrators
- Allow/disallow users to change user attributes
- Force user attribute sharing for user discovery
- Link to external user management registration (see [Registration](#registration))
- Link to external 'manage account' view
- MAS registration options (T&Cs, privacy policy, captcha, etc.)
