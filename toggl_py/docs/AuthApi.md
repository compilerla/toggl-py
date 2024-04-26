# toggl.AuthApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**desktop_login_get**](AuthApi.md#desktop_login_get) | **GET** /desktop_login | Get desktop login token
[**desktop_login_tokens_post**](AuthApi.md#desktop_login_tokens_post) | **POST** /desktop_login_tokens | Post desktop login token


## `desktop_login_get`
> desktop_login_get()

Get desktop login token

Store new desktop login token

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthApi()

try:
    # Get desktop login token
    api_instance.desktop_login_get()
except ApiException as e:
    print("Exception when calling AuthApi->desktop_login_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `desktop_login_tokens_post`
> DesktopLoginToken desktop_login_tokens_post()

Post desktop login token

Store new desktop login token

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthApi()

try:
    # Post desktop login token
    api_response = api_instance.desktop_login_tokens_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->desktop_login_tokens_post: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DesktopLoginToken**](DesktopLoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

