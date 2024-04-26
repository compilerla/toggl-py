# toggl.OrganizationssubscriptionbillingApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_portal_session**](OrganizationssubscriptionbillingApi.md#create_billing_portal_session) | **POST** /organizations/{organization_id}/subscription/billing_portal | Create a billing portal session in the unified subscription system


## `create_billing_portal_session`
> create_billing_portal_session(organization_id, params)

Create a billing portal session in the unified subscription system

Create a subscription billing portal session in the unified subscription system

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
api_instance = toggl.OrganizationssubscriptionbillingApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.BillingportalPayload() # BillingportalPayload | The billing portal session data

try:
    # Create a billing portal session in the unified subscription system
    api_instance.create_billing_portal_session(organization_id, params)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptionbillingApi->create_billing_portal_session: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **params** | [**BillingportalPayload**](BillingportalPayload.md)| The billing portal session data | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

