# `toggl-py` codegen

This folder contains configuration and scripts for generating the `toggl-py` source from
[Toggl's OpenApi (Swagger) spec](./spec.json).

Code generation uses the Docker image wrapping [`swagger-codegen`](https://github.com/swagger-api/swagger-codegen.git).

## Generate the code

From the root of this repository, run the generate script:

```bash
codegen/bin/run.sh
```

_Requires Docker_

## Edit configuration

Some configuration values can be changed in [`config.json`](./config.json).

Other flags for `swagger-codegen` can be modified in the [`run.sh`](./bin/run.sh) script.

Use the [`help.sh`](./bin/help.sh) script to find out more about `swagger-codegen` configuration options:

```bash
codegen/bin/help.sh
```

_Requires Docker_

## Edit templates

The [`templates`](./templates/) directory contains [Mustache](https://mustache.github.io/) templates for the generated files.
