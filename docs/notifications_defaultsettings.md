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

| Web Setting | Default | What does it mean | Push rules (see [predefined rules](https://spec.matrix.org/v1.6/client-server-api/#predefined-rules) |
|---|---|---|---|
| Enable Notifications for this account | On | Setting previously existed. No change. | `.m.rule.master` |
| Enable desktop notifications | Off | We have to ask permission before turning this on. The setting previously existed, there's no change. | N/A | 
| Show message preview in desktop notification | Off | Setting previously existed. No change. | N/A | 
| Enable audible notifications | On | Setting previously existed. No change. | N/A | 
| Default settings for all rooms | All messages | All messages in all rooms are set to "On" by default. There's more information on this decision [here](https://docs.google.com/document/d/1J6-XyVQsthkylffD20UrCFbWF_g9mao8JS2bhn5z1SU/edit#bookmark=id.ayc00ag4dkdj). | `.m.rule.encrypted_room_one_to_one`, `.m.rule.room_one_to_one`, `.m.rule.message`, `.m.rule.encrypted`, and maybe more. |
| Play a sound for | All messages | This is the equivalent of "Noisy". | N/A | 
| Invited to a room | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | `.m.rule.invite_for_me` | 
| New room activity, upgrades, and status messages | Off | This is a catch-all bucket. Better explanation pending discussion. | `.m.rule.tombstone` + new ones | 
| Messages sent by a bot | On | Setting previously existed. No change. | `.m.rule.suppress_notices` |
| Mentions when someone uses "@room" | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | `.m.rule.roomnotif` ([MCS3952](https://github.com/matrix-org/matrix-spec-proposals/pull/3952) defines `.m.rule.is_room_mention`) | 
| Mentions when someone uses "@displayname" | On | Setting previously existed. Its default is “On” and the “Noisy” aspect is determined by the user's Sound settings. | `.m.rule.contains_display_name` and `.m.rule.constains_user_name` (maybe?) ([MCS3952](https://github.com/matrix-org/matrix-spec-proposals/pull/3952) defines `.m.rule.is_user_mention`) | 
| Notify when someone users a keyword | On | There are no preset keywords configured. Setting previously existed. No change. | A custom rule is created for each keyword | 
| Email summary | Off | Setting previously existed. We should improve our emails before subjecting all users to them. | N/A | 
| This line is blank intentionally | N/A | N/A | N/A | 

## How this looks on Mobile

The Element X team is currently working on which settings they will show to users. The above list has been collaboratively designed by both the Web and Element X Mobile teams and therefore we will have platform parity at launch. 
When Element X Notifications Settings screens have been designed and built, this document should be updated and a new table added to the above section.

## The Work In Progress Design
While this work is still being built, we'll include the design here for reference:
| WIP |
|---|
| ![Web](https://user-images.githubusercontent.com/89144281/231469501-7ab7b530-e0e2-4e87-8caa-ebc62ec8f609.png) |

