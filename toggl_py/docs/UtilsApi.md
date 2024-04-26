# toggl.UtilsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_workspace_workspace_id_action_tasks_auth_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_action_tasks_auth_post) | **POST** /reports/api/v3/workspace/{workspace_id}/{action}/tasks_auth | List tasks
[**reports_api_v3_workspace_workspace_id_action_tasks_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_action_tasks_post) | **POST** /reports/api/v3/workspace/{workspace_id}/{action}/tasks | List tasks
[**reports_api_v3_workspace_workspace_id_filters_clients_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_clients_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/clients | List clients
[**reports_api_v3_workspace_workspace_id_filters_project_groups_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_project_groups_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/project_groups | List project groups filter
[**reports_api_v3_workspace_workspace_id_filters_project_users_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_project_users_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/project_users | List project users
[**reports_api_v3_workspace_workspace_id_filters_projects_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_projects_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/projects | List projects
[**reports_api_v3_workspace_workspace_id_filters_projects_status_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_projects_status_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/projects/status | List projects statuses
[**reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/tasks_auth/status | List tasks statuses
[**reports_api_v3_workspace_workspace_id_filters_tasks_status_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_tasks_status_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/tasks/status | List tasks statuses
[**reports_api_v3_workspace_workspace_id_filters_users_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_filters_users_post) | **POST** /reports/api/v3/workspace/{workspace_id}/filters/users | List users
[**reports_api_v3_workspace_workspace_id_search_clients_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_search_clients_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/clients | Search clients
[**reports_api_v3_workspace_workspace_id_search_projects_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_search_projects_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/projects | List projects
[**reports_api_v3_workspace_workspace_id_search_users_post**](UtilsApi.md#reports_api_v3_workspace_workspace_id_search_users_post) | **POST** /reports/api/v3/workspace/{workspace_id}/search/users | List users


## `reports_api_v3_workspace_workspace_id_action_tasks_auth_post`
> list[ModelsTask] reports_api_v3_workspace_workspace_id_action_tasks_auth_post(workspace_id, action, tasks_post=tasks_post)

List tasks

Returns filtered tasks from workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
action = 'action_example' # str | search,filters
tasks_post = toggl.TasksTasksPost() # TasksTasksPost | Task search conditions (optional)

try:
    # List tasks
    api_response = api_instance.reports_api_v3_workspace_workspace_id_action_tasks_auth_post(workspace_id, action, tasks_post=tasks_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_action_tasks_auth_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **action** | **str**| search,filters | 
 **tasks_post** | [**TasksTasksPost**](TasksTasksPost.md)| Task search conditions | [optional] 

### Return type

[**list[ModelsTask]**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_action_tasks_post`
> list[ModelsTask] reports_api_v3_workspace_workspace_id_action_tasks_post(workspace_id, action, tasks_post=tasks_post)

List tasks

Returns filtered tasks from workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
action = 'action_example' # str | search,filters
tasks_post = toggl.TasksTasksPost() # TasksTasksPost | Task search conditions (optional)

try:
    # List tasks
    api_response = api_instance.reports_api_v3_workspace_workspace_id_action_tasks_post(workspace_id, action, tasks_post=tasks_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_action_tasks_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **action** | **str**| search,filters | 
 **tasks_post** | [**TasksTasksPost**](TasksTasksPost.md)| Task search conditions | [optional] 

### Return type

[**list[ModelsTask]**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_clients_post`
> list[ClientsClientsResponse] reports_api_v3_workspace_workspace_id_filters_clients_post(workspace_id, clients_post=clients_post)

List clients

Returns filtered clients from a workspace (only ID and name).

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
clients_post = toggl.ClientsClientsPost() # ClientsClientsPost | Clients filter conditions (optional)

try:
    # List clients
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_clients_post(workspace_id, clients_post=clients_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_clients_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **clients_post** | [**ClientsClientsPost**](ClientsClientsPost.md)| Clients filter conditions | [optional] 

### Return type

[**list[ClientsClientsResponse]**](ClientsClientsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_project_groups_post`
> list[GroupsProjectGroup] reports_api_v3_workspace_workspace_id_filters_project_groups_post(workspace_id, project_groups_post=project_groups_post)

List project groups filter

Returns the project groups from a workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
project_groups_post = toggl.GroupsProjectGroupsPost() # GroupsProjectGroupsPost | Project groups filter conditions (optional)

try:
    # List project groups filter
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_project_groups_post(workspace_id, project_groups_post=project_groups_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_project_groups_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **project_groups_post** | [**GroupsProjectGroupsPost**](GroupsProjectGroupsPost.md)| Project groups filter conditions | [optional] 

### Return type

[**list[GroupsProjectGroup]**](GroupsProjectGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_project_users_post`
> list[UsersProjectUser] reports_api_v3_workspace_workspace_id_filters_project_users_post(workspace_id, status_post)

List project users

Returns filtered user projects.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
status_post = toggl.UsersProjectUsersPost() # UsersProjectUsersPost | User projects filter conditions

try:
    # List project users
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_project_users_post(workspace_id, status_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_project_users_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **status_post** | [**UsersProjectUsersPost**](UsersProjectUsersPost.md)| User projects filter conditions | 

### Return type

[**list[UsersProjectUser]**](UsersProjectUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_projects_post`
> list[ProjectsProjectResponse] reports_api_v3_workspace_workspace_id_filters_projects_post(workspace_id, projects_post=projects_post)

List projects

Returns filtered projects from a workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
projects_post = toggl.ProjectsProjectsPost() # ProjectsProjectsPost | Projects filter conditions (optional)

try:
    # List projects
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_projects_post(workspace_id, projects_post=projects_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_projects_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **projects_post** | [**ProjectsProjectsPost**](ProjectsProjectsPost.md)| Projects filter conditions | [optional] 

### Return type

[**list[ProjectsProjectResponse]**](ProjectsProjectResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_projects_status_post`
> list[DtoProjectStatusResponse] reports_api_v3_workspace_workspace_id_filters_projects_status_post(workspace_id, status_filter_params=status_filter_params)

List projects statuses

Returns filtered projects statuses from a workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
status_filter_params = toggl.DtoProjectStatusParamsRequest() # DtoProjectStatusParamsRequest | Projects statuses filter conditions (optional)

try:
    # List projects statuses
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_projects_status_post(workspace_id, status_filter_params=status_filter_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_projects_status_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **status_filter_params** | [**DtoProjectStatusParamsRequest**](DtoProjectStatusParamsRequest.md)| Projects statuses filter conditions | [optional] 

### Return type

[**list[DtoProjectStatusResponse]**](DtoProjectStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post`
> list[TasksTaskStatus] reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post(workspace_id, tasks_status_post)

List tasks statuses

Filter tasks statuses from a workspace

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
tasks_status_post = toggl.TasksTasksStatusPost() # TasksTasksStatusPost | Task filter conditions

try:
    # List tasks statuses
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post(workspace_id, tasks_status_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_tasks_auth_status_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **tasks_status_post** | [**TasksTasksStatusPost**](TasksTasksStatusPost.md)| Task filter conditions | 

### Return type

[**list[TasksTaskStatus]**](TasksTaskStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_tasks_status_post`
> list[TasksTaskStatus] reports_api_v3_workspace_workspace_id_filters_tasks_status_post(workspace_id, tasks_status_post)

List tasks statuses

Filter tasks statuses from a workspace

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
tasks_status_post = toggl.TasksTasksStatusPost() # TasksTasksStatusPost | Task filter conditions

try:
    # List tasks statuses
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_tasks_status_post(workspace_id, tasks_status_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_tasks_status_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **tasks_status_post** | [**TasksTasksStatusPost**](TasksTasksStatusPost.md)| Task filter conditions | 

### Return type

[**list[TasksTaskStatus]**](TasksTaskStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_filters_users_post`
> list[DtoUserFilterResponse] reports_api_v3_workspace_workspace_id_filters_users_post(workspace_id, users_filter=users_filter)

List users

Returns filtered users from a workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
users_filter = toggl.DtoUserFilterParamsRequest() # DtoUserFilterParamsRequest | Users filter conditions (optional)

try:
    # List users
    api_response = api_instance.reports_api_v3_workspace_workspace_id_filters_users_post(workspace_id, users_filter=users_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_filters_users_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **users_filter** | [**DtoUserFilterParamsRequest**](DtoUserFilterParamsRequest.md)| Users filter conditions | [optional] 

### Return type

[**list[DtoUserFilterResponse]**](DtoUserFilterResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_clients_post`
> list[object] reports_api_v3_workspace_workspace_id_search_clients_post(workspace_id, clients_post)

Search clients

Returns filtered clients from a workspace (whole client object).

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
clients_post = toggl.ClientsClientsPost() # ClientsClientsPost | Clients search conditions

try:
    # Search clients
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_clients_post(workspace_id, clients_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_search_clients_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **clients_post** | [**ClientsClientsPost**](ClientsClientsPost.md)| Clients search conditions | 

### Return type

**list[object]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_projects_post`
> list[object] reports_api_v3_workspace_workspace_id_search_projects_post(workspace_id, projects_post)

List projects

Returns filtered projects from a workspace (whole project object).

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
projects_post = toggl.ProjectsProjectsPost() # ProjectsProjectsPost | Projects list conditions

try:
    # List projects
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_projects_post(workspace_id, projects_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_search_projects_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **projects_post** | [**ProjectsProjectsPost**](ProjectsProjectsPost.md)| Projects list conditions | 

### Return type

**list[object]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_search_users_post`
> list[DtoUserFilterResponse] reports_api_v3_workspace_workspace_id_search_users_post(workspace_id, users_filter)

List users

Returns filtered users from a workspace.

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
api_instance = toggl.UtilsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
users_filter = toggl.DtoUserFilterParamsRequest() # DtoUserFilterParamsRequest | Users list conditions

try:
    # List users
    api_response = api_instance.reports_api_v3_workspace_workspace_id_search_users_post(workspace_id, users_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->reports_api_v3_workspace_workspace_id_search_users_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **users_filter** | [**DtoUserFilterParamsRequest**](DtoUserFilterParamsRequest.md)| Users list conditions | 

### Return type

[**list[DtoUserFilterResponse]**](DtoUserFilterResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

