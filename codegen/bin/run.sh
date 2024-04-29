#!/usr/bin/env bash
set -eux

java -cp $CODEGEN_JAR:$CODEGEN_DIR/$CODEGEN_LANG/target/* \
    io.swagger.codegen.SwaggerCodegen generate \
    --config $CODEGEN_DIR/config.json \
    --git-repo-id toggl-py \
    --git-user-id compilerla \
    --http-user-agent compilerla/toggl-py \
    --input-spec $CODEGEN_DIR/spec.json \
    --lang $CODEGEN_LANG \
    --output $CODEGEN_TARGET \
    --template-dir $CODEGEN_DIR/$CODEGEN_LANG/src/main/resources/$CODEGEN_LANG

black $CODEGEN_TARGET
