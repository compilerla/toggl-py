# toggl.ClientsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_client**](ClientsApi.md#archive_client) | **POST** /workspaces/{workspace_id}/clients/{client_id}/archive | Archives client
[**delete_workspace_clients**](ClientsApi.md#delete_workspace_clients) | **DELETE** /workspaces/{workspace_id}/clients/{client_id} | Delete client
[**get_workspace_client**](ClientsApi.md#get_workspace_client) | **GET** /workspaces/{workspace_id}/clients/{client_id} | Load client from ID
[**get_workspace_clients**](ClientsApi.md#get_workspace_clients) | **GET** /workspaces/{workspace_id}/clients | List clients
[**post_workspace_clients**](ClientsApi.md#post_workspace_clients) | **POST** /workspaces/{workspace_id}/clients | Create client
[**put_workspace_clients**](ClientsApi.md#put_workspace_clients) | **PUT** /workspaces/{workspace_id}/clients/{client_id} | Change client
[**restore_client**](ClientsApi.md#restore_client) | **POST** /workspaces/{workspace_id}/clients/{client_id}/restore | Restores client and related projects.


## `archive_client`
> list[int] archive_client(workspace_id, client_id)

Archives client

Archives a workspace client and related projects. Only for premium workspaces.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
client_id = 56 # int | Numeric ID of the client

try:
    # Archives client
    api_response = api_instance.archive_client(workspace_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->archive_client: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **client_id** | **int**| Numeric ID of the client | 

### Return type

**list[int]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_clients`
> float delete_workspace_clients(workspace_id, client_id)

Delete client

Delete workspace client.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
client_id = 56 # int | Numeric ID of the client

try:
    # Delete client
    api_response = api_instance.delete_workspace_clients(workspace_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->delete_workspace_clients: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **client_id** | **int**| Numeric ID of the client | 

### Return type

**float**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_client`
> ModelsClient get_workspace_client(workspace_id, client_id)

Load client from ID

Load client from workspace.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
client_id = 56 # int | Numeric ID of the client

try:
    # Load client from ID
    api_response = api_instance.get_workspace_client(workspace_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_workspace_client: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **client_id** | **int**| Numeric ID of the client | 

### Return type

[**ModelsClient**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_clients`
> list[ModelsClient] get_workspace_clients(workspace_id, status=status, name=name)

List clients

List clients from workspace.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
status = 'status_example' # str | Use 'active' to only list active clients, 'archived' to only list archived clients and 'both' to retrieve active and archived clients. If not provided, only active clients are returned. (optional)
name = 'name_example' # str | If provided, allows to filter by client name in a case insensitive manner, returning all the ones that contain the given string. (optional)

try:
    # List clients
    api_response = api_instance.get_workspace_clients(workspace_id, status=status, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_workspace_clients: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **status** | **str**| Use &#39;active&#39; to only list active clients, &#39;archived&#39; to only list archived clients and &#39;both&#39; to retrieve active and archived clients. If not provided, only active clients are returned. | [optional] 
 **name** | **str**| If provided, allows to filter by client name in a case insensitive manner, returning all the ones that contain the given string. | [optional] 

### Return type

[**list[ModelsClient]**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_clients`
> ModelsClient post_workspace_clients(workspace_id, posted_client)

Create client

Create workspace client.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
posted_client = toggl.ClientPayload() # ClientPayload | Client

try:
    # Create client
    api_response = api_instance.post_workspace_clients(workspace_id, posted_client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->post_workspace_clients: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **posted_client** | [**ClientPayload**](ClientPayload.md)| Client | 

### Return type

[**ModelsClient**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_clients`
> ModelsClient put_workspace_clients(workspace_id, client_id, posted_client)

Change client

Update workspace client.  Note: use /workspaces/{workspace_id}/clients/{client_id}/archive to archive the client and /workspaces/{workspace_id}/clients/{client_id}/restore to restore it.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
client_id = 56 # int | Numeric ID of the client
posted_client = toggl.ClientPayload() # ClientPayload | Client

try:
    # Change client
    api_response = api_instance.put_workspace_clients(workspace_id, client_id, posted_client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->put_workspace_clients: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **client_id** | **int**| Numeric ID of the client | 
 **posted_client** | [**ClientPayload**](ClientPayload.md)| Client | 

### Return type

[**ModelsClient**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `restore_client`
> ModelsClient restore_client(workspace_id, client_id, restore_params=restore_params)

Restores client and related projects.

Restores client and all related or specified projects from the given workspace.

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
api_instance = toggl.ClientsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
client_id = 56 # int | Numeric ID of the client
restore_params = toggl.ProjectRestoreParams() # ProjectRestoreParams | Specify which projects should be restored with the client (optional)

try:
    # Restores client and related projects.
    api_response = api_instance.restore_client(workspace_id, client_id, restore_params=restore_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->restore_client: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **client_id** | **int**| Numeric ID of the client | 
 **restore_params** | [**ProjectRestoreParams**](ProjectRestoreParams.md)| Specify which projects should be restored with the client | [optional] 

### Return type

[**ModelsClient**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

