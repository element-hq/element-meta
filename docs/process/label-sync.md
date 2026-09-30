# Label sync

element-meta provides a reusable workflow, [`sync-labels.yml`](../../.github/workflows/sync-labels.yml),
that keeps a repository's labels in sync with one or more sources. A source is either a GitHub
repository, whose current labels are used, or a local YAML file in the
[github-label-sync format](https://github.com/Financial-Times/github-label-sync#label-config-file).
Later sources override earlier ones.

element-web and matrix-js-sdk use it with the labels of element-meta itself as the shared base,
plus their own `.github/labels.yml`. So a label created in element-meta appears in those
repositories at their next sync.

## Setting it up in another repository

Create an empty `.github/labels.yml` and a workflow `.github/workflows/sync-labels.yml`:

```yaml
name: Sync labels
on:
    workflow_dispatch: {}
    schedule:
        - cron: "0 2 * * *" # 2am every day
    push:
        branches:
            - develop
        paths:
            - .github/labels.yml

permissions: {} # We use ELEMENT_BOT_TOKEN instead

jobs:
    sync-labels:
        uses: element-hq/element-meta/.github/workflows/sync-labels.yml@develop
        with:
            LABELS: |
                element-hq/element-meta
                .github/labels.yml
            DELETE: true
            WET: false
        secrets:
            ELEMENT_BOT_TOKEN: ${{ secrets.ELEMENT_BOT_TOKEN }}
```

This syncs the labels of element-hq/element-meta and of the local `labels.yml`. `WET: false` makes
the workflow run in dry mode, without changing any label.

Run the workflow once by hand. Its logs summarise the changes it would apply. Look in particular at
the labels that exist only in your repository:

```
The following labels exist in <your repository> but are missing in all sources. They will be deleted.
- name: "bug"
  description: "Something isn't working"
  color: "d73a4a"
- name: "documentation"
  ...
```

To keep them, either copy them to `labels.yml` or set `DELETE: false`.

Then set `WET: true` and run the workflow again. The first run may hit GitHub's rate limits:

```
Error: You have exceeded a secondary rate limit. Please wait a few minutes before you try again.
```

If so, wait a few minutes and run it again to apply the remaining changes. From then on, the labels
stay in sync automatically.
