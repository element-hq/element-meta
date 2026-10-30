# Localazy report

Usage of the Localazy strings by Element X Android (`develop` at [`b5832472`](https://github.com/element-hq/element-x-android/commit/b58324725868691ba4ab6ce1b24dc66924949b0c)) and Element X iOS (`develop` at [`d87d74d`](https://github.com/element-hq/element-x-ios/commit/d87d74d2c0e0fe8a2cf2b8ad10b3690e24c544cd)), generated on 2026-10-30, out of 1937 keys found in the English string files of both projects:

- [Unused strings](#unused-strings): **244** keys
- [Strings not used on Android](#strings-not-used-on-android): **188** keys
- [Strings not used on iOS](#strings-not-used-on-ios): **359** keys

How this was computed:
- Android: a key counts as used when it appears as a word in production `.kt`, `.kts` or `.xml` files (excluding `res/values*/`, `src/test`, `src/androidTest` and `tools/`).
- iOS: a key counts as used when its SwiftGen accessor (`L10n.xxx`) or the raw key literal appears in production `.swift` files (excluding `Sources/Generated`, `UnitTests`, `UITests`, `PreviewTests`, `IntegrationTests` and `AccessibilityTests`).
- Keys with the `_android` suffix are not imported in the iOS project, and keys with the `_ios` suffix are not imported in the Android project, so they are only checked on their platform.

Caveats: keys built dynamically at runtime are not detected, so check each key before you change it. A string used only in tests counts as unused.

## Unused strings

Strings used neither by Element X Android nor by Element X iOS. They can probably be removed from Localazy. **244** keys.

<details>
<summary>Show the 244 keys</summary>

| Key | English value | Localazy |
|---|---|---|
| `a11y.notifications_mentions_only` | Mentions only | [link](https://localazy.com/p/element/source-language?search=a11y.notifications_mentions_only&searchOptions=KEY,EXACT_MATCH) |
| `a11y.other_user_avatar` | Other user's avatar | [link](https://localazy.com/p/element/source-language?search=a11y.other_user_avatar&searchOptions=KEY,EXACT_MATCH) |
| `a11y.send_files` | Send files | [link](https://localazy.com/p/element/source-language?search=a11y.send_files&searchOptions=KEY,EXACT_MATCH) |
| `a11y.your_avatar` | Your avatar | [link](https://localazy.com/p/element/source-language?search=a11y.your_avatar&searchOptions=KEY,EXACT_MATCH) |
| `action_complete_verification` | Complete verification | [link](https://localazy.com/p/element/source-language?search=action_complete_verification&searchOptions=KEY,EXACT_MATCH) |
| `action.copy_link` | Copy link | [link](https://localazy.com/p/element/source-language?search=action.copy_link&searchOptions=KEY,EXACT_MATCH) |
| `action_deactivate` | Deactivate | [link](https://localazy.com/p/element/source-language?search=action_deactivate&searchOptions=KEY,EXACT_MATCH) |
| `action_deactivate_account` | Deactivate account | [link](https://localazy.com/p/element/source-language?search=action_deactivate_account&searchOptions=KEY,EXACT_MATCH) |
| `action.enable` | Enable | [link](https://localazy.com/p/element/source-language?search=action.enable&searchOptions=KEY,EXACT_MATCH) |
| `action.go_back` | Go back | [link](https://localazy.com/p/element/source-language?search=action.go_back&searchOptions=KEY,EXACT_MATCH) |
| `action.go_to_settings` | Go to settings | [link](https://localazy.com/p/element/source-language?search=action.go_to_settings&searchOptions=KEY,EXACT_MATCH) |
| `action.invites_list` | Invites | [link](https://localazy.com/p/element/source-language?search=action.invites_list&searchOptions=KEY,EXACT_MATCH) |
| `action_manage_account` | Manage account | [link](https://localazy.com/p/element/source-language?search=action_manage_account&searchOptions=KEY,EXACT_MATCH) |
| `action_manage_devices` | Manage devices | [link](https://localazy.com/p/element/source-language?search=action_manage_devices&searchOptions=KEY,EXACT_MATCH) |
| `action.minimize` | Minimise | [link](https://localazy.com/p/element/source-language?search=action.minimize&searchOptions=KEY,EXACT_MATCH) |
| `action.quote` | Quote | [link](https://localazy.com/p/element/source-language?search=action.quote&searchOptions=KEY,EXACT_MATCH) |
| `action_report_bug` | Report bug | [link](https://localazy.com/p/element/source-language?search=action_report_bug&searchOptions=KEY,EXACT_MATCH) |
| `action.report_dm` | Report conversation | [link](https://localazy.com/p/element/source-language?search=action.report_dm&searchOptions=KEY,EXACT_MATCH) |
| `action.retry_decryption` | Retry decryption | [link](https://localazy.com/p/element/source-language?search=action.retry_decryption&searchOptions=KEY,EXACT_MATCH) |
| `action.share_link` | Share link | [link](https://localazy.com/p/element/source-language?search=action.share_link&searchOptions=KEY,EXACT_MATCH) |
| `action_sign_in_again` | Sign in again | [link](https://localazy.com/p/element/source-language?search=action_sign_in_again&searchOptions=KEY,EXACT_MATCH) |
| `action.tap_for_options` | Tap for options | [link](https://localazy.com/p/element/source-language?search=action.tap_for_options&searchOptions=KEY,EXACT_MATCH) |
| `banner_migrate_to_native_sliding_sync_description` | Your server now supports a new, faster protocol. Log out and log back in to upgrade now. Doing this now will help you… | [link](https://localazy.com/p/element/source-language?search=banner_migrate_to_native_sliding_sync_description&searchOptions=KEY,EXACT_MATCH) |
| `banner_migrate_to_native_sliding_sync_force_logout_title` | Your account provider no longer supports the old protocol. Please sign out and sign back in to continue using the app. | [link](https://localazy.com/p/element/source-language?search=banner_migrate_to_native_sliding_sync_force_logout_title&searchOptions=KEY,EXACT_MATCH) |
| `banner_migrate_to_native_sliding_sync_title` | Upgrade available | [link](https://localazy.com/p/element/source-language?search=banner_migrate_to_native_sliding_sync_title&searchOptions=KEY,EXACT_MATCH) |
| `common_add_account` | Add an account | [link](https://localazy.com/p/element/source-language?search=common_add_account&searchOptions=KEY,EXACT_MATCH) |
| `common_bubbles` | Bubbles | [link](https://localazy.com/p/element/source-language?search=common_bubbles&searchOptions=KEY,EXACT_MATCH) |
| `common.chat_backup` | Chat backup | [link](https://localazy.com/p/element/source-language?search=common.chat_backup&searchOptions=KEY,EXACT_MATCH) |
| `common.decryption_error` | Decryption error | [link](https://localazy.com/p/element/source-language?search=common.decryption_error&searchOptions=KEY,EXACT_MATCH) |
| `common.direct_chat` | Direct chat | [link](https://localazy.com/p/element/source-language?search=common.direct_chat&searchOptions=KEY,EXACT_MATCH) |
| `common.forward_message` | Forward message | [link](https://localazy.com/p/element/source-language?search=common.forward_message&searchOptions=KEY,EXACT_MATCH) |
| `common.gif` | GIF | [link](https://localazy.com/p/element/source-language?search=common.gif&searchOptions=KEY,EXACT_MATCH) |
| `common.message_layout` | Message layout | [link](https://localazy.com/p/element/source-language?search=common.message_layout&searchOptions=KEY,EXACT_MATCH) |
| `common.modern` | Modern | [link](https://localazy.com/p/element/source-language?search=common.modern&searchOptions=KEY,EXACT_MATCH) |
| `common.or` | or | [link](https://localazy.com/p/element/source-language?search=common.or&searchOptions=KEY,EXACT_MATCH) |
| `common.permalink` | Permalink | [link](https://localazy.com/p/element/source-language?search=common.permalink&searchOptions=KEY,EXACT_MATCH) |
| `common.private_room` | Private room | [link](https://localazy.com/p/element/source-language?search=common.private_room&searchOptions=KEY,EXACT_MATCH) |
| `common.public_room` | Public room | [link](https://localazy.com/p/element/source-language?search=common.public_room&searchOptions=KEY,EXACT_MATCH) |
| `common.reaction` | Reaction | [link](https://localazy.com/p/element/source-language?search=common.reaction&searchOptions=KEY,EXACT_MATCH) |
| `common.refreshing` | Refreshing… | [link](https://localazy.com/p/element/source-language?search=common.refreshing&searchOptions=KEY,EXACT_MATCH) |
| `common.replying_to` | Replying to %1$s | [link](https://localazy.com/p/element/source-language?search=common.replying_to&searchOptions=KEY,EXACT_MATCH) |
| `common.rich_text_editor` | Rich text editor | [link](https://localazy.com/p/element/source-language?search=common.rich_text_editor&searchOptions=KEY,EXACT_MATCH) |
| `common.role` | Role | [link](https://localazy.com/p/element/source-language?search=common.role&searchOptions=KEY,EXACT_MATCH) |
| `common.room` | Room | [link](https://localazy.com/p/element/source-language?search=common.room&searchOptions=KEY,EXACT_MATCH) |
| `common.server_url` | Server URL | [link](https://localazy.com/p/element/source-language?search=common.server_url&searchOptions=KEY,EXACT_MATCH) |
| `common.suggested` | Suggested | [link](https://localazy.com/p/element/source-language?search=common.suggested&searchOptions=KEY,EXACT_MATCH) |
| `common.third_party_notices` | Third-party notices | [link](https://localazy.com/p/element/source-language?search=common.third_party_notices&searchOptions=KEY,EXACT_MATCH) |
| `common.unlock` | Unlock | [link](https://localazy.com/p/element/source-language?search=common.unlock&searchOptions=KEY,EXACT_MATCH) |
| `common.verification_cancelled` | Verification cancelled | [link](https://localazy.com/p/element/source-language?search=common.verification_cancelled&searchOptions=KEY,EXACT_MATCH) |
| `common.verify_device` | Verify device | [link](https://localazy.com/p/element/source-language?search=common.verify_device&searchOptions=KEY,EXACT_MATCH) |
| `common.verify_identity` | Verify identity | [link](https://localazy.com/p/element/source-language?search=common.verify_identity&searchOptions=KEY,EXACT_MATCH) |
| `common.waiting` | Waiting… | [link](https://localazy.com/p/element/source-language?search=common.waiting&searchOptions=KEY,EXACT_MATCH) |
| `common.your_account` | Your account | [link](https://localazy.com/p/element/source-language?search=common.your_account&searchOptions=KEY,EXACT_MATCH) |
| `crypto.history_visible` | This room has been configured so that new members can read history. %1$s | [link](https://localazy.com/p/element/source-language?search=crypto.history_visible&searchOptions=KEY,EXACT_MATCH) |
| `crypto.identity_change.pin_violation` | %1$s's digital identity was reset. %2$s | [link](https://localazy.com/p/element/source-language?search=crypto.identity_change.pin_violation&searchOptions=KEY,EXACT_MATCH) |
| `dialog_default_video_quality_selector_title` | Video upload quality | [link](https://localazy.com/p/element/source-language?search=dialog_default_video_quality_selector_title&searchOptions=KEY,EXACT_MATCH) |
| `dialog_title_success` | Success | [link](https://localazy.com/p/element/source-language?search=dialog_title_success&searchOptions=KEY,EXACT_MATCH) |
| `notification_channel_listening_for_events` | Listening for events | [link](https://localazy.com/p/element/source-language?search=notification_channel_listening_for_events&searchOptions=KEY,EXACT_MATCH) |
| `notification_compat_summary_line_for_room` | %1$s: %2$d messages | [link](https://localazy.com/p/element/source-language?search=notification_compat_summary_line_for_room&searchOptions=KEY,EXACT_MATCH) |
| `notification_fallback_content` | You have new messages. | [link](https://localazy.com/p/element/source-language?search=notification_fallback_content&searchOptions=KEY,EXACT_MATCH) |
| `notification_invitation_action_join` | Join | [link](https://localazy.com/p/element/source-language?search=notification_invitation_action_join&searchOptions=KEY,EXACT_MATCH) |
| `notification_invitation_action_reject` | Reject | [link](https://localazy.com/p/element/source-language?search=notification_invitation_action_reject&searchOptions=KEY,EXACT_MATCH) |
| `notification_invitations` | %d invitations | [link](https://localazy.com/p/element/source-language?search=notification_invitations&searchOptions=KEY,EXACT_MATCH) |
| `notification_mentioned_you_body` | Mentioned you: %1$s | [link](https://localazy.com/p/element/source-language?search=notification_mentioned_you_body&searchOptions=KEY,EXACT_MATCH) |
| `notification_new_messages` | New Messages | [link](https://localazy.com/p/element/source-language?search=notification_new_messages&searchOptions=KEY,EXACT_MATCH) |
| `notification_new_messages_for_room` | %d new messages | [link](https://localazy.com/p/element/source-language?search=notification_new_messages_for_room&searchOptions=KEY,EXACT_MATCH) |
| `notification_reaction_body` | Reacted with %1$s | [link](https://localazy.com/p/element/source-language?search=notification_reaction_body&searchOptions=KEY,EXACT_MATCH) |
| `notification_unread_notified_messages` | %d unread notified messages | [link](https://localazy.com/p/element/source-language?search=notification_unread_notified_messages&searchOptions=KEY,EXACT_MATCH) |
| `notification_unread_notified_messages_and_invitation` | %1$s and %2$s | [link](https://localazy.com/p/element/source-language?search=notification_unread_notified_messages_and_invitation&searchOptions=KEY,EXACT_MATCH) |
| `notification_unread_notified_messages_in_room` | %1$s in %2$s | [link](https://localazy.com/p/element/source-language?search=notification_unread_notified_messages_in_room&searchOptions=KEY,EXACT_MATCH) |
| `notification_unread_notified_messages_in_room_and_invitation` | %1$s in %2$s and %3$s | [link](https://localazy.com/p/element/source-language?search=notification_unread_notified_messages_in_room_and_invitation&searchOptions=KEY,EXACT_MATCH) |
| `notification_unread_notified_messages_in_room_rooms` | %d rooms | [link](https://localazy.com/p/element/source-language?search=notification_unread_notified_messages_in_room_rooms&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.composer_encrypted_placeholder` | Encrypted message… | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.composer_encrypted_placeholder&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.composer_unencrypted_placeholder` | Unencrypted message… | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.composer_unencrypted_placeholder&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.full_screen_toggle` | Toggle full screen mode | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.full_screen_toggle&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.open_compose_options` | Open compose options | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.open_compose_options&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_change` | Change account provider | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_change&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_form_hint` | Homeserver address | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_form_hint&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_form_notice` | Enter a search term or a domain address. | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_form_notice&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_form_subtitle` | Search for a company, community, or private server. | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_form_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_form_title` | Find an account provider | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_form_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_signin_subtitle` | This is where your conversations will live — just like you would use an email provider to keep your emails. | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_signin_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_signup_subtitle` | This is where your conversations will live — just like you would use an email provider to keep your emails. | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_signup_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_signup_title` | You’re about to create an account on %s | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_signup_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_developer_mode` | Developer mode | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_developer_mode&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_developer_mode_description` | Enable to have access to features and functionality for developers. | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_developer_mode_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_hide_timeline_media_toggle_title` | Hide media previews in timeline | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_hide_timeline_media_toggle_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_moderation_and_safety_section_title` | Moderation and Safety | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_moderation_and_safety_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_rich_text_editor_description` | Disable the rich text editor to type Markdown manually. | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_rich_text_editor_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_send_read_receipts` | Read receipts | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_send_read_receipts&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_send_read_receipts_description` | If turned off, your read receipts won't be sent to anyone. You will still receive read receipts from other users. | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_send_read_receipts_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.bottom_sheet.manage_room_member.remove_confirmation_title` | Remove member and ban from joining in the future? | [link](https://localazy.com/p/element/source-language?search=screen.bottom_sheet.manage_room_member.remove_confirmation_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_editor_supporting` | If possible, please write the description in English. | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_editor_supporting&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_include_crash_logs` | Send crash logs | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_include_crash_logs&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_rash_logs_alert_title` | %1$s crashed the last time it was used. Would you like to share a crash report with us? | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_rash_logs_alert_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_account_provider_matrix_org_subtitle` | Matrix.org is a large, free server on the public Matrix network for secure, decentralised communication, run by the M… | [link](https://localazy.com/p/element/source-language?search=screen_change_account_provider_matrix_org_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_account_provider_other` | Other | [link](https://localazy.com/p/element/source-language?search=screen_change_account_provider_other&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_account_provider_subtitle` | Use a different account provider, such as your own private server or a work account. | [link](https://localazy.com/p/element/source-language?search=screen_change_account_provider_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_account_provider_title` | Change account provider | [link](https://localazy.com/p/element/source-language?search=screen_change_account_provider_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_server_form_header` | Homeserver URL | [link](https://localazy.com/p/element/source-language?search=screen_change_server_form_header&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_server_form_notice` | Enter a domain address. | [link](https://localazy.com/p/element/source-language?search=screen_change_server_form_notice&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_server_subtitle` | What is the address of your server? | [link](https://localazy.com/p/element/source-language?search=screen_change_server_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.change_server.title` | Select your server | [link](https://localazy.com/p/element/source-language?search=screen.change_server.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_chat_backup_key_backup_action_enable` | Turn on backup | [link](https://localazy.com/p/element/source-language?search=screen_chat_backup_key_backup_action_enable&searchOptions=KEY,EXACT_MATCH) |
| `screen_chat_backup_key_storage_toggle_description` | Upload keys from this device | [link](https://localazy.com/p/element/source-language?search=screen_chat_backup_key_storage_toggle_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_1` | Open %1$s on a desktop device | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_1&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_2` | Sign into your account again | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_2&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_3` | When asked to verify your device, select %1$s | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_3&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_3_reset_all` | “Reset all” | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_3_reset_all&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_4` | Follow the instructions to create a new recovery key | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_4&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_list_item_5` | Save your new recovery key in a password manager or encrypted note | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_list_item_5&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_new_recovery_key_title` | Reset the encryption for your account using another device | [link](https://localazy.com/p/element/source-language?search=screen_create_new_recovery_key_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_room_private_option_description` | Only people invited can join. | [link](https://localazy.com/p/element/source-language?search=screen_create_room_private_option_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_room_private_option_title` | Private | [link](https://localazy.com/p/element/source-language?search=screen_create_room_private_option_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_room_public_option_description` | Anyone can find this room. You can change this anytime in room settings. | [link](https://localazy.com/p/element/source-language?search=screen_create_room_public_option_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_room.public_option_short_description` | Anyone can join, including people outside your organisation. | [link](https://localazy.com/p/element/source-language?search=screen.create_room.public_option_short_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_room_public_option_title` | Public | [link](https://localazy.com/p/element/source-language?search=screen_create_room_public_option_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_room.room_visibility_section_title` | Room visibility | [link](https://localazy.com/p/element/source-language?search=screen.create_room.room_visibility_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_room.space_selection_no_space_description` | (no space) | [link](https://localazy.com/p/element/source-language?search=screen.create_room.space_selection_no_space_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.confirm.error.mismatch` | The recovery key you entered doesn't match | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.confirm.error.mismatch&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.confirm.submit` | Finish setup | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.confirm.submit&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.confirm.subtitle` | Enter your recovery key again. | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.confirm.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.confirm.title` | Confirm your recovery key | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.confirm.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.notice` | Minimum %1$d characters. Do not use your account password | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.notice&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength` | Strength | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.a11y` | Passphrase strength: %1$s | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.a11y&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.moderate` | Moderate | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.moderate&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.strong` | Strong | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.strong&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.very_strong` | Very strong | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.very_strong&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.very_weak` | Very weak | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.very_weak&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.strength.weak` | Weak | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.strength.weak&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.subtitle` | Choose a recovery key that you can memorize. | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.input.title` | Enter a recovery key | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.input.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.loading.a11y` | Loading recovery key requirements | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.loading.a11y&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.success.notice` | To change your recovery key, go to Settings → Encryption → Backup | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.success.notice&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.success.subtitle` | You can use your recovery key to confirm new devices or restore your encrypted chats if you lose access to all your d… | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.success.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.custom_recovery_key.success.title` | Your backup is now fully set up | [link](https://localazy.com/p/element/source-language?search=screen.custom_recovery_key.success.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_encryption_reset_bullet_4` | Any devices you’re signed in to will need to be reconfirmed | [link](https://localazy.com/p/element/source-language?search=screen_encryption_reset_bullet_4&searchOptions=KEY,EXACT_MATCH) |
| `screen_encryption_reset_no_chats_message` | It looks like you don’t have any chats yet. If this is correct, you can safely proceed with resetting your digital id… | [link](https://localazy.com/p/element/source-language?search=screen_encryption_reset_no_chats_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_encryption_reset_no_options_subtitle` | You don’t have access to any other verified devices or a recovery key, so you’ll need to reset your digital identity … | [link](https://localazy.com/p/element/source-language?search=screen_encryption_reset_no_options_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_encryption_reset_no_options_title` | You need to reset your digital identity | [link](https://localazy.com/p/element/source-language?search=screen_encryption_reset_no_options_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_encryption_reset_subtitle` | If you don’t have access to any other verified devices and you don’t have your recovery key, then you’ll need to rese… | [link](https://localazy.com/p/element/source-language?search=screen_encryption_reset_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_confirmation_create_new_recovery_key` | Create a new recovery key | [link](https://localazy.com/p/element/source-language?search=screen_identity_confirmation_create_new_recovery_key&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_waiting_on_other_device` | Waiting on other device… | [link](https://localazy.com/p/element/source-language?search=screen_identity_waiting_on_other_device&searchOptions=KEY,EXACT_MATCH) |
| `screen_invites_empty_list` | No Invites | [link](https://localazy.com/p/element/source-language?search=screen_invites_empty_list&searchOptions=KEY,EXACT_MATCH) |
| `screen_join_room_space_not_supported_description` | %1$s does not support spaces yet. You can access spaces on web. | [link](https://localazy.com/p/element/source-language?search=screen_join_room_space_not_supported_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_join_room_space_not_supported_title` | Spaces are not supported yet | [link](https://localazy.com/p/element/source-language?search=screen_join_room_space_not_supported_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_join_room_subtitle_knock` | Tap the button below and a chat administrator will be notified. You'll be able to join the conversation once approved. | [link](https://localazy.com/p/element/source-language?search=screen_join_room_subtitle_knock&searchOptions=KEY,EXACT_MATCH) |
| `screen_join_room_subtitle_no_preview` | You must be a member of this room to view the message history. | [link](https://localazy.com/p/element/source-language?search=screen_join_room_subtitle_no_preview&searchOptions=KEY,EXACT_MATCH) |
| `screen_join_room_title_knock` | Want to join this room? | [link](https://localazy.com/p/element/source-language?search=screen_join_room_title_knock&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.app_not_supported.subtitle` | Your account provider does not support %1$s. | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.app_not_supported.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.app_not_supported.title` | %1$s not supported | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.app_not_supported.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_login_error_invalid_user_id` | This is not a valid user identifier. Expected format: ‘@user:homeserver.org’ | [link](https://localazy.com/p/element/source-language?search=screen_login_error_invalid_user_id&searchOptions=KEY,EXACT_MATCH) |
| `screen_login_title` | Welcome back! | [link](https://localazy.com/p/element/source-language?search=screen_login_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.processing` | Processing… | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.processing&searchOptions=KEY,EXACT_MATCH) |
| `screen_migration_message` | This is a one time process, thanks for waiting. | [link](https://localazy.com/p/element/source-language?search=screen_migration_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_migration_title` | Setting up your account. | [link](https://localazy.com/p/element/source-language?search=screen_migration_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_mentions_section_title` | Mentions | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_mentions_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_onboarding_welcome_subtitle` | Welcome to %1$s. Supercharged, for speed and simplicity. | [link](https://localazy.com/p/element/source-language?search=screen_onboarding_welcome_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_qr_code_login_start_over_button` | Start over | [link](https://localazy.com/p/element/source-language?search=screen_qr_code_login_start_over_button&searchOptions=KEY,EXACT_MATCH) |
| `screen_recovery_key_confirm_create_new_recovery_key` | Create new recovery key | [link](https://localazy.com/p/element/source-language?search=screen_recovery_key_confirm_create_new_recovery_key&searchOptions=KEY,EXACT_MATCH) |
| `screen_recovery_key_confirm_lost_recovery_key` | Lost your recovery key? | [link](https://localazy.com/p/element/source-language?search=screen_recovery_key_confirm_lost_recovery_key&searchOptions=KEY,EXACT_MATCH) |
| `screen_recovery_key_success_title` | Your new recovery key is now active | [link](https://localazy.com/p/element/source-language?search=screen_recovery_key_success_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_reset_identity_confirmation_subtitle` | You're about to go to your %1$s account to reset your digital identity. Afterwards you'll be taken back to the app. | [link](https://localazy.com/p/element/source-language?search=screen_reset_identity_confirmation_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_reset_identity_confirmation_title` | Can't confirm? Go to your account to reset your digital identity. | [link](https://localazy.com/p/element/source-language?search=screen_reset_identity_confirmation_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_change_permissions.change_settings` | Change settings | [link](https://localazy.com/p/element/source-language?search=screen.room_change_permissions.change_settings&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_confirm_demote_self_action` | Demote | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_confirm_demote_self_action&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_confirm_demote_self_title` | Demote yourself? | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_confirm_demote_self_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_invited_member_name` | %1$s (Pending) | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_invited_member_name&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_details.audio_push_to_talk` | Push to talk | [link](https://localazy.com/p/element/source-language?search=screen.room_details.audio_push_to_talk&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_details.audio_title` | Room Audio | [link](https://localazy.com/p/element/source-language?search=screen.room_details.audio_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_details.audio_video_calls` | Video calls | [link](https://localazy.com/p/element/source-language?search=screen.room_details.audio_video_calls&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_leave_conversation_title` | Leave conversation | [link](https://localazy.com/p/element/source-language?search=screen_room_details_leave_conversation_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_room_name_label` | Name | [link](https://localazy.com/p/element/source-language?search=screen_room_details_room_name_label&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_topic_title` | Topic | [link](https://localazy.com/p/element/source-language?search=screen_room_details_topic_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_encrypted_history_banner` | Message history is currently unavailable. | [link](https://localazy.com/p/element/source-language?search=screen_room_encrypted_history_banner&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_encrypted_history_banner_unverified` | Message history is unavailable in this room. Verify this device to see your message history. | [link](https://localazy.com/p/element/source-language?search=screen_room_encrypted_history_banner_unverified&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_error_failed_retrieving_user_details` | Could not retrieve user details | [link](https://localazy.com/p/element/source-language?search=screen_room_error_failed_retrieving_user_details&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_event_pill` | Message in %1$s | [link](https://localazy.com/p/element/source-language?search=screen_room_event_pill&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_verify_button_subtitle` | Use the web app to verify this user. | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_verify_button_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_verify_button_title` | Verify %1$s | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_verify_button_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_banned_empty` | There are no banned users. | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_banned_empty&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_manage_member_remove_confirmation_ban` | Ban user | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_manage_member_remove_confirmation_ban&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_manage_member_remove_confirmation_kick` | Only remove member | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_manage_member_remove_confirmation_kick&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_manage_member_unban_action` | Unban | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_manage_member_unban_action&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_manage_member_unban_message` | They will be able to join this room again if invited. | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_manage_member_unban_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_manage_member_unban_title` | Unban user | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_manage_member_unban_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_room_members_header_title` | Room members | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_room_members_header_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_list_unbanning_user` | Unbanning %1$s | [link](https://localazy.com/p/element/source-language?search=screen_room_member_list_unbanning_user&searchOptions=KEY,EXACT_MATCH) |
| `screen.room.mentions_at_room_subtitle` | Notify the whole room | [link](https://localazy.com/p/element/source-language?search=screen.room.mentions_at_room_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_retry_send_menu_send_again_action` | Send again | [link](https://localazy.com/p/element/source-language?search=screen_room_retry_send_menu_send_again_action&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_retry_send_menu_title` | Your message failed to send | [link](https://localazy.com/p/element/source-language?search=screen_room_retry_send_menu_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_roles_and_permissions_member_moderation` | Member moderation | [link](https://localazy.com/p/element/source-language?search=screen_room_roles_and_permissions_member_moderation&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_roles_and_permissions_messages_and_content` | Messages and content | [link](https://localazy.com/p/element/source-language?search=screen_room_roles_and_permissions_messages_and_content&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_roles_and_permissions_room_details` | Room details | [link](https://localazy.com/p/element/source-language?search=screen_room_roles_and_permissions_room_details&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_roles_and_permissions.space_details` | Space details | [link](https://localazy.com/p/element/source-language?search=screen.room_roles_and_permissions.space_details&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_voice_message_tooltip` | Hold to record | [link](https://localazy.com/p/element/source-language?search=screen_room_voice_message_tooltip&searchOptions=KEY,EXACT_MATCH) |
| `screen_roomlist_a11y_create_message` | Create a new conversation or room | [link](https://localazy.com/p/element/source-language?search=screen_roomlist_a11y_create_message&searchOptions=KEY,EXACT_MATCH) |
| `screen.security_and_privacy.room_directory_visibility_section_footer` | Allow for this room to be found by searching %1$s public room directory | [link](https://localazy.com/p/element/source-language?search=screen.security_and_privacy.room_directory_visibility_section_footer&searchOptions=KEY,EXACT_MATCH) |
| `screen.security_and_privacy.room_publishing_section_footer` | Room addresses are ways to find and access rooms. This also ensures you can easily share your room with others. You c… | [link](https://localazy.com/p/element/source-language?search=screen.security_and_privacy.room_publishing_section_footer&searchOptions=KEY,EXACT_MATCH) |
| `screen.security_and_privacy.room_publishing_section_header` | Room publishing | [link](https://localazy.com/p/element/source-language?search=screen.security_and_privacy.room_publishing_section_header&searchOptions=KEY,EXACT_MATCH) |
| `screen.select_account.permalink.room.subtitle` | None of your accounts have joined this room yet, choose which one to use. | [link](https://localazy.com/p/element/source-language?search=screen.select_account.permalink.room.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.select_account.permalink.title` | Select an account to open the link: | [link](https://localazy.com/p/element/source-language?search=screen.select_account.permalink.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_change_server` | Change account provider | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_change_server&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_message_login_element_dot_io` | A private server for Element employees. | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_message_login_element_dot_io&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_message_login_matrix_dot_org` | Matrix is an open network for secure, decentralised communication. | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_message_login_matrix_dot_org&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_message_register` | This is where your conversations will live — just like you would use an email provider to keep your emails. | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_message_register&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_title_login` | You’re about to sign in to %1$s | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_title_login&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_title_register` | You’re about to create an account on %1$s | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_title_register&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_cancelled_subtitle` | Something doesn’t seem right. Either the request timed out or the request was denied. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_cancelled_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_enter_recovery_key` | Enter recovery key | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_enter_recovery_key&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_open_existing_session_subtitle` | Prove it’s you in order to access your encrypted message history. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_open_existing_session_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_open_existing_session_title` | Open an existing session | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_open_existing_session_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_positive_button_canceled` | Retry verification | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_positive_button_canceled&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_positive_button_initial` | I am ready | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_positive_button_initial&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_accepted_subtitle` | Compare the unique emoji, ensuring they appear in the same order. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_accepted_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_success_subtitle` | Now you can read or send messages securely on your other device. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_success_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_success_title` | Device verified | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_success_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_unavailable_subtitle` | Please use another device or recovery key. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_unavailable_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_unavailable_title` | Verification with this device is currently unavailable | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_unavailable_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_another_device_subtitle` | You should see a popup on the other device. Start the verification from there now. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_another_device_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_other_device_title` | Start verification on the other device | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_other_device_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_to_accept_subtitle` | Accept the request to start the verification process in your other session to continue. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_to_accept_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_to_accept_title` | Waiting to accept request | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_to_accept_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_subtitle` | You might have been signed out for one of the reasons listed below. Please sign in again to continue using %s. | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_other_verified_device_dialog_content` | Make sure you always have access to another verified device or your recovery key to avoid losing your encrypted chat … | [link](https://localazy.com/p/element/source-language?search=screen_signout_other_verified_device_dialog_content&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_other_verified_device_dialog_title` | Are you sure you want to remove this device? | [link](https://localazy.com/p/element/source-language?search=screen_signout_other_verified_device_dialog_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_save_recovery_key_action_continue` | Continue to remove this device | [link](https://localazy.com/p/element/source-language?search=screen_signout_save_recovery_key_action_continue&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_save_recovery_key_action_generate` | Generate new recovery key | [link](https://localazy.com/p/element/source-language?search=screen_signout_save_recovery_key_action_generate&searchOptions=KEY,EXACT_MATCH) |
| `screen.space.add_room_action` | Room | [link](https://localazy.com/p/element/source-language?search=screen.space.add_room_action&searchOptions=KEY,EXACT_MATCH) |
| `screen.space_list.parent_space` | %1$s space | [link](https://localazy.com/p/element/source-language?search=screen.space_list.parent_space&searchOptions=KEY,EXACT_MATCH) |
| `session_verification_banner_message` | Looks like you’re using a new device. Verify with another device to access your encrypted messages. | [link](https://localazy.com/p/element/source-language?search=session_verification_banner_message&searchOptions=KEY,EXACT_MATCH) |
| `session_verification_banner_title` | Verify it’s you | [link](https://localazy.com/p/element/source-language?search=session_verification_banner_title&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.error` | Command error | [link](https://localazy.com/p/element/source-language?search=slash_command.error&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.error.discard_session_not_handled` | Only supported in encrypted rooms | [link](https://localazy.com/p/element/source-language?search=slash_command.error.discard_session_not_handled&searchOptions=KEY,EXACT_MATCH) |
| `state_event_demoted_to_member` | %1$s was demoted to member | [link](https://localazy.com/p/element/source-language?search=state_event_demoted_to_member&searchOptions=KEY,EXACT_MATCH) |
| `state_event_demoted_to_moderator` | %1$s was demoted to moderator | [link](https://localazy.com/p/element/source-language?search=state_event_demoted_to_moderator&searchOptions=KEY,EXACT_MATCH) |
| `state_event_promoted_to_administrator` | %1$s was promoted to admin | [link](https://localazy.com/p/element/source-language?search=state_event_promoted_to_administrator&searchOptions=KEY,EXACT_MATCH) |
| `state_event_promoted_to_moderator` | %1$s was promoted to moderator | [link](https://localazy.com/p/element/source-language?search=state_event_promoted_to_moderator&searchOptions=KEY,EXACT_MATCH) |
| `state_event_room_unknown_membership_change` | %1$s made an unknown change to their membership | [link](https://localazy.com/p/element/source-language?search=state_event_room_unknown_membership_change&searchOptions=KEY,EXACT_MATCH) |
| `test_language_identifier` | en | [link](https://localazy.com/p/element/source-language?search=test_language_identifier&searchOptions=KEY,EXACT_MATCH) |
| `test_untranslated_default_language_identifier` | en | [link](https://localazy.com/p/element/source-language?search=test_untranslated_default_language_identifier&searchOptions=KEY,EXACT_MATCH) |
| `timeline.decryption_failure.historical_event_user_not_joined` | You don't have access to this message | [link](https://localazy.com/p/element/source-language?search=timeline.decryption_failure.historical_event_user_not_joined&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_detect_push_provider_success` | Found %1$d push providers: %2$s | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_detect_push_provider_success&searchOptions=KEY,EXACT_MATCH) |

</details>

## Strings not used on Android

Strings used by Element X iOS but not by Element X Android. Keys with the `_android` suffix can probably be removed. For the other keys, this can be a difference between the implementations of both projects, or a feature not implemented yet on Android. If the difference is expected, the key can be renamed with the `_ios` suffix. **188** keys.

<details>
<summary>Show the 188 keys</summary>

| Key | English value | Localazy |
|---|---|---|
| `dialog_unsaved_changes_description_android` | Your changes have not been saved. Are you sure you want to go back? | [link](https://localazy.com/p/element/source-language?search=dialog_unsaved_changes_description_android&searchOptions=KEY,EXACT_MATCH) |
| `login_initial_device_name_android` | %1$s Android | [link](https://localazy.com/p/element/source-language?search=login_initial_device_name_android&searchOptions=KEY,EXACT_MATCH) |
| `push_distributor_background_sync_android` | Background synchronisation | [link](https://localazy.com/p/element/source-language?search=push_distributor_background_sync_android&searchOptions=KEY,EXACT_MATCH) |
| `push_distributor_firebase_android` | Google Services | [link](https://localazy.com/p/element/source-language?search=push_distributor_firebase_android&searchOptions=KEY,EXACT_MATCH) |
| `push_no_valid_google_play_services_apk_android` | No valid Google Play Services found. Notifications may not work properly. | [link](https://localazy.com/p/element/source-language?search=push_no_valid_google_play_services_apk_android&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_poll_cancel_confirmation_content_android` | Your changes have not been saved. Are you sure you want to go back? | [link](https://localazy.com/p/element/source-language?search=screen_create_poll_cancel_confirmation_content_android&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_invited_member_name_android` | (Pending) | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_invited_member_name_android&searchOptions=KEY,EXACT_MATCH) |
| `Notification` | Notification | [link](https://localazy.com/p/element/source-language?search=Notification&searchOptions=KEY,EXACT_MATCH) |
| `a11y.add_avatar` | Add avatar | [link](https://localazy.com/p/element/source-language?search=a11y.add_avatar&searchOptions=KEY,EXACT_MATCH) |
| `a11y.add_reaction` | Add reaction: %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.add_reaction&searchOptions=KEY,EXACT_MATCH) |
| `a11y.address` | Address | [link](https://localazy.com/p/element/source-language?search=a11y.address&searchOptions=KEY,EXACT_MATCH) |
| `a11y.custom_emoji` | Custom emoji | [link](https://localazy.com/p/element/source-language?search=a11y.custom_emoji&searchOptions=KEY,EXACT_MATCH) |
| `a11y.edit_room_address_hint` | The full address will be %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.edit_room_address_hint&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_attachment` | Gallery, attachment %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_attachment&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_failed_scan` | Gallery, failed scan %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_failed_scan&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_image` | Gallery, image %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_image&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_more_media` | Gallery, %1$d more medias | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_more_media&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_scanning` | Gallery, scanning %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_scanning&searchOptions=KEY,EXACT_MATCH) |
| `a11y.gallery_video` | Gallery, video %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.gallery_video&searchOptions=KEY,EXACT_MATCH) |
| `a11y.join_call` | Join call | [link](https://localazy.com/p/element/source-language?search=a11y.join_call&searchOptions=KEY,EXACT_MATCH) |
| `a11y_jump_to_unread` | Jump to unread | [link](https://localazy.com/p/element/source-language?search=a11y_jump_to_unread&searchOptions=KEY,EXACT_MATCH) |
| `a11y.paused_voice_message` | Voice message, duration: %1$s, current position: %2$s | [link](https://localazy.com/p/element/source-language?search=a11y.paused_voice_message&searchOptions=KEY,EXACT_MATCH) |
| `a11y.pinned_location` | Pinned location | [link](https://localazy.com/p/element/source-language?search=a11y.pinned_location&searchOptions=KEY,EXACT_MATCH) |
| `a11y.playback_speed` | Playback speed | [link](https://localazy.com/p/element/source-language?search=a11y.playback_speed&searchOptions=KEY,EXACT_MATCH) |
| `a11y.polls.will_remove_selection` | Will remove previous selection | [link](https://localazy.com/p/element/source-language?search=a11y.polls.will_remove_selection&searchOptions=KEY,EXACT_MATCH) |
| `a11y.qr_code` | QR Code | [link](https://localazy.com/p/element/source-language?search=a11y.qr_code&searchOptions=KEY,EXACT_MATCH) |
| `a11y.remove_reaction` | Remove reaction: %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.remove_reaction&searchOptions=KEY,EXACT_MATCH) |
| `a11y.sender_location` | Sender location | [link](https://localazy.com/p/element/source-language?search=a11y.sender_location&searchOptions=KEY,EXACT_MATCH) |
| `a11y.start_video_call` | Start a video call | [link](https://localazy.com/p/element/source-language?search=a11y.start_video_call&searchOptions=KEY,EXACT_MATCH) |
| `a11y.status` | Status | [link](https://localazy.com/p/element/source-language?search=a11y.status&searchOptions=KEY,EXACT_MATCH) |
| `a11y.tombstoned_room` | Tombstoned room | [link](https://localazy.com/p/element/source-language?search=a11y.tombstoned_room&searchOptions=KEY,EXACT_MATCH) |
| `a11y.view_avatar` | View avatar | [link](https://localazy.com/p/element/source-language?search=a11y.view_avatar&searchOptions=KEY,EXACT_MATCH) |
| `action.add_to_timeline` | Add to timeline | [link](https://localazy.com/p/element/source-language?search=action.add_to_timeline&searchOptions=KEY,EXACT_MATCH) |
| `action.choose_file` | Choose file | [link](https://localazy.com/p/element/source-language?search=action.choose_file&searchOptions=KEY,EXACT_MATCH) |
| `action.enter_pin` | Enter PIN | [link](https://localazy.com/p/element/source-language?search=action.enter_pin&searchOptions=KEY,EXACT_MATCH) |
| `action.forgot_password` | Forgot password? | [link](https://localazy.com/p/element/source-language?search=action.forgot_password&searchOptions=KEY,EXACT_MATCH) |
| `action.forward_messages` | Forward %1$d messages | [link](https://localazy.com/p/element/source-language?search=action.forward_messages&searchOptions=KEY,EXACT_MATCH) |
| `action.invite_people_to_app` | Invite people to %1$s | [link](https://localazy.com/p/element/source-language?search=action.invite_people_to_app&searchOptions=KEY,EXACT_MATCH) |
| `action.next` | Next | [link](https://localazy.com/p/element/source-language?search=action.next&searchOptions=KEY,EXACT_MATCH) |
| `action.quick_reply` | Quick reply | [link](https://localazy.com/p/element/source-language?search=action.quick_reply&searchOptions=KEY,EXACT_MATCH) |
| `action.react` | React | [link](https://localazy.com/p/element/source-language?search=action.react&searchOptions=KEY,EXACT_MATCH) |
| `action.start_over` | Start over | [link](https://localazy.com/p/element/source-language?search=action.start_over&searchOptions=KEY,EXACT_MATCH) |
| `action.translate` | Translate | [link](https://localazy.com/p/element/source-language?search=action.translate&searchOptions=KEY,EXACT_MATCH) |
| `action.voice_call` | Voice call | [link](https://localazy.com/p/element/source-language?search=action.voice_call&searchOptions=KEY,EXACT_MATCH) |
| `action.yes_try_again` | Yes, try again | [link](https://localazy.com/p/element/source-language?search=action.yes_try_again&searchOptions=KEY,EXACT_MATCH) |
| `common.chats` | Chats | [link](https://localazy.com/p/element/source-language?search=common.chats&searchOptions=KEY,EXACT_MATCH) |
| `common.download_failed` | Download failed | [link](https://localazy.com/p/element/source-language?search=common.download_failed&searchOptions=KEY,EXACT_MATCH) |
| `common.emote` | * %1$s %2$s | [link](https://localazy.com/p/element/source-language?search=common.emote&searchOptions=KEY,EXACT_MATCH) |
| `common.everyone` | Everyone | [link](https://localazy.com/p/element/source-language?search=common.everyone&searchOptions=KEY,EXACT_MATCH) |
| `common.file_deleted` | File deleted | [link](https://localazy.com/p/element/source-language?search=common.file_deleted&searchOptions=KEY,EXACT_MATCH) |
| `common.file_saved` | File saved | [link](https://localazy.com/p/element/source-language?search=common.file_saved&searchOptions=KEY,EXACT_MATCH) |
| `common.frequently_used` | Frequently used | [link](https://localazy.com/p/element/source-language?search=common.frequently_used&searchOptions=KEY,EXACT_MATCH) |
| `common.leaving_space` | Leaving space | [link](https://localazy.com/p/element/source-language?search=common.leaving_space&searchOptions=KEY,EXACT_MATCH) |
| `common.many_members` | %d others | [link](https://localazy.com/p/element/source-language?search=common.many_members&searchOptions=KEY,EXACT_MATCH) |
| `common.message` | Message | [link](https://localazy.com/p/element/source-language?search=common.message&searchOptions=KEY,EXACT_MATCH) |
| `common.private_space` | Private space | [link](https://localazy.com/p/element/source-language?search=common.private_space&searchOptions=KEY,EXACT_MATCH) |
| `common.public_space` | Public space | [link](https://localazy.com/p/element/source-language?search=common.public_space&searchOptions=KEY,EXACT_MATCH) |
| `common.reactions` | Reactions | [link](https://localazy.com/p/element/source-language?search=common.reactions&searchOptions=KEY,EXACT_MATCH) |
| `common.removing` | Removing… | [link](https://localazy.com/p/element/source-language?search=common.removing&searchOptions=KEY,EXACT_MATCH) |
| `common.security` | Security | [link](https://localazy.com/p/element/source-language?search=common.security&searchOptions=KEY,EXACT_MATCH) |
| `common.server_not_supported` | Server not supported | [link](https://localazy.com/p/element/source-language?search=common.server_not_supported&searchOptions=KEY,EXACT_MATCH) |
| `common.shared_space` | Shared space | [link](https://localazy.com/p/element/source-language?search=common.shared_space&searchOptions=KEY,EXACT_MATCH) |
| `common.signing_out` | Removing device | [link](https://localazy.com/p/element/source-language?search=common.signing_out&searchOptions=KEY,EXACT_MATCH) |
| `confirm_recovery_key_banner_primary_button_title` | Enter your recovery key | [link](https://localazy.com/p/element/source-language?search=confirm_recovery_key_banner_primary_button_title&searchOptions=KEY,EXACT_MATCH) |
| `confirm_recovery_key_banner_secondary_button_title` | Forgot your recovery key? | [link](https://localazy.com/p/element/source-language?search=confirm_recovery_key_banner_secondary_button_title&searchOptions=KEY,EXACT_MATCH) |
| `dialog.room_reported` | Room reported | [link](https://localazy.com/p/element/source-language?search=dialog.room_reported&searchOptions=KEY,EXACT_MATCH) |
| `dialog.room_reported_and_left` | Reported and left room | [link](https://localazy.com/p/element/source-language?search=dialog.room_reported_and_left&searchOptions=KEY,EXACT_MATCH) |
| `error.camera_unavailable` | The camera is not available | [link](https://localazy.com/p/element/source-language?search=error.camera_unavailable&searchOptions=KEY,EXACT_MATCH) |
| `error_failed_creating_the_permalink` | Failed creating the permalink | [link](https://localazy.com/p/element/source-language?search=error_failed_creating_the_permalink&searchOptions=KEY,EXACT_MATCH) |
| `error_failed_loading_map` | %1$s could not load the map. Please try again later. | [link](https://localazy.com/p/element/source-language?search=error_failed_loading_map&searchOptions=KEY,EXACT_MATCH) |
| `error_failed_locating_user` | %1$s could not access your location. Please try again later. | [link](https://localazy.com/p/element/source-language?search=error_failed_locating_user&searchOptions=KEY,EXACT_MATCH) |
| `error_some_messages_have_not_been_sent` | Some messages have not been sent | [link](https://localazy.com/p/element/source-language?search=error_some_messages_have_not_been_sent&searchOptions=KEY,EXACT_MATCH) |
| `leave_conversation_alert_subtitle` | Are you sure that you want to leave this conversation? This conversation is not public and you won't be able to rejoi… | [link](https://localazy.com/p/element/source-language?search=leave_conversation_alert_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `notification.gallery_body` | Shared %1$d attachments | [link](https://localazy.com/p/element/source-language?search=notification.gallery_body&searchOptions=KEY,EXACT_MATCH) |
| `notification_invite_body` | Invited you to chat | [link](https://localazy.com/p/element/source-language?search=notification_invite_body&searchOptions=KEY,EXACT_MATCH) |
| `notification_room_invite_body` | Invited you to join the room | [link](https://localazy.com/p/element/source-language?search=notification_room_invite_body&searchOptions=KEY,EXACT_MATCH) |
| `notification_space_invite_body` | Invited you to join the space | [link](https://localazy.com/p/element/source-language?search=notification_space_invite_body&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.format_action` | %1$s, state: %2$s | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.format_action&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.format_state_disabled` | disabled | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.format_state_disabled&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.format_state_off` | off | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.format_state_off&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.format_state_on` | on | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.format_state_on&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.labs` | Labs | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.labs&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_biometric_unlock` | biometric unlock | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_biometric_unlock&searchOptions=KEY,EXACT_MATCH) |
| `screen_blocked_users_empty` | You have no blocked users | [link](https://localazy.com/p/element/source-language?search=screen_blocked_users_empty&searchOptions=KEY,EXACT_MATCH) |
| `screen.bottom_sheet.manage_room_member.ban_member_from_space_confirmation_description` | They won’t be able to join this space again if invited, but they’ll still keep their memberships of any rooms or subs… | [link](https://localazy.com/p/element/source-language?search=screen.bottom_sheet.manage_room_member.ban_member_from_space_confirmation_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.bottom_sheet.manage_room_member.kick_member_from_space_confirmation_description` | They will be able to join this space again if invited, and they’ll still keep their memberships of any rooms or subsp… | [link](https://localazy.com/p/element/source-language?search=screen.bottom_sheet.manage_room_member.kick_member_from_space_confirmation_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.bug_report.a11y_screenshot` | Screenshot | [link](https://localazy.com/p/element/source-language?search=screen.bug_report.a11y_screenshot&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_attach_screenshot` | Attach screenshot | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_attach_screenshot&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_edit_screenshot` | Edit screenshot | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_edit_screenshot&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_include_logs_error` | Your logs are excessively large so cannot be included in this report, please send them to us another way. | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_include_logs_error&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_server_error_invalid_well_known` | Server isn't available due to an issue in the .well-known file: %1$s | [link](https://localazy.com/p/element/source-language?search=screen_change_server_error_invalid_well_known&searchOptions=KEY,EXACT_MATCH) |
| `screen.change_server.navigation_title.login` | Sign in | [link](https://localazy.com/p/element/source-language?search=screen.change_server.navigation_title.login&searchOptions=KEY,EXACT_MATCH) |
| `screen.change_server.navigation_title.register` | Create account | [link](https://localazy.com/p/element/source-language?search=screen.change_server.navigation_title.register&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_account_title` | Create account | [link](https://localazy.com/p/element/source-language?search=screen_create_account_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_poll.option_accessibility_label` | %1$s: %2$s | [link](https://localazy.com/p/element/source-language?search=screen.create_poll.option_accessibility_label&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_poll.options_section_title` | Options | [link](https://localazy.com/p/element/source-language?search=screen.create_poll.options_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_poll.remove_accessibility_label` | Remove %1$s | [link](https://localazy.com/p/element/source-language?search=screen.create_poll.remove_accessibility_label&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_poll.settings_section_title` | Settings | [link](https://localazy.com/p/element/source-language?search=screen.create_poll.settings_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_edit_profile_display_name_placeholder` | Your display name | [link](https://localazy.com/p/element/source-language?search=screen_edit_profile_display_name_placeholder&searchOptions=KEY,EXACT_MATCH) |
| `screen.home.tab_search` | Search | [link](https://localazy.com/p/element/source-language?search=screen.home.tab_search&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_confirmation_use_another_device` | Use another device | [link](https://localazy.com/p/element/source-language?search=screen_identity_confirmation_use_another_device&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_confirmed_title` | Device verified | [link](https://localazy.com/p/element/source-language?search=screen_identity_confirmed_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_invites_decline_direct_chat_message` | Are you sure you want to decline this private chat with %1$s? | [link](https://localazy.com/p/element/source-language?search=screen_invites_decline_direct_chat_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_invites_decline_direct_chat_title` | Decline chat | [link](https://localazy.com/p/element/source-language?search=screen_invites_decline_direct_chat_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.join_room.decline_and_block_alert_message` | Are you sure you want to decline the invite to join this room? This will also prevent %1$s from contacting you or inv… | [link](https://localazy.com/p/element/source-language?search=screen.join_room.decline_and_block_alert_message&searchOptions=KEY,EXACT_MATCH) |
| `screen.join_room.knock_message_characters_count` | Allowed characters %1$d of %2$d | [link](https://localazy.com/p/element/source-language?search=screen.join_room.knock_message_characters_count&searchOptions=KEY,EXACT_MATCH) |
| `screen.join_room.loading_alert_message` | We could not display the room preview. This may be due to network or server issues. | [link](https://localazy.com/p/element/source-language?search=screen.join_room.loading_alert_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_key_backup_disable_confirmation_action_turn_off` | Delete | [link](https://localazy.com/p/element/source-language?search=screen_key_backup_disable_confirmation_action_turn_off&searchOptions=KEY,EXACT_MATCH) |
| `screen_key_backup_disable_confirmation_description` | You will lose your encrypted chat history and need to reset your digital identity if you remove all your devices. | [link](https://localazy.com/p/element/source-language?search=screen_key_backup_disable_confirmation_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_key_backup_disable_confirmation_title` | Are you sure you want to delete key storage? | [link](https://localazy.com/p/element/source-language?search=screen_key_backup_disable_confirmation_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.knock_requests_list.accept_all_failed_alert_title` | Failed to accept all requests | [link](https://localazy.com/p/element/source-language?search=screen.knock_requests_list.accept_all_failed_alert_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.knock_requests_list.accept_failed_alert_title` | Failed to accept request | [link](https://localazy.com/p/element/source-language?search=screen.knock_requests_list.accept_failed_alert_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.knock_requests_list.decline_failed_alert_title` | Failed to decline request | [link](https://localazy.com/p/element/source-language?search=screen.knock_requests_list.decline_failed_alert_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.live_location.sheet_sharing_live_location` | Sharing live location | [link](https://localazy.com/p/element/source-language?search=screen.live_location.sheet_sharing_live_location&searchOptions=KEY,EXACT_MATCH) |
| `screen.live_location_sheet.subtitle` | %1$d people | [link](https://localazy.com/p/element/source-language?search=screen.live_location_sheet.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.live_location_sheet.title` | On the map | [link](https://localazy.com/p/element/source-language?search=screen.live_location_sheet.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_login_error_refresh_tokens` | This server is configured to use refresh tokens. These aren't supported when using password based login. | [link](https://localazy.com/p/element/source-language?search=screen_login_error_refresh_tokens&searchOptions=KEY,EXACT_MATCH) |
| `screen_login_title_with_homeserver` | Sign in to %1$s | [link](https://localazy.com/p/element/source-language?search=screen_login_title_with_homeserver&searchOptions=KEY,EXACT_MATCH) |
| `screen_media_browser_download_error_message` | Check your internet connection and try again. | [link](https://localazy.com/p/element/source-language?search=screen_media_browser_download_error_message&searchOptions=KEY,EXACT_MATCH) |
| `screen_media_browser_title` | Media and files | [link](https://localazy.com/p/element/source-language?search=screen_media_browser_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_media_picker_error_failed_selection` | Failed selecting media, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_media_picker_error_failed_selection&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.error_could_not_be_uploaded` | The file could not be uploaded. | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.error_could_not_be_uploaded&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.error_too_large_message` | The maximum file size allowed is %1$s. | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.error_too_large_message&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.error_too_large_title` | The file is too large to upload | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.error_too_large_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_additional_settings_section_title` | Additional settings | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_additional_settings_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_mode_all` | All | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_mode_all&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_mode_mentions` | Mentions | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_mode_mentions&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_sound_custom_sound_button_title` | Custom sound… | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_sound_custom_sound_button_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_sound_delete_sound_error_title` | Error deleting file | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_sound_delete_sound_error_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_sound_import_sound_error_title` | Error importing file | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_sound_import_sound_error_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_notification_settings_sound_preview_sound_error_title` | Problem previewing alert sound | [link](https://localazy.com/p/element/source-language?search=screen_notification_settings_sound_preview_sound_error_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.onboarding.checking_account` | Checking account | [link](https://localazy.com/p/element/source-language?search=screen.onboarding.checking_account&searchOptions=KEY,EXACT_MATCH) |
| `screen_qr_code_login_no_camera_permission_button` | Go to camera settings | [link](https://localazy.com/p/element/source-language?search=screen_qr_code_login_no_camera_permission_button&searchOptions=KEY,EXACT_MATCH) |
| `screen_recovery_key_confirm_success` | Recovery key confirmed | [link](https://localazy.com/p/element/source-language?search=screen_recovery_key_confirm_success&searchOptions=KEY,EXACT_MATCH) |
| `screen_reset_encryption_password_placeholder` | Enter… | [link](https://localazy.com/p/element/source-language?search=screen_reset_encryption_password_placeholder&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_attachment_source_camera` | Camera | [link](https://localazy.com/p/element/source-language?search=screen_room_attachment_source_camera&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_permissions_administrators` | Admin | [link](https://localazy.com/p/element/source-language?search=screen_room_change_permissions_administrators&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_permissions_moderators` | Moderator | [link](https://localazy.com/p/element/source-language?search=screen_room_change_permissions_moderators&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_change_permissions.title` | Permissions | [link](https://localazy.com/p/element/source-language?search=screen.room_change_permissions.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_change_role.administrators_or_owners_title` | Edit Admins or Owners | [link](https://localazy.com/p/element/source-language?search=screen.room_change_role.administrators_or_owners_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_section_administrators` | Admins | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_section_administrators&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_section_moderators` | Moderators | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_section_moderators&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_section_users` | Members | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_section_users&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_unsaved_changes_description` | You have unsaved changes. | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_unsaved_changes_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_change_role_unsaved_changes_title` | Save changes? | [link](https://localazy.com/p/element/source-language?search=screen_room_change_role_unsaved_changes_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room.confirm_removal_reason_label` | Reason (optional) | [link](https://localazy.com/p/element/source-language?search=screen.room.confirm_removal_reason_label&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_edition_error_title` | Unable to update room | [link](https://localazy.com/p/element/source-language?search=screen_room_details_edition_error_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_error_loading_notification_settings` | An error occurred when loading notification settings. | [link](https://localazy.com/p/element/source-language?search=screen_room_details_error_loading_notification_settings&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_error_muting` | Failed muting this room, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_room_details_error_muting&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_error_unmuting` | Failed unmuting this room, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_room_details_error_unmuting&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_leave_room_title` | Leave room | [link](https://localazy.com/p/element/source-language?search=screen_room_details_leave_room_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_title` | Room info | [link](https://localazy.com/p/element/source-language?search=screen_room_details_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_directory_search_loading_error` | Failed loading | [link](https://localazy.com/p/element/source-language?search=screen_room_directory_search_loading_error&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_error_failed_processing_media` | Failed processing media to upload, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_room_error_failed_processing_media&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_grouped_state_events_expand` | Expand | [link](https://localazy.com/p/element/source-language?search=screen.room_grouped_state_events_expand&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_grouped_state_events_reduce` | Reduce | [link](https://localazy.com/p/element/source-language?search=screen.room_grouped_state_events_reduce&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_block_alert_action` | Block | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_block_alert_action&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_block_alert_description` | Blocked users won't be able to send you messages and all their messages will be hidden. You can unblock them anytime. | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_block_alert_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_block_user` | Block user | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_block_user&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_title` | Profile | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_unblock_alert_action` | Unblock | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_unblock_alert_action&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_unblock_alert_description` | You'll be able to see all messages from them again. | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_unblock_alert_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_member_details_unblock_user` | Unblock user | [link](https://localazy.com/p/element/source-language?search=screen_room_member_details_unblock_user&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_error_loading_settings` | An error occurred while loading notification settings. | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_error_loading_settings&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_error_restoring_default` | Failed restoring the default mode, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_error_restoring_default&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_error_setting_mode` | Failed setting the mode, please try again. | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_error_setting_mode&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_mentions_only_disclaimer` | Your account provider does not support this option in encrypted chats, you won't get notified in this chat. | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_mentions_only_disclaimer&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_room_custom_settings_title` | In this room, notify me for | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_room_custom_settings_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_timeline_reactions_show_reactions_summary` | Show reactions summary | [link](https://localazy.com/p/element/source-language?search=screen.room_timeline_reactions_show_reactions_summary&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_title` | Chat | [link](https://localazy.com/p/element/source-language?search=screen_room_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_roomlist_filter_low_priority` | Low Priority | [link](https://localazy.com/p/element/source-language?search=screen_roomlist_filter_low_priority&searchOptions=KEY,EXACT_MATCH) |
| `screen_roomlist_filter_low_priority_empty_state_title` | You don’t have any low priority chats yet | [link](https://localazy.com/p/element/source-language?search=screen_roomlist_filter_low_priority_empty_state_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.roomlist.filter_mention` | Mention | [link](https://localazy.com/p/element/source-language?search=screen.roomlist.filter_mention&searchOptions=KEY,EXACT_MATCH) |
| `screen.roomlist.filter_mention_empty_state_title` | You don’t have any unread mentions | [link](https://localazy.com/p/element/source-language?search=screen.roomlist.filter_mention_empty_state_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_roomlist_main_space_title` | Chats | [link](https://localazy.com/p/element/source-language?search=screen_roomlist_main_space_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_details_timestamp` | Signed in | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_details_timestamp&searchOptions=KEY,EXACT_MATCH) |
| `screen.settings.add_account` | Add account | [link](https://localazy.com/p/element/source-language?search=screen.settings.add_account&searchOptions=KEY,EXACT_MATCH) |
| `screen_share_open_apple_maps` | Open in Apple Maps | [link](https://localazy.com/p/element/source-language?search=screen_share_open_apple_maps&searchOptions=KEY,EXACT_MATCH) |
| `screen_share_open_google_maps` | Open in Google Maps | [link](https://localazy.com/p/element/source-language?search=screen_share_open_google_maps&searchOptions=KEY,EXACT_MATCH) |
| `screen_share_open_osm_maps` | Open in OpenStreetMap | [link](https://localazy.com/p/element/source-language?search=screen_share_open_osm_maps&searchOptions=KEY,EXACT_MATCH) |
| `screen.sharing_location_option_sheet.title` | Sharing options | [link](https://localazy.com/p/element/source-language?search=screen.sharing_location_option_sheet.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_confirmation_dialog_submit` | Remove this device | [link](https://localazy.com/p/element/source-language?search=screen_signout_confirmation_dialog_submit&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_confirmation_dialog_title` | Remove this device | [link](https://localazy.com/p/element/source-language?search=screen_signout_confirmation_dialog_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_key_backup_offline_title` | Your keys are still being backed up | [link](https://localazy.com/p/element/source-language?search=screen_signout_key_backup_offline_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_preference_item` | Remove this device | [link](https://localazy.com/p/element/source-language?search=screen_signout_preference_item&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_recovery_disabled_subtitle` | This is your only device. If you remove it you’ll need a recovery key in order to confirm your digital identity and r… | [link](https://localazy.com/p/element/source-language?search=screen_signout_recovery_disabled_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_save_recovery_key_subtitle` | This is your only device. If you remove it you’ll need a recovery key in order to confirm your digital identity and r… | [link](https://localazy.com/p/element/source-language?search=screen_signout_save_recovery_key_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.space_settings.leave_space` | Leave space | [link](https://localazy.com/p/element/source-language?search=screen.space_settings.leave_space&searchOptions=KEY,EXACT_MATCH) |

</details>

## Strings not used on iOS

Strings used by Element X Android but not by Element X iOS. Keys with the `_ios` suffix can probably be removed. For the other keys, this can be a difference between the implementations of both projects, or a feature not implemented yet on iOS. If the difference is expected, the key can be renamed with the `_android` suffix. **359** keys.

<details>
<summary>Show the 359 keys</summary>

| Key | English value | Localazy |
|---|---|---|
| `dialog.permission_location_title_ios` | %1$@ does not have access to your location. | [link](https://localazy.com/p/element/source-language?search=dialog.permission_location_title_ios&searchOptions=KEY,EXACT_MATCH) |
| `dialog_unsaved_changes_description_ios` | Your changes won’t be saved | [link](https://localazy.com/p/element/source-language?search=dialog_unsaved_changes_description_ios&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_settings_enable_face_id_ios` | Allow Face ID | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_settings_enable_face_id_ios&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_settings_enable_optic_id_ios` | Allow Optic ID | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_settings_enable_optic_id_ios&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_settings_enable_touch_id_ios` | Allow Touch ID | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_settings_enable_touch_id_ios&searchOptions=KEY,EXACT_MATCH) |
| `a11y.active` | Active | [link](https://localazy.com/p/element/source-language?search=a11y.active&searchOptions=KEY,EXACT_MATCH) |
| `a11y.clear_search_field` | Clear search field | [link](https://localazy.com/p/element/source-language?search=a11y.clear_search_field&searchOptions=KEY,EXACT_MATCH) |
| `a11y.collapse_message_text_field` | Minimise message text field | [link](https://localazy.com/p/element/source-language?search=a11y.collapse_message_text_field&searchOptions=KEY,EXACT_MATCH) |
| `a11y.duration` | Duration: %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.duration&searchOptions=KEY,EXACT_MATCH) |
| `a11y.encryption_details` | Encryption details | [link](https://localazy.com/p/element/source-language?search=a11y.encryption_details&searchOptions=KEY,EXACT_MATCH) |
| `a11y.expand_message_text_field` | Expand message text field | [link](https://localazy.com/p/element/source-language?search=a11y.expand_message_text_field&searchOptions=KEY,EXACT_MATCH) |
| `a11y.inactive` | Inactive | [link](https://localazy.com/p/element/source-language?search=a11y.inactive&searchOptions=KEY,EXACT_MATCH) |
| `a11y.jump_to_unread_messages` | Jump to first unread message | [link](https://localazy.com/p/element/source-language?search=a11y.jump_to_unread_messages&searchOptions=KEY,EXACT_MATCH) |
| `a11y.move_the_map_to_my_location` | Move the map to my location | [link](https://localazy.com/p/element/source-language?search=a11y.move_the_map_to_my_location&searchOptions=KEY,EXACT_MATCH) |
| `a11y.page_n` | Page %1$d | [link](https://localazy.com/p/element/source-language?search=a11y.page_n&searchOptions=KEY,EXACT_MATCH) |
| `a11y.polls.percent_of_total` | %1$d percents of total votes | [link](https://localazy.com/p/element/source-language?search=a11y.polls.percent_of_total&searchOptions=KEY,EXACT_MATCH) |
| `a11y.position` | Position: %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.position&searchOptions=KEY,EXACT_MATCH) |
| `a11y.react_with` | React with %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.react_with&searchOptions=KEY,EXACT_MATCH) |
| `a11y.react_with_other_emojis` | React with other emojis | [link](https://localazy.com/p/element/source-language?search=a11y.react_with_other_emojis&searchOptions=KEY,EXACT_MATCH) |
| `a11y.remove_reaction_with` | Remove reaction with %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.remove_reaction_with&searchOptions=KEY,EXACT_MATCH) |
| `a11y.sent_by_sender_at_date` | Sent by %1$s at %2$s | [link](https://localazy.com/p/element/source-language?search=a11y.sent_by_sender_at_date&searchOptions=KEY,EXACT_MATCH) |
| `a11y.settings_with_required_action` | Settings, action required | [link](https://localazy.com/p/element/source-language?search=a11y.settings_with_required_action&searchOptions=KEY,EXACT_MATCH) |
| `a11y.state_collapsed` | Collapsed | [link](https://localazy.com/p/element/source-language?search=a11y.state_collapsed&searchOptions=KEY,EXACT_MATCH) |
| `a11y.state_expanded` | Expanded | [link](https://localazy.com/p/element/source-language?search=a11y.state_expanded&searchOptions=KEY,EXACT_MATCH) |
| `a11y.thread_in_room` | Thread in %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.thread_in_room&searchOptions=KEY,EXACT_MATCH) |
| `a11y.threads_in_room` | Threads in %1$s | [link](https://localazy.com/p/element/source-language?search=a11y.threads_in_room&searchOptions=KEY,EXACT_MATCH) |
| `a11y.user_menu` | User menu | [link](https://localazy.com/p/element/source-language?search=a11y.user_menu&searchOptions=KEY,EXACT_MATCH) |
| `action.copy_to_clipboard` | Copy to clipboard | [link](https://localazy.com/p/element/source-language?search=action.copy_to_clipboard&searchOptions=KEY,EXACT_MATCH) |
| `action.disable` | Disable | [link](https://localazy.com/p/element/source-language?search=action.disable&searchOptions=KEY,EXACT_MATCH) |
| `action.explore_public_spaces` | Explore public spaces | [link](https://localazy.com/p/element/source-language?search=action.explore_public_spaces&searchOptions=KEY,EXACT_MATCH) |
| `action.finish` | Finish | [link](https://localazy.com/p/element/source-language?search=action.finish&searchOptions=KEY,EXACT_MATCH) |
| `action.invite_friends` | Invite people | [link](https://localazy.com/p/element/source-language?search=action.invite_friends&searchOptions=KEY,EXACT_MATCH) |
| `action.invite_friends_to_app` | Invite people to %1$s | [link](https://localazy.com/p/element/source-language?search=action.invite_friends_to_app&searchOptions=KEY,EXACT_MATCH) |
| `action.mark_as_read` | Mark as read | [link](https://localazy.com/p/element/source-language?search=action.mark_as_read&searchOptions=KEY,EXACT_MATCH) |
| `action.message` | Message | [link](https://localazy.com/p/element/source-language?search=action.message&searchOptions=KEY,EXACT_MATCH) |
| `action.open_settings` | Settings | [link](https://localazy.com/p/element/source-language?search=action.open_settings&searchOptions=KEY,EXACT_MATCH) |
| `action.open_with` | Open with | [link](https://localazy.com/p/element/source-language?search=action.open_with&searchOptions=KEY,EXACT_MATCH) |
| `action.reject` | Reject | [link](https://localazy.com/p/element/source-language?search=action.reject&searchOptions=KEY,EXACT_MATCH) |
| `action.send_edited_message` | Send edited message | [link](https://localazy.com/p/element/source-language?search=action.send_edited_message&searchOptions=KEY,EXACT_MATCH) |
| `action.send_message` | Send message | [link](https://localazy.com/p/element/source-language?search=action.send_message&searchOptions=KEY,EXACT_MATCH) |
| `action.send_voice_message` | Send voice message | [link](https://localazy.com/p/element/source-language?search=action.send_voice_message&searchOptions=KEY,EXACT_MATCH) |
| `action.signout_anyway` | Remove this device anyway | [link](https://localazy.com/p/element/source-language?search=action.signout_anyway&searchOptions=KEY,EXACT_MATCH) |
| `action.start` | Start | [link](https://localazy.com/p/element/source-language?search=action.start&searchOptions=KEY,EXACT_MATCH) |
| `action.view` | View | [link](https://localazy.com/p/element/source-language?search=action.view&searchOptions=KEY,EXACT_MATCH) |
| `banner.migrate_to_native_sliding_sync.action` | Log Out & Upgrade | [link](https://localazy.com/p/element/source-language?search=banner.migrate_to_native_sliding_sync.action&searchOptions=KEY,EXACT_MATCH) |
| `banner.migrate_to_native_sliding_sync.app_force_logout.title` | %1$s no longer supports the old protocol. Please log out and log back in to continue using the app. | [link](https://localazy.com/p/element/source-language?search=banner.migrate_to_native_sliding_sync.app_force_logout.title&searchOptions=KEY,EXACT_MATCH) |
| `banner.swipe_avatar.content` | Swipe up or down on your avatar to switch between your accounts without going to the app settings. | [link](https://localazy.com/p/element/source-language?search=banner.swipe_avatar.content&searchOptions=KEY,EXACT_MATCH) |
| `banner.swipe_avatar.title` | Swipe your avatar to switch accounts | [link](https://localazy.com/p/element/source-language?search=banner.swipe_avatar.title&searchOptions=KEY,EXACT_MATCH) |
| `call_invalid_audio_device_bluetooth_devices_disabled` | Element Call does not support using Bluetooth audio devices in this Android version. Please select a different audio … | [link](https://localazy.com/p/element/source-language?search=call_invalid_audio_device_bluetooth_devices_disabled&searchOptions=KEY,EXACT_MATCH) |
| `common.add_another_account` | Add account | [link](https://localazy.com/p/element/source-language?search=common.add_another_account&searchOptions=KEY,EXACT_MATCH) |
| `common.advanced_settings` | Advanced settings | [link](https://localazy.com/p/element/source-language?search=common.advanced_settings&searchOptions=KEY,EXACT_MATCH) |
| `common.an_image` | an image | [link](https://localazy.com/p/element/source-language?search=common.an_image&searchOptions=KEY,EXACT_MATCH) |
| `common.android.shortcuts_remove_reason_left_room` | You left the room | [link](https://localazy.com/p/element/source-language?search=common.android.shortcuts_remove_reason_left_room&searchOptions=KEY,EXACT_MATCH) |
| `common.android.shortcuts_remove_reason_session_logged_out` | You were logged out of the session | [link](https://localazy.com/p/element/source-language?search=common.android.shortcuts_remove_reason_session_logged_out&searchOptions=KEY,EXACT_MATCH) |
| `common.beta` | Beta | [link](https://localazy.com/p/element/source-language?search=common.beta&searchOptions=KEY,EXACT_MATCH) |
| `common.code_block` | Code block | [link](https://localazy.com/p/element/source-language?search=common.code_block&searchOptions=KEY,EXACT_MATCH) |
| `common.creating_space` | Creating space… | [link](https://localazy.com/p/element/source-language?search=common.creating_space&searchOptions=KEY,EXACT_MATCH) |
| `common.current_user_canceled_knock` | Request canceled | [link](https://localazy.com/p/element/source-language?search=common.current_user_canceled_knock&searchOptions=KEY,EXACT_MATCH) |
| `common.current_user_left_space` | Left space | [link](https://localazy.com/p/element/source-language?search=common.current_user_left_space&searchOptions=KEY,EXACT_MATCH) |
| `common.current_user_rejected_invite` | Invite declined | [link](https://localazy.com/p/element/source-language?search=common.current_user_rejected_invite&searchOptions=KEY,EXACT_MATCH) |
| `common.date.date_at_time` | %1$s at %2$s | [link](https://localazy.com/p/element/source-language?search=common.date.date_at_time&searchOptions=KEY,EXACT_MATCH) |
| `common.do_not_show_this_again` | Do not show this again | [link](https://localazy.com/p/element/source-language?search=common.do_not_show_this_again&searchOptions=KEY,EXACT_MATCH) |
| `common.downloading` | Downloading | [link](https://localazy.com/p/element/source-language?search=common.downloading&searchOptions=KEY,EXACT_MATCH) |
| `common.empty_file` | Empty file | [link](https://localazy.com/p/element/source-language?search=common.empty_file&searchOptions=KEY,EXACT_MATCH) |
| `common.header_rooms` | Rooms | [link](https://localazy.com/p/element/source-language?search=common.header_rooms&searchOptions=KEY,EXACT_MATCH) |
| `common.line_copied_to_clipboard` | Line copied to clipboard | [link](https://localazy.com/p/element/source-language?search=common.line_copied_to_clipboard&searchOptions=KEY,EXACT_MATCH) |
| `common.link_copied_to_clipboard` | Link copied to clipboard | [link](https://localazy.com/p/element/source-language?search=common.link_copied_to_clipboard&searchOptions=KEY,EXACT_MATCH) |
| `common.no_results_for` | There are no results for “%1$s”. Try a new search term. | [link](https://localazy.com/p/element/source-language?search=common.no_results_for&searchOptions=KEY,EXACT_MATCH) |
| `common.no_room_name` | No room name | [link](https://localazy.com/p/element/source-language?search=common.no_room_name&searchOptions=KEY,EXACT_MATCH) |
| `common.no_space_name` | No space name | [link](https://localazy.com/p/element/source-language?search=common.no_space_name&searchOptions=KEY,EXACT_MATCH) |
| `common.open_source_licenses` | Open source licenses | [link](https://localazy.com/p/element/source-language?search=common.open_source_licenses&searchOptions=KEY,EXACT_MATCH) |
| `common.permission` | Permission | [link](https://localazy.com/p/element/source-language?search=common.permission&searchOptions=KEY,EXACT_MATCH) |
| `common.poll_summary_prefix` | Poll | [link](https://localazy.com/p/element/source-language?search=common.poll_summary_prefix&searchOptions=KEY,EXACT_MATCH) |
| `common.results_for` | Results for “%1$s” | [link](https://localazy.com/p/element/source-language?search=common.results_for&searchOptions=KEY,EXACT_MATCH) |
| `common.room_name` | Room name | [link](https://localazy.com/p/element/source-language?search=common.room_name&searchOptions=KEY,EXACT_MATCH) |
| `common.rooms` | %1$d Rooms | [link](https://localazy.com/p/element/source-language?search=common.rooms&searchOptions=KEY,EXACT_MATCH) |
| `common.saved_changes` | Saved changes | [link](https://localazy.com/p/element/source-language?search=common.saved_changes&searchOptions=KEY,EXACT_MATCH) |
| `common.search_results` | Search results | [link](https://localazy.com/p/element/source-language?search=common.search_results&searchOptions=KEY,EXACT_MATCH) |
| `common.select_account` | Select an account | [link](https://localazy.com/p/element/source-language?search=common.select_account&searchOptions=KEY,EXACT_MATCH) |
| `common.selected_count` | %1$d selected | [link](https://localazy.com/p/element/source-language?search=common.selected_count&searchOptions=KEY,EXACT_MATCH) |
| `common.send_to` | Send to | [link](https://localazy.com/p/element/source-language?search=common.send_to&searchOptions=KEY,EXACT_MATCH) |
| `common.sentence_delimiter` | . | [link](https://localazy.com/p/element/source-language?search=common.sentence_delimiter&searchOptions=KEY,EXACT_MATCH) |
| `common.share_space` | Share space | [link](https://localazy.com/p/element/source-language?search=common.share_space&searchOptions=KEY,EXACT_MATCH) |
| `common.shared_history` | New members see history | [link](https://localazy.com/p/element/source-language?search=common.shared_history&searchOptions=KEY,EXACT_MATCH) |
| `common.signed_in` | Signed in | [link](https://localazy.com/p/element/source-language?search=common.signed_in&searchOptions=KEY,EXACT_MATCH) |
| `common.spoiler` | Spoiler | [link](https://localazy.com/p/element/source-language?search=common.spoiler&searchOptions=KEY,EXACT_MATCH) |
| `common.starting_chat` | Starting chat… | [link](https://localazy.com/p/element/source-language?search=common.starting_chat&searchOptions=KEY,EXACT_MATCH) |
| `common.switch_accounts` | Switch accounts | [link](https://localazy.com/p/element/source-language?search=common.switch_accounts&searchOptions=KEY,EXACT_MATCH) |
| `common.unable_to_decrypt` | Unable to decrypt | [link](https://localazy.com/p/element/source-language?search=common.unable_to_decrypt&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_high` | High quality | [link](https://localazy.com/p/element/source-language?search=common.video_quality_high&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_high_description` | Best quality but larger file size | [link](https://localazy.com/p/element/source-language?search=common.video_quality_high_description&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_low` | Low quality | [link](https://localazy.com/p/element/source-language?search=common.video_quality_low&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_low_description` | Fastest upload speed and smallest file size | [link](https://localazy.com/p/element/source-language?search=common.video_quality_low_description&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_standard` | Standard quality | [link](https://localazy.com/p/element/source-language?search=common.video_quality_standard&searchOptions=KEY,EXACT_MATCH) |
| `common.video_quality_standard_description` | Balance of quality and upload speed | [link](https://localazy.com/p/element/source-language?search=common.video_quality_standard_description&searchOptions=KEY,EXACT_MATCH) |
| `common.waiting_live_location` | Waiting for live location… | [link](https://localazy.com/p/element/source-language?search=common.waiting_live_location&searchOptions=KEY,EXACT_MATCH) |
| `common.world_readable_history` | Anyone can see history | [link](https://localazy.com/p/element/source-language?search=common.world_readable_history&searchOptions=KEY,EXACT_MATCH) |
| `dialog_default_video_quality_selector_subtitle` | Select the default quality of videos you upload. | [link](https://localazy.com/p/element/source-language?search=dialog_default_video_quality_selector_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `dialog.file_too_large_to_upload.subtitle` | The max file size allowed is: %1$s | [link](https://localazy.com/p/element/source-language?search=dialog.file_too_large_to_upload.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `dialog.file_too_large_to_upload.title` | The file size is too large to upload | [link](https://localazy.com/p/element/source-language?search=dialog.file_too_large_to_upload.title&searchOptions=KEY,EXACT_MATCH) |
| `dialog.permission_camera` | In order to let the application use the camera, please grant the permission in the system settings. | [link](https://localazy.com/p/element/source-language?search=dialog.permission_camera&searchOptions=KEY,EXACT_MATCH) |
| `dialog.permission_generic` | Please grant the permission in the system settings. | [link](https://localazy.com/p/element/source-language?search=dialog.permission_generic&searchOptions=KEY,EXACT_MATCH) |
| `dialog.permission_microphone` | In order to let the application use the microphone, please grant the permission in the system settings. | [link](https://localazy.com/p/element/source-language?search=dialog.permission_microphone&searchOptions=KEY,EXACT_MATCH) |
| `dialog.permission_notification` | In order to let the application display notifications, please grant the permission in the system settings. | [link](https://localazy.com/p/element/source-language?search=dialog.permission_notification&searchOptions=KEY,EXACT_MATCH) |
| `dialog_title_confirmation` | Confirmation | [link](https://localazy.com/p/element/source-language?search=dialog_title_confirmation&searchOptions=KEY,EXACT_MATCH) |
| `dialog_title_warning` | Warning | [link](https://localazy.com/p/element/source-language?search=dialog_title_warning&searchOptions=KEY,EXACT_MATCH) |
| `dialog_video_quality_selector_subtitle_file_size` | The max file size allowed is: %1$s | [link](https://localazy.com/p/element/source-language?search=dialog_video_quality_selector_subtitle_file_size&searchOptions=KEY,EXACT_MATCH) |
| `dialog_video_quality_selector_subtitle_no_file_size` | Select the quality of the video you want to upload. | [link](https://localazy.com/p/element/source-language?search=dialog_video_quality_selector_subtitle_no_file_size&searchOptions=KEY,EXACT_MATCH) |
| `dialog_video_quality_selector_title` | Select video upload quality | [link](https://localazy.com/p/element/source-language?search=dialog_video_quality_selector_title&searchOptions=KEY,EXACT_MATCH) |
| `emoji_picker_category_recent` | Recent emojis | [link](https://localazy.com/p/element/source-language?search=emoji_picker_category_recent&searchOptions=KEY,EXACT_MATCH) |
| `emoji_picker_search_placeholder` | Search emojis | [link](https://localazy.com/p/element/source-language?search=emoji_picker_search_placeholder&searchOptions=KEY,EXACT_MATCH) |
| `error.account_already_logged_in` | You’re already signed in as %1$s. | [link](https://localazy.com/p/element/source-language?search=error.account_already_logged_in&searchOptions=KEY,EXACT_MATCH) |
| `error.account_already_logged_in.title` | Duplicate sign-in | [link](https://localazy.com/p/element/source-language?search=error.account_already_logged_in.title&searchOptions=KEY,EXACT_MATCH) |
| `error.network_or_server_issue` | This may be due to network or server issues. | [link](https://localazy.com/p/element/source-language?search=error.network_or_server_issue&searchOptions=KEY,EXACT_MATCH) |
| `error_no_compatible_app_found` | No compatible app was found to handle this action. | [link](https://localazy.com/p/element/source-language?search=error_no_compatible_app_found&searchOptions=KEY,EXACT_MATCH) |
| `error.sending_failure.invalid_mime_type` | Invalid mime type: %s | [link](https://localazy.com/p/element/source-language?search=error.sending_failure.invalid_mime_type&searchOptions=KEY,EXACT_MATCH) |
| `error.sending_failure.missing_media_content` | Missing media content | [link](https://localazy.com/p/element/source-language?search=error.sending_failure.missing_media_content&searchOptions=KEY,EXACT_MATCH) |
| `error.sending_failure.other` | Error details: %s | [link](https://localazy.com/p/element/source-language?search=error.sending_failure.other&searchOptions=KEY,EXACT_MATCH) |
| `error.sending_failure.sending_from_unverified_device` | Sending from unverified device | [link](https://localazy.com/p/element/source-language?search=error.sending_failure.sending_from_unverified_device&searchOptions=KEY,EXACT_MATCH) |
| `error.sending_failure.unknown` | Unknown error | [link](https://localazy.com/p/element/source-language?search=error.sending_failure.unknown&searchOptions=KEY,EXACT_MATCH) |
| `full_screen_intent_banner_message` | To ensure you never miss an important call, please change your settings to allow full-screen notifications when your … | [link](https://localazy.com/p/element/source-language?search=full_screen_intent_banner_message&searchOptions=KEY,EXACT_MATCH) |
| `full_screen_intent_banner_title` | Enhance your call experience | [link](https://localazy.com/p/element/source-language?search=full_screen_intent_banner_title&searchOptions=KEY,EXACT_MATCH) |
| `invite_friends_rich_title` | 🔐️ Join me on %1$s | [link](https://localazy.com/p/element/source-language?search=invite_friends_rich_title&searchOptions=KEY,EXACT_MATCH) |
| `notification_channel_call` | Call | [link](https://localazy.com/p/element/source-language?search=notification_channel_call&searchOptions=KEY,EXACT_MATCH) |
| `notification_channel_noisy` | Noisy notifications | [link](https://localazy.com/p/element/source-language?search=notification_channel_noisy&searchOptions=KEY,EXACT_MATCH) |
| `notification_channel_ringing_calls` | Ringing calls | [link](https://localazy.com/p/element/source-language?search=notification_channel_ringing_calls&searchOptions=KEY,EXACT_MATCH) |
| `notification_channel_silent` | Silent notifications | [link](https://localazy.com/p/element/source-language?search=notification_channel_silent&searchOptions=KEY,EXACT_MATCH) |
| `notification_compat_summary_title` | %d notifications | [link](https://localazy.com/p/element/source-language?search=notification_compat_summary_title&searchOptions=KEY,EXACT_MATCH) |
| `notification_fallback_n_content` | You have %d new messages. | [link](https://localazy.com/p/element/source-language?search=notification_fallback_n_content&searchOptions=KEY,EXACT_MATCH) |
| `notification_incoming_audio_call` | 📞 Incoming call | [link](https://localazy.com/p/element/source-language?search=notification_incoming_audio_call&searchOptions=KEY,EXACT_MATCH) |
| `notification_inline_reply_failed` | ** Failed to send - please open room | [link](https://localazy.com/p/element/source-language?search=notification_inline_reply_failed&searchOptions=KEY,EXACT_MATCH) |
| `notification_invite_body_with_sender` | %1$s invited you to chat | [link](https://localazy.com/p/element/source-language?search=notification_invite_body_with_sender&searchOptions=KEY,EXACT_MATCH) |
| `notification.knock_request.body` | Requested to join | [link](https://localazy.com/p/element/source-language?search=notification.knock_request.body&searchOptions=KEY,EXACT_MATCH) |
| `notification_room_action_mark_as_read` | Mark as read | [link](https://localazy.com/p/element/source-language?search=notification_room_action_mark_as_read&searchOptions=KEY,EXACT_MATCH) |
| `notification_room_action_quick_reply` | Quick reply | [link](https://localazy.com/p/element/source-language?search=notification_room_action_quick_reply&searchOptions=KEY,EXACT_MATCH) |
| `notification_room_invite_body_with_sender` | %1$s invited you to join the room | [link](https://localazy.com/p/element/source-language?search=notification_room_invite_body_with_sender&searchOptions=KEY,EXACT_MATCH) |
| `notification_sender_me` | Me | [link](https://localazy.com/p/element/source-language?search=notification_sender_me&searchOptions=KEY,EXACT_MATCH) |
| `notification_space_invite_body_with_sender` | %1$s invited you to join the space | [link](https://localazy.com/p/element/source-language?search=notification_space_invite_body_with_sender&searchOptions=KEY,EXACT_MATCH) |
| `notification_test_push_notification_content` | You are viewing the notification! Tap me! | [link](https://localazy.com/p/element/source-language?search=notification_test_push_notification_content&searchOptions=KEY,EXACT_MATCH) |
| `notification_ticker_text_dm` | %1$s: %2$s | [link](https://localazy.com/p/element/source-language?search=notification_ticker_text_dm&searchOptions=KEY,EXACT_MATCH) |
| `notification_ticker_text_group` | %1$s: %2$s %3$s | [link](https://localazy.com/p/element/source-language?search=notification_ticker_text_group&searchOptions=KEY,EXACT_MATCH) |
| `preference_rageshake` | Rageshake to report bug | [link](https://localazy.com/p/element/source-language?search=preference_rageshake&searchOptions=KEY,EXACT_MATCH) |
| `rageshake_detection_dialog_content` | You seem to be shaking the phone in frustration. Would you like to open the bug report screen? | [link](https://localazy.com/p/element/source-language?search=rageshake_detection_dialog_content&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor_a11y_add_attachment` | Add attachment | [link](https://localazy.com/p/element/source-language?search=rich_text_editor_a11y_add_attachment&searchOptions=KEY,EXACT_MATCH) |
| `rich_text_editor.remove_link` | Remove link | [link](https://localazy.com/p/element/source-language?search=rich_text_editor.remove_link&searchOptions=KEY,EXACT_MATCH) |
| `screen_account_provider_signin_title` | You’re about to sign in to %s | [link](https://localazy.com/p/element/source-language?search=screen_account_provider_signin_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.element_call_base_url` | Custom Element Call base URL | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.element_call_base_url&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.element_call_base_url_description` | Set a custom base URL for Element Call. | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.element_call_base_url_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.element_call_base_url_validation_error` | Invalid URL, please make sure you include the protocol (http/https) and the correct address. | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.element_call_base_url_validation_error&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_image_upload_quality_description` | Automatically optimise images for faster uploads and smaller file sizes. | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_image_upload_quality_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_image_upload_quality_title` | Optimise image upload quality | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_image_upload_quality_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_video_upload_quality_description` | %1$s. Tap here to change. | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_video_upload_quality_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_video_upload_quality_high` | High (1080p) | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_video_upload_quality_high&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_video_upload_quality_low` | Low (480p) | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_video_upload_quality_low&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_video_upload_quality_standard` | Standard (720p) | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_video_upload_quality_standard&searchOptions=KEY,EXACT_MATCH) |
| `screen.advanced_settings.optimise_video_upload_quality_title` | Video upload quality | [link](https://localazy.com/p/element/source-language?search=screen.advanced_settings.optimise_video_upload_quality_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_advanced_settings_view_source_description` | Enable option to view message source in the timeline. | [link](https://localazy.com/p/element/source-language?search=screen_advanced_settings_view_source_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_analytics_prompt_read_terms` | You can read all our terms %1$s. | [link](https://localazy.com/p/element/source-language?search=screen_analytics_prompt_read_terms&searchOptions=KEY,EXACT_MATCH) |
| `screen_analytics_prompt_read_terms_content_link` | here | [link](https://localazy.com/p/element/source-language?search=screen_analytics_prompt_read_terms_content_link&searchOptions=KEY,EXACT_MATCH) |
| `screen_analytics_settings_help_us_improve` | Share anonymous usage data to help us identify issues. | [link](https://localazy.com/p/element/source-language?search=screen_analytics_settings_help_us_improve&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_biometric_authentication` | biometric authentication | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_biometric_authentication&searchOptions=KEY,EXACT_MATCH) |
| `screen_app_lock_settings_enable_biometric_unlock` | Allow biometric unlock | [link](https://localazy.com/p/element/source-language?search=screen_app_lock_settings_enable_biometric_unlock&searchOptions=KEY,EXACT_MATCH) |
| `screen_blocked_users_unblocking` | Unblocking… | [link](https://localazy.com/p/element/source-language?search=screen_blocked_users_unblocking&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_error_description_too_short` | The description is too short, please provide more details about what happened. Thanks! | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_error_description_too_short&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_github_issue_description` | You can enter the number of an associated GitHub issue, if any. | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_github_issue_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_github_issue_label` | GitHub issue | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_github_issue_label&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_include_screenshot` | Send screenshot | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_include_screenshot&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_send_notification_settings_description` | If you are having issues with notifications, uploading the notification push rules can help us pinpoint the root caus… | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_send_notification_settings_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_bug_report_send_notification_settings_title` | Send notification settings | [link](https://localazy.com/p/element/source-language?search=screen_bug_report_send_notification_settings_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_change_server_error_unauthorized_homeserver` | %1$s is not allowed to connect to %2$s. | [link](https://localazy.com/p/element/source-language?search=screen_change_server_error_unauthorized_homeserver&searchOptions=KEY,EXACT_MATCH) |
| `screen_chat_backup_recovery_action_setup_description` | Your chats are automatically backed up with end-to-end encryption. To restore this backup and retain your digital ide… | [link](https://localazy.com/p/element/source-language?search=screen_chat_backup_recovery_action_setup_description&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_poll_anonymous_headline` | Hide votes | [link](https://localazy.com/p/element/source-language?search=screen_create_poll_anonymous_headline&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_poll_delete_option_a11y` | Delete option %1$s | [link](https://localazy.com/p/element/source-language?search=screen_create_poll_delete_option_a11y&searchOptions=KEY,EXACT_MATCH) |
| `screen_create_room_error_creating_room` | An error occurred when creating the room | [link](https://localazy.com/p/element/source-language?search=screen_create_room_error_creating_room&searchOptions=KEY,EXACT_MATCH) |
| `screen.create_room.error_creating_space` | The space could not be created because of an unknown error. Try again later. | [link](https://localazy.com/p/element/source-language?search=screen.create_room.error_creating_space&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_confirmation_sign_out` | Sign out | [link](https://localazy.com/p/element/source-language?search=screen_identity_confirmation_sign_out&searchOptions=KEY,EXACT_MATCH) |
| `screen_identity_use_another_device` | Use another device | [link](https://localazy.com/p/element/source-language?search=screen_identity_use_another_device&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_horizontally` | Flip image horizontally | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_horizontally&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_horizontally_state_flipped` | Flipped horizontally | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_horizontally_state_flipped&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_horizontally_state_original` | Original | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_horizontally_state_original&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_vertically` | Flip image vertically | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_vertically&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_vertically_state_flipped` | Flipped vertically | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_vertically_state_flipped&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_flip_image_vertically_state_original` | Original | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_flip_image_vertically_state_original&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y.rotate_to_the_left` | Rotate the image to the left | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y.rotate_to_the_left&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.a11y_rotation_state` | %1$d degrees | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.a11y_rotation_state&searchOptions=KEY,EXACT_MATCH) |
| `screen.image_edition.title` | Edit photo | [link](https://localazy.com/p/element/source-language?search=screen.image_edition.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.join_room.loading_alert_title` | We couldn’t display this room preview | [link](https://localazy.com/p/element/source-language?search=screen.join_room.loading_alert_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.knock_requests_list.ban_alert_description` | Are you sure you want to decline and ban %1$s? This user won’t be able to request access to join this room again. | [link](https://localazy.com/p/element/source-language?search=screen.knock_requests_list.ban_alert_description&searchOptions=KEY,EXACT_MATCH) |
| `screen.leave_space.choose_owners_action` | Choose owners | [link](https://localazy.com/p/element/source-language?search=screen.leave_space.choose_owners_action&searchOptions=KEY,EXACT_MATCH) |
| `screen.leave_space.last_admin_info` | %1$s (Admin) | [link](https://localazy.com/p/element/source-language?search=screen.leave_space.last_admin_info&searchOptions=KEY,EXACT_MATCH) |
| `screen.leave_space.title_last_owner` | Transfer ownership | [link](https://localazy.com/p/element/source-language?search=screen.leave_space.title_last_owner&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.desktop.scanning.title` | Scan the QR code | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.desktop.scanning.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.request_cancelled.subtitle` | The sign in was cancelled on the other device. | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.request_cancelled.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.request_cancelled.title` | Sign in request cancelled | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.request_cancelled.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.request_timeout.subtitle` | Sign in expired. Please try again. | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.request_timeout.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.error.request_timeout.title` | The sign in was not completed in time | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.error.request_timeout.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.wrong_number.subtitle` | Please try again and make sure that you’ve entered the 2-digit code correctly. If the numbers still don’t match then … | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.wrong_number.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.link_new_device.wrong_number.title` | The numbers don’t match | [link](https://localazy.com/p/element/source-language?search=screen.link_new_device.wrong_number.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.local_network_opt_in.subtitle` | Your homeserver is on your local network. To connect, %1$s needs permission to reach devices on this network. | [link](https://localazy.com/p/element/source-language?search=screen.local_network_opt_in.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.local_network_opt_in.title` | Allow access to local network | [link](https://localazy.com/p/element/source-language?search=screen.local_network_opt_in.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_login_subtitle` | Matrix is an open network for secure, decentralised communication. | [link](https://localazy.com/p/element/source-language?search=screen_login_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_media_browser_list_loading_files` | Loading files… | [link](https://localazy.com/p/element/source-language?search=screen_media_browser_list_loading_files&searchOptions=KEY,EXACT_MATCH) |
| `screen_media_browser_list_loading_media` | Loading media… | [link](https://localazy.com/p/element/source-language?search=screen_media_browser_list_loading_media&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_details.no_more_files_to_show` | No more files to show | [link](https://localazy.com/p/element/source-language?search=screen.media_details.no_more_files_to_show&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.change_video_quality_prompt` | Tap to change the video upload quality | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.change_video_quality_prompt&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.optimize_image_quality_title` | Optimise image quality | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.optimize_image_quality_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.media_upload_preview.title` | Add media | [link](https://localazy.com/p/element/source-language?search=screen.media_upload_preview.title&searchOptions=KEY,EXACT_MATCH) |
| `screen.moderation_and_safety.other_users_heading` | Other users | [link](https://localazy.com/p/element/source-language?search=screen.moderation_and_safety.other_users_heading&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.activity_section_title` | Activity | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.activity_section_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.call_ringtone_label` | Call ringtone | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.call_ringtone_label&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.message_sound_dialog_choose_other` | Choose another sound… | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.message_sound_dialog_choose_other&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.message_sound_dialog_current_subtitle` | Currently using %1$s | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.message_sound_dialog_current_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.message_sound_dialog_title` | Message sound | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.message_sound_dialog_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.message_sound_label` | Message sound | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.message_sound_label&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.sound_custom_fallback` | Custom | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.sound_custom_fallback&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.sound_set_sound_error_dismiss_a11y` | Dismiss alert sound error | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.sound_set_sound_error_dismiss_a11y&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.sound_silent` | Silent | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.sound_silent&searchOptions=KEY,EXACT_MATCH) |
| `screen.notification_settings.sound_system_default` | System Default | [link](https://localazy.com/p/element/source-language?search=screen.notification_settings.sound_system_default&searchOptions=KEY,EXACT_MATCH) |
| `screen.onboarding.add_account.subtitle` | You can add multiple accounts to the app and switch between them easily. | [link](https://localazy.com/p/element/source-language?search=screen.onboarding.add_account.subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen.onboarding.add_account.title` | Sign in to another account | [link](https://localazy.com/p/element/source-language?search=screen.onboarding.add_account.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_onboarding_sign_up` | Create account | [link](https://localazy.com/p/element/source-language?search=screen_onboarding_sign_up&searchOptions=KEY,EXACT_MATCH) |
| `screen.push_history.title` | Push history | [link](https://localazy.com/p/element/source-language?search=screen.push_history.title&searchOptions=KEY,EXACT_MATCH) |
| `screen_recovery_key_copied_to_clipboard` | Copied recovery key | [link](https://localazy.com/p/element/source-language?search=screen_recovery_key_copied_to_clipboard&searchOptions=KEY,EXACT_MATCH) |
| `screen.reset_encryption_password.error` | An unknown error happened. Please check your account password is correct and try again. | [link](https://localazy.com/p/element/source-language?search=screen.reset_encryption_password.error&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_alias_resolver_resolve_alias_failure` | Failed to resolve room alias. | [link](https://localazy.com/p/element/source-language?search=screen_room_alias_resolver_resolve_alias_failure&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_attachment_source_camera_photo` | Take photo | [link](https://localazy.com/p/element/source-language?search=screen_room_attachment_source_camera_photo&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_attachment_source_camera_video` | Record video | [link](https://localazy.com/p/element/source-language?search=screen_room_attachment_source_camera_video&searchOptions=KEY,EXACT_MATCH) |
| `screen.room.confirm_removal_reason_supporting_text` | (Optional) | [link](https://localazy.com/p/element/source-language?search=screen.room.confirm_removal_reason_supporting_text&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_invite_people_title` | Invite people | [link](https://localazy.com/p/element/source-language?search=screen_room_details_invite_people_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_details.invite_title` | Invite | [link](https://localazy.com/p/element/source-language?search=screen.room_details.invite_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_media_gallery_title` | Media and files | [link](https://localazy.com/p/element/source-language?search=screen_room_details_media_gallery_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_security_title` | Security | [link](https://localazy.com/p/element/source-language?search=screen_room_details_security_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_details_share_room_title` | Share room | [link](https://localazy.com/p/element/source-language?search=screen_room_details_share_room_title&searchOptions=KEY,EXACT_MATCH) |
| `screen.room.mentions_at_room_title` | Everyone | [link](https://localazy.com/p/element/source-language?search=screen.room.mentions_at_room_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_notification_settings_mode_mute` | Mute | [link](https://localazy.com/p/element/source-language?search=screen_room_notification_settings_mode_mute&searchOptions=KEY,EXACT_MATCH) |
| `screen.room_select.error.cannot_load_rooms` | The room list associated with this account cannot be loaded. | [link](https://localazy.com/p/element/source-language?search=screen.room_select.error.cannot_load_rooms&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_timeline_add_reaction` | Add a reaction | [link](https://localazy.com/p/element/source-language?search=screen_room_timeline_add_reaction&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_timeline_less_reactions` | Show less | [link](https://localazy.com/p/element/source-language?search=screen_room_timeline_less_reactions&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_timeline_message_copied` | Message copied | [link](https://localazy.com/p/element/source-language?search=screen_room_timeline_message_copied&searchOptions=KEY,EXACT_MATCH) |
| `screen.room.timeline_redacted_messages` | %1$d removed messages | [link](https://localazy.com/p/element/source-language?search=screen.room.timeline_redacted_messages&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_typing_many_members` | %1$s, %2$s and %3$d others | [link](https://localazy.com/p/element/source-language?search=screen_room_typing_many_members&searchOptions=KEY,EXACT_MATCH) |
| `screen_room_typing_notification` | %1$s are typing | [link](https://localazy.com/p/element/source-language?search=screen_room_typing_notification&searchOptions=KEY,EXACT_MATCH) |
| `screen_search_from_your_messages_header` | From your messages | [link](https://localazy.com/p/element/source-language?search=screen_search_from_your_messages_header&searchOptions=KEY,EXACT_MATCH) |
| `screen_server_confirmation_title_picker_mode` | Choose account provider | [link](https://localazy.com/p/element/source-language?search=screen_server_confirmation_title_picker_mode&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_compare_numbers_subtitle` | Confirm that the numbers below match those shown on your other session. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_compare_numbers_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_compare_numbers_title` | Compare numbers | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_compare_numbers_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_positive_button_verifying_ongoing` | Waiting to match… | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_positive_button_verifying_ongoing&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_ready_subtitle` | Compare a unique set of emojis. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_ready_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_failure_subtitle` | Either the request timed out, the request was denied, or there was a verification mismatch. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_failure_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_request_failure_title` | Verification failed | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_request_failure_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_user_requesting_verification` | User requesting verification: | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_user_requesting_verification&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_another_device_title` | Start verification on the other device | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_another_device_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_other_user_title` | Waiting for the other user | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_other_user_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_session_verification_waiting_subtitle` | Once accepted you’ll be able to continue with the verification. | [link](https://localazy.com/p/element/source-language?search=screen_session_verification_waiting_subtitle&searchOptions=KEY,EXACT_MATCH) |
| `screen_share_location_title` | Share location | [link](https://localazy.com/p/element/source-language?search=screen_share_location_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_reason_1` | You removed this device from your account | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_reason_1&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_reason_2` | You’ve changed your password on another device | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_reason_2&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_reason_3` | Your server's session expired or the administrator has blocked your access | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_reason_3&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_subtitle_v2` | This device was removed for one of the reasons listed below. Please sign in again to connect this device to your acco… | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_subtitle_v2&searchOptions=KEY,EXACT_MATCH) |
| `screen_signed_out_title` | Device removed | [link](https://localazy.com/p/element/source-language?search=screen_signed_out_title&searchOptions=KEY,EXACT_MATCH) |
| `screen_signout_in_progress_dialog_content` | Removing device… | [link](https://localazy.com/p/element/source-language?search=screen_signout_in_progress_dialog_content&searchOptions=KEY,EXACT_MATCH) |
| `screen.space_list.details` | %1$s • %2$s | [link](https://localazy.com/p/element/source-language?search=screen.space_list.details&searchOptions=KEY,EXACT_MATCH) |
| `screen.space.remove_rooms_confirmation_title` | Remove %1$d rooms from %2$s | [link](https://localazy.com/p/element/source-language?search=screen.space.remove_rooms_confirmation_title&searchOptions=KEY,EXACT_MATCH) |
| `settings_rageshake` | Rageshake | [link](https://localazy.com/p/element/source-language?search=settings_rageshake&searchOptions=KEY,EXACT_MATCH) |
| `settings_rageshake_detection_threshold` | Detection threshold | [link](https://localazy.com/p/element/source-language?search=settings_rageshake_detection_threshold&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_avatar` | Changes your profile picture in all rooms | [link](https://localazy.com/p/element/source-language?search=slash_command.description_avatar&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_avatar_for_room` | Changes your avatar in this current room only | [link](https://localazy.com/p/element/source-language?search=slash_command.description_avatar_for_room&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_ban_user` | Bans user with given id | [link](https://localazy.com/p/element/source-language?search=slash_command.description_ban_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_confetti` | Sends the given message with confetti | [link](https://localazy.com/p/element/source-language?search=slash_command.description_confetti&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_crash_application` | Crash the application. | [link](https://localazy.com/p/element/source-language?search=slash_command.description_crash_application&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_deop_user` | Deops user with given id | [link](https://localazy.com/p/element/source-language?search=slash_command.description_deop_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_devtools` | Open the developer tools screen | [link](https://localazy.com/p/element/source-language?search=slash_command.description_devtools&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_discard_session` | Forces the current outbound group session in an encrypted room to be discarded | [link](https://localazy.com/p/element/source-language?search=slash_command.description_discard_session&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_emote` | Displays action | [link](https://localazy.com/p/element/source-language?search=slash_command.description_emote&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_ignore_user` | Ignores a user, hiding their messages from you | [link](https://localazy.com/p/element/source-language?search=slash_command.description_ignore_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_invite_user` | Invites user with given id to current room | [link](https://localazy.com/p/element/source-language?search=slash_command.description_invite_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_join_room` | Joins room with given address | [link](https://localazy.com/p/element/source-language?search=slash_command.description_join_room&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_leave_room` | Leave the current room | [link](https://localazy.com/p/element/source-language?search=slash_command.description_leave_room&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_lenny` | Prepends ( ͡° ͜ʖ ͡°) to a plain-text message | [link](https://localazy.com/p/element/source-language?search=slash_command.description_lenny&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_nick` | Changes your display nickname | [link](https://localazy.com/p/element/source-language?search=slash_command.description_nick&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_nick_for_room` | Changes your display nickname in the current room only | [link](https://localazy.com/p/element/source-language?search=slash_command.description_nick_for_room&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_op_user` | Define the power level of a user | [link](https://localazy.com/p/element/source-language?search=slash_command.description_op_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_plain` | Sends a message as plain text, without interpreting it as markdown | [link](https://localazy.com/p/element/source-language?search=slash_command.description_plain&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_rainbow` | Sends the given message colored as a rainbow | [link](https://localazy.com/p/element/source-language?search=slash_command.description_rainbow&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_rainbow_emote` | Sends the given emote colored as a rainbow | [link](https://localazy.com/p/element/source-language?search=slash_command.description_rainbow_emote&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_remove_user` | Removes user with given id from this room | [link](https://localazy.com/p/element/source-language?search=slash_command.description_remove_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_room_avatar` | Changes the avatar of the current room | [link](https://localazy.com/p/element/source-language?search=slash_command.description_room_avatar&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_room_name` | Sets the room name | [link](https://localazy.com/p/element/source-language?search=slash_command.description_room_name&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_shrug` | Prepends ¯\\_(ツ)_/¯ to a plain-text message | [link](https://localazy.com/p/element/source-language?search=slash_command.description_shrug&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_snow` | Sends the given message with snowfall | [link](https://localazy.com/p/element/source-language?search=slash_command.description_snow&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_spoiler` | Sends the given message as a spoiler | [link](https://localazy.com/p/element/source-language?search=slash_command.description_spoiler&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_table_flip` | Prepends (╯°□°）╯︵ ┻━┻ to a plain-text message | [link](https://localazy.com/p/element/source-language?search=slash_command.description_table_flip&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_topic` | Set the room topic | [link](https://localazy.com/p/element/source-language?search=slash_command.description_topic&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_unban_user` | Unbans user with given id | [link](https://localazy.com/p/element/source-language?search=slash_command.description_unban_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_unflip` | Prepends ┬──┬ ノ( ゜-゜ノ) to a plain-text message | [link](https://localazy.com/p/element/source-language?search=slash_command.description_unflip&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_unignore_user` | Stops ignoring a user, showing their messages going forward | [link](https://localazy.com/p/element/source-language?search=slash_command.description_unignore_user&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_upgrade_room` | Upgrades a room to a new version | [link](https://localazy.com/p/element/source-language?search=slash_command.description_upgrade_room&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.description_whois` | Displays information about a user | [link](https://localazy.com/p/element/source-language?search=slash_command.description_whois&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.not_supported_in_threads` | The command "%1$s" is recognized but not supported in threads. | [link](https://localazy.com/p/element/source-language?search=slash_command.not_supported_in_threads&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.parameters_error` | The command "%1$s" needs more parameters, or some parameters are incorrect. The syntax is  %2$s | [link](https://localazy.com/p/element/source-language?search=slash_command.parameters_error&searchOptions=KEY,EXACT_MATCH) |
| `slash_command.unrecognized` | Unrecognized command: %1$s | [link](https://localazy.com/p/element/source-language?search=slash_command.unrecognized&searchOptions=KEY,EXACT_MATCH) |
| `state_event_room_none` | %1$s made no changes | [link](https://localazy.com/p/element/source-language?search=state_event_room_none&searchOptions=KEY,EXACT_MATCH) |
| `state_event_room_none_by_you` | You made no changes | [link](https://localazy.com/p/element/source-language?search=state_event_room_none_by_you&searchOptions=KEY,EXACT_MATCH) |
| `theme.black` | Black | [link](https://localazy.com/p/element/source-language?search=theme.black&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_entry_point_push_history_title` | Push history | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_entry_point_push_history_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_entry_point_section` | Troubleshoot | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_entry_point_section&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_entry_point_title` | Troubleshoot notifications | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_entry_point_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_action` | Run tests | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_action&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_action_again` | Run tests again | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_action_again&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_failure` | Some tests failed. Please check the details. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_notice` | Run the tests to detect any issue in your configuration that may make notifications not behave as expected. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_notice&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_quick_fix_action` | Attempt to fix | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_quick_fix_action&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_success` | All tests passed successfully. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_title` | Troubleshoot notifications | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_screen_waiting` | Some tests require your attention. Please check the details. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_screen_waiting&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications.test_blocked_users.description` | Checking blocked users | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications.test_blocked_users.description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications.test_blocked_users.quick_fix` | View blocked users | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications.test_blocked_users.quick_fix&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications.test_blocked_users.result_none` | No users are blocked. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications.test_blocked_users.result_none&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications.test_blocked_users.result_some` | You blocked %1$d users. You will not receive notifications for these users. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications.test_blocked_users.result_some&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications.test_blocked_users.title` | Blocked users | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications.test_blocked_users.title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_check_permission_description` | Check that the application can show notifications. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_check_permission_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_check_permission_title` | Check permissions | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_check_permission_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_description` | Get the name of the current provider. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_failure` | No push providers selected. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_failure_distributor_not_found` | Current push provider: %1$s and current distributor: %2$s. But the distributor %3$s is not found. Maybe the applicati… | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_failure_distributor_not_found&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_failure_no_distributor` | Current push provider: %1$s, but no distributors have been configured. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_failure_no_distributor&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_success` | Current push provider: %1$s. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_success_with_distributor` | Current push provider: %1$s (%2$s) | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_success_with_distributor&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_current_push_provider_title` | Current push provider | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_current_push_provider_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_detect_push_provider_description` | Ensure that the application supports at least one push provider. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_detect_push_provider_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_detect_push_provider_failure` | No push provider support found. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_detect_push_provider_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_detect_push_provider_success_2` | The application was built with support for: %1$s | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_detect_push_provider_success_2&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_detect_push_provider_title` | Push provider support | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_detect_push_provider_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_description` | Check that the application can display notification. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_failure` | The notification has not been clicked. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_permission_failure` | Cannot display the notification. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_permission_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_success` | The notification has been clicked! | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_title` | Display notification | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_display_notification_waiting` | Please tap the notification to continue the test. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_display_notification_waiting&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_availability_description` | Ensure that Firebase is available. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_availability_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_availability_failure` | Firebase is not available. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_availability_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_availability_success` | Firebase is available. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_availability_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_availability_title` | Check Firebase | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_availability_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_token_description` | Ensure that Firebase token is available. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_token_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_token_failure` | Firebase token is not known. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_token_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_token_success` | Firebase token: %1$s. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_token_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_firebase_token_title` | Check Firebase token | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_firebase_token_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_description` | Ensure that the application is receiving push. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_failure_1` | Error: pusher has rejected the request. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_failure_1&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_failure_2` | Error: %1$s. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_failure_2&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_failure_3` | Error, cannot test push. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_failure_3&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_failure_4` | Error, timeout waiting for push. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_failure_4&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_failure_rate_limit` | Error: the push gateway is rate limiting this device, so notifications won't be reliable. Please set up a different p… | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_failure_rate_limit&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_success` | Push loop back took %1$d ms. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_push_loop_back_title` | Test Push loop back | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_push_loop_back_title&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_unified_push_description` | Ensure that UnifiedPush distributors are available. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_unified_push_description&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_unified_push_failure` | No push distributors found. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_unified_push_failure&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_unified_push_success` | %1$d distributors found: %2$s. | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_unified_push_success&searchOptions=KEY,EXACT_MATCH) |
| `troubleshoot_notifications_test_unified_push_title` | Check UnifiedPush | [link](https://localazy.com/p/element/source-language?search=troubleshoot_notifications_test_unified_push_title&searchOptions=KEY,EXACT_MATCH) |

</details>
