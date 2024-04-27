# toggl.ExportsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me_export**](ExportsApi.md#get_me_export) | **GET** /me/export | Get a list of objects to be downloaded
[**get_me_export_data_uuid_zip**](ExportsApi.md#get_me_export_data_uuid_zip) | **GET** /me/export/data/{uuid}.zip | Get the zip file with download requests
[**get_workspace_exports**](ExportsApi.md#get_workspace_exports) | **GET** /workspaces/{workspace_id}/exports | Get a list with the workspace download requests
[**get_workspace_exports_data_uuid_zip**](ExportsApi.md#get_workspace_exports_data_uuid_zip) | **GET** /workspaces/{workspace_id}/exports/data/{uuid}.zip | Get the zip file with workspace download requests
[**insights_api_v1_workspace_workspace_id_profitability_employees_extension_post**](ExportsApi.md#insights_api_v1_workspace_workspace_id_profitability_employees_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/profitability/employees.{extension} | Export employee profitability insights
[**insights_api_v1_workspace_workspace_id_profitability_projects_extension_post**](ExportsApi.md#insights_api_v1_workspace_workspace_id_profitability_projects_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/profitability/projects.{extension} | Export profitability project insights
[**insights_api_v1_workspace_workspace_id_trends_projects_extension_post**](ExportsApi.md#insights_api_v1_workspace_workspace_id_trends_projects_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/trends/projects.{extension} | Export projects data trends
[**post_me_export**](ExportsApi.md#post_me_export) | **POST** /me/export | Post an object which data to be downloaded
[**post_workspace_exports**](ExportsApi.md#post_workspace_exports) | **POST** /workspaces/{workspace_id}/exports | Post a list with the workspace to be downloaded
[**reports_api_v3_shared_report_token_csv_post**](ExportsApi.md#reports_api_v3_shared_report_token_csv_post) | **POST** /reports/api/v3/shared/{report_token}.csv | Export CSV for saved report
[**reports_api_v3_shared_report_token_pdf_post**](ExportsApi.md#reports_api_v3_shared_report_token_pdf_post) | **POST** /reports/api/v3/shared/{report_token}/pdf | Export saved report in pdf format
[**reports_api_v3_shared_report_token_xlsx_post**](ExportsApi.md#reports_api_v3_shared_report_token_xlsx_post) | **POST** /reports/api/v3/shared/{report_token}.xlsx | Export XSLX saved report
[**reports_api_v3_workspace_workspace_id_search_time_entries_extension_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_extension_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries.{extension} | Export detailed report
[**reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries.pdf | Export detailed report
[**reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post) | **POST** /reports/api/v3/workspace/{workspace_id}/summary/time_entries.{extension} | Export summary report
[**reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/summary/time_entries.pdf | Export summary report
[**reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post) | **POST** /reports/api/v3/workspace/{workspace_id}/weekly/time_entries.csv | Export weekly report
[**reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post**](ExportsApi.md#reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/weekly/time_entries.pdf | Export weekly report


## `get_me_export`
> list[ModelsDownloadRequestRecord] get_me_export()

Get a list of objects to be downloaded

List of objects to be downloaded for an user

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))

try:
    # Get a list of objects to be downloaded
    api_response = api_instance.get_me_export()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->get_me_export: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsDownloadRequestRecord]**](ModelsDownloadRequestRecord.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_export_data_uuid_zip`
> str get_me_export_data_uuid_zip()

Get the zip file with download requests

Get a zip file List of download requests from an user.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))

try:
    # Get the zip file with download requests
    api_response = api_instance.get_me_export_data_uuid_zip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->get_me_export_data_uuid_zip: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_exports`
> list[ModelsDownloadRequestRecord] get_workspace_exports(workspace_id)

Get a list with the workspace download requests

List of workspace download requests from a given workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get a list with the workspace download requests
    api_response = api_instance.get_workspace_exports(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->get_workspace_exports: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsDownloadRequestRecord]**](ModelsDownloadRequestRecord.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_exports_data_uuid_zip`
> str get_workspace_exports_data_uuid_zip(workspace_id)

Get the zip file with workspace download requests

Send a zip file List of workspace download requests from a given workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get the zip file with workspace download requests
    api_response = api_instance.get_workspace_exports_data_uuid_zip(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->get_workspace_exports_data_uuid_zip: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_profitability_employees_extension_post`
> str insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(parameters)

Export employee profitability insights

Downloads employee profitability insights in the specified format: csv or xlsx.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
parameters = toggl.RequestsEmployeeProfitability() # RequestsEmployeeProfitability | Parameters for report

try:
    # Export employee profitability insights
    api_response = api_instance.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->insights_api_v1_workspace_workspace_id_profitability_employees_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**RequestsEmployeeProfitability**](RequestsEmployeeProfitability.md)| Parameters for report | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_profitability_projects_extension_post`
> str insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(parameters, extension)

Export profitability project insights

Downloads profitability project insights in the specified format: csv or xlsx.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
parameters = toggl.RequestsProjectProfitability() # RequestsProjectProfitability | Parameters for report
extension = 'extension_example' # str | csv,xlsx

try:
    # Export profitability project insights
    api_response = api_instance.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(parameters, extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->insights_api_v1_workspace_workspace_id_profitability_projects_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**RequestsProjectProfitability**](RequestsProjectProfitability.md)| Parameters for report | 
 **extension** | **str**| csv,xlsx | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_trends_projects_extension_post`
> list[ProjectsProjectTrends] insights_api_v1_workspace_workspace_id_trends_projects_extension_post(workspace_id, extension, project_trend=project_trend)

Export projects data trends

Downloads projects data trends in the specified format: csv or xlsx.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
project_trend = toggl.ProjectsProjectTrend() # ProjectsProjectTrend | Projects filter conditions (optional)

try:
    # Export projects data trends
    api_response = api_instance.insights_api_v1_workspace_workspace_id_trends_projects_extension_post(workspace_id, extension, project_trend=project_trend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->insights_api_v1_workspace_workspace_id_trends_projects_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **extension** | **str**| csv,xlsx | 
 **project_trend** | [**ProjectsProjectTrend**](ProjectsProjectTrend.md)| Projects filter conditions | [optional] 

### Return type

[**list[ProjectsProjectTrends]**](ProjectsProjectTrends.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_me_export`
> str post_me_export(data_export_object)

Post an object which data to be downloaded

An object which data to be downloaded for an user

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
data_export_object = toggl.ExportPayload() # ExportPayload | Objects to export

try:
    # Post an object which data to be downloaded
    api_response = api_instance.post_me_export(data_export_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->post_me_export: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_export_object** | [**ExportPayload**](ExportPayload.md)| Objects to export | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_exports`
> str post_workspace_exports(workspace_id, tokens_list)

Post a list with the workspace to be downloaded

List of workspaces downloaded from a given workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
tokens_list = [toggl.list[str]()] # list[str] | Objects to export

try:
    # Post a list with the workspace to be downloaded
    api_response = api_instance.post_workspace_exports(workspace_id, tokens_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->post_workspace_exports: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **tokens_list** | **list[str]**| Objects to export | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_csv_post`
> str reports_api_v3_shared_report_token_csv_post(report_token, start_date=start_date, end_date=end_date)

Export CSV for saved report

<p>Downloads a previously saved report in csv.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.ExportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)

try:
    # Export CSV for saved report
    api_response = api_instance.reports_api_v3_shared_report_token_csv_post(report_token, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_shared_report_token_csv_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_pdf_post`
> str reports_api_v3_shared_report_token_pdf_post(report_token, start_date=start_date, end_date=end_date, display_mode=display_mode)

Export saved report in pdf format

<p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.ExportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)
display_mode = 'display_mode_example' # str | Display mode for time data, only for detailed reports. Possible values: 'date_only', 'time_only', 'date_time'. Default value: 'date_and_time' (optional)

try:
    # Export saved report in pdf format
    api_response = api_instance.reports_api_v3_shared_report_token_pdf_post(report_token, start_date=start_date, end_date=end_date, display_mode=display_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_shared_report_token_pdf_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 
 **display_mode** | **str**| Display mode for time data, only for detailed reports. Possible values: &#39;date_only&#39;, &#39;time_only&#39;, &#39;date_time&#39;. Default value: &#39;date_and_time&#39; | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_xlsx_post`
> str reports_api_v3_shared_report_token_xlsx_post(report_token, start_date=start_date, end_date=end_date)

Export XSLX saved report

<p>Downloads a previously saved report in xlsx.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.ExportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)

try:
    # Export XSLX saved report
    api_response = api_instance.reports_api_v3_shared_report_token_xlsx_post(report_token, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_shared_report_token_xlsx_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_time_entries_extension_post`
> str reports_api_v3_workspace_workspace_id_search_time_entries_extension_post(workspace_id, extension, detailed_export_post)

Export detailed report

Downloads detailed report in the specified format: csv or xlsx.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
detailed_export_post = toggl.DetailedSearchExportPost() # DetailedSearchExportPost | Detailed report conditions

try:
    # Export detailed report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_extension_post(workspace_id, extension, detailed_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **extension** | **str**| csv,xlsx | 
 **detailed_export_post** | [**DetailedSearchExportPost**](DetailedSearchExportPost.md)| Detailed report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post`
> str reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post(workspace_id, detailed_export_pdf_post)

Export detailed report

Downloads detailed report in pdf format.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
detailed_export_pdf_post = toggl.DetailedExportPDFPost() # DetailedExportPDFPost | Detailed report conditions

try:
    # Export detailed report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post(workspace_id, detailed_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **detailed_export_pdf_post** | [**DetailedExportPDFPost**](DetailedExportPDFPost.md)| Detailed report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post`
> str reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post(workspace_id, extension, summary_export_post)

Export summary report

Downloads summary report in the specified in the specified format: csv or xlsx.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.ExportsApi()
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
summary_export_post = toggl.SummaryExportPost() # SummaryExportPost | Summary report conditions

try:
    # Export summary report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post(workspace_id, extension, summary_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **extension** | **str**| csv,xlsx | 
 **summary_export_post** | [**SummaryExportPost**](SummaryExportPost.md)| Summary report conditions | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post`
> str reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post(workspace_id, summary_export_pdf_post)

Export summary report

Downloads summary report in pdf format.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
summary_export_pdf_post = toggl.SummaryExportPDFPost() # SummaryExportPDFPost | Summary report conditions

try:
    # Export summary report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post(workspace_id, summary_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **summary_export_pdf_post** | [**SummaryExportPDFPost**](SummaryExportPDFPost.md)| Summary report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post`
> str reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post(workspace_id, weekly_export_post)

Export weekly report

Downloads weekly report in csv format.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
weekly_export_post = toggl.WeeklyExportPost() # WeeklyExportPost | Weekly report conditions

try:
    # Export weekly report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post(workspace_id, weekly_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **weekly_export_post** | [**WeeklyExportPost**](WeeklyExportPost.md)| Weekly report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post`
> str reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post(workspace_id, weekly_export_pdf_post)

Export weekly report

Downloads weekly report in pdf format.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.ExportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
weekly_export_pdf_post = toggl.WeeklyExportPDFPost() # WeeklyExportPDFPost | Weekly report conditions

try:
    # Export weekly report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post(workspace_id, weekly_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **weekly_export_pdf_post** | [**WeeklyExportPDFPost**](WeeklyExportPDFPost.md)| Weekly report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

