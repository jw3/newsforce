News Check Action
===

This GitHub Action provides an opinionated interface to enforce changelog entries on PRs for towncrier.

## Example workflow

```yaml
name: build
on: [push, pull_request]

jobs:
  rpm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: jw3/newscheck@v0
```

## License

MIT
