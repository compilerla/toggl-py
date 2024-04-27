# toggl.AvatarsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_avatars**](AvatarsApi.md#delete_avatars) | **DELETE** /avatars | Avatars
[**post_avatars**](AvatarsApi.md#post_avatars) | **POST** /avatars | Avatars
[**post_use_gravatar**](AvatarsApi.md#post_use_gravatar) | **POST** /avatars/use_gravatar | UseGravatar


## `delete_avatars`
> str delete_avatars()

Avatars

Handles DELETE avatar requests.

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
api_instance = toggl.AvatarsApi(toggl.ApiClient(configuration))

try:
    # Avatars
    api_response = api_instance.delete_avatars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvatarsApi->delete_avatars: %s\n" % e)
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

## `post_avatars`
> ModelsAvatar post_avatars(file)

Avatars

Handles POST avatar requests.

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
api_instance = toggl.AvatarsApi(toggl.ApiClient(configuration))
file = 'file_example' # str | file form data

try:
    # Avatars
    api_response = api_instance.post_avatars(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvatarsApi->post_avatars: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| file form data | 

### Return type

[**ModelsAvatar**](ModelsAvatar.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_use_gravatar`
> ModelsAvatar post_use_gravatar()

UseGravatar

Change user avatar to gravatar.

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
api_instance = toggl.AvatarsApi(toggl.ApiClient(configuration))

try:
    # UseGravatar
    api_response = api_instance.post_use_gravatar()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvatarsApi->post_use_gravatar: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsAvatar**](ModelsAvatar.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

