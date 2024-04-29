#!/usr/bin/env bash
set -eux

# run normal pytests
coverage run -m pytest

# clean out old coverage results
rm -rf docs/coverage

coverage html --directory docs/coverage
