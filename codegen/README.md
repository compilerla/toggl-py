# toggl-py codegen

This folder contains configuration and scripts for generating the `toggl-py` source from
[Toggl's OpenApi (Swagger) spec](./spec.json).

Code generation uses a custom Docker image wrapping the
[`swagger-codegen-cli`](https://github.com/swagger-api/swagger-codegen.git).

## Setup

From the root of this repository

1. Create an environment file from the sample (defaults are good for now)

   ```bash
   cp .env.sample .env
   ```

2. Then build the main Docker image:

   ```bash
   docker compose build
   ```

## Open a devcontainer

Open this repository in VS Code, then `Rebuild and Reopen in Container`.

## Generate the code

(Outside a devcontainer), run the Docker Compose `codegen` service:

```bash
docker compose run codegen
```

(Inside the devcontainer), run the codegen script directly:

```bash
codegen/bin/run.sh
```

## Edit configuration

Some configuration values can be changed in [`config.json`](./config.json).

Other flags for `swagger-codegen` can be modified in the [`run.sh`](./bin/run.sh) script.

Use the [`help.sh`](./bin/help.sh) script to find out more about `swagger-codegen-cli` configuration options:

```bash
codegen/bin/help.sh
```

## Edit templates

Custom [Mustache](https://mustache.github.io/) templates used to generate the files live under [`./TogglPythonClientCodegen/src/main/resources/TogglPythonClientCodegen/`](./TogglPythonClientCodegen/src/main/resources/TogglPythonClientCodegen/).

## Edit the generator class

[`TogglPythonClientCodegen`](./TogglPythonClientCodegen/src/main/java/la/compiler/codegen/TogglPythonClientCodegen.java) is the
custom Java class, inheriting from and overriding some behavior of Swagger's [`PythonClientCodegen`](https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen/src/main/java/io/swagger/codegen/languages/PythonClientCodegen.java),
serving as the "language" implementation that `swagger-codegen-cli` uses to generate `toggl-py`.
