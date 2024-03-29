# Moderating Rooms 

| Status | Last updated |
|--|--|
| Draft | May 2, 2022 |

<hr />

This document is an extension of the Matrix.org docs, [found here](https://matrix.org/docs/guides/moderation#power-levels)

## Room commands for joining, leaving, or kicking 

| Action | Command | Description | 
|---|---|---|
| Invite | /invite <user_id> | Invite a user to join the room you're in. Users can join public rooms without an invite, though sending them an invite will work too.| 
| Remove | /remove <user_id>  | Remove a user from the room you're in. User's can re-join if the room is public, or if you send them another Invite. This was previously known as "kick" | 
| Ban | /ban <user_id>  | The user is banned from the room you're in. The user cannot re-join unless "unbanned"| 
| Unban | /unban <user_id> | The user is no longer banned and may join the room if invited (or if it's a public room, they can join without an invite) |
| Join | /join <room_address> | You'll join the room specified in the room address. | 
| Part | /part  | You'll leave the room specified in the room address. If the room is public, you may rejoin. If the room is invite only, you will need to be invited to join again. |  

<hr />
From the Matrix.org website:
"The act of kicking a user temporarily removes them from the room. If the room is publicly joinable, the user can immediately rejoin it. If the room is invite-only, the user will need to be re-invited to join.
The act of banning a user stops them from joining a room until the ban is removed. Banning automatically kicks the user from the room"

Scenarios that may impact this decision: 
- Public rooms are public and, unless a user is banned, can be joined and left at will. 
- Invite-only rooms are invite only. The invite should 'count' once.
  - Imagine if a user is invited as they're joining a new team at work: That team's internal chat room is priavte and relevant to that team. If that user leaves the team and are removed, they should not be able to rejoin later. "Ban" does not work in this scenario as the user's mental model is that benning a user is a punishment for behaviour rather than a removal due to irrelevance and a bias for privacy. 
<hr /> 

This document is a result of the [issue here](https://github.com/vector-im/element-web/issues/3093) and may be extended or updated later.
