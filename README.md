# action-set-env-from-yaml
Set environment variables from YAML key-value pairs

# Requirements

The action was tested to work on ubuntu runners with no prior setup required.

# Overview

The action takes a YAML file of the following format as input:

```
some_var: some_value
other_var: other_value
...
```

It then uses each key-value pair to set a corresponding environment variable,
so that it is available in subsequent steps.

An example use case is a YAML file containing versions of
dependencies required to build or run a project. The action can then be used
as a single step to extract all the dependencies.

## Inputs

| Input | Description | Required | Default |
|---|---|---|---|
| file  | Path to the YAML file | true | none |

## Outputs

| Output | Description |
|---|---|


# Example

The following is an example of the action being used in a workflow.
In the example, the action is used to fetch dependency versions and
expose them to subsequent steps. Another action can then be used to
fetch those dependencies.

```
name: Example Workflow
on:
  workflow_dispatch:
    inputs:

jobs:
  check-deps:
    name: Check Dependencies
    runs-on: ubuntu-latest
    steps:
      -
        name: Get Deps
        id: get-deps
        uses: husarion-ci/action-set-env-from-yaml@v0.1.0
        with:
          file: ${{ github.workspace }}/dependencies.yaml
      -
        name: Fetch dependencies
        uses: 
```