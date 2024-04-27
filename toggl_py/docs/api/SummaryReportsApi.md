# toggl.SummaryReportsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_workspace_workspace_id_projects_project_id_summary_post**](SummaryReportsApi.md#reports_api_v3_workspace_workspace_id_projects_project_id_summary_post) | **POST** /reports/api/v3/workspace/{workspace_id}/projects/{project_id}/summary | Load project summary
[**reports_api_v3_workspace_workspace_id_projects_summary_post**](SummaryReportsApi.md#reports_api_v3_workspace_workspace_id_projects_summary_post) | **POST** /reports/api/v3/workspace/{workspace_id}/projects/summary | List project users
[**reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post**](SummaryReportsApi.md#reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post) | **POST** /reports/api/v3/workspace/{workspace_id}/summary/time_entries.{extension} | Export summary report
[**reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post**](SummaryReportsApi.md#reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/summary/time_entries.pdf | Export summary report
[**reports_api_v3_workspace_workspace_id_summary_time_entries_post**](SummaryReportsApi.md#reports_api_v3_workspace_workspace_id_summary_time_entries_post) | **POST** /reports/api/v3/workspace/{workspace_id}/summary/time_entries | Search time entries


## `reports_api_v3_workspace_workspace_id_projects_project_id_summary_post`
> TotalsReportData reports_api_v3_workspace_workspace_id_projects_project_id_summary_post(workspace_id, project_id, range_post=range_post)

Load project summary

Returns project's summary.

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
api_instance = toggl.SummaryReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
project_id = 56 # int | Project ID
range_post = toggl.BaseRangePost() # BaseRangePost | Date range conditions (optional)

try:
    # Load project summary
    api_response = api_instance.reports_api_v3_workspace_workspace_id_projects_project_id_summary_post(workspace_id, project_id, range_post=range_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryReportsApi->reports_api_v3_workspace_workspace_id_projects_project_id_summary_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **project_id** | **int**| Project ID | 
 **range_post** | [**BaseRangePost**](BaseRangePost.md)| Date range conditions | [optional] 

### Return type

[**TotalsReportData**](TotalsReportData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_projects_summary_post`
> list[UsersProjectUsersSummaryRow] reports_api_v3_workspace_workspace_id_projects_summary_post(workspace_id, project_users_input)

List project users

Returns summary user projects.

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
api_instance = toggl.SummaryReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
project_users_input = toggl.DtoProjectUsersRequest() # DtoProjectUsersRequest | User projects summary input filter

try:
    # List project users
    api_response = api_instance.reports_api_v3_workspace_workspace_id_projects_summary_post(workspace_id, project_users_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryReportsApi->reports_api_v3_workspace_workspace_id_projects_summary_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **project_users_input** | [**DtoProjectUsersRequest**](DtoProjectUsersRequest.md)| User projects summary input filter | 

### Return type

[**list[UsersProjectUsersSummaryRow]**](UsersProjectUsersSummaryRow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.SummaryReportsApi()
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
summary_export_post = toggl.SummaryExportPost() # SummaryExportPost | Summary report conditions

try:
    # Export summary report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post(workspace_id, extension, summary_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryReportsApi->reports_api_v3_workspace_workspace_id_summary_time_entries_extension_post: %s\n" % e)
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
api_instance = toggl.SummaryReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
summary_export_pdf_post = toggl.SummaryExportPDFPost() # SummaryExportPDFPost | Summary report conditions

try:
    # Export summary report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post(workspace_id, summary_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryReportsApi->reports_api_v3_workspace_workspace_id_summary_time_entries_pdf_post: %s\n" % e)
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

## `reports_api_v3_workspace_workspace_id_summary_time_entries_post`
> str reports_api_v3_workspace_workspace_id_summary_time_entries_post(workspace_id, summary_post)

Search time entries

Returns time entries for summary report according to the given filters.

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
api_instance = toggl.SummaryReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
summary_post = toggl.SummaryReportPost() # SummaryReportPost | Summary report conditions

try:
    # Search time entries
    api_response = api_instance.reports_api_v3_workspace_workspace_id_summary_time_entries_post(workspace_id, summary_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryReportsApi->reports_api_v3_workspace_workspace_id_summary_time_entries_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **summary_post** | [**SummaryReportPost**](SummaryReportPost.md)| Summary report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

