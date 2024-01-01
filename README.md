News Force Action
===

This GitHub Action provides enforcement of changelog entries on PRs.

This action ensures that a news article that relates to the current PR has been created.

## Example workflow

```yaml
name: build
on: pull_request

jobs:
  enforce-changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: jw3/newsforce@v0
```

## towncrier

The intended consumer of the news articles is `towncrier`.

The intent of this action can perhaps be better understood through their documentation:

> `towncrier` delivers the news which is convenient to those that hear it, not those that write it.
>
> That is, by duplicating what has changed from the “developer log” (which may contain complex information about the original issue, how it was fixed, who authored the fix, and who reviewed the fix) into a “news fragment” (a small file containing just enough information to be useful to end users), towncrier can produce a digest of the changes which is valuable to those who may wish to use the software. These fragments are also commonly called “topfiles” or “newsfiles”.
>
> towncrier works best in a development system where all merges involve closing a ticket.

It is noteworthy that this action does not invoke `towncrier`, so the news articles guaranteed could be consumed by
other changelog generators.

## License

MIT
