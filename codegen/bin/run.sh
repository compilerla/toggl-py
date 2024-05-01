#!/usr/bin/env bash
set -eux

CODEGEN_DOCS="$CODEGEN_TARGET/docs"
CODEGEN_PKG="$CODEGEN_TARGET/toggl"
CODEGEN_TESTS="$CODEGEN_TARGET/tests"

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

# generation produces 2 api files, both defining a DefaultApi class, with endpoints represented elsewhere

# the first one is named api/_api.py and contains OrganizationApi endpoints, it can be removed
rm $CODEGEN_PKG/api/_api.py
rm $CODEGEN_TESTS/api/test__api.py
# select all lines except those that match and write back to the file
sed -i "/from toggl.api.default_api import DefaultApi/d" $CODEGEN_PKG/__init__.py
sed -i "/from toggl.api.default_api import DefaultApi/d" $CODEGEN_PKG/api/__init__.py

# the second one is named api/default_api.py and contains reports_api_v3 endpoints
mv $CODEGEN_PKG/api/default_api.py $CODEGEN_PKG/api/reports_api_v3.py
mv $CODEGEN_TESTS/api/test_default_api.py $CODEGEN_TESTS/api/test_reports_api_v3.py
# replace the old class and package name
sed -i "s/DefaultApi/ReportsApiv3/g" $CODEGEN_PKG/api/reports_api_v3.py
sed -i "s/reports_api_v3_workspace_workspace_id_//g" $CODEGEN_PKG/api/reports_api_v3.py
sed -i "s/DefaultApi/ReportsApiv3/g" $CODEGEN_TESTS/api/test_reports_api_v3.py
sed -i "s/default_api/reports_api_v3/g" $CODEGEN_TESTS/api/test_reports_api_v3.py
sed -i "s/reports_api_v3_workspace_workspace_id_//g" $CODEGEN_TESTS/api/test_reports_api_v3.py
IMPORT_LINE="from toggl.api.reports_api_v3 import ReportsApiv3  # noqa: F401"
echo $IMPORT_LINE >> $CODEGEN_PKG/__init__.py
echo $IMPORT_LINE >> $CODEGEN_PKG/api/__init__.py

black $CODEGEN_TARGET

rm -f $CODEGEN_PKG/api/*.pye
