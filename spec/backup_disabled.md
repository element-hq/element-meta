# m.org.matrix.custom.backup_disabled: Recording whether key backup is enabled or disabled

## Problem

We allow users to disable key backup, and if a user does so, we do not want to
continue to nag them.  This information needs to be synced between clients so
that users are not nagged is several places after having disabled backup.

## Proposal

We introduce a new account data event, `m.org.matrix.custom.backup_disabled`,
which is an object with a boolean property, `disabled`.  If the user has chosen
to not enable key backup (for example, by disabling key backup, or by dismissing
a toast prompting them to enable recovery), `disabled` is set to `true`.  If the
user has chosen to enable key backup, `disabled` is set to `false`.  If
`disabled` is set to `true` but key backup is set up, the client should ignore
the value of `disabled`.

If there is no `m.org.matrix.custom.backup_disabled` event, this indicates that
the user has not make any decision yet about key backup.  In this case, if
backup is not yet set up, we prompt the user to enable backup.

## MSC

This is an older version of
[MSC4287](https://github.com/matrix-org/matrix-spec-proposals/pull/4287), and [we
should eventually migrate to the system described there](https://github.com/element-hq/element-meta/issues/2745).

The main difference between this proposal and the MSC is that the MSC uses an
`enabled` property with the values having the reverse meaning of the `disabled`
property used in this proposal.

## Security considerations

A malicious actor could set the value of `disabled` to `true` for a new user, in
which case they would not be prompted to enable key backup.  However, this will
not allow the attacker to gain any information, nor will it prevent the user
from enabling key backup.  It only prevents the user from being prompted to
enable key backup.

## Implementations

* `element-web` implemented this in February 2025:
  * https://github.com/element-hq/element-web/pull/29290
TODO: record when Element X implemented this
