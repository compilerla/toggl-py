# toggl.FeedbackApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_feedback_web**](FeedbackApi.md#post_feedback_web) | **POST** /feedback/web | FeedbackWeb
[**post_unified_feedback**](FeedbackApi.md#post_unified_feedback) | **POST** /feedback | Feedback


## `post_feedback_web`
> post_feedback_web(toggl_version, _date, details, update_channel=update_channel, subject=subject, latest=latest, files=files)

FeedbackWeb

Send Feedback web.

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
api_instance = toggl.FeedbackApi(toggl.ApiClient(configuration))
toggl_version = 'toggl_version_example' # str | Toggl version.
_date = '_date_example' # str | Feedback date.
details = 'details_example' # str | Feedback details.
update_channel = 'update_channel_example' # str | Update channel. (optional)
subject = 'subject_example' # str | Email subject. (optional)
latest = true # bool | Latest feedback. (optional)
files = '/path/to/file.txt' # file | One or more files. (optional)

try:
    # FeedbackWeb
    api_instance.post_feedback_web(toggl_version, _date, details, update_channel=update_channel, subject=subject, latest=latest, files=files)
except ApiException as e:
    print("Exception when calling FeedbackApi->post_feedback_web: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggl_version** | **str**| Toggl version. | 
 **_date** | **str**| Feedback date. | 
 **details** | **str**| Feedback details. | 
 **update_channel** | **str**| Update channel. | [optional] 
 **subject** | **str**| Email subject. | [optional] 
 **latest** | **bool**| Latest feedback. | [optional] 
 **files** | **file**| One or more files. | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_unified_feedback`
> post_unified_feedback(toggl_version, _date, details, update_channel=update_channel, subject=subject, device_model=device_model, build_number=build_number, operating_system=operating_system, latest=latest, files=files)

Feedback

Send Feedback

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
api_instance = toggl.FeedbackApi(toggl.ApiClient(configuration))
toggl_version = 'toggl_version_example' # str | Toggl version.
_date = '_date_example' # str | Feedback date.
details = 'details_example' # str | Feedback details.
update_channel = 'update_channel_example' # str | Update channel. (optional)
subject = 'subject_example' # str | Email subject. (optional)
device_model = 'device_model_example' # str | Device Model. (optional)
build_number = 'build_number_example' # str | Build Number. (optional)
operating_system = 'operating_system_example' # str | Operating system. (optional)
latest = true # bool | Latest feedback. (optional)
files = '/path/to/file.txt' # file | One or more files. (optional)

try:
    # Feedback
    api_instance.post_unified_feedback(toggl_version, _date, details, update_channel=update_channel, subject=subject, device_model=device_model, build_number=build_number, operating_system=operating_system, latest=latest, files=files)
except ApiException as e:
    print("Exception when calling FeedbackApi->post_unified_feedback: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggl_version** | **str**| Toggl version. | 
 **_date** | **str**| Feedback date. | 
 **details** | **str**| Feedback details. | 
 **update_channel** | **str**| Update channel. | [optional] 
 **subject** | **str**| Email subject. | [optional] 
 **device_model** | **str**| Device Model. | [optional] 
 **build_number** | **str**| Build Number. | [optional] 
 **operating_system** | **str**| Operating system. | [optional] 
 **latest** | **bool**| Latest feedback. | [optional] 
 **files** | **file**| One or more files. | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

