# toggl.MobileApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_mobile_feedback**](MobileApi.md#post_mobile_feedback) | **POST** /mobile/feedback | MobileFeedback


## `post_mobile_feedback`
> str post_mobile_feedback(mobile_feedback_post)

MobileFeedback

Send Mobile Feedback.

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
api_instance = toggl.MobileApi(toggl.ApiClient(configuration))
mobile_feedback_post = toggl.ModelsMobileFeedback() # ModelsMobileFeedback | Feedback parameters.

try:
    # MobileFeedback
    api_response = api_instance.post_mobile_feedback(mobile_feedback_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->post_mobile_feedback: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_feedback_post** | [**ModelsMobileFeedback**](ModelsMobileFeedback.md)| Feedback parameters. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

