#!/usr/bin/env bash
set -eux

CODEGEN_DOCS="$CODEGEN_TARGET/docs"
CODEGEN_PKG="$CODEGEN_TARGET/toggl"
CODEGEN_TESTS="$CODEGEN_TARGET/tests"

# replaces invalid generated type hint syntax for dictionaries
# from:
#   dict(str, ModelClass)
# to:
#   dict[str, ModelClass]
find $CODEGEN_PKG/**/*.py -type f -exec \
    sed -Ei "s/([^\"])dict\((\w+), (\w+)\)/\1dict[\2, \3]/g" {} \;

# generation produces 2 api files, both defining a DefaultApi class, with endpoints represented elsewhere

# the first one is named api/_api.py and contains OrganizationApi endpoints, it can be removed
rm $CODEGEN_PKG/api/_api.py

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

# add the new import line back
IMPORT_LINE="from toggl.api.reports_api_v3 import ReportsApiv3  # noqa: F401"
echo $IMPORT_LINE >> $CODEGEN_PKG/__init__.py
echo $IMPORT_LINE >> $CODEGEN_PKG/api/__init__.py

# generation produces a class for the JSON Schema type utils.Int64Slice
# which is just an alias for list[int], so overwrite it
echo "UtilsInt64Slice = list[int]" > $CODEGEN_PKG/models/utils_int64_slice.py

# the spec has a reference to, but no definition for, #/definitions/summary.GroupData
# make it an alias for Any
echo "from typing import Any" > $CODEGEN_PKG/models/summary_group_data.py
echo "SummaryGroupData = Any" >> $CODEGEN_PKG/models/summary_group_data.py

# remove the rates API
# at this time this is undocumented on https://engineering.toggl.com/docs/
# and the definition contains a circular reference causing an import error
rm $CODEGEN_PKG/api/rates_api.py

# remove lines importing rates API
sed -i "/from toggl.api.rates_api/d" $CODEGEN_PKG/__init__.py $CODEGEN_PKG/api/__init__.py

# reformat all python files
black $CODEGEN_TARGET

# remove strange .pye files
rm -f $CODEGEN_PKG/**/*.pye
