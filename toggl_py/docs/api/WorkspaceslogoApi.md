# toggl.WorkspaceslogoApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_logo**](WorkspaceslogoApi.md#get_workspace_logo) | **GET** /workspaces/{workspace_id}/logo | Get workspace logo
[**get_workspace_logo_0**](WorkspaceslogoApi.md#get_workspace_logo_0) | **DELETE** /workspaces/{workspace_id}/logo | Delete workspace logo
[**post_workspace_logo**](WorkspaceslogoApi.md#post_workspace_logo) | **POST** /workspaces/{workspace_id}/logo | Post workspace logo


## `get_workspace_logo`
> ModelsLogo get_workspace_logo(workspace_id)

Get workspace logo

Get the logo for a given workspace.

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
api_instance = toggl.WorkspaceslogoApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace logo
    api_response = api_instance.get_workspace_logo(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceslogoApi->get_workspace_logo: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsLogo**](ModelsLogo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_logo_0`
> ModelsLogo get_workspace_logo_0(workspace_id)

Delete workspace logo

Delete the logo for a given workspace.

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
api_instance = toggl.WorkspaceslogoApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Delete workspace logo
    api_response = api_instance.get_workspace_logo_0(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceslogoApi->get_workspace_logo_0: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsLogo**](ModelsLogo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_logo`
> ModelsLogo post_workspace_logo(workspace_id)

Post workspace logo

Post the logo for a given workspace.

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
api_instance = toggl.WorkspaceslogoApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Post workspace logo
    api_response = api_instance.post_workspace_logo(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceslogoApi->post_workspace_logo: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsLogo**](ModelsLogo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

