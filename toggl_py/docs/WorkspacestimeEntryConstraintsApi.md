# toggl.WorkspacestimeEntryConstraintsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_workspace_time_entry_constraints**](WorkspacestimeEntryConstraintsApi.md#post_workspace_time_entry_constraints) | **POST** /workspaces/{workspace_id}/time_entry_constraints | Post workspace time entry constraints


## `post_workspace_time_entry_constraints`
> WorkspacesJSONResult post_workspace_time_entry_constraints(workspace_id, time_entry_constraints)

Post workspace time entry constraints

Post the time entry constraints for a given workspace.

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
api_instance = toggl.WorkspacestimeEntryConstraintsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_constraints = toggl.ModelsTimeEntryConstraints() # ModelsTimeEntryConstraints | Input data of the time entry constraints.

try:
    # Post workspace time entry constraints
    api_response = api_instance.post_workspace_time_entry_constraints(workspace_id, time_entry_constraints)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacestimeEntryConstraintsApi->post_workspace_time_entry_constraints: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_constraints** | [**ModelsTimeEntryConstraints**](ModelsTimeEntryConstraints.md)| Input data of the time entry constraints. | 

### Return type

[**WorkspacesJSONResult**](WorkspacesJSONResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

