# toggl.WorkspacesreportssharedApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_saved_report_resource**](WorkspacesreportssharedApi.md#bulk_delete_saved_report_resource) | **PATCH** /workspaces/{workspace_id}/reports/shared/bulk_delete | SavedReport


## `bulk_delete_saved_report_resource`
> list[ModelsSavedReport] bulk_delete_saved_report_resource(workspace_id, input_data)

SavedReport

Bulk delete saved report.

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
api_instance = toggl.WorkspacesreportssharedApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
input_data = toggl.SharedBulkDeleteInputData() # SharedBulkDeleteInputData | Input data

try:
    # SavedReport
    api_response = api_instance.bulk_delete_saved_report_resource(workspace_id, input_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesreportssharedApi->bulk_delete_saved_report_resource: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **input_data** | [**SharedBulkDeleteInputData**](SharedBulkDeleteInputData.md)| Input data | 

### Return type

[**list[ModelsSavedReport]**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

