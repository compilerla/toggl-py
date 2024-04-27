# toggl.WeeklyReportsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post**](WeeklyReportsApi.md#reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post) | **POST** /reports/api/v3/workspace/{workspace_id}/weekly/time_entries.csv | Export weekly report
[**reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post**](WeeklyReportsApi.md#reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/weekly/time_entries.pdf | Export weekly report
[**reports_api_v3_workspace_workspace_id_weekly_time_entries_post**](WeeklyReportsApi.md#reports_api_v3_workspace_workspace_id_weekly_time_entries_post) | **POST** /reports/api/v3/workspace/{workspace_id}/weekly/time_entries | Search time entries


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
api_instance = toggl.WeeklyReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
weekly_export_post = toggl.WeeklyExportPost() # WeeklyExportPost | Weekly report conditions

try:
    # Export weekly report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post(workspace_id, weekly_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeeklyReportsApi->reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post: %s\n" % e)
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
api_instance = toggl.WeeklyReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
weekly_export_pdf_post = toggl.WeeklyExportPDFPost() # WeeklyExportPDFPost | Weekly report conditions

try:
    # Export weekly report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post(workspace_id, weekly_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeeklyReportsApi->reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post: %s\n" % e)
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

## `reports_api_v3_workspace_workspace_id_weekly_time_entries_post`
> str reports_api_v3_workspace_workspace_id_weekly_time_entries_post(workspace_id, post)

Search time entries

Returns time entries for weekly report according to the given filters.

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
api_instance = toggl.WeeklyReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
post = toggl.BasePost() # BasePost | Weekly report conditions

try:
    # Search time entries
    api_response = api_instance.reports_api_v3_workspace_workspace_id_weekly_time_entries_post(workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeeklyReportsApi->reports_api_v3_workspace_workspace_id_weekly_time_entries_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **post** | [**BasePost**](BasePost.md)| Weekly report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

