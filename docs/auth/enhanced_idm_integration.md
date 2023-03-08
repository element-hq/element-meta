# Enhanced IDM integration

This document aims to describe the product specification of the 'Enhanced IDM integration'. This commercial module should deliver advanced IDM integration functionalities targeted for larger organizations which enrich the basic FOSS feature set for user and identity management and make administration of larger deployments easier, more cost-efficient and user-friendly.

| Status | Last updated |
|--|--|
| Draft | March 8, 2023 |

## Story, context & use cases

1. As an administrator I want to manage users centrally in the IDM tool(s) of choice, for that I can control them and impose policies independent of the application.
2. As an organization I want that users can easily find each other via certain, known and usable identifiers and start communicating. As I have all these identifiers available in the IDM, I want applications to pick those up automatically to reduce maintenance cost and to prevent human error.
3. As an organization I want to make user onboarding and deboarding an automated process for that user adoption and satisfaction is high and for that the organization's policies are respected.

IDM is defined as the customer's user directory and/or identity management system. These can be one system or a combination of systems (LDAP / IdP / SCIM / etc.).

## Prerequisites

- Pull additional (arbitrary) user attributes from IDM with dynamic mappings (user state, avatar, phone number, mail address etc.)

## Features

- Regularly sync configured/mapped user attributes from IDM
	- Synapse (legacy) user DB
	- with MAS DB (Matrix Authentication Service)
	- with Identity Server DB (Sydent)
- IDM-backed user lifecycle management
	- User pre-provisioning
		- Automatically populate users in Synapse and Identity Servers (if applicable) once they become available in IDM
		- Allow to find and contact new users before they have logged-in for the first time (might require dehydrated devices features for encryption)
		- Automatically generate and send invitation links to new users to facilitate onboarding on the clients
	- User de-provisioning
		- Automatically disable user accounts if their state (e.g., disable/delete/remove from group) changes in IDM (block login or read-only access)
		- Configurable grace period before login gets blocked or the account is automatically deleted

## Side requirements

- The 'Enhanced IDM integration' should be delivered as a separate, commercial module.
- The 'Enhanced IDM integration' should be deployable together with (or on top of) MAS which delivers the basic IDM connectivity.
- Customers should only configure their IDM settings once and in one location. This should be used by advanced IDM components like 'Group Sync' or the 'Enhanced IDM integration'.
- The attribute sync interval should be configurable to cover different requirements towards performance and currency.

## Delivery models?
- on-premises
- cloud-hosted
- cloud-hosted + VPN link to an on-prem IDM
