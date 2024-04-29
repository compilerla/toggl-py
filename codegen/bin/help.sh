#!/usr/bin/env bash
set -eux

java -cp $CODEGEN_JAR:$CODEGEN_DIR/$CODEGEN_LANG/target/* io.swagger.codegen.SwaggerCodegen help generate
java -cp $CODEGEN_JAR:$CODEGEN_DIR/$CODEGEN_LANG/target/* io.swagger.codegen.SwaggerCodegen config-help -l $CODEGEN_LANG
