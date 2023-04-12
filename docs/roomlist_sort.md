# Room list sorting on Web 

| Status | Last updated |
|--|--|
| In progress | April 12, 2023 |

<hr />

## Objective

The way the Web product sorts the room list is complicated and may be confusing. This document outlines the desired user experience of the room list and how it sorts depending on settings available.
The Element X team is changing the sorting on Mobile - when finalised, we will need to address how to bring the two platforms to parity. For the moment we're doing the best we can given the information and time available to us. 

## Sorting algorithms

| Setting | What happens | Muted rooms | 
|---|---|---|
| Sort by: A-Z | The room list is sorted alphabetically, regardless of notification settings or counts/activity | Muted rooms are mixed in |
| Sort by: A-Z and Show rooms with unread messages first | The room list is sorted alphabetically. Rooms with a highlight or notification count (red or grey) are A-Z, followed by all other rooms A-Z | Muted rooms are mixed in depending on their notification state |
| Sort by: Activity | Regardless of the count, the room list has the latest activity at the top of the list (where activity is [defined here](https://docs.google.com/document/d/1ryZjVuYBSfsu4e6fqYHIC9hJhY-aEWukcWMig1ewRA4/edit?usp=sharing)). | Muted rooms are not included in the sort, and they are at the bottom of each list. |
| Sort by: Activity and Show rooms with unread messages first | Rooms with a highlight count or notification count (red or grey) are at the top of the list, sorted by latest activity (where activity that impacts sorting from table above). These are followed by all other rooms. | Muted rooms are not included in the sort, and they are at the bottom of each list. |

## Muted Rooms
[More information can be found here](https://docs.google.com/document/d/1J6-XyVQsthkylffD20UrCFbWF_g9mao8JS2bhn5z1SU/edit#bookmark=id.4zqm2egzql0b)
When a user has muted a room they have actively told Element that they are not interested in seeing the updates available in that room. They do not wish to receive notifications from this muted room. In that case, it may be confusing to users to see that room always at the top of their room list (if it's a high activity room). Therefore, the decision was made to remove Muted rooms from the room sort. 

When a user puts a room on mute, the timestamp of that action should be considered as the 'lastest activity' in the activity sort and therefore, as other rooms have newer activity the muted room moves further down. If a user posts to the muted room, this latest message event is now the timestamp that should be considered for the activity. 
- The Element X team is building the room list from scratch and will be implementing this desired state. The Web team do not have this same advantage and will not be committing to this method immediately. [Track the Room Sort issues here](https://github.com/vector-im/element-web/issues/25032)
