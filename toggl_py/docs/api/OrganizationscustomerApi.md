# toggl.OrganizationscustomerApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_customer**](OrganizationscustomerApi.md#get_organization_customer) | **GET** /organizations/{organization_id}/customer | Customer
[**get_unified_customer**](OrganizationscustomerApi.md#get_unified_customer) | **GET** /organizations/{organization_id}/subscription/customer | Retrieve unified customer
[**post_organization_customer**](OrganizationscustomerApi.md#post_organization_customer) | **POST** /organizations/{organization_id}/customer/contact_detail | ContactDetails
[**post_unified_customer**](OrganizationscustomerApi.md#post_unified_customer) | **POST** /organizations/{organization_id}/subscription/customer | Create unified customer
[**put_unified_customer**](OrganizationscustomerApi.md#put_unified_customer) | **PUT** /organizations/{organization_id}/subscription/customer | Update unified customer


## `get_organization_customer`
> ModelsCustomer get_organization_customer(organization_id)

Customer

Allows to fetch customer data.

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
api_instance = toggl.OrganizationscustomerApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Customer
    api_response = api_instance.get_organization_customer(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationscustomerApi->get_organization_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**ModelsCustomer**](ModelsCustomer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_unified_customer`
> CustomerUnifiedCustomerResponse get_unified_customer(organization_id)

Retrieve unified customer

Retrieve unified customer belonging to the organization.

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
api_instance = toggl.OrganizationscustomerApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Retrieve unified customer
    api_response = api_instance.get_unified_customer(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationscustomerApi->get_unified_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**CustomerUnifiedCustomerResponse**](CustomerUnifiedCustomerResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_customer`
> ModelsContactDetail post_organization_customer(organization_id, contact_detail_request)

ContactDetails

Allows to save contact details.

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
api_instance = toggl.OrganizationscustomerApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the workspace.
contact_detail_request = toggl.SubscriptionContactDetailRequest() # SubscriptionContactDetailRequest | Input data for contact details.

try:
    # ContactDetails
    api_response = api_instance.post_organization_customer(organization_id, contact_detail_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationscustomerApi->post_organization_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the workspace. | 
 **contact_detail_request** | [**SubscriptionContactDetailRequest**](SubscriptionContactDetailRequest.md)| Input data for contact details. | 

### Return type

[**ModelsContactDetail**](ModelsContactDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_unified_customer`
> CustomerUnifiedCustomerResponse post_unified_customer(organization_id)

Create unified customer

Creates unified customer for organization.

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
api_instance = toggl.OrganizationscustomerApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Create unified customer
    api_response = api_instance.post_unified_customer(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationscustomerApi->post_unified_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**CustomerUnifiedCustomerResponse**](CustomerUnifiedCustomerResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_unified_customer`
> CustomerUnifiedCustomerResponse put_unified_customer(organization_id)

Update unified customer

Allows to update unified customer data. Customer name, email, country & postal code are mandatory fields. Optional fields will be cleared if they don't have a value.

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
api_instance = toggl.OrganizationscustomerApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Update unified customer
    api_response = api_instance.put_unified_customer(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationscustomerApi->put_unified_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**CustomerUnifiedCustomerResponse**](CustomerUnifiedCustomerResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

