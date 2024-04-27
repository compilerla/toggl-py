# toggl.UserInvoicesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_invoice**](UserInvoicesApi.md#delete_workspace_invoice) | **DELETE** /workspaces/{workspace_id}/invoices/{user_invoice_id} | Delete user invoice.
[**get_workspace_invoices**](UserInvoicesApi.md#get_workspace_invoices) | **GET** /workspaces/{workspace_id}/invoices | Get workspace invoices.
[**post_workspace_user_invoice**](UserInvoicesApi.md#post_workspace_user_invoice) | **POST** /workspaces/{workspace_id}/invoices | Create user invoice


## `delete_workspace_invoice`
> str delete_workspace_invoice(workspace_id, user_invoice_id)

Delete user invoice.

Deletes user invoice by ID if exists.

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
api_instance = toggl.UserInvoicesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
user_invoice_id = 56 # int | User invoice ID to be deleted

try:
    # Delete user invoice.
    api_response = api_instance.delete_workspace_invoice(workspace_id, user_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvoicesApi->delete_workspace_invoice: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **user_invoice_id** | **int**| User invoice ID to be deleted | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_invoices`
> list[ModelsUserInvoice] get_workspace_invoices(sort_order=sort_order, per_page=per_page, page=page, sort_field=sort_field)

Get workspace invoices.

Get invoices for given workspace with pagination.

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
api_instance = toggl.UserInvoicesApi(toggl.ApiClient(configuration))
sort_order = 'sort_order_example' # str | Sort order, default ASC. (optional)
per_page = 56 # int | Number of items per page, default 50. (optional)
page = 56 # int | Page number, default 1. (optional)
sort_field = 'sort_field_example' # str | Sort field, default created_at. (optional)

try:
    # Get workspace invoices.
    api_response = api_instance.get_workspace_invoices(sort_order=sort_order, per_page=per_page, page=page, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvoicesApi->get_workspace_invoices: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_order** | **str**| Sort order, default ASC. | [optional] 
 **per_page** | **int**| Number of items per page, default 50. | [optional] 
 **page** | **int**| Page number, default 1. | [optional] 
 **sort_field** | **str**| Sort field, default created_at. | [optional] 

### Return type

[**list[ModelsUserInvoice]**](ModelsUserInvoice.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_user_invoice`
> list[ModelsUserInvoice] post_workspace_user_invoice(workspace_id, tag_post)

Create user invoice

Creates new user invoice.

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
api_instance = toggl.UserInvoicesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
tag_post = toggl.ModelsUserInvoice() # ModelsUserInvoice | Post data

try:
    # Create user invoice
    api_response = api_instance.post_workspace_user_invoice(workspace_id, tag_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvoicesApi->post_workspace_user_invoice: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **tag_post** | [**ModelsUserInvoice**](ModelsUserInvoice.md)| Post data | 

### Return type

[**list[ModelsUserInvoice]**](ModelsUserInvoice.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

