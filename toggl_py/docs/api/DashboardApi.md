# toggl.DashboardApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_all_activities**](DashboardApi.md#get_workspace_all_activities) | **GET** /workspaces/{workspace_id}/dashboard/all_activity | Get last activity for every workspace user
[**get_workspace_most_active**](DashboardApi.md#get_workspace_most_active) | **GET** /workspaces/{workspace_id}/dashboard/most_active | Get most active users
[**get_workspace_top_activity**](DashboardApi.md#get_workspace_top_activity) | **GET** /workspaces/{workspace_id}/dashboard/top_activity | Get top activities


## `get_workspace_all_activities`
> list[DashboardAllActivities] get_workspace_all_activities(workspace_id, since=since)

Get last activity for every workspace user

Dashboard's main purpose is to give an overview of what users in the workspace are doing and have been doing. The activity object holds the data of 20 latest actions in the workspace or latest activity for every workspace user. Activity object has the following properties * user_id: user ID * project_id: project ID (ID is 0 if time entry doesn't have project connected to it) * duration: time entry duration in seconds. If the time entry is currently running, the duration attribute contains a negative value, denoting the start of the time entry in seconds since epoch (Jan 1 1970). The correct duration can be calculated as current_time + duration, where current_time is the current time in seconds since epoch. * description: (Description property is not present if time entry description is empty) * stop: time entry stop time (ISO 8601 date and time. Stop property is not present when time entry is still running) * tid: task id, if applicable

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
api_instance = toggl.DashboardApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
since = 56 # int | Filter activities since this date using UNIX timestamp. (optional)

try:
    # Get last activity for every workspace user
    api_response = api_instance.get_workspace_all_activities(workspace_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_workspace_all_activities: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **since** | **int**| Filter activities since this date using UNIX timestamp. | [optional] 

### Return type

[**list[DashboardAllActivities]**](DashboardAllActivities.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_most_active`
> list[ModelsMostActiveUser] get_workspace_most_active(workspace_id, since=since)

Get most active users

Dashboard's main purpose is to give an overview of what users in the workspace are doing and have been doing. The most active user object holds the data of the top 5 users who have tracked the most time during last 7 days. Most active user object has the following properties * user_id: user ID * duration: Sum of time entry durations that have been created during last 7 days.

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
api_instance = toggl.DashboardApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
since = 56 # int | Filter activities since this date using UNIX timestamp. (optional)

try:
    # Get most active users
    api_response = api_instance.get_workspace_most_active(workspace_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_workspace_most_active: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **since** | **int**| Filter activities since this date using UNIX timestamp. | [optional] 

### Return type

[**list[ModelsMostActiveUser]**](ModelsMostActiveUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_top_activity`
> list[DashboardAllActivities] get_workspace_top_activity(workspace_id, since=since)

Get top activities

Dashboard's main purpose is to give an overview of what users in the workspace are doing and have been doing. Return objects are same as with the `/workspaces/{workspace_id}/dashboard/all_activity` request.

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
api_instance = toggl.DashboardApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
since = 56 # int | Filter activities since this date using UNIX timestamp. (optional)

try:
    # Get top activities
    api_response = api_instance.get_workspace_top_activity(workspace_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_workspace_top_activity: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **since** | **int**| Filter activities since this date using UNIX timestamp. | [optional] 

### Return type

[**list[DashboardAllActivities]**](DashboardAllActivities.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

