# toggl.TimeEntryConstraintsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_time_entry_constraints**](TimeEntryConstraintsApi.md#get_workspace_time_entry_constraints) | **GET** /workspaces/{workspace_id}/time_entry_constraints | Get workspace time entry constraints


## `get_workspace_time_entry_constraints`
> ModelsTimeEntryConstraints get_workspace_time_entry_constraints(workspace_id)

Get workspace time entry constraints

Get the time entry constraints for a given workspace.

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
api_instance = toggl.TimeEntryConstraintsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace time entry constraints
    api_response = api_instance.get_workspace_time_entry_constraints(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntryConstraintsApi->get_workspace_time_entry_constraints: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsTimeEntryConstraints**](ModelsTimeEntryConstraints.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

