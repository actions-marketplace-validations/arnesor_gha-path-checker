# GitHub Action for detecting spaces and non-ascii characters in paths

[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)
[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Integration%20Test/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)

This GitHub action contains a small Python application which will be built into a minimal [Container Action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-a-docker-container-action). Our final container from this template is ~50MB, yours may be a little bigger once you add some code.

In `main.py` you will find a small example of accessing Action inputs and returning Action outputs. For more information on communicating with the workflow see the [development tools for GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/development-tools-for-github-actions).

Article describing [how to make a python-based GitHub action](https://jacobtomlinson.dev/posts/2019/creating-github-actions-in-python/).

## Usage

Describe how to use your action here.

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action

      # Put your action repo here
      uses: me/myaction@master

      # Put an example of your mandatory inputs here
      with:
        myInput: world
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `myInput`  | An example mandatory input    |
| `anotherInput` _(optional)_  | An example optional input    |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `myOutput`  | An example output (returns 'Hello world')    |

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!

### Using the optional input

This is how to use the optional input.

```yaml
with:
  myInput: world
  anotherInput: optional
```

### Using outputs

Show people how to use your outputs in another action.

```yaml
steps:
- uses: actions/checkout@master
- name: Run action
  id: myaction

  # Put your action name here
  uses: me/myaction@master

  # Put an example of your mandatory arguments here
  with:
    myInput: world

# Put an example of using your outputs here
- name: Check outputs
    run: |
    echo "Outputs - ${{ steps.myaction.outputs.myOutput }}"
```