# toggl.SmailApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_smail_contact**](SmailApi.md#post_smail_contact) | **POST** /smail/contact | Send an email to a contact
[**post_smail_demo**](SmailApi.md#post_smail_demo) | **POST** /smail/demo | Send an email for a demo
[**post_smail_meet**](SmailApi.md#post_smail_meet) | **POST** /smail/meet | Send an email for meet


## `post_smail_contact`
> str post_smail_contact(email_info)

Send an email to a contact

Send an email to a contact

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
api_instance = toggl.SmailApi(toggl.ApiClient(configuration))
email_info = toggl.SmailContactPayload() # SmailContactPayload | Email informations

try:
    # Send an email to a contact
    api_response = api_instance.post_smail_contact(email_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmailApi->post_smail_contact: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_info** | [**SmailContactPayload**](SmailContactPayload.md)| Email informations | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_smail_demo`
> str post_smail_demo(email_info)

Send an email for a demo

Send an email for a demo

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
api_instance = toggl.SmailApi(toggl.ApiClient(configuration))
email_info = toggl.SmailDemoPayload() # SmailDemoPayload | Email informations

try:
    # Send an email for a demo
    api_response = api_instance.post_smail_demo(email_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmailApi->post_smail_demo: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_info** | [**SmailDemoPayload**](SmailDemoPayload.md)| Email informations | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_smail_meet`
> str post_smail_meet(email_location)

Send an email for meet

Send an email for meet with message and location

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
api_instance = toggl.SmailApi(toggl.ApiClient(configuration))
email_location = toggl.SmailMeetPayload() # SmailMeetPayload | Email and Location

try:
    # Send an email for meet
    api_response = api_instance.post_smail_meet(email_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmailApi->post_smail_meet: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_location** | [**SmailMeetPayload**](SmailMeetPayload.md)| Email and Location | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

