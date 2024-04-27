# toggl.GroupsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organization_group**](GroupsApi.md#delete_organization_group) | **DELETE** /organizations/{organization_id}/groups/{group_id} | Deletes group
[**delete_project_group**](GroupsApi.md#delete_project_group) | **DELETE** /workspaces/{workspace_id}/project_groups/{project_group_id} | Remove project group.
[**delete_workspace_group**](GroupsApi.md#delete_workspace_group) | **DELETE** /workspaces/{workspace_id}/groups/{group_id} | Delete group
[**get_organization_groups**](GroupsApi.md#get_organization_groups) | **GET** /organizations/{organization_id}/groups | List of groups in organization with user and workspace assignments
[**get_organization_workspaces_groups**](GroupsApi.md#get_organization_workspaces_groups) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/groups | List of groups in a workspace within an organization with user assignments.
[**get_project_groups**](GroupsApi.md#get_project_groups) | **GET** /workspaces/{workspace_id}/project_groups | Get workspace project groups.
[**get_workspace_groups**](GroupsApi.md#get_workspace_groups) | **GET** /workspaces/{workspace_id}/groups | Get workspace groups
[**patch_organization_group**](GroupsApi.md#patch_organization_group) | **PATCH** /organizations/{organization_id}/groups/{group_id} | Patch group
[**post_organization_group**](GroupsApi.md#post_organization_group) | **POST** /organizations/{organization_id}/groups | Create group
[**post_project_group**](GroupsApi.md#post_project_group) | **POST** /workspaces/{workspace_id}/project_groups | Adds group to project.
[**post_workspace_group**](GroupsApi.md#post_workspace_group) | **POST** /workspaces/{workspace_id}/groups | Create group
[**put_organization_group**](GroupsApi.md#put_organization_group) | **PUT** /organizations/{organization_id}/groups/{group_id} | Edit group
[**put_organization_workspaces_assignments**](GroupsApi.md#put_organization_workspaces_assignments) | **PUT** /organizations/{organization_id}/workspaces/{workspace_id}/assignments | Change assignments of users within a workspace.
[**put_workspace_group**](GroupsApi.md#put_workspace_group) | **PUT** /workspaces/{workspace_id}/groups/{group_id} | Update group


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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
group_id = 56 # int | Numeric ID of the group.

try:
    # Deletes group
    api_response = api_instance.delete_organization_group(organization_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_organization_group: %s\n" % e)
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

## `delete_project_group`
> str delete_project_group(workspace_id, project_group_id)

Remove project group.

Remove project group for a given workspace.

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_group_id = 56 # int | Numeric ID of the project group

try:
    # Remove project group.
    api_response = api_instance.delete_project_group(workspace_id, project_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_project_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_group_id** | **int**| Numeric ID of the project group | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_group`
> delete_workspace_group(workspace_id, group_id)

Delete group

Deletes the group.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.GroupsApi()
workspace_id = 56 # int | Numeric ID of the workspace.
group_id = 56 # int | Numeric ID of the group.

try:
    # Delete group
    api_instance.delete_workspace_group(workspace_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_workspace_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **group_id** | **int**| Numeric ID of the group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
name = 'name_example' # str | Returns records where name contains this string (optional)
workspace = 'workspace_example' # str | ID of workspace. Returns groups assigned to this workspace (optional)

try:
    # List of groups in organization with user and workspace assignments
    api_response = api_instance.get_organization_groups(organization_id, name=name, workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_organization_groups: %s\n" % e)
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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization

try:
    # List of groups in a workspace within an organization with user assignments.
    api_response = api_instance.get_organization_workspaces_groups(organization_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_organization_workspaces_groups: %s\n" % e)
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

## `get_project_groups`
> list[ModelsProjectGroup] get_project_groups(workspace_id, project_ids)

Get workspace project groups.

Get project groups for given workspace.

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_ids = 'project_ids_example' # str | Project IDs separated by comma.

try:
    # Get workspace project groups.
    api_response = api_instance.get_project_groups(workspace_id, project_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_project_groups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_ids** | **str**| Project IDs separated by comma. | 

### Return type

[**list[ModelsProjectGroup]**](ModelsProjectGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_groups`
> list[ModelsGroup] get_workspace_groups(workspace_id)

Get workspace groups

Returns a list of groups for the specified workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.GroupsApi()
workspace_id = 56 # int | Numeric ID of the workspace.

try:
    # Get workspace groups
    api_response = api_instance.get_workspace_groups(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_workspace_groups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 

### Return type

[**list[ModelsGroup]**](ModelsGroup.md)

### Authorization

No authorization required

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
group_id = 56 # int | Numeric ID of the group.
patch_group_request = [toggl.GroupsPatchInput()] # list[GroupsPatchInput] | Array of patch operations.

try:
    # Patch group
    api_response = api_instance.patch_organization_group(organization_id, group_id, patch_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->patch_organization_group: %s\n" % e)
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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
post_group_request = toggl.GroupPayload() # GroupPayload | Input data for group creation.

try:
    # Create group
    api_response = api_instance.post_organization_group(organization_id, post_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_organization_group: %s\n" % e)
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

## `post_project_group`
> str post_project_group(workspace_id, project_group_post)

Adds group to project.

Adds group to project for given workspace.

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_group_post = toggl.GroupProjectGroupPayload() # GroupProjectGroupPayload | Input data

try:
    # Adds group to project.
    api_response = api_instance.post_project_group(workspace_id, project_group_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_project_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_group_post** | [**GroupProjectGroupPayload**](GroupProjectGroupPayload.md)| Input data | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_group`
> ModelsGroup post_workspace_group(workspace_id, post_group_request)

Create group

Creates a group in the specified workspace

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.GroupsApi()
workspace_id = 56 # int | Numeric ID of the workspace.
post_group_request = toggl.GroupNamePayload() # GroupNamePayload | Input data for group creation.

try:
    # Create group
    api_response = api_instance.post_workspace_group(workspace_id, post_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_workspace_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **post_group_request** | [**GroupNamePayload**](GroupNamePayload.md)| Input data for group creation. | 

### Return type

[**ModelsGroup**](ModelsGroup.md)

### Authorization

No authorization required

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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
put_group_request = toggl.GroupPayload() # GroupPayload | Input data for group modification.

try:
    # Edit group
    api_response = api_instance.put_organization_group(organization_id, put_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->put_organization_group: %s\n" % e)
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
api_instance = toggl.GroupsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
post = toggl.UserAssignmentsPayload() # UserAssignmentsPayload | Describes the change in assignment

try:
    # Change assignments of users within a workspace.
    api_response = api_instance.put_organization_workspaces_assignments(organization_id, workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->put_organization_workspaces_assignments: %s\n" % e)
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

## `put_workspace_group`
> ModelsGroup put_workspace_group(workspace_id, group_id, put_group_request)

Update group

Updates the group.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.GroupsApi()
workspace_id = 56 # int | Numeric ID of the workspace.
group_id = 56 # int | Numeric ID of the group.
put_group_request = toggl.GroupNamePayload() # GroupNamePayload | Input data for group update.

try:
    # Update group
    api_response = api_instance.put_workspace_group(workspace_id, group_id, put_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->put_workspace_group: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **group_id** | **int**| Numeric ID of the group. | 
 **put_group_request** | [**GroupNamePayload**](GroupNamePayload.md)| Input data for group update. | 

### Return type

[**ModelsGroup**](ModelsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

