# toggl.TimelineApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeline_delete**](TimelineApi.md#timeline_delete) | **DELETE** /timeline | Delete all timeline data
[**timeline_get**](TimelineApi.md#timeline_get) | **GET** /timeline | Get timeline events
[**timeline_post**](TimelineApi.md#timeline_post) | **POST** /timeline | Save timeline events


## `timeline_delete`
> timeline_delete()

Delete all timeline data

Delete all timeline data for the current user

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.TimelineApi()

try:
    # Delete all timeline data
    api_instance.timeline_delete()
except ApiException as e:
    print("Exception when calling TimelineApi->timeline_delete: %s\n" % e)
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

## `timeline_get`
> list[ModelsTimelineEvent] timeline_get(start_date=start_date, end_date=end_date)

Get timeline events

Get timeline events

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
api_instance = toggl.TimelineApi(toggl.ApiClient(configuration))
start_date = 56 # int | Unix timestamp of the start date (optional)
end_date = 56 # int | Unix timestamp of the end date (optional)

try:
    # Get timeline events
    api_response = api_instance.timeline_get(start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimelineApi->timeline_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Unix timestamp of the start date | [optional] 
 **end_date** | **int**| Unix timestamp of the end date | [optional] 

### Return type

[**list[ModelsTimelineEvent]**](ModelsTimelineEvent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `timeline_post`
> ModelsTimelineSettings timeline_post(timeline_post=timeline_post)

Save timeline events

Save timeline events and returns timeline settings

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.TimelineApi()
timeline_post = [toggl.ModelsTimelineEvent()] # list[ModelsTimelineEvent] | timeline events (optional)

try:
    # Save timeline events
    api_response = api_instance.timeline_post(timeline_post=timeline_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimelineApi->timeline_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeline_post** | [**list[ModelsTimelineEvent]**](ModelsTimelineEvent.md)| timeline events | [optional] 

### Return type

[**ModelsTimelineSettings**](ModelsTimelineSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

