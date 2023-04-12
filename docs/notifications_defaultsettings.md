# Default Notification Settings 

| Status | Last updated |
|--|--|
| In Progress | April 12, 2023 |

<hr />

## Objective

New Users should have default notification settings that make sense. They should be easy to grok, and easy to change. 

## Notifications

_Notification documentation is currently in progress. [Track along here (Internal only)](https://docs.google.com/document/d/1J6-XyVQsthkylffD20UrCFbWF_g9mao8JS2bhn5z1SU/edit?usp=sharing)_

## Global Settings

The Global Settings screen for Notifications has been redesigned. [The issue regarding these changes can be found here.](https://github.com/vector-im/element-web/issues/24567)

## Default Settings for new Users

| Web Setting | Default | What does it mean |
|---|---|---|
| Enable Notifications for this account | On | Setting previously existed. No change. | 
| Enable desktop notifications | Off | We have to ask permission before turning this on. The setting previously existed, there's no change. | 
| Show message preview in desktop notification | Off | Setting previously existed. No change. | 
| Enable audible notifications | On | Setting previously existed. No change. | 
| Default settings for all rooms | All messages | All messages in all rooms are set to "On" by default. There's more information on this decision [here](https://docs.google.com/document/d/1J6-XyVQsthkylffD20UrCFbWF_g9mao8JS2bhn5z1SU/edit#bookmark=id.ayc00ag4dkdj). |
| Play a sound for | All messages | This is the equivalent of "Noisy". | 
| Invited to a room | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | 
| New room activity, upgrades, and status messages | Off | This is a catch-all bucket. Better explanation pending discussion. | 
| Messages sent by a bot | On | Setting previously existed. No change. | 
| Mentions when someone uses "@room" | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | 
| Mentions when someone uses "@displayname" | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | 
| Notify when someone users a keyword | On | There are no preset keywords configured. Setting previously existed. No change.  | 
| Email summary | Off | Setting previously existed. We should improve our emails before subjecting all users to them. | 
| This line is blank intentionally | N/A | N/A | 

## How this looks on Mobile

The Element X team is currently working on which settings they will show to users. The above list has been collaboratively designed by both the Web and Element X Mobile teams and therefore we will have platform parity at launch. 
When Element X Notifications Settings screens have been designed and built, this document should be updated and a new table added to the above section.

## The Work In Progress Design
While this work is still being built, we'll include the design here for reference:
| WIP |
|---|
| ![Web](https://user-images.githubusercontent.com/89144281/231469501-7ab7b530-e0e2-4e87-8caa-ebc62ec8f609.png) |

