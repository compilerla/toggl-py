#!/usr/bin/env bash
set -eux

codegen/bin/package.sh

cd toggl_py && pip install -e .[test]
