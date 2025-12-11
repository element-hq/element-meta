# io.element.recovery: Recording whether recovery is enabled or disabled

## Problem

We allow users to disable recovery (secret storage), and if a user does so, we
do not want to continue to nag them.  This information needs to be synced
between clients so that users are not nagged in different places after having
disabled recovery.

## Proposal

We introduce a new account data event, `io.element.recovery`, which is an object
with a boolean property, `enabled`.  If the user has chosen to not enable
recovery (for example, by disabling recovery, or by dismissing a toast prompting
them to enable recovery), `enabled` is set to `false`.  If the user has chosen
to enable recovery, `enabled` is set to `true`.  If `enabled` is set to `false`
but recovery is set up, the client should ignore the value of `enabled`.

If there is no `io.element.recovery` event, this indicates that the user has not
make any decision yet about recovery.  In this case, if recovery is not yet set
up (but key backup is enabled), we prompt the user to enable recovery.

Note that we will only enable recovery if key backup is enabled.  This means
that the value of this account data event is affected by the value of
[`m.org.matrix.custom.backup_disabled`](backup_disabled.md) account data event.
In particular, if `m.org.matrix.custom.backup_disabled` has `"disabled": true`,
then we ignore this account data, since we will not prompt the user to enable
recovery.  However, if a user enables key backup
(`m.org.matrix.custom.backup_disabled` set to `{"disabled": false}`), they may
disable or enable recovery.

## MSC

None

## Security considerations

A malicious actor could set the value of `enabled` to `false` for a new user, in
which case they would not be prompted to enable recovery.  However, this will
not allow the attacker to gain any information, nor will it prevent the user
from enabling recovery.  It only prevents the user from being prompted to enable
recovery.

## Implementations

* `element-web` implemented this in June 2025
  * https://github.com/element-hq/element-web/pull/30075
