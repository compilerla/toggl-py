#!/usr/bin/env bash
set -eux

cd $CODEGEN_DIR/$CODEGEN_LANG

mvn package
