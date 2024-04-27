# toggl.TimeEntriesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_time_entries**](TimeEntriesApi.md#delete_workspace_time_entries) | **DELETE** /workspaces/{workspace_id}/time_entries/{time_entry_id} | TimeEntries
[**get_current_time_entry**](TimeEntriesApi.md#get_current_time_entry) | **GET** /me/time_entries/current | Get current time entry
[**get_time_entries**](TimeEntriesApi.md#get_time_entries) | **GET** /me/time_entries | TimeEntries
[**get_time_entry_by_id**](TimeEntriesApi.md#get_time_entry_by_id) | **GET** /me/time_entries/{time_entry_id} | Get a time entry by ID.
[**get_time_notes_entry_notes_by_id**](TimeEntriesApi.md#get_time_notes_entry_notes_by_id) | **GET** /me/time_entries/{time_entry_id}/notes | Get a time entries&#39; notes by ID.
[**get_workspace_time_entry_invitations**](TimeEntriesApi.md#get_workspace_time_entry_invitations) | **GET** /workspaces/{workspace_id}/time_entry_invitations | TimeEntries
[**patch_time_entries**](TimeEntriesApi.md#patch_time_entries) | **PATCH** /workspaces/{workspace_id}/time_entries/{time_entry_ids} | Bulk editing time entries
[**patch_workspace_stop_time_entry_handler**](TimeEntriesApi.md#patch_workspace_stop_time_entry_handler) | **PATCH** /workspaces/{workspace_id}/time_entries/{time_entry_id}/stop | Stop TimeEntry
[**post_workspace_time_entries**](TimeEntriesApi.md#post_workspace_time_entries) | **POST** /workspaces/{workspace_id}/time_entries | TimeEntries
[**post_workspace_time_entry_invitation_action**](TimeEntriesApi.md#post_workspace_time_entry_invitation_action) | **POST** /workspaces/{workspace_id}/time_entry_invitations/{time_entry_invitation_id}/{action} | TimeEntries
[**put_time_entry_notes_by_id**](TimeEntriesApi.md#put_time_entry_notes_by_id) | **PUT** /me/time_entries/{time_entry_id}/notes | Put a time entry notes by ID.
[**put_workspace_time_entry_handler**](TimeEntriesApi.md#put_workspace_time_entry_handler) | **PUT** /workspaces/{workspace_id}/time_entries/{time_entry_id} | TimeEntries


## `delete_workspace_time_entries`
> str delete_workspace_time_entries(workspace_id, time_entry_id)

TimeEntries

Deletes a workspace time entry.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_id = 56 # int | TimeEntry ID.

try:
    # TimeEntries
    api_response = api_instance.delete_workspace_time_entries(workspace_id, time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->delete_workspace_time_entries: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_id** | **int**| TimeEntry ID. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_current_time_entry`
> ModelsTimeEntry get_current_time_entry()

Get current time entry

Load running time entry for user ID.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))

try:
    # Get current time entry
    api_response = api_instance.get_current_time_entry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->get_current_time_entry: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsTimeEntry**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_time_entries`
> list[ModelsTimeEntry] get_time_entries(since=since, before=before, start_date=start_date, end_date=end_date, meta=meta, include_sharing=include_sharing)

TimeEntries

Lists latest time entries.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
since = 56 # int | Get entries modified since this date using UNIX timestamp, including deleted ones. (optional)
before = 'before_example' # str | Get entries with start time, before given date (YYYY-MM-DD) or with time in RFC3339 format. (optional)
start_date = 'start_date_example' # str | Get entries with start time, from start_date YYYY-MM-DD or with time in RFC3339 format. To be used with end_date. (optional)
end_date = 'end_date_example' # str | Get entries with start time, until end_date YYYY-MM-DD or with time in RFC3339 format. To be used with start_date. (optional)
meta = true # bool | Should the response contain data for meta entities (optional)
include_sharing = true # bool | Include sharing details in the response (optional)

try:
    # TimeEntries
    api_response = api_instance.get_time_entries(since=since, before=before, start_date=start_date, end_date=end_date, meta=meta, include_sharing=include_sharing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->get_time_entries: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Get entries modified since this date using UNIX timestamp, including deleted ones. | [optional] 
 **before** | **str**| Get entries with start time, before given date (YYYY-MM-DD) or with time in RFC3339 format. | [optional] 
 **start_date** | **str**| Get entries with start time, from start_date YYYY-MM-DD or with time in RFC3339 format. To be used with end_date. | [optional] 
 **end_date** | **str**| Get entries with start time, until end_date YYYY-MM-DD or with time in RFC3339 format. To be used with start_date. | [optional] 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 
 **include_sharing** | **bool**| Include sharing details in the response | [optional] 

### Return type

[**list[ModelsTimeEntry]**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_time_entry_by_id`
> ModelsTimeEntry get_time_entry_by_id(time_entry_id, meta=meta, include_sharing=include_sharing)

Get a time entry by ID.

Load time entry by ID that is accessible by the current user.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
time_entry_id = 56 # int | TimeEntry ID.
meta = true # bool | Should the response contain data for meta entities (optional)
include_sharing = true # bool | Include sharing details in the response (optional)

try:
    # Get a time entry by ID.
    api_response = api_instance.get_time_entry_by_id(time_entry_id, meta=meta, include_sharing=include_sharing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->get_time_entry_by_id: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **int**| TimeEntry ID. | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 
 **include_sharing** | **bool**| Include sharing details in the response | [optional] 

### Return type

[**ModelsTimeEntry**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_time_notes_entry_notes_by_id`
> ModelsTimeEntryNotes get_time_notes_entry_notes_by_id(time_entry_id)

Get a time entries' notes by ID.

Load time entry by ID that is accessible by the current user.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
time_entry_id = 56 # int | TimeEntry ID.

try:
    # Get a time entries' notes by ID.
    api_response = api_instance.get_time_notes_entry_notes_by_id(time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->get_time_notes_entry_notes_by_id: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **int**| TimeEntry ID. | 

### Return type

[**ModelsTimeEntryNotes**](ModelsTimeEntryNotes.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_time_entry_invitations`
> list[TimeentriesGetTimEntryInvitationsResponse] get_workspace_time_entry_invitations(workspace_id)

TimeEntries

Get invitations for time entries

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # TimeEntries
    api_response = api_instance.get_workspace_time_entry_invitations(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->get_workspace_time_entry_invitations: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[TimeentriesGetTimEntryInvitationsResponse]**](TimeentriesGetTimEntryInvitationsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_time_entries`
> TimeentryPatchOutput patch_time_entries(workspace_id, time_entry_ids, patch_input, meta=meta)

Bulk editing time entries

In short: http://tools.ietf.org/html/rfc6902 and http://tools.ietf.org/html/rfc6901 with some additions. Patch will be executed partially when there are errors with some records. No transaction, no rollback.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_ids = 'time_entry_ids_example' # str | Numeric IDs of time_entries, separated by comma. E.g.: `204301830,202700150,202687559`. The limit is 100 IDs per request.
patch_input = toggl.TimeentriesPatchPost() # TimeentriesPatchPost | Array of batch operations
meta = true # bool | Should the response contain data for meta entities (optional)

try:
    # Bulk editing time entries
    api_response = api_instance.patch_time_entries(workspace_id, time_entry_ids, patch_input, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->patch_time_entries: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_ids** | **str**| Numeric IDs of time_entries, separated by comma. E.g.: &#x60;204301830,202700150,202687559&#x60;. The limit is 100 IDs per request. | 
 **patch_input** | [**TimeentriesPatchPost**](TimeentriesPatchPost.md)| Array of batch operations | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 

### Return type

[**TimeentryPatchOutput**](TimeentryPatchOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_stop_time_entry_handler`
> ModelsTimeEntry patch_workspace_stop_time_entry_handler(workspace_id, time_entry_id)

Stop TimeEntry

Stops a workspace time entry.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_id = 56 # int | TimeEntry ID.

try:
    # Stop TimeEntry
    api_response = api_instance.patch_workspace_stop_time_entry_handler(workspace_id, time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->patch_workspace_stop_time_entry_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_id** | **int**| TimeEntry ID. | 

### Return type

[**ModelsTimeEntry**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_time_entries`
> ModelsTimeEntry post_workspace_time_entries(workspace_id, workspace_time_entry_post, meta=meta)

TimeEntries

Creates a new workspace TimeEntry.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
workspace_time_entry_post = toggl.TimeentryPayload() # TimeentryPayload | TimeEntry parameters.
meta = true # bool | Should the response contain data for meta entities (optional)

try:
    # TimeEntries
    api_response = api_instance.post_workspace_time_entries(workspace_id, workspace_time_entry_post, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->post_workspace_time_entries: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **workspace_time_entry_post** | [**TimeentryPayload**](TimeentryPayload.md)| TimeEntry parameters. | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 

### Return type

[**ModelsTimeEntry**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_time_entry_invitation_action`
> str post_workspace_time_entry_invitation_action(workspace_id, time_entry_invitation_id)

TimeEntries

Accept or reject an invitation for a time entry

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_invitation_id = 56 # int | Numeric ID of the time entry invitation

try:
    # TimeEntries
    api_response = api_instance.post_workspace_time_entry_invitation_action(workspace_id, time_entry_invitation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->post_workspace_time_entry_invitation_action: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_invitation_id** | **int**| Numeric ID of the time entry invitation | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_time_entry_notes_by_id`
> ModelsTimeEntryNotes put_time_entry_notes_by_id(time_entry_id)

Put a time entry notes by ID.

Load time entry notes by ID that is accessible by the current user.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
time_entry_id = 56 # int | TimeEntry ID.

try:
    # Put a time entry notes by ID.
    api_response = api_instance.put_time_entry_notes_by_id(time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->put_time_entry_notes_by_id: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **int**| TimeEntry ID. | 

### Return type

[**ModelsTimeEntryNotes**](ModelsTimeEntryNotes.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_time_entry_handler`
> ModelsTimeEntry put_workspace_time_entry_handler(workspace_id, time_entry_id, workspace_time_entry_post, meta=meta, include_sharing=include_sharing)

TimeEntries

Updates a workspace time entry.

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
api_instance = toggl.TimeEntriesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
time_entry_id = 56 # int | TimeEntry ID.
workspace_time_entry_post = toggl.TimeentryPayload() # TimeentryPayload | TimeEntry parameters.
meta = true # bool | Should the response contain data for meta entities (optional)
include_sharing = true # bool | Should the response contain time entry sharing details (optional)

try:
    # TimeEntries
    api_response = api_instance.put_workspace_time_entry_handler(workspace_id, time_entry_id, workspace_time_entry_post, meta=meta, include_sharing=include_sharing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesApi->put_workspace_time_entry_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **time_entry_id** | **int**| TimeEntry ID. | 
 **workspace_time_entry_post** | [**TimeentryPayload**](TimeentryPayload.md)| TimeEntry parameters. | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 
 **include_sharing** | **bool**| Should the response contain time entry sharing details | [optional] 

### Return type

[**ModelsTimeEntry**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

