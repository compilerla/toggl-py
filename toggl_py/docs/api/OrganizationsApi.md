# toggl.OrganizationsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organization_group**](OrganizationsApi.md#delete_organization_group) | **DELETE** /organizations/{organization_id}/groups/{group_id} | Deletes group
[**delete_organization_users_leave**](OrganizationsApi.md#delete_organization_users_leave) | **DELETE** /organizations/{organization_id}/users/leave | Leaves organization
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organizations/{organization_id} | Organization data
[**get_organization_groups**](OrganizationsApi.md#get_organization_groups) | **GET** /organizations/{organization_id}/groups | List of groups in organization with user and workspace assignments
[**get_organization_owner**](OrganizationsApi.md#get_organization_owner) | **GET** /organizations/{organization_id}/owner | Get owner of the organization
[**get_organization_segmentation**](OrganizationsApi.md#get_organization_segmentation) | **GET** /organizations/{organization_id}/segmentation | Organization segmentation data
[**get_organization_users**](OrganizationsApi.md#get_organization_users) | **GET** /organizations/{organization_id}/users | List of users in organization
[**get_organization_users_detailed**](OrganizationsApi.md#get_organization_users_detailed) | **GET** /organizations/{organization_id}/users/detailed | List of users in organization with details
[**get_organization_workspaces_groups**](OrganizationsApi.md#get_organization_workspaces_groups) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/groups | List of groups in a workspace within an organization with user assignments.
[**get_organization_workspaces_statistics**](OrganizationsApi.md#get_organization_workspaces_statistics) | **GET** /organizations/{organization_id}/workspaces/statistics | Statistics for all workspaces in the organization
[**get_organizations_payments_records**](OrganizationsApi.md#get_organizations_payments_records) | **GET** /organizations/{organization_id}/payment_records | OrganizationsPaymentRecords
[**get_organizations_plans**](OrganizationsApi.md#get_organizations_plans) | **GET** /organizations/{organization_id}/plans | OrganizationsPlans
[**get_organizations_plans_0**](OrganizationsApi.md#get_organizations_plans_0) | **GET** /organizations/{organization_id}/plans/{plan_id} | OrganizationsPlan
[**patch_organization_group**](OrganizationsApi.md#patch_organization_group) | **PATCH** /organizations/{organization_id}/groups/{group_id} | Patch group
[**patch_organization_users**](OrganizationsApi.md#patch_organization_users) | **PATCH** /organizations/{organization_id}/users | Apply changes in bulk to users in an organization
[**post_organization**](OrganizationsApi.md#post_organization) | **POST** /organizations | Creates a new organization
[**post_organization_accept_invitation**](OrganizationsApi.md#post_organization_accept_invitation) | **POST** /organizations/invitations/{invitation_code}/accept | Accepts invitation
[**post_organization_group**](OrganizationsApi.md#post_organization_group) | **POST** /organizations/{organization_id}/groups | Create group
[**post_organization_invitation**](OrganizationsApi.md#post_organization_invitation) | **POST** /organizations/{organization_id}/invitations | Creates a new invitation for the user
[**post_organization_workspaces**](OrganizationsApi.md#post_organization_workspaces) | **POST** /organizations/{organization_id}/workspaces | Create a new workspace.
[**put_organization**](OrganizationsApi.md#put_organization) | **PUT** /organizations/{organization_id} | Updates an existing organization
[**put_organization_group**](OrganizationsApi.md#put_organization_group) | **PUT** /organizations/{organization_id}/groups/{group_id} | Edit group
[**put_organization_segmentation**](OrganizationsApi.md#put_organization_segmentation) | **PUT** /organizations/{organization_id}/segmentation | Organization segmentation data
[**put_organization_users**](OrganizationsApi.md#put_organization_users) | **PUT** /organizations/{organization_id}/users/{organization_user_id} | Changes a single organization-user
[**put_organization_workspaces_assignments**](OrganizationsApi.md#put_organization_workspaces_assignments) | **PUT** /organizations/{organization_id}/workspaces/{workspace_id}/assignments | Change assignments of users within a workspace.


## `delete_organization_group`
> str delete_organization_group(organization_id, group_id)

Deletes group

Deletes a group from the specified organization

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
group_id = 56 # int | Numeric ID of the group.

try:
    # Deletes group
    api_response = api_instance.delete_organization_group(organization_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **group_id** | **int**| Numeric ID of the group. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_organization_users_leave`
> str delete_organization_users_leave(organization_id)

Leaves organization

Leaves organization, effectively delete user account in org and delete organization if it is last user

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Leaves organization
    api_response = api_instance.delete_organization_users_leave(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organization_users_leave: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization`
> ModelsMeOrganization get_organization(organization_id)

Organization data

Returns organization name and current pricing plan

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Organization data
    api_response = api_instance.get_organization(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**ModelsMeOrganization**](ModelsMeOrganization.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_groups`
> list[GroupOrganizationGroupResponse] get_organization_groups(organization_id, name=name, workspace=workspace)

List of groups in organization with user and workspace assignments

Returns list of groups in organization based on set of url parameters. List is sorted by name.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
name = 'name_example' # str | Returns records where name contains this string (optional)
workspace = 'workspace_example' # str | ID of workspace. Returns groups assigned to this workspace (optional)

try:
    # List of groups in organization with user and workspace assignments
    api_response = api_instance.get_organization_groups(organization_id, name=name, workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_groups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **name** | **str**| Returns records where name contains this string | [optional] 
 **workspace** | **str**| ID of workspace. Returns groups assigned to this workspace | [optional] 

### Return type

[**list[GroupOrganizationGroupResponse]**](GroupOrganizationGroupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_owner`
> ModelsOrganizationOwner get_organization_owner(organization_id)

Get owner of the organization

Returns organization owner data.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Get owner of the organization
    api_response = api_instance.get_organization_owner(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_owner: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**ModelsOrganizationOwner**](ModelsOrganizationOwner.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_segmentation`
> ModelsOrganizationSegmentation get_organization_segmentation(organization_id)

Organization segmentation data

Returns organization segmentation information

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Organization segmentation data
    api_response = api_instance.get_organization_segmentation(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_segmentation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**ModelsOrganizationSegmentation**](ModelsOrganizationSegmentation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_users`
> list[ModelsOrgUser] get_organization_users(organization_id, filter=filter, active_status=active_status, only_admins=only_admins, groups=groups, workspaces=workspaces, page=page, per_page=per_page, sort_dir=sort_dir)

List of users in organization

Returns list of users in organization based on set of url parameters: Result is paginated. Pagination params are returned in headers

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
filter = 'filter_example' # str | Returns records where name or email contains this string (optional)
active_status = 'active_status_example' # str | List of `active` `inactive` `invited` comma separated(if not present, all statuses) (optional)
only_admins = 'only_admins_example' # str | If true returns admins only (optional)
groups = 'groups_example' # str | Comma-separated list of groups ids, returns users belonging to these groups only (optional)
workspaces = 'workspaces_example' # str | Comma-separated list of workspaces ids, returns users belonging to this workspaces only (optional)
page = 56 # int | Page number, default 1 (optional)
per_page = 56 # int | Number of items per page, default 50 (optional)
sort_dir = 'sort_dir_example' # str | Values 'asc' or 'desc', result is sorted on 'names' column, default 'asc' (optional)

try:
    # List of users in organization
    api_response = api_instance.get_organization_users(organization_id, filter=filter, active_status=active_status, only_admins=only_admins, groups=groups, workspaces=workspaces, page=page, per_page=per_page, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **filter** | **str**| Returns records where name or email contains this string | [optional] 
 **active_status** | **str**| List of &#x60;active&#x60; &#x60;inactive&#x60; &#x60;invited&#x60; comma separated(if not present, all statuses) | [optional] 
 **only_admins** | **str**| If true returns admins only | [optional] 
 **groups** | **str**| Comma-separated list of groups ids, returns users belonging to these groups only | [optional] 
 **workspaces** | **str**| Comma-separated list of workspaces ids, returns users belonging to this workspaces only | [optional] 
 **page** | **int**| Page number, default 1 | [optional] 
 **per_page** | **int**| Number of items per page, default 50 | [optional] 
 **sort_dir** | **str**| Values &#39;asc&#39; or &#39;desc&#39;, result is sorted on &#39;names&#39; column, default &#39;asc&#39; | [optional] 

### Return type

[**list[ModelsOrgUser]**](ModelsOrgUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_users_detailed`
> list[ModelsOrgUserDetailed] get_organization_users_detailed(organization_id, filter=filter, active_status=active_status, only_admins=only_admins, groups=groups, workspaces=workspaces, page=page, per_page=per_page, sort_dir=sort_dir)

List of users in organization with details

Returns list of users in organization based on set of url parameters: Result is paginated. Pagination params are returned in headers

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
filter = 'filter_example' # str | Returns records where name or email contains this string (optional)
active_status = 'active_status_example' # str | List of `active` `inactive` `invited` comma separated(if not present, all statuses) (optional)
only_admins = 'only_admins_example' # str | If true returns admins only (optional)
groups = 'groups_example' # str | Comma-separated list of groups ids, returns users belonging to these groups only (optional)
workspaces = 'workspaces_example' # str | Comma-separated list of workspaces ids, returns users belonging to this workspaces only (optional)
page = 56 # int | Page number, default 1 (optional)
per_page = 56 # int | Number of items per page, default 50 (optional)
sort_dir = 'sort_dir_example' # str | Values 'asc' or 'desc', result is sorted on 'names' column, default 'asc' (optional)

try:
    # List of users in organization with details
    api_response = api_instance.get_organization_users_detailed(organization_id, filter=filter, active_status=active_status, only_admins=only_admins, groups=groups, workspaces=workspaces, page=page, per_page=per_page, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_users_detailed: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **filter** | **str**| Returns records where name or email contains this string | [optional] 
 **active_status** | **str**| List of &#x60;active&#x60; &#x60;inactive&#x60; &#x60;invited&#x60; comma separated(if not present, all statuses) | [optional] 
 **only_admins** | **str**| If true returns admins only | [optional] 
 **groups** | **str**| Comma-separated list of groups ids, returns users belonging to these groups only | [optional] 
 **workspaces** | **str**| Comma-separated list of workspaces ids, returns users belonging to this workspaces only | [optional] 
 **page** | **int**| Page number, default 1 | [optional] 
 **per_page** | **int**| Number of items per page, default 50 | [optional] 
 **sort_dir** | **str**| Values &#39;asc&#39; or &#39;desc&#39;, result is sorted on &#39;names&#39; column, default &#39;asc&#39; | [optional] 

### Return type

[**list[ModelsOrgUserDetailed]**](ModelsOrgUserDetailed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_workspaces_groups`
> list[GroupOrganizationGroupResponse] get_organization_workspaces_groups(organization_id, workspace_id)

List of groups in a workspace within an organization with user assignments.

Returns list of groups in a workspace based on set of url parameters. List is sorted by name.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization

try:
    # List of groups in a workspace within an organization with user assignments.
    api_response = api_instance.get_organization_workspaces_groups(organization_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_workspaces_groups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **workspace_id** | **int**| Numeric ID of the workspace within the organization | 

### Return type

[**list[GroupOrganizationGroupResponse]**](GroupOrganizationGroupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_workspaces_statistics`
> dict(str, ModelsStatistics) get_organization_workspaces_statistics()

Statistics for all workspaces in the organization

Returns map indexed by workspace ID where each map element contains workspace admins list, members count and groups count.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))

try:
    # Statistics for all workspaces in the organization
    api_response = api_instance.get_organization_workspaces_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization_workspaces_statistics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**dict(str, ModelsStatistics)**](ModelsStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organizations_payments_records`
> list[ModelsUnifiedSubscriptionInvoiceList] get_organizations_payments_records(organization_id, is_unified=is_unified, next=next, prev=prev)

OrganizationsPaymentRecords

Returns paid invoices

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
is_unified = true # bool | If 'true', returns unified invoices (optional)
next = 'next_example' # str | Next cursor for unified subsriptions. Cannot be used at the same time `prev` (optional)
prev = 'prev_example' # str | Previous cursor for unified subsriptions. Cannot be used at the same time with `next` (optional)

try:
    # OrganizationsPaymentRecords
    api_response = api_instance.get_organizations_payments_records(organization_id, is_unified=is_unified, next=next, prev=prev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_payments_records: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **is_unified** | **bool**| If &#39;true&#39;, returns unified invoices | [optional] 
 **next** | **str**| Next cursor for unified subsriptions. Cannot be used at the same time &#x60;prev&#x60; | [optional] 
 **prev** | **str**| Previous cursor for unified subsriptions. Cannot be used at the same time with &#x60;next&#x60; | [optional] 

### Return type

[**list[ModelsUnifiedSubscriptionInvoiceList]**](ModelsUnifiedSubscriptionInvoiceList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organizations_plans`
> BillingPricingStruct get_organizations_plans(organization_id)

OrganizationsPlans

Returns pricing plans for an organization

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # OrganizationsPlans
    api_response = api_instance.get_organizations_plans(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_plans: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**BillingPricingStruct**](BillingPricingStruct.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organizations_plans_0`
> BillingPricingStruct get_organizations_plans_0(organization_id, plan_id)

OrganizationsPlan

Returns pricing plan for an organization identified by plan_id

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
plan_id = 56 # int | Numeric ID of the plan

try:
    # OrganizationsPlan
    api_response = api_instance.get_organizations_plans_0(organization_id, plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_plans_0: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **plan_id** | **int**| Numeric ID of the plan | 

### Return type

[**BillingPricingStruct**](BillingPricingStruct.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_organization_group`
> GroupsPatchOutput patch_organization_group(organization_id, group_id, patch_group_request)

Patch group

Patches a group in the specified organization. Patches are applied individually.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
group_id = 56 # int | Numeric ID of the group.
patch_group_request = [toggl.GroupsPatchInput()] # list[GroupsPatchInput] | Array of patch operations.

try:
    # Patch group
    api_response = api_instance.patch_organization_group(organization_id, group_id, patch_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patch_organization_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **group_id** | **int**| Numeric ID of the group. | 
 **patch_group_request** | [**list[GroupsPatchInput]**](GroupsPatchInput.md)| Array of patch operations. | 

### Return type

[**GroupsPatchOutput**](GroupsPatchOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_organization_users`
> str patch_organization_users(organization_id, params)

Apply changes in bulk to users in an organization

Apply changes in bulk to users in an organization (currently deletion only).

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.UserPatchParams() # UserPatchParams | Input data of the users to be patched.

try:
    # Apply changes in bulk to users in an organization
    api_response = api_instance.patch_organization_users(organization_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patch_organization_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **params** | [**UserPatchParams**](UserPatchParams.md)| Input data of the users to be patched. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization`
> OrganizationPostOrganizationReply post_organization(post_organizations_request)

Creates a new organization

Creates a new organization with a single workspace and assigns current user as the organization owner

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
post_organizations_request = toggl.ModelsPostPayload() # ModelsPostPayload | Input data for organization.

try:
    # Creates a new organization
    api_response = api_instance.post_organization(post_organizations_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organization: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_organizations_request** | [**ModelsPostPayload**](ModelsPostPayload.md)| Input data for organization. | 

### Return type

[**OrganizationPostOrganizationReply**](OrganizationPostOrganizationReply.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_accept_invitation`
> str post_organization_accept_invitation(inviutation_code)

Accepts invitation

User connected with invitation is marked as joined, email is sent to the inviter.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.OrganizationsApi()
inviutation_code = 'inviutation_code_example' # str | Invitation code

try:
    # Accepts invitation
    api_response = api_instance.post_organization_accept_invitation(inviutation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organization_accept_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inviutation_code** | **str**| Invitation code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_group`
> GroupOrganizationGroupResponse post_organization_group(organization_id, post_group_request)

Create group

Creates a group in the specified organization

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
post_group_request = toggl.GroupPayload() # GroupPayload | Input data for group creation.

try:
    # Create group
    api_response = api_instance.post_organization_group(organization_id, post_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organization_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **post_group_request** | [**GroupPayload**](GroupPayload.md)| Input data for group creation. | 

### Return type

[**GroupOrganizationGroupResponse**](GroupOrganizationGroupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_invitation`
> InvitationResult post_organization_invitation(organization_id, post_invitation_request)

Creates a new invitation for the user

Creates a new invitation for the user.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
post_invitation_request = toggl.InvitationPost() # InvitationPost | Input data for invitation creation

try:
    # Creates a new invitation for the user
    api_response = api_instance.post_organization_invitation(organization_id, post_invitation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organization_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **post_invitation_request** | [**InvitationPost**](InvitationPost.md)| Input data for invitation creation | 

### Return type

[**InvitationResult**](InvitationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_workspaces`
> WorkspaceWorkspace post_organization_workspaces(organization_id, post)

Create a new workspace.

Create a workspace within an existing organization.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
post = toggl.WorkspacePayload() # WorkspacePayload | Parameters of the new workspace

try:
    # Create a new workspace.
    api_response = api_instance.post_organization_workspaces(organization_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organization_workspaces: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **post** | [**WorkspacePayload**](WorkspacePayload.md)| Parameters of the new workspace | 

### Return type

[**WorkspaceWorkspace**](WorkspaceWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization`
> str put_organization(organization_id, put_organizations_request)

Updates an existing organization

Updates an existing organization

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
put_organizations_request = toggl.ModelsPutPayload() # ModelsPutPayload | Input data for organization.

try:
    # Updates an existing organization
    api_response = api_instance.put_organization(organization_id, put_organizations_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organization: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **put_organizations_request** | [**ModelsPutPayload**](ModelsPutPayload.md)| Input data for organization. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization_group`
> GroupOrganizationGroupResponse put_organization_group(organization_id, put_group_request)

Edit group

Edits a group in the specified organization

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
put_group_request = toggl.GroupPayload() # GroupPayload | Input data for group modification.

try:
    # Edit group
    api_response = api_instance.put_organization_group(organization_id, put_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organization_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **put_group_request** | [**GroupPayload**](GroupPayload.md)| Input data for group modification. | 

### Return type

[**GroupOrganizationGroupResponse**](GroupOrganizationGroupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization_segmentation`
> ModelsOrganizationSegmentation put_organization_segmentation(organization_id)

Organization segmentation data

Save organization segmentation information

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Organization segmentation data
    api_response = api_instance.put_organization_segmentation(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organization_segmentation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 

### Return type

[**ModelsOrganizationSegmentation**](ModelsOrganizationSegmentation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization_users`
> str put_organization_users(organization_id, params)

Changes a single organization-user

Changes a single organization-user. Can affect the following values:

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.UserPayload() # UserPayload | Input data of the organization user to be changed.

try:
    # Changes a single organization-user
    api_response = api_instance.put_organization_users(organization_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organization_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **params** | [**UserPayload**](UserPayload.md)| Input data of the organization user to be changed. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization_workspaces_assignments`
> str put_organization_workspaces_assignments(organization_id, workspace_id, post)

Change assignments of users within a workspace.

Assign or remove users to/from a workspace or to/from groups belonging to said workspace.

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
api_instance = toggl.OrganizationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
post = toggl.UserAssignmentsPayload() # UserAssignmentsPayload | Describes the change in assignment

try:
    # Change assignments of users within a workspace.
    api_response = api_instance.put_organization_workspaces_assignments(organization_id, workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organization_workspaces_assignments: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **workspace_id** | **int**| Numeric ID of the workspace within the organization | 
 **post** | [**UserAssignmentsPayload**](UserAssignmentsPayload.md)| Describes the change in assignment | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

