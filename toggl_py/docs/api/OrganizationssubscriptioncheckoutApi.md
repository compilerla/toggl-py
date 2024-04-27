# toggl.OrganizationssubscriptioncheckoutApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_checkout_session**](OrganizationssubscriptioncheckoutApi.md#create_subscription_checkout_session) | **POST** /organizations/{organization_id}/subscription/checkout_session | Create a subscription checkout session in the unified subscription system


## `create_subscription_checkout_session`
> create_subscription_checkout_session(organization_id, params)

Create a subscription checkout session in the unified subscription system

Create a subscription checkout session in the unified subscription system

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
api_instance = toggl.OrganizationssubscriptioncheckoutApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.SubscriptionsCheckoutSessionPayload() # SubscriptionsCheckoutSessionPayload | The checkout session data

try:
    # Create a subscription checkout session in the unified subscription system
    api_instance.create_subscription_checkout_session(organization_id, params)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptioncheckoutApi->create_subscription_checkout_session: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **params** | [**SubscriptionsCheckoutSessionPayload**](SubscriptionsCheckoutSessionPayload.md)| The checkout session data | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

