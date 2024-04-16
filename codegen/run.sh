#!/usr/bin/env bash
set -eux

docker run --rm -u 1000:1000 -v ${PWD}:/dist -w /dist swaggerapi/swagger-codegen-cli generate \
    --config codegen/config.json \
    --git-repo-id toggl-py \
    --git-user-id compilerla \
    --http-user-agent compilerla/toggl-py \
    --input-spec codegen/spec.json \
    --lang python \
    --output toggl_py
