# toggl.OrganizationsOwnerApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ownership_transfer**](OrganizationsOwnerApi.md#get_ownership_transfer) | **GET** /organizations/{organization_id}/owner/transfer/{transfer_id} | Returns single organization transfer in the organization
[**get_ownership_transfers**](OrganizationsOwnerApi.md#get_ownership_transfers) | **GET** /organizations/{organization_id}/owner/transfer | Returns list of organization transfers made in the organization
[**post_ownership_transfer**](OrganizationsOwnerApi.md#post_ownership_transfer) | **POST** /organizations/{organization_id}/owner/transfer | Creates new ownership transfer process
[**post_ownership_transfer_actions**](OrganizationsOwnerApi.md#post_ownership_transfer_actions) | **POST** /organizations/{organization_id}/owner/transfer/{transfer_id}/{action} | Updates transfer process and emails stakeholders


## `get_ownership_transfer`
> ModelsTransfer get_ownership_transfer(organization_id, transfer_id)

Returns single organization transfer in the organization

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.OrganizationsOwnerApi()
organization_id = 56 # int | Numeric ID of the organization.
transfer_id = 56 # int | Numeric ID of the transfer.

try:
    # Returns single organization transfer in the organization
    api_response = api_instance.get_ownership_transfer(organization_id, transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsOwnerApi->get_ownership_transfer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **transfer_id** | **int**| Numeric ID of the transfer. | 

### Return type

[**ModelsTransfer**](ModelsTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_ownership_transfers`
> list[ModelsTransfer] get_ownership_transfers(organization_id, ongoing=ongoing)

Returns list of organization transfers made in the organization

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.OrganizationsOwnerApi()
organization_id = 56 # int | Numeric ID of the organization.
ongoing = 'ongoing_example' # str | If true, returns only current, not finished transfer (optional)

try:
    # Returns list of organization transfers made in the organization
    api_response = api_instance.get_ownership_transfers(organization_id, ongoing=ongoing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsOwnerApi->get_ownership_transfers: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **ongoing** | **str**| If true, returns only current, not finished transfer | [optional] 

### Return type

[**list[ModelsTransfer]**](ModelsTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_ownership_transfer`
> ModelsTransfer post_ownership_transfer(organization_id)

Creates new ownership transfer process

Return the ownership transfer for a given organization.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.OrganizationsOwnerApi()
organization_id = 56 # int | Numeric ID of the organization.

try:
    # Creates new ownership transfer process
    api_response = api_instance.post_ownership_transfer(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsOwnerApi->post_ownership_transfer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 

### Return type

[**ModelsTransfer**](ModelsTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_ownership_transfer_actions`
> ModelsTransfer post_ownership_transfer_actions(organization_id, transfer_id, action)

Updates transfer process and emails stakeholders

Return the ownership transfer for a given organization and emails stakeholders.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.OrganizationsOwnerApi()
organization_id = 56 # int | Numeric ID of the organization.
transfer_id = 56 # int | Numeric ID of the transfer.
action = 'action_example' # str | Action to update transfer with.

try:
    # Updates transfer process and emails stakeholders
    api_response = api_instance.post_ownership_transfer_actions(organization_id, transfer_id, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsOwnerApi->post_ownership_transfer_actions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **transfer_id** | **int**| Numeric ID of the transfer. | 
 **action** | **str**| Action to update transfer with. | 

### Return type

[**ModelsTransfer**](ModelsTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

