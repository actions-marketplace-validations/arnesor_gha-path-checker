# GitHub Action for detecting spaces and non-ascii characters in paths

[![Actions Status](https://github.com/arnesor/gha-path-checker/workflows/Lint/badge.svg)](https://github.com/arnesor/gha-path-checker/actions)
[![Actions Status](https://github.com/arnesor/gha-path-checker/workflows/Integration%20Test/badge.svg)](https://github.com/arnesor/gha-path-checker/actions)

This GitHub Action checks your repository for problematic path names (both in the
directory part and in the filename part). If it detects problematic paths, the
problematic paths are listed and the action fails.

Problematic path names are paths with space characters. The GitHub Action can also
optionally check for paths with non-ascii characters, using the  `allow_non_ascii `
option. For example paths with the norwegian letters "æøå".

The article [how to make a python-based GitHub action](https://jacobtomlinson.dev/posts/2019/creating-github-actions-in-python/)
has been a great help for developing this GitHub Action. 

## Usage

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Path checks
        id: pathcheck
        uses: arnesor/gha-path-checker@master
        with:
          allow_non_ascii: false
```

### Inputs

| Input                          | Description                                          |
|--------------------------------|------------------------------------------------------|
| `allow_non_ascii` _(optional)_ | Allow non-ascii characters in paths. Default _true_. |

### Outputs

| Output    | Description                  |
|-----------|------------------------------|
| `errors`  | Number of paths with errors. |
