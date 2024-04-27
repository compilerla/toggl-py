# toggl.IcalApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ical**](IcalApi.md#get_ical) | **GET** /ical/workspace_user/{token} | Ical file
[**post_workspace_ical_reset**](IcalApi.md#post_workspace_ical_reset) | **POST** /workspaces/{workspace_id}/ical/reset | Reset iCal token
[**post_workspace_ical_toggle**](IcalApi.md#post_workspace_ical_toggle) | **POST** /workspaces/{workspace_id}/ical/toggle | Toggle the iCal token


## `get_ical`
> get_ical()

Ical file

Returns ical file with TEs from last 14 days

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.IcalApi()

try:
    # Ical file
    api_instance.get_ical()
except ApiException as e:
    print("Exception when calling IcalApi->get_ical: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/calendar

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_ical_reset`
> str post_workspace_ical_reset(workspace_id)

Reset iCal token

Reset the iCal token for a given workspace.

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
api_instance = toggl.IcalApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Reset iCal token
    api_response = api_instance.post_workspace_ical_reset(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcalApi->post_workspace_ical_reset: %s\n" % e)
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

## `post_workspace_ical_toggle`
> str post_workspace_ical_toggle(workspace_id)

Toggle the iCal token

Toggle the iCal token on/off for a given workspace.

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
api_instance = toggl.IcalApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Toggle the iCal token
    api_response = api_instance.post_workspace_ical_toggle(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IcalApi->post_workspace_ical_toggle: %s\n" % e)
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

