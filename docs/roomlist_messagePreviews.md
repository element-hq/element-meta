# Message Previews 

| Status | Last updated |
|--|--|
| In progress | April 12, 2023 |

<hr />

## Objective

Message previews appear in the room list and show users the latest activity in a room. 
This document outlines how they are used, and any complications or extensions to message previews. 

## Eligible Events
Certain events should not appear in the message previews 

| Event type | Included in message preview? | Notes | Status on Web | Status on Mobile | 
|---|---|---|---|---|
| New messages in the timeline | Yes | | ✅ | | 
| Reactions | Yes | In order for users to be able to determine whether a reaction is a message event emoji or a reaction event emoji we should prepend the text, ie: "Reacted with [emoji] | https://github.com/vector-im/element-web/issues/25083 | |
| Edits | Yes, if the last message in the room | | Currently displays all message edits, regardless of place in timeline (needs GH issue) | | 
| Message is deleted | Yes | | https://github.com/vector-im/element-web/issues/22334 | | 
| Polls | Awaiting input from Polls PM | | | |
| Audio and Video calls | Yes | Calls should show up in previews, either incoming or missed | Needs testing | | 
| Someone leaves the room | Yes | | Needs testing | | 
| A new users or bot joins the room | Yes | | Needs testing | | 
| Room change relating to the user | No | EG: Display name changes | Needs testing | |
| Room changes relating to the room itself | No | EG: Upgrade | Needs testing | |
| Threaded messages | Yes | They should be clearly in a thread | https://github.com/vector-im/element-web/issues/23920 | |
| Spoilers | Yes, but with hidden content | Needs a design | https://github.com/vector-im/element-web/issues/14447 | |
| Ignored user content | No | The user has been ignored, their messages should not show at all | https://github.com/vector-im/element-web/issues/16161 | |
| Draft message available in composer | Yes | This is an enhancement that has been raised by the community but not yet considered by teams | https://github.com/vector-im/element-web/issues/16769 | | 


## Web
On Web, Message Previews may be toggled on or off from the room list. User's may have different message preview preferences by room tag (favourites, people, rooms, low priority, etc.)
Many of the Element X ideals are not yet implemented on web due to time restrictions and lack of resources. Where parity does not exist, a GH issue should be available as work on the backlog.


