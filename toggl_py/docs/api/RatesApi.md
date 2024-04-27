# toggl.RatesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate**](RatesApi.md#create_rate) | **POST** /workspaces/{workspace_id}/rates | Rates creation
[**delete_rate**](RatesApi.md#delete_rate) | **DELETE** /workspaces/{workspace_id}/rates/{rate_id} | Rates delete
[**get_rates_by_level**](RatesApi.md#get_rates_by_level) | **GET** /workspaces/{workspace_id}/rates/{level}/{level_id} | Rates list


## `create_rate`
> DtoGetResponse create_rate(workspace_id, rate_post)

Rates creation

Creates a new rate.

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
api_instance = toggl.RatesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
rate_post = toggl.DtoCreationRequest() # DtoCreationRequest | Rate attributes

try:
    # Rates creation
    api_response = api_instance.create_rate(workspace_id, rate_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->create_rate: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **rate_post** | [**DtoCreationRequest**](DtoCreationRequest.md)| Rate attributes | 

### Return type

[**DtoGetResponse**](DtoGetResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_rate`
> delete_rate(workspace_id, rate_id)

Rates delete

Removes a rate.

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
api_instance = toggl.RatesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
rate_id = 56 # int | Numeric ID of the rate

try:
    # Rates delete
    api_instance.delete_rate(workspace_id, rate_id)
except ApiException as e:
    print("Exception when calling RatesApi->delete_rate: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **rate_id** | **int**| Numeric ID of the rate | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_rates_by_level`
> list[DtoGetResponse] get_rates_by_level(workspace_id, level, level_id)

Rates list

Get rates by level(workspace|project|user).

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
api_instance = toggl.RatesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
level = 'level_example' # str | Rates level: workspace, project or user
level_id = 56 # int | Numeric ID of the entity level

try:
    # Rates list
    api_response = api_instance.get_rates_by_level(workspace_id, level, level_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->get_rates_by_level: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **level** | **str**| Rates level: workspace, project or user | 
 **level_id** | **int**| Numeric ID of the entity level | 

### Return type

[**list[DtoGetResponse]**](DtoGetResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

