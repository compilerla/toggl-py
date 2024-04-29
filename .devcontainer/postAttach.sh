#!/usr/bin/env bash
set -eux

codegen/bin/package.sh

pip install -e toggl_py/[test]
