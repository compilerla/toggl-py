#!/usr/bin/env bash
set -eux

java -jar $CODEGEN_JAR meta \
    --name $CODEGEN_LANG \
    --output $CODEGEN_DIR/$CODEGEN_LANG \
    --package la.compiler.codegen
