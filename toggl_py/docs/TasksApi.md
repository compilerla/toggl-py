# toggl.TasksApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_project_task**](TasksApi.md#delete_workspace_project_task) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id} | WorkspaceProjectTask
[**get_workspace_project_task**](TasksApi.md#get_workspace_project_task) | **GET** /workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id} | WorkspaceProjectTask
[**get_workspace_project_tasks**](TasksApi.md#get_workspace_project_tasks) | **GET** /workspaces/{workspace_id}/projects/{project_id}/tasks | WorkspaceProjectTasks
[**get_workspace_tasks**](TasksApi.md#get_workspace_tasks) | **GET** /workspaces/{workspace_id}/tasks | Tasks
[**patch_workspace_project_tasks**](TasksApi.md#patch_workspace_project_tasks) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/tasks/{task_ids} | WorkspaceProjectTasks
[**post_workspace_project_tasks**](TasksApi.md#post_workspace_project_tasks) | **POST** /workspaces/{workspace_id}/projects/{project_id}/tasks | WorkspaceProjectTasks
[**put_workspace_project_task**](TasksApi.md#put_workspace_project_task) | **PUT** /workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id} | WorkspaceProjectTask


## `delete_workspace_project_task`
> str delete_workspace_project_task(workspace_id, project_id, task_id)

WorkspaceProjectTask

Delete projects task for given workspace.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
task_id = 56 # int | Numeric ID of the task

try:
    # WorkspaceProjectTask
    api_response = api_instance.delete_workspace_project_task(workspace_id, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_workspace_project_task: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **task_id** | **int**| Numeric ID of the task | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_project_task`
> ModelsTask get_workspace_project_task(workspace_id, project_id, task_id)

WorkspaceProjectTask

Get project task for given task id.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
task_id = 56 # int | Numeric ID of the task

try:
    # WorkspaceProjectTask
    api_response = api_instance.get_workspace_project_task(workspace_id, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_workspace_project_task: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **task_id** | **int**| Numeric ID of the task | 

### Return type

[**ModelsTask**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_project_tasks`
> ModelsTask get_workspace_project_tasks(workspace_id, project_id)

WorkspaceProjectTasks

Get project tasks for given workspace.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project

try:
    # WorkspaceProjectTasks
    api_response = api_instance.get_workspace_project_tasks(workspace_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_workspace_project_tasks: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 

### Return type

[**ModelsTask**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_tasks`
> TaskResponse get_workspace_tasks(workspace_id, since=since, page=page, per_page=per_page, sort_order=sort_order, sort_field=sort_field, active=active, pid=pid, start_date=start_date, end_date=end_date)

Tasks

List Workspace tasks.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
since = 56 # int | Retrieve tasks created/modified/deleted since this date using UNIX timestamp. (optional)
page = 56 # int | Page number, default 1 (optional)
per_page = 56 # int | Number of items per page, default 50 (optional)
sort_order = 'sort_order_example' # str | Sort order, default ASC (optional)
sort_field = 'sort_field_example' # str | Field used for sorting (optional)
active = true # bool | Filter by active state (optional)
pid = 56 # int | Filter by project id (optional)
start_date = '2013-10-20' # date | Smallest boundary date in the format YYYY-MM-DD (optional)
end_date = '2013-10-20' # date | Biggest boundary date in the format YYYY-MM-DD (optional)

try:
    # Tasks
    api_response = api_instance.get_workspace_tasks(workspace_id, since=since, page=page, per_page=per_page, sort_order=sort_order, sort_field=sort_field, active=active, pid=pid, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_workspace_tasks: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **since** | **int**| Retrieve tasks created/modified/deleted since this date using UNIX timestamp. | [optional] 
 **page** | **int**| Page number, default 1 | [optional] 
 **per_page** | **int**| Number of items per page, default 50 | [optional] 
 **sort_order** | **str**| Sort order, default ASC | [optional] 
 **sort_field** | **str**| Field used for sorting | [optional] 
 **active** | **bool**| Filter by active state | [optional] 
 **pid** | **int**| Filter by project id | [optional] 
 **start_date** | **date**| Smallest boundary date in the format YYYY-MM-DD | [optional] 
 **end_date** | **date**| Biggest boundary date in the format YYYY-MM-DD | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_project_tasks`
> TaskPatchOutput patch_workspace_project_tasks(workspace_id, project_id, task_ids, patch_input)

WorkspaceProjectTasks

Patch project tasks for given workspace.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
task_ids = 'task_ids_example' # str | Numeric IDs of project tasks separated by comma
patch_input = [toggl.TaskPatchInput()] # list[TaskPatchInput] | Patch operations

try:
    # WorkspaceProjectTasks
    api_response = api_instance.patch_workspace_project_tasks(workspace_id, project_id, task_ids, patch_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->patch_workspace_project_tasks: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **task_ids** | **str**| Numeric IDs of project tasks separated by comma | 
 **patch_input** | [**list[TaskPatchInput]**](TaskPatchInput.md)| Patch operations | 

### Return type

[**TaskPatchOutput**](TaskPatchOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_project_tasks`
> ModelsTask post_workspace_project_tasks(workspace_id, project_id, post_input)

WorkspaceProjectTasks

Post project tasks for given workspace.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
post_input = toggl.TaskPayload() # TaskPayload | Post parameters

try:
    # WorkspaceProjectTasks
    api_response = api_instance.post_workspace_project_tasks(workspace_id, project_id, post_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_workspace_project_tasks: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **post_input** | [**TaskPayload**](TaskPayload.md)| Post parameters | 

### Return type

[**ModelsTask**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_project_task`
> ModelsTask put_workspace_project_task(workspace_id, project_id, task_id, patch_input)

WorkspaceProjectTask

Put project task for given workspace.

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
api_instance = toggl.TasksApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
project_id = 56 # int | Numeric ID of the project
task_id = 'task_id_example' # str | Numeric ID of project task
patch_input = toggl.TaskPayload() # TaskPayload | Put parameters

try:
    # WorkspaceProjectTask
    api_response = api_instance.put_workspace_project_task(workspace_id, project_id, task_id, patch_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_workspace_project_task: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **project_id** | **int**| Numeric ID of the project | 
 **task_id** | **str**| Numeric ID of project task | 
 **patch_input** | [**TaskPayload**](TaskPayload.md)| Put parameters | 

### Return type

[**ModelsTask**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

