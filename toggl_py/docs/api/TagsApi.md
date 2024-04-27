# toggl.TagsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_tag**](TagsApi.md#delete_workspace_tag) | **DELETE** /workspaces/{workspace_id}/tags/{tag_id} | Delete tag
[**get_workspace_tag**](TagsApi.md#get_workspace_tag) | **GET** /workspaces/{workspace_id}/tags | Tags
[**patch_workspace_tags**](TagsApi.md#patch_workspace_tags) | **PATCH** /workspaces/{workspace_id}/tags | Bulk delete tags
[**post_workspace_tag**](TagsApi.md#post_workspace_tag) | **POST** /workspaces/{workspace_id}/tags | Create tag
[**put_workspace_tag**](TagsApi.md#put_workspace_tag) | **PUT** /workspaces/{workspace_id}/tags/{tag_id} | Update tag


## `delete_workspace_tag`
> str delete_workspace_tag(workspace_id, tag_id)

Delete tag

Delete workspace tags.

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
api_instance = toggl.TagsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
tag_id = 56 # int | Numeric ID of the tag

try:
    # Delete tag
    api_response = api_instance.delete_workspace_tag(workspace_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->delete_workspace_tag: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **tag_id** | **int**| Numeric ID of the tag | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_tag`
> list[ModelsTag] get_workspace_tag(workspace_id)

Tags

List Workspace tags.

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
api_instance = toggl.TagsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Tags
    api_response = api_instance.get_workspace_tag(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_workspace_tag: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsTag]**](ModelsTag.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_tags`
> str patch_workspace_tags(workspace_id)

Bulk delete tags

Patch will not be executed if there are errors with some records.

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
api_instance = toggl.TagsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Bulk delete tags
    api_response = api_instance.patch_workspace_tags(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->patch_workspace_tags: %s\n" % e)
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

## `post_workspace_tag`
> list[ModelsTag] post_workspace_tag(workspace_id, tag_post)

Create tag

Create workspace tags.

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
api_instance = toggl.TagsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
tag_post = toggl.TagsPayload() # TagsPayload | Post data

try:
    # Create tag
    api_response = api_instance.post_workspace_tag(workspace_id, tag_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->post_workspace_tag: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **tag_post** | [**TagsPayload**](TagsPayload.md)| Post data | 

### Return type

[**list[ModelsTag]**](ModelsTag.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_tag`
> list[ModelsTag] put_workspace_tag(workspace_id, tag_id, tag_post)

Update tag

Update workspace tags.

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
api_instance = toggl.TagsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
tag_id = 56 # int | Numeric ID of the tag
tag_post = toggl.TagsPayload() # TagsPayload | Put data

try:
    # Update tag
    api_response = api_instance.put_workspace_tag(workspace_id, tag_id, tag_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->put_workspace_tag: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **tag_id** | **int**| Numeric ID of the tag | 
 **tag_post** | [**TagsPayload**](TagsPayload.md)| Put data | 

### Return type

[**list[ModelsTag]**](ModelsTag.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

