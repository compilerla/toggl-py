# toggl.ProjectsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_project**](ProjectsApi.md#delete_workspace_project) | **DELETE** /workspaces/{workspace_id}/projects/{project_id} | WorkspaceProject
[**delete_workspace_project_users**](ProjectsApi.md#delete_workspace_project_users) | **DELETE** /workspaces/{workspace_id}/project_users/{project_user_id} | Delete a project user from workspace projects users
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /workspaces/{workspace_id}/projects | WorkspaceProjects
[**get_projects_templates**](ProjectsApi.md#get_projects_templates) | **GET** /workspaces/{workspace_id}/projects/templates | WorkspaceProjectsTemplates
[**get_workspace_project_periods**](ProjectsApi.md#get_workspace_project_periods) | **GET** /workspaces/{workspace_id}/projects/{project_id}/periods | Get Recurring Project Periods
[**get_workspace_project_users**](ProjectsApi.md#get_workspace_project_users) | **GET** /workspaces/{workspace_id}/project_users | Get workspace projects users
[**patch_workspace_project_users_ids**](ProjectsApi.md#patch_workspace_project_users_ids) | **PATCH** /workspaces/{workspace_id}/project_users/{project_user_ids} | Patch project users from workspace
[**patch_workspace_projects**](ProjectsApi.md#patch_workspace_projects) | **PATCH** /workspaces/{workspace_id}/projects/{project_ids} | WorkspaceProjects
[**post_workspace_project_create**](ProjectsApi.md#post_workspace_project_create) | **POST** /workspaces/{workspace_id}/projects | WorkspaceProjects
[**post_workspace_project_users**](ProjectsApi.md#post_workspace_project_users) | **POST** /workspaces/{workspace_id}/project_users | Add an user into workspace projects users
[**put_workspace_project**](ProjectsApi.md#put_workspace_project) | **PUT** /workspaces/{workspace_id}/projects/{project_id} | WorkspaceProject
[**put_workspace_project_users**](ProjectsApi.md#put_workspace_project_users) | **PUT** /workspaces/{workspace_id}/project_users/{project_user_id} | Update an user into workspace projects users
[**workspaces_workspace_id_projects_billable_amounts_post**](ProjectsApi.md#workspaces_workspace_id_projects_billable_amounts_post) | **POST** /workspaces/{workspace_id}/projects/billable-amounts | Projects
[**workspaces_workspace_id_projects_project_id_get**](ProjectsApi.md#workspaces_workspace_id_projects_project_id_get) | **GET** /workspaces/{workspace_id}/projects/{project_id} | WorkspaceProject
[**workspaces_workspace_id_projects_project_id_statistics_get**](ProjectsApi.md#workspaces_workspace_id_projects_project_id_statistics_get) | **GET** /workspaces/{workspace_id}/projects/{project_id}/statistics | WorkspaceProject


## `delete_workspace_project`
> int delete_workspace_project(workspace_id, project_id, te_deletion_mode=te_deletion_mode)

WorkspaceProject

Delete project for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
te_deletion_mode = 'te_deletion_mode_example' # str | Time entries deletion mode: 'delete' or 'unassign' (optional)

try:
    # WorkspaceProject
    api_response = api_instance.delete_workspace_project(workspace_id, project_id, te_deletion_mode=te_deletion_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_workspace_project: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **te_deletion_mode** | **str**| Time entries deletion mode: &#39;delete&#39; or &#39;unassign&#39; | [optional] 

### Return type

**int**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_project_users`
> int delete_workspace_project_users(workspace_id, project_user_id)

Delete a project user from workspace projects users

Delete a project user for a given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_user_id = 56 # int | Numeric ID of the project user

try:
    # Delete a project user from workspace projects users
    api_response = api_instance.delete_workspace_project_users(workspace_id, project_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_workspace_project_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_user_id** | **int**| Numeric ID of the project user | 

### Return type

**int**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_projects`
> list[ModelsProject] get_projects(workspace_id, name, page, sort_field, sort_order, only_templates, active=active, since=since, billable=billable, user_ids=user_ids, client_ids=client_ids, group_ids=group_ids, statuses=statuses, per_page=per_page)

WorkspaceProjects

Get projects for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
name = 'name_example' # str | name
page = 56 # int | page
sort_field = 'sort_field_example' # str | sort_field
sort_order = 'sort_order_example' # str | sort_order
only_templates = true # bool | only_templates
active = true # bool | active (optional)
since = 56 # int | Retrieve projects created/modified/deleted since this date using UNIX timestamp. (optional)
billable = true # bool | billable (optional)
user_ids = ['user_ids_example'] # list[str] | user_ids (optional)
client_ids = ['client_ids_example'] # list[str] | client_ids (optional)
group_ids = ['group_ids_example'] # list[str] | group_ids (optional)
statuses = ['statuses_example'] # list[str] | statuses (optional)
per_page = 56 # int | Number of items per page, default 151. Cannot exceed 200. (optional)

try:
    # WorkspaceProjects
    api_response = api_instance.get_projects(workspace_id, name, page, sort_field, sort_order, only_templates, active=active, since=since, billable=billable, user_ids=user_ids, client_ids=client_ids, group_ids=group_ids, statuses=statuses, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **name** | **str**| name | 
 **page** | **int**| page | 
 **sort_field** | **str**| sort_field | 
 **sort_order** | **str**| sort_order | 
 **only_templates** | **bool**| only_templates | 
 **active** | **bool**| active | [optional] 
 **since** | **int**| Retrieve projects created/modified/deleted since this date using UNIX timestamp. | [optional] 
 **billable** | **bool**| billable | [optional] 
 **user_ids** | [**list[str]**](str.md)| user_ids | [optional] 
 **client_ids** | [**list[str]**](str.md)| client_ids | [optional] 
 **group_ids** | [**list[str]**](str.md)| group_ids | [optional] 
 **statuses** | [**list[str]**](str.md)| statuses | [optional] 
 **per_page** | **int**| Number of items per page, default 151. Cannot exceed 200. | [optional] 

### Return type

[**list[ModelsProject]**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_projects_templates`
> str get_projects_templates(workspace_id)

WorkspaceProjectsTemplates

Get projects templates for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # WorkspaceProjectsTemplates
    api_response = api_instance.get_projects_templates(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_templates: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_project_periods`
> ModelsRecurringPeriod get_workspace_project_periods(workspace_id, project_id, start_date=start_date, end_date=end_date)

Get Recurring Project Periods

Get recurring project periods for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
start_date = 'start_date_example' # str | Smallest boundary date to search for recurring periods (optional)
end_date = 'end_date_example' # str | Biggest boundary date to search for for recurring periods (optional)

try:
    # Get Recurring Project Periods
    api_response = api_instance.get_workspace_project_periods(workspace_id, project_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_workspace_project_periods: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **start_date** | **str**| Smallest boundary date to search for recurring periods | [optional] 
 **end_date** | **str**| Biggest boundary date to search for for recurring periods | [optional] 

### Return type

[**ModelsRecurringPeriod**](ModelsRecurringPeriod.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_project_users`
> list[ModelsProjectUser] get_workspace_project_users(workspace_id, project_ids=project_ids, with_group_members=with_group_members)

Get workspace projects users

List all projects users for a given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_ids = 'project_ids_example' # str | Numeric IDs of projects, comma-separated (optional)
with_group_members = true # bool | Include group members (optional)

try:
    # Get workspace projects users
    api_response = api_instance.get_workspace_project_users(workspace_id, project_ids=project_ids, with_group_members=with_group_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_workspace_project_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_ids** | **str**| Numeric IDs of projects, comma-separated | [optional] 
 **with_group_members** | **bool**| Include group members | [optional] 

### Return type

[**list[ModelsProjectUser]**](ModelsProjectUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_project_users_ids`
> UserOutput patch_workspace_project_users_ids(workspace_id, project_user_ids)

Patch project users from workspace

Patch a list of project users for a given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_user_ids = [56] # list[int] | Numeric IDs of the project users

try:
    # Patch project users from workspace
    api_response = api_instance.patch_workspace_project_users_ids(workspace_id, project_user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->patch_workspace_project_users_ids: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_user_ids** | [**list[int]**](int.md)| Numeric IDs of the project users | 

### Return type

[**UserOutput**](UserOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_projects`
> ProjectsPatchOutput patch_workspace_projects(workspace_id, project_ids, patch_input)

WorkspaceProjects

Bulk editing workspace projects.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_ids = 'project_ids_example' # str | Numeric IDs of project ids, separated by comma. E.g.: `204301830,202700150,202687559`
patch_input = toggl.ProjectsPatchPost() # ProjectsPatchPost | Array of batch operations

try:
    # WorkspaceProjects
    api_response = api_instance.patch_workspace_projects(workspace_id, project_ids, patch_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->patch_workspace_projects: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_ids** | **str**| Numeric IDs of project ids, separated by comma. E.g.: &#x60;204301830,202700150,202687559&#x60; | 
 **patch_input** | [**ProjectsPatchPost**](ProjectsPatchPost.md)| Array of batch operations | 

### Return type

[**ProjectsPatchOutput**](ProjectsPatchOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_project_create`
> ModelsProject post_workspace_project_create(workspace_id, post_input)

WorkspaceProjects

Create project for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
post_input = toggl.ProjectPayload() # ProjectPayload | Post parameters

try:
    # WorkspaceProjects
    api_response = api_instance.post_workspace_project_create(workspace_id, post_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->post_workspace_project_create: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **post_input** | [**ProjectPayload**](ProjectPayload.md)| Post parameters | 

### Return type

[**ModelsProject**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_project_users`
> ModelsProjectUser post_workspace_project_users(workspace_id, project_user)

Add an user into workspace projects users

Include a project user for a given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_user = toggl.UserPostPayload() # UserPostPayload | Input data of the user.

try:
    # Add an user into workspace projects users
    api_response = api_instance.post_workspace_project_users(workspace_id, project_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->post_workspace_project_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_user** | [**UserPostPayload**](UserPostPayload.md)| Input data of the user. | 

### Return type

[**ModelsProjectUser**](ModelsProjectUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_project`
> ModelsProject put_workspace_project(workspace_id, project_id, post_input)

WorkspaceProject

Update project for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
post_input = toggl.ProjectPayload() # ProjectPayload | Post parameters

try:
    # WorkspaceProject
    api_response = api_instance.put_workspace_project(workspace_id, project_id, post_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->put_workspace_project: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **post_input** | [**ProjectPayload**](ProjectPayload.md)| Post parameters | 

### Return type

[**ModelsProject**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_project_users`
> ModelsProjectUser put_workspace_project_users(workspace_id, project_user_id, project_user)

Update an user into workspace projects users

Update the data for a project user for a given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_user_id = 56 # int | Numeric ID of the project user
project_user = toggl.UserPutPayload() # UserPutPayload | Input data of the user.

try:
    # Update an user into workspace projects users
    api_response = api_instance.put_workspace_project_users(workspace_id, project_user_id, project_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->put_workspace_project_users: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_user_id** | **int**| Numeric ID of the project user | 
 **project_user** | [**UserPutPayload**](UserPutPayload.md)| Input data of the user. | 

### Return type

[**ModelsProjectUser**](ModelsProjectUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `workspaces_workspace_id_projects_billable_amounts_post`
> list[ModelsProject] workspaces_workspace_id_projects_billable_amounts_post(workspace_id, post_input)

Projects

Get projects billable amounts

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
post_input = toggl.ProjectsPayload() # ProjectsPayload | Project IDs

try:
    # Projects
    api_response = api_instance.workspaces_workspace_id_projects_billable_amounts_post(workspace_id, post_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->workspaces_workspace_id_projects_billable_amounts_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **post_input** | [**ProjectsPayload**](ProjectsPayload.md)| Project IDs | 

### Return type

[**list[ModelsProject]**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `workspaces_workspace_id_projects_project_id_get`
> ModelsProject workspaces_workspace_id_projects_project_id_get(workspace_id, project_id)

WorkspaceProject

Get project for given workspace.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project

try:
    # WorkspaceProject
    api_response = api_instance.workspaces_workspace_id_projects_project_id_get(workspace_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->workspaces_workspace_id_projects_project_id_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 

### Return type

[**ModelsProject**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `workspaces_workspace_id_projects_project_id_statistics_get`
> ModelsProjectStatistics workspaces_workspace_id_projects_project_id_statistics_get(workspace_id, project_id)

WorkspaceProject

Get statistics for given workspace and project. For time entry related information, this endpoint does not consider running ones.

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
api_instance = toggl.ProjectsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project

try:
    # WorkspaceProject
    api_response = api_instance.workspaces_workspace_id_projects_project_id_statistics_get(workspace_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->workspaces_workspace_id_projects_project_id_statistics_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 

### Return type

[**ModelsProjectStatistics**](ModelsProjectStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

