# toggl.KeysApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keys**](KeysApi.md#get_keys) | **GET** /keys | get keys


## `get_keys`
> JwkSet get_keys()

get keys

Returns the current JWKS keyset used to sign JWT tokens.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.KeysApi()

try:
    # get keys
    api_response = api_instance.get_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->get_keys: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**JwkSet**](JwkSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

