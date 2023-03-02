# First Time User Experience

This document aims to make first time user experience as simple as possible. FTUE refers to either the first registration/login of a user or to linking additional devices. All FTUE scenarios need to be covered within the initial setup of Element clients.

| Status | Last updated |
|--|--|
| Draft | March 1, 2023 |

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
5. (Login provider choice?)
6. Open web view overlay for login (or redirect to IdP on Web/Desktop; OIDC flow; requires consent on iOS)
7. User authenticates, web view closes (or redirect back to Web/Desktop app), user is back in the app
8. [user is logged in]
9. [user attributes are pulled from the server]
10. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs)
11. User account summary? (your name, avatar, etc.)
12. Element is set up, user sees their 'All chats' list 


### 1b) Regular user invitation

1. User receives an invite link and clicks it
2. Browser opens and loads Element Web or the mobile app is opened (platform-dependent)
	1. User doesn't have the app => Open app store and allow to install, then launch it
	2. User has the app => Launch it
3. [homeserver and/or other information are imported via clipboard in the background ]
4. Welcome screen
5. Simplified homeserver choice ("You are about to register on homeserver.tld"; continue/change)
6. (Login provider choice?)
7. Open web view overlay for registration (or redirect to IDM registration on Web/Desktop; OIDC flow; requires consent on iOS)
8. User creates account
9. User might get a verification token (e.g., via mail) and needs to supply it
10. Web view closes (or redirect back to Web/Desktop app), user is back in the app
11. [user is logged in]
12. Additional user attributes: display name, avatar, e-mail, phone number (user can skip)
13. How do you want others to find you? (which user identifiers to associate with MXID and upload to identity server; potentially ask for consent / accept T&Cs)
14. User account summary? (your name, avatar, etc.)
15. Element is set up, user sees their 'All chats' list 

### 2. Manual login / registration

1.  Welcome screen
2.  Let's get you set up (options)
	1.  Log in with another device (highlighted prominently)
	2.  Log in manually (email / username)
	3.  Register new account
3a.  Log in with another device (QR code flow)
	1.  ‘Scan QR code’ view is shown with camera view and advice => "open Element on another logged-in device and click ‘Link additional device’"; QR code is shown
	2.  User scans QR code
	3.  [user/homeserver information and recovery key are imported in the background]
	4.  [user is logged in]
	5.  [message history and key backup are fetched from server, device is cross-signed]
	6.  Element is fully set up, user sees their 'All chats' list
3b. Log in manually (email / username)
	1. Simplified homeserver choice ("You are about to sign in to your account on matrix.org"; continue/change)
	2. (Login provider choice?)
	3. Open web view overlay for login (or redirect to IdP on Web/Desktop; OIDC flow; requires consent on iOS)
	4. User authenticates, web view closes (or redirect back to Web/Desktop app), user is back in the app
	5. [user is logged in]
	6. [ask server if single device or additional device]
		0. If no encryption or secure backup enabled => skip this step
		1. Single device => Ask for recovery method to obtain 4S (offer to reset?) => can't be skipped
		2. Additional device => Ask for cross-signing with another device (QR code or 6-digit code comparison) => can't be skipped
	7. Element is fully set up, user sees their 'All chats' list
3c. Register new account
	TBC

## Related solution concepts

### How do you want others to find you

TBC
