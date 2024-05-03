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

# remove lines that import either api
sed -i "/from toggl.api.default_api/d" $CODEGEN_PKG/__init__.py $CODEGEN_PKG/api/__init__.py
sed -i "/from toggl.api.utils_api/d" $CODEGEN_PKG/__init__.py $CODEGEN_PKG/api/__init__.py

# the second one is named api/default_api.py and contains reports_api_v3 endpoints
# this file was generated and then updated manually
rm $CODEGEN_PKG/api/default_api.py

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

# remove unused and circular DTO objects
declare -a dto_classes=(
    "dto_agg_filter_request"
    "dto_aggregation_request"
    "dto_attribute_request"
    "dto_creation_request"
    "dto_filter_request"
    "dto_get_response"
    "dto_grouping_request"
    "dto_ordination_request"
    "dto_period_request"
    "dto_project_filter_param_request"
    "dto_project_filter_response"
    "dto_project_group_params_request"
    "dto_project_group_response"
    "dto_project_user_params_request"
    "dto_project_user_response"
    "dto_query_request"
    "dto_transformation_request"
)

for cls in "${dto_classes[@]}"
do
    rm "$CODEGEN_PKG/models/$cls.py"
    sed -i "/from toggl.models.$cls/d" $CODEGEN_PKG/__init__.py $CODEGEN_PKG/models/__init__.py
done

# reformat all python files
black $CODEGEN_TARGET

# remove strange .pye files
rm -f $CODEGEN_PKG/**/*.pye
