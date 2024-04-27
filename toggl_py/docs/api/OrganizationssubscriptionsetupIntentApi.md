# toggl.OrganizationssubscriptionsetupIntentApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_setup_intent**](OrganizationssubscriptionsetupIntentApi.md#create_setup_intent) | **POST** /organizations/{organization_id}/subscription/setup_intent | Create a setup intent for collecting customer&#39;s payment method


## `create_setup_intent`
> create_setup_intent(organization_id)

Create a setup intent for collecting customer's payment method

Create a setup intent for collecting customer's payment method for future payments

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
api_instance = toggl.OrganizationssubscriptionsetupIntentApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Create a setup intent for collecting customer's payment method
    api_instance.create_setup_intent(organization_id)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptionsetupIntentApi->create_setup_intent: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

