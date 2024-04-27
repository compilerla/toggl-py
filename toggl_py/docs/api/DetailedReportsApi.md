# toggl.DetailedReportsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_workspace_workspace_id_search_time_entries_extension_post**](DetailedReportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_extension_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries.{extension} | Export detailed report
[**reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post**](DetailedReportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries.pdf | Export detailed report
[**reports_api_v3_workspace_workspace_id_search_time_entries_post**](DetailedReportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries | Search time entries
[**reports_api_v3_workspace_workspace_id_search_time_entries_totals_post**](DetailedReportsApi.md#reports_api_v3_workspace_workspace_id_search_time_entries_totals_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/time_entries/totals | Load totals detailed report


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
api_instance = toggl.DetailedReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
detailed_export_post = toggl.DetailedSearchExportPost() # DetailedSearchExportPost | Detailed report conditions

try:
    # Export detailed report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_extension_post(workspace_id, extension, detailed_export_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetailedReportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_extension_post: %s\n" % e)
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
api_instance = toggl.DetailedReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
detailed_export_pdf_post = toggl.DetailedExportPDFPost() # DetailedExportPDFPost | Detailed report conditions

try:
    # Export detailed report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post(workspace_id, detailed_export_pdf_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetailedReportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post: %s\n" % e)
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

## `reports_api_v3_workspace_workspace_id_search_time_entries_post`
> str reports_api_v3_workspace_workspace_id_search_time_entries_post(workspace_id, search_post)

Search time entries

Returns time entries for detailed report according to the given filters. Supports pagination via X-Next-ID and X-Next-Row-Number headers returned in the response. See [Overview](https://developers.track.toggl.com/docs/reports_start#detailed-reports)

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
api_instance = toggl.DetailedReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
search_post = toggl.DetailedPost() # DetailedPost | Search report conditions

try:
    # Search time entries
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_post(workspace_id, search_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetailedReportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **search_post** | [**DetailedPost**](DetailedPost.md)| Search report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_time_entries_totals_post`
> str reports_api_v3_workspace_workspace_id_search_time_entries_totals_post(workspace_id, totals_post)

Load totals detailed report

Returns totals sums for detailed report.

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
api_instance = toggl.DetailedReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
totals_post = toggl.TotalsReportPost() # TotalsReportPost | Totals detailed report conditions

try:
    # Load totals detailed report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_time_entries_totals_post(workspace_id, totals_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetailedReportsApi->reports_api_v3_workspace_workspace_id_search_time_entries_totals_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **totals_post** | [**TotalsReportPost**](TotalsReportPost.md)| Totals detailed report conditions | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

