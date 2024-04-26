#!/usr/bin/env bash
set -eux

docker run --rm -u 1000:1000 -v ${PWD}:/dist -w /dist swaggerapi/swagger-codegen-cli meta \
    --name TogglPythonClientCodegen \
    --output codegen/TogglPythonClientCodegen \
    --package la.compiler.codegen
