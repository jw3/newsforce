News Force Action
===

This GitHub Action provides enforcement of changelog entries on PRs.

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

## License

MIT
