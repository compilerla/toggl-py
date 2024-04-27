# toggl.OrganizationssubscriptionApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_organization_subscription_calculate**](OrganizationssubscriptionApi.md#post_organization_subscription_calculate) | **POST** /organizations/{organization_id}/subscription/calculate | SubscriptionCalculation


## `post_organization_subscription_calculate`
> CalculateResponse post_organization_subscription_calculate(organization_id, calculation_data_request)

SubscriptionCalculation

Returns calculation of the subscription price for given pricing plan, period count, user count, currency, taxes etc.

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
api_instance = toggl.OrganizationssubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organizaiton.
calculation_data_request = toggl.CalculateCalculateRequest() # CalculateCalculateRequest | Input data for calculation.

try:
    # SubscriptionCalculation
    api_response = api_instance.post_organization_subscription_calculate(organization_id, calculation_data_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptionApi->post_organization_subscription_calculate: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organizaiton. | 
 **calculation_data_request** | [**CalculateCalculateRequest**](CalculateCalculateRequest.md)| Input data for calculation. | 

### Return type

[**CalculateResponse**](CalculateResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

