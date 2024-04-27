# toggl.UsersApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organization_users_leave**](UsersApi.md#delete_organization_users_leave) | **DELETE** /organizations/{organization_id}/users/leave | Leaves organization
[**delete_workspace_user**](UsersApi.md#delete_workspace_user) | **DELETE** /workspaces/{workspace_id}/workspace_users/{workspace_user_id} | Delete workspace user
[**get_organization_users**](UsersApi.md#get_organization_users) | **GET** /organizations/{organization_id}/users | List of users in organization
[**get_organization_users_detailed**](UsersApi.md#get_organization_users_detailed) | **GET** /organizations/{organization_id}/users/detailed | List of users in organization with details
[**get_organization_workspaces_workspaceusers**](UsersApi.md#get_organization_workspaces_workspaceusers) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/workspace_users | List of users who belong to the given workspace.
[**get_workspace_users**](UsersApi.md#get_workspace_users) | **GET** /workspaces/{workspace_id}/users | Get workspace users
[**get_workspace_workspace_users**](UsersApi.md#get_workspace_workspace_users) | **GET** /workspaces/{workspace_id}/workspace_users | Get workspace workspace-users
[**patch_organization_users**](UsersApi.md#patch_organization_users) | **PATCH** /organizations/{organization_id}/users | Apply changes in bulk to users in an organization
[**patch_organization_workspace_users**](UsersApi.md#patch_organization_workspace_users) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/workspace_users | Changes the users in a workspace.
[**post_workspace_users_lost_password**](UsersApi.md#post_workspace_users_lost_password) | **POST** /workspaces/{workspace_id}/users/{user_id}/lost_password | Change a lost password
[**put_organization_users**](UsersApi.md#put_organization_users) | **PUT** /organizations/{organization_id}/users/{organization_user_id} | Changes a single organization-user
[**put_organization_workspaces_assignments**](UsersApi.md#put_organization_workspaces_assignments) | **PUT** /organizations/{organization_id}/workspaces/{workspace_id}/assignments | Change assignments of users within a workspace.
[**put_workspace_users**](UsersApi.md#put_workspace_users) | **PUT** /workspaces/{workspace_id}/users/{user_id} | Update workspace user
[**put_workspace_workspace_users**](UsersApi.md#put_workspace_workspace_users) | **PUT** /workspaces/{workspace_id}/workspace_users/{workspace_user_id} | Update workspace-user


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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization

try:
    # Leaves organization
    api_response = api_instance.delete_organization_users_leave(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_organization_users_leave: %s\n" % e)
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

## `delete_workspace_user`
> delete_workspace_user(workspace_id, workspace_user_id)

Delete workspace user

Removes user from workspace

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.UsersApi()
workspace_id = 56 # int | Numeric ID of the workspace.
workspace_user_id = 56 # int | Numeric ID of the workspace user.

try:
    # Delete workspace user
    api_instance.delete_workspace_user(workspace_id, workspace_user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_workspace_user: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **workspace_user_id** | **int**| Numeric ID of the workspace user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
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
    print("Exception when calling UsersApi->get_organization_users: %s\n" % e)
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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
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
    print("Exception when calling UsersApi->get_organization_users_detailed: %s\n" % e)
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

## `get_organization_workspaces_workspaceusers`
> list[ModelsOrganizationWorkspaceUser] get_organization_workspaces_workspaceusers(organization_id, workspace_id, name)

List of users who belong to the given workspace.

Returns any users who belong to the workspace directly or through at least one group.

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
name = 'name_example' # str | Workspace user name to filter by

try:
    # List of users who belong to the given workspace.
    api_response = api_instance.get_organization_workspaces_workspaceusers(organization_id, workspace_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_organization_workspaces_workspaceusers: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **workspace_id** | **int**| Numeric ID of the workspace within the organization | 
 **name** | **str**| Workspace user name to filter by | 

### Return type

[**list[ModelsOrganizationWorkspaceUser]**](ModelsOrganizationWorkspaceUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_users`
> list[ModelsSimpleWorkspaceUser] get_workspace_users(workspace_id)

Get workspace users

List all users for a given workspace.

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace users
    api_response = api_instance.get_workspace_users(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_workspace_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsSimpleWorkspaceUser]**](ModelsSimpleWorkspaceUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_workspace_users`
> list[ModelsWorkspaceUser] get_workspace_workspace_users(workspace_id, include_indirect)

Get workspace workspace-users

List all workspace_users for a given workspace.

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
include_indirect = 'include_indirect_example' # str | If true, includes indirect users (i.e. users assigned via group) to workspace user list

try:
    # Get workspace workspace-users
    api_response = api_instance.get_workspace_workspace_users(workspace_id, include_indirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_workspace_workspace_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **include_indirect** | **str**| If true, includes indirect users (i.e. users assigned via group) to workspace user list | 

### Return type

[**list[ModelsWorkspaceUser]**](ModelsWorkspaceUser.md)

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.UserPatchParams() # UserPatchParams | Input data of the users to be patched.

try:
    # Apply changes in bulk to users in an organization
    api_response = api_instance.patch_organization_users(organization_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_organization_users: %s\n" % e)
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

## `patch_organization_workspace_users`
> str patch_organization_workspace_users(organization_id, workspace_id, params)

Changes the users in a workspace.

Changes the users in a workspace (currently deletion only).

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace
params = toggl.WorkspaceUsersPatchParams() # WorkspaceUsersPatchParams | Input data of the users to be patched.

try:
    # Changes the users in a workspace.
    api_response = api_instance.patch_organization_workspace_users(organization_id, workspace_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_organization_workspace_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **params** | [**WorkspaceUsersPatchParams**](WorkspaceUsersPatchParams.md)| Input data of the users to be patched. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_users_lost_password`
> UsersLostPasswordURL post_workspace_users_lost_password(workspace_id, user_id)

Change a lost password

Request a change password action

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
user_id = 56 # int | Numeric ID of the user

try:
    # Change a lost password
    api_response = api_instance.post_workspace_users_lost_password(workspace_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_workspace_users_lost_password: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **user_id** | **int**| Numeric ID of the user | 

### Return type

[**UsersLostPasswordURL**](UsersLostPasswordURL.md)

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
params = toggl.UserPayload() # UserPayload | Input data of the organization user to be changed.

try:
    # Changes a single organization-user
    api_response = api_instance.put_organization_users(organization_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_organization_users: %s\n" % e)
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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
post = toggl.UserAssignmentsPayload() # UserAssignmentsPayload | Describes the change in assignment

try:
    # Change assignments of users within a workspace.
    api_response = api_instance.put_organization_workspaces_assignments(organization_id, workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_organization_workspaces_assignments: %s\n" % e)
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

## `put_workspace_users`
> str put_workspace_users(workspace_id, user_id)

Update workspace user

Update the data for a user in a given workspace.

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
user_id = 56 # int | Numeric ID of the user

try:
    # Update workspace user
    api_response = api_instance.put_workspace_users(workspace_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_workspace_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **user_id** | **int**| Numeric ID of the user | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_workspace_users`
> str put_workspace_workspace_users(workspace_id, workspace_user_id, post)

Update workspace-user

Update the data for a workspace_user in a given workspace.

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
api_instance = toggl.UsersApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
workspace_user_id = 56 # int | Numeric ID of the workspace user
post = toggl.UserPayload() # UserPayload | Changes that need to be applied to the user data.

try:
    # Update workspace-user
    api_response = api_instance.put_workspace_workspace_users(workspace_id, workspace_user_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_workspace_workspace_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **workspace_user_id** | **int**| Numeric ID of the workspace user | 
 **post** | [**UserPayload**](UserPayload.md)| Changes that need to be applied to the user data. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

