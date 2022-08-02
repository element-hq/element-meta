# io.element.functional_members: Marking room members as unimportant functional members

## Problem

Bots and bridges can be helpful assistants when chatting. Like a home assistant, they can provide information from the Internet, log events or teach room members to avoid inappropriate words. These bots listen to a conversations but are not a full participant. They are functional members helping out.

Direct Message rooms and those of small groups may not set a room name (`m.room.name`) so clients use the names of other room members to generate a dynamic title. When Alice and Bob are chatting, she sees the room as "Bob" and he sees the room as "Alice". When they add a bot, the room name becomes "Bob and Weather Bot" or "Alice and Weather Bot" respectively.

A key use case is the addition of audit bots, which an organisation may add because of regulatory requirements of having auditable log of their employee's conversations. This is a requirement 

## Proposal

This MSC adds the ability to exclude functional members from being present in room summaries like the dynamically generated name. 

We introduce the state event `io.element.functional_members`. It has no state key.

An example event is:

```json5
{
  "type": "io.element.functional_members",
  "state_key": "",
  "content": {
    "service_members": [
      "@slackbot:matrix.org"
    ]
  }
}
```

`service_members` is an optional array of strings. All strings should be Matrix user IDs. If the Matrix user ID of a room member is included in this list, the client should exclude the Matrix user from room summaries.

## Client advisory

When calculating a room name:

1. Read the room state of type `io.element.functional_members`. (no state key)
2. In the content, check if there's an array of strings called `service_members`.
3. Exclude those user ids from the name generation.

## Security considerations

A malicious actor could hide their room membership by setting this state event, therefore being less visible to other users. Mitigating this threat is the opposed goal of what this is trying to achieve and a balance has to be found.

At Element we decided to exclude functional users from the dynamic room name. This does not exclude them from the list of room members, making their presence visible to people investigating the room. Other events like invites, power level changes and messages of functional members are also not obscured in any way.

State events can commonly only be edited by room moderators, limiting the threat of a stranger hiding themselves. In Direct Message rooms, both room members are Administrators by default which would allow them to invite and hide a third party. However, the threat is not any higher than one member leaking the conversation otherwise. In contrast, by providing a way to declare functional members, people are encouraged to add bots as a room member visible to the other person.

## Related MSCs

[MSC2199](https://github.com/matrix-org/matrix-spec-proposals/pull/2199) describes Canonical DMs and adds a definition of `unimportant` users, which are likely going to accomplish the same.
However, it's still uncertain where MSC2199 is going.

## Implementations

* The `matrix-js-sdk` which powers Element Web and Desktop implemented this in July 2021.
  * https://github.com/matrix-org/matrix-js-sdk/pull/1771
* Element iOS implemented this in August 2021.
  * https://github.com/vector-im/element-ios/issues/4609
* Element Android is expected to implement this.
  * https://github.com/vector-im/element-android/issues/3736
