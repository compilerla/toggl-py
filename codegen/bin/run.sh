#!/usr/bin/env bash
set -eux

TARGET=toggl_py

rm -rf $TARGET

java -cp ~/swagger-codegen-cli.jar:codegen/TogglPythonClientCodegen/target/* \
    io.swagger.codegen.SwaggerCodegen generate \
    --config codegen/config.json \
    --git-repo-id toggl-py \
    --git-user-id compilerla \
    --http-user-agent compilerla/toggl-py \
    --input-spec codegen/spec.json \
    --lang TogglPythonClientCodegen \
    --output $TARGET \
    --template-dir codegen/TogglPythonClientCodegen/src/main/resources/TogglPythonClientCodegen

rm -rf $TARGET/test

black $TARGET

pip install -e $TARGET
