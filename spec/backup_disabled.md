# m.org.matrix.custom.backup_disabled: Recording whether key backup is enabled or disabled

The `m.org.matrix.custom.backup_disabled` account data event records whether the
user has disabled key backup, so that this information is synchronised between
their devices.  Its main purpose is to avoid continuously nagging the user on
multiple devices if they have already chosen to disable key backup.

It is an object with a boolean property, `disabled`.  If the user has chosen to
not enable key backup (for example, by disabling key backup, or by dismissing a
toast prompting them to enable recovery), `disabled` is set to `true`.  If the
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


## Implementations

* `element-web` implemented this in February 2025:
  * https://github.com/element-hq/element-web/pull/29290
* `matrix-rust-sdk` implemented this in November 2023:
  * https://github.com/matrix-org/matrix-rust-sdk/pull/2842
