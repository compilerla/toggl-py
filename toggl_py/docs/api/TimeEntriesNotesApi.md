# toggl.TimeEntriesNotesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_entry_notes_by_id**](TimeEntriesNotesApi.md#delete_time_entry_notes_by_id) | **DELETE** /me/time_entries/{time_entry_id}/notes | delete a time entry note by ID.


## `delete_time_entry_notes_by_id`
> str delete_time_entry_notes_by_id(time_entry_id)

delete a time entry note by ID.

Delete time entry notes by ID that is accessible by the current user.

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
api_instance = toggl.TimeEntriesNotesApi(toggl.ApiClient(configuration))
time_entry_id = 56 # int | TimeEntry ID.

try:
    # delete a time entry note by ID.
    api_response = api_instance.delete_time_entry_notes_by_id(time_entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeEntriesNotesApi->delete_time_entry_notes_by_id: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **int**| TimeEntry ID. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

