# toggl.TimezonesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offsets**](TimezonesApi.md#get_offsets) | **GET** /timezones/offsets | Offsets
[**get_timezones**](TimezonesApi.md#get_timezones) | **GET** /timezones | Timezones


## `get_offsets`
> list[ModelsTimezone] get_offsets()

Offsets

Returns known timezones with their offsets.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.TimezonesApi()

try:
    # Offsets
    api_response = api_instance.get_offsets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimezonesApi->get_offsets: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsTimezone]**](ModelsTimezone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_timezones`
> list[str] get_timezones()

Timezones

Returns known timezones.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.TimezonesApi()

try:
    # Timezones
    api_response = api_instance.get_timezones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimezonesApi->get_timezones: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

