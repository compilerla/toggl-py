# toggl.OrganizationssubscriptionpromocodeApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_promotion_code**](OrganizationssubscriptionpromocodeApi.md#delete_promotion_code) | **DELETE** /organizations/{organization_id}/subscription/promocode | Removes any discount (promotion code) applied to the organization&#39;s customer
[**post_promotion_code**](OrganizationssubscriptionpromocodeApi.md#post_promotion_code) | **POST** /organizations/{organization_id}/subscription/promocode | Applies the given promotion code to organization&#39;s customer


## `delete_promotion_code`
> delete_promotion_code(organization_id)

Removes any discount (promotion code) applied to the organization's customer

Removes any discount (promotion code) applied to the organization's customer

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
api_instance = toggl.OrganizationssubscriptionpromocodeApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Removes any discount (promotion code) applied to the organization's customer
    api_instance.delete_promotion_code(organization_id)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptionpromocodeApi->delete_promotion_code: %s\n" % e)
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

## `post_promotion_code`
> post_promotion_code(organization_id)

Applies the given promotion code to organization's customer

Applies the given promotion code to organization's customer If the customer already has the promotion code, then it will be overridden

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
api_instance = toggl.OrganizationssubscriptionpromocodeApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Applies the given promotion code to organization's customer
    api_instance.post_promotion_code(organization_id)
except ApiException as e:
    print("Exception when calling OrganizationssubscriptionpromocodeApi->post_promotion_code: %s\n" % e)
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

