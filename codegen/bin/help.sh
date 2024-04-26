#!/usr/bin/env bash
set -eux

java -cp ~/swagger-codegen-cli.jar:codegen/TogglPythonClientCodegen/target/* io.swagger.codegen.SwaggerCodegen help generate
java -cp ~/swagger-codegen-cli.jar:codegen/TogglPythonClientCodegen/target/* io.swagger.codegen.SwaggerCodegen config-help -l TogglPythonClientCodegen
