#!/usr/bin/env bash
set -eux

docker run --rm -u 1000:1000 -v ${PWD}:/dist -w /dist swaggerapi/swagger-codegen-cli help generate
docker run --rm -u 1000:1000 -v ${PWD}:/dist -w /dist swaggerapi/swagger-codegen-cli config-help -l python
