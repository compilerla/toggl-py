# toggl.OrganizationsSubscriptionApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_purchase_order_pdf**](OrganizationsSubscriptionApi.md#get_organization_purchase_order_pdf) | **GET** /organizations/{organization_id}/subscription/purchase_orders/{purchase_order_uid}.pdf | PurchaseOrderPdf


## `get_organization_purchase_order_pdf`
> str get_organization_purchase_order_pdf(organization_id, purchase_order_uid)

PurchaseOrderPdf

Returns a Purchase Order document in PDF form.

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
api_instance = toggl.OrganizationsSubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
purchase_order_uid = 'purchase_order_uid_example' # str | Numeric ID or string ID of the purchase order.

try:
    # PurchaseOrderPdf
    api_response = api_instance.get_organization_purchase_order_pdf(organization_id, purchase_order_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsSubscriptionApi->get_organization_purchase_order_pdf: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **purchase_order_uid** | **str**| Numeric ID or string ID of the purchase order. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

