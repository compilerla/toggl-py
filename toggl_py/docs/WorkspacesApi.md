# toggl.WorkspacesApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alerts**](WorkspacesApi.md#delete_alerts) | **DELETE** /workspaces/{workspace_id}/alerts/{alert_id} | Alerts
[**delete_timesheet_setups**](WorkspacesApi.md#delete_timesheet_setups) | **DELETE** /workspaces/{workspace_id}/timesheet_setups/{setup_id} | Delete a timesheet setup
[**delete_workspace_track_reminder**](WorkspacesApi.md#delete_workspace_track_reminder) | **DELETE** /workspaces/{workspace_id}/track_reminders/{reminder_id} | TrackReminder
[**delete_workspace_user**](WorkspacesApi.md#delete_workspace_user) | **DELETE** /workspaces/{workspace_id}/workspace_users/{workspace_user_id} | Delete workspace user
[**get_organization_workspaces_groups**](WorkspacesApi.md#get_organization_workspaces_groups) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/groups | List of groups in a workspace within an organization with user assignments.
[**get_organization_workspaces_statistics**](WorkspacesApi.md#get_organization_workspaces_statistics) | **GET** /organizations/{organization_id}/workspaces/statistics | Statistics for all workspaces in the organization
[**get_organization_workspaces_workspaceusers**](WorkspacesApi.md#get_organization_workspaces_workspaceusers) | **GET** /organizations/{organization_id}/workspaces/{workspace_id}/workspace_users | List of users who belong to the given workspace.
[**get_timesheet_setups**](WorkspacesApi.md#get_timesheet_setups) | **GET** /workspaces/{workspace_id}/timesheet_setups | Get timesheet setups
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_id} | Get single workspace
[**get_workspace_statistics**](WorkspacesApi.md#get_workspace_statistics) | **GET** /workspaces/{workspace_id}/statistics | Workspace statistics
[**get_workspace_time_entry_constraints**](WorkspacesApi.md#get_workspace_time_entry_constraints) | **GET** /workspaces/{workspace_id}/time_entry_constraints | Get workspace time entry constraints
[**get_workspace_timesheet_hours_handler**](WorkspacesApi.md#get_workspace_timesheet_hours_handler) | **POST** /workspaces/{workspace_id}/timesheets/hours | Get timesheets hours
[**get_workspace_timesheet_time_entries_handler**](WorkspacesApi.md#get_workspace_timesheet_time_entries_handler) | **GET** /workspaces/{workspace_id}/timesheets/{setup_id}/{start_date} | Get timesheet time entries
[**get_workspace_timesheets_handler**](WorkspacesApi.md#get_workspace_timesheets_handler) | **GET** /workspaces/{workspace_id}/timesheets | Get timesheets
[**get_workspace_track_reminders**](WorkspacesApi.md#get_workspace_track_reminders) | **GET** /workspaces/{workspace_id}/track_reminders | TrackReminders
[**get_workspace_users**](WorkspacesApi.md#get_workspace_users) | **GET** /workspaces/{workspace_id}/users | Get workspace users
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /me/all_workspaces | Workspaces
[**get_workspaces_0**](WorkspacesApi.md#get_workspaces_0) | **GET** /me/workspaces | Workspaces
[**patch_organization_workspace_users**](WorkspacesApi.md#patch_organization_workspace_users) | **PATCH** /organizations/{organization_id}/workspaces/{workspace_id}/workspace_users | Changes the users in a workspace.
[**post_alerts**](WorkspacesApi.md#post_alerts) | **POST** /workspaces/{workspace_id}/alerts | Alerts
[**post_organization_workspaces**](WorkspacesApi.md#post_organization_workspaces) | **POST** /organizations/{organization_id}/workspaces | Create a new workspace.
[**post_timesheet_setups**](WorkspacesApi.md#post_timesheet_setups) | **POST** /workspaces/{workspace_id}/timesheet_setups | Create a timesheet setup
[**post_workspace_track_reminders**](WorkspacesApi.md#post_workspace_track_reminders) | **POST** /workspaces/{workspace_id}/track_reminders | TrackReminders
[**post_workspace_users_lost_password**](WorkspacesApi.md#post_workspace_users_lost_password) | **POST** /workspaces/{workspace_id}/users/{user_id}/lost_password | Change a lost password
[**post_workspaces**](WorkspacesApi.md#post_workspaces) | **POST** /workspaces | Workspaces
[**put_organization_workspaces_assignments**](WorkspacesApi.md#put_organization_workspaces_assignments) | **PUT** /organizations/{organization_id}/workspaces/{workspace_id}/assignments | Change assignments of users within a workspace.
[**put_timesheet_setups**](WorkspacesApi.md#put_timesheet_setups) | **POST** /workspaces/{workspace_id}/timesheet_setups/{setup_id} | Update a timesheet setup
[**put_workspace_timesheets_handler**](WorkspacesApi.md#put_workspace_timesheets_handler) | **PUT** /workspaces/{workspace_id}/timesheets/{setup_id}/{start_date} | Update timesheets
[**put_workspace_track_reminder**](WorkspacesApi.md#put_workspace_track_reminder) | **PUT** /workspaces/{workspace_id}/track_reminders/{reminder_id} | TrackReminder
[**put_workspace_users**](WorkspacesApi.md#put_workspace_users) | **PUT** /workspaces/{workspace_id}/users/{user_id} | Update workspace user
[**put_workspace_workspace_users**](WorkspacesApi.md#put_workspace_workspace_users) | **PUT** /workspaces/{workspace_id}/workspace_users/{workspace_user_id} | Update workspace-user
[**put_workspaces**](WorkspacesApi.md#put_workspaces) | **PUT** /workspaces/{workspace_id} | Update workspace


## `delete_alerts`
> str delete_alerts()

Alerts

Handles DELETE alert requests.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))

try:
    # Alerts
    api_response = api_instance.delete_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_alerts: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_timesheet_setups`
> str delete_timesheet_setups(workspace_id, setup_id)

Delete a timesheet setup

Delete a timesheet setup for a given workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup

try:
    # Delete a timesheet setup
    api_response = api_instance.delete_timesheet_setups(workspace_id, setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_timesheet_setups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **setup_id** | **int**| Numeric ID of the timesheet setup | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_track_reminder`
> str delete_workspace_track_reminder(workspace_id, reminder_id)

TrackReminder

Deletes a workspace tracking reminder.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
reminder_id = 56 # int | Reminder ID.

try:
    # TrackReminder
    api_response = api_instance.delete_workspace_track_reminder(workspace_id, reminder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace_track_reminder: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **reminder_id** | **int**| Reminder ID. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.WorkspacesApi()
workspace_id = 56 # int | Numeric ID of the workspace.
workspace_user_id = 56 # int | Numeric ID of the workspace user.

try:
    # Delete workspace user
    api_instance.delete_workspace_user(workspace_id, workspace_user_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace_user: %s\n" % e)
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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization

try:
    # List of groups in a workspace within an organization with user assignments.
    api_response = api_instance.get_organization_workspaces_groups(organization_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_organization_workspaces_groups: %s\n" % e)
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

## `get_organization_workspaces_statistics`
> dict(str, ModelsStatistics) get_organization_workspaces_statistics()

Statistics for all workspaces in the organization

Returns map indexed by workspace ID where each map element contains workspace admins list, members count and groups count.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))

try:
    # Statistics for all workspaces in the organization
    api_response = api_instance.get_organization_workspaces_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_organization_workspaces_statistics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**dict(str, ModelsStatistics)**](ModelsStatistics.md)

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
name = 'name_example' # str | Workspace user name to filter by

try:
    # List of users who belong to the given workspace.
    api_response = api_instance.get_organization_workspaces_workspaceusers(organization_id, workspace_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_organization_workspaces_workspaceusers: %s\n" % e)
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

## `get_timesheet_setups`
> TimesheetsetupsGetPaginatedResponse get_timesheet_setups(workspace_id, member_ids=member_ids, approver_ids=approver_ids, sort_field=sort_field, sort_order=sort_order)

Get timesheet setups

Get timesheet setups for a given workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
member_ids = 56 # int | Numeric ID of the members, comma-separated (optional)
approver_ids = 56 # int | Numeric ID of the approvers, comma-separated (optional)
sort_field = 'sort_field_example' # str | Field used for sorting, default start_date. (optional)
sort_order = 'sort_order_example' # str | Sort order. (optional)

try:
    # Get timesheet setups
    api_response = api_instance.get_timesheet_setups(workspace_id, member_ids=member_ids, approver_ids=approver_ids, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_timesheet_setups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **member_ids** | **int**| Numeric ID of the members, comma-separated | [optional] 
 **approver_ids** | **int**| Numeric ID of the approvers, comma-separated | [optional] 
 **sort_field** | **str**| Field used for sorting, default start_date. | [optional] 
 **sort_order** | **str**| Sort order. | [optional] 

### Return type

[**TimesheetsetupsGetPaginatedResponse**](TimesheetsetupsGetPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace`
> WorkspaceWorkspace get_workspace(workspace_id)

Get single workspace

Get information of single workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric Workspace ID

try:
    # Get single workspace
    api_response = api_instance.get_workspace(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric Workspace ID | 

### Return type

[**WorkspaceWorkspace**](WorkspaceWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_statistics`
> ModelsStatistics get_workspace_statistics()

Workspace statistics

Returns workspace admins list, members count and groups count

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))

try:
    # Workspace statistics
    api_response = api_instance.get_workspace_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_statistics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsStatistics**](ModelsStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_time_entry_constraints`
> ModelsTimeEntryConstraints get_workspace_time_entry_constraints(workspace_id)

Get workspace time entry constraints

Get the time entry constraints for a given workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace time entry constraints
    api_response = api_instance.get_workspace_time_entry_constraints(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_time_entry_constraints: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsTimeEntryConstraints**](ModelsTimeEntryConstraints.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_timesheet_hours_handler`
> list[TimesheetsTimesheetHoursResponse] get_workspace_timesheet_hours_handler(workspace_id, payload)

Get timesheets hours

Get timesheet working hours and total tracked seconds.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
payload = toggl.TimesheetsPostTimesheetHoursPayload() # TimesheetsPostTimesheetHoursPayload | Array of timesheet setup IDs and start dates.

try:
    # Get timesheets hours
    api_response = api_instance.get_workspace_timesheet_hours_handler(workspace_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_timesheet_hours_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **payload** | [**TimesheetsPostTimesheetHoursPayload**](TimesheetsPostTimesheetHoursPayload.md)| Array of timesheet setup IDs and start dates. | 

### Return type

[**list[TimesheetsTimesheetHoursResponse]**](TimesheetsTimesheetHoursResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_timesheet_time_entries_handler`
> list[ModelsTimeEntry] get_workspace_timesheet_time_entries_handler(workspace_id, setup_id, start_date)

Get timesheet time entries

Get the time entries from within a timesheet timeframe.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup.
start_date = 'start_date_example' # str | Start date (YYYY-MM-DD) of the timesheet.

try:
    # Get timesheet time entries
    api_response = api_instance.get_workspace_timesheet_time_entries_handler(workspace_id, setup_id, start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_timesheet_time_entries_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **setup_id** | **int**| Numeric ID of the timesheet setup. | 
 **start_date** | **str**| Start date (YYYY-MM-DD) of the timesheet. | 

### Return type

[**list[ModelsTimeEntry]**](ModelsTimeEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_timesheets_handler`
> list[TimesheetsGetPaginatedResponse] get_workspace_timesheets_handler(workspace_id, member_ids=member_ids, approver_ids=approver_ids, timesheet_setup_ids=timesheet_setup_ids, statuses=statuses, before=before, after=after, page=page, per_page=per_page, sort_field=sort_field, sort_order=sort_order)

Get timesheets

Get timesheets applying various filters.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
member_ids = 56 # int | Numeric ID of the members, comma-separated (optional)
approver_ids = 56 # int | Numeric ID of the approvers, comma-separated (optional)
timesheet_setup_ids = 56 # int | Numeric ID for timesheet setup, comma-separated. (optional)
statuses = 56 # int | Timesheet status, comma-separated. (optional)
before = 56 # int | Timesheets starting before this date (YYYY-MM-DD). (optional)
after = 56 # int | Timesheets starting after this date (YYYY-MM-DD). (optional)
page = 56 # int | Page number, default 1. (optional)
per_page = 56 # int | Number of items per page, default 20. Also defaults to 20 if provided an greater than 1000. (optional)
sort_field = 'sort_field_example' # str | Field used for sorting, default start_date. (optional)
sort_order = 'sort_order_example' # str | Sort order. (optional)

try:
    # Get timesheets
    api_response = api_instance.get_workspace_timesheets_handler(workspace_id, member_ids=member_ids, approver_ids=approver_ids, timesheet_setup_ids=timesheet_setup_ids, statuses=statuses, before=before, after=after, page=page, per_page=per_page, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_timesheets_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **member_ids** | **int**| Numeric ID of the members, comma-separated | [optional] 
 **approver_ids** | **int**| Numeric ID of the approvers, comma-separated | [optional] 
 **timesheet_setup_ids** | **int**| Numeric ID for timesheet setup, comma-separated. | [optional] 
 **statuses** | **int**| Timesheet status, comma-separated. | [optional] 
 **before** | **int**| Timesheets starting before this date (YYYY-MM-DD). | [optional] 
 **after** | **int**| Timesheets starting after this date (YYYY-MM-DD). | [optional] 
 **page** | **int**| Page number, default 1. | [optional] 
 **per_page** | **int**| Number of items per page, default 20. Also defaults to 20 if provided an greater than 1000. | [optional] 
 **sort_field** | **str**| Field used for sorting, default start_date. | [optional] 
 **sort_order** | **str**| Sort order. | [optional] 

### Return type

[**list[TimesheetsGetPaginatedResponse]**](TimesheetsGetPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_track_reminders`
> list[ModelsTrackReminder] get_workspace_track_reminders(workspace_id)

TrackReminders

Returns a list of track reminders.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # TrackReminders
    api_response = api_instance.get_workspace_track_reminders(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_track_reminders: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsTrackReminder]**](ModelsTrackReminder.md)

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace users
    api_response = api_instance.get_workspace_users(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_users: %s\n" % e)
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

## `get_workspaces`
> list[WorkspaceWithActiveProjectCount] get_workspaces(since=since)

Workspaces

Lists workspaces for given user, including all workspaces in an organization for an adminj.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve workspaces created/modified/deleted since this date using UNIX timestamp, including the dates a workspace member got added, removed or updated in the workspace. (optional)

try:
    # Workspaces
    api_response = api_instance.get_workspaces(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve workspaces created/modified/deleted since this date using UNIX timestamp, including the dates a workspace member got added, removed or updated in the workspace. | [optional] 

### Return type

[**list[WorkspaceWithActiveProjectCount]**](WorkspaceWithActiveProjectCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspaces_0`
> list[WorkspaceWorkspace] get_workspaces_0(since=since)

Workspaces

Lists workspaces for given user.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve workspaces created/modified/deleted since this date using UNIX timestamp, including the dates a workspace member got added, removed or updated in the workspace. (optional)

try:
    # Workspaces
    api_response = api_instance.get_workspaces_0(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces_0: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve workspaces created/modified/deleted since this date using UNIX timestamp, including the dates a workspace member got added, removed or updated in the workspace. | [optional] 

### Return type

[**list[WorkspaceWorkspace]**](WorkspaceWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace
params = toggl.WorkspaceUsersPatchParams() # WorkspaceUsersPatchParams | Input data of the users to be patched.

try:
    # Changes the users in a workspace.
    api_response = api_instance.patch_organization_workspace_users(organization_id, workspace_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->patch_organization_workspace_users: %s\n" % e)
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

## `post_alerts`
> ModelsAlert post_alerts(request)

Alerts

Handles POST alert requests.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
request = NULL # object | Alert data

try:
    # Alerts
    api_response = api_instance.post_alerts(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_alerts: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**object**](.md)| Alert data | 

### Return type

[**ModelsAlert**](ModelsAlert.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_workspaces`
> WorkspaceWorkspace post_organization_workspaces(organization_id, post)

Create a new workspace.

Create a workspace within an existing organization.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
post = toggl.WorkspacePayload() # WorkspacePayload | Parameters of the new workspace

try:
    # Create a new workspace.
    api_response = api_instance.post_organization_workspaces(organization_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_organization_workspaces: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **post** | [**WorkspacePayload**](WorkspacePayload.md)| Parameters of the new workspace | 

### Return type

[**WorkspaceWorkspace**](WorkspaceWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_timesheet_setups`
> list[TimesheetsetupsAPITimesheetSetup] post_timesheet_setups(workspace_id, payload)

Create a timesheet setup

Create timesheet setups.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
payload = toggl.TimesheetsetupsCreatePayload() # TimesheetsetupsCreatePayload | Arrays of setup creation parameters.

try:
    # Create a timesheet setup
    api_response = api_instance.post_timesheet_setups(workspace_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_timesheet_setups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **payload** | [**TimesheetsetupsCreatePayload**](TimesheetsetupsCreatePayload.md)| Arrays of setup creation parameters. | 

### Return type

[**list[TimesheetsetupsAPITimesheetSetup]**](TimesheetsetupsAPITimesheetSetup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_track_reminders`
> ModelsTrackReminder post_workspace_track_reminders(workspace_id, track_reminder_post)

TrackReminders

Creates a workspace tracking reminder.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
track_reminder_post = toggl.RemindersPayload() # RemindersPayload | Reminder parameters.

try:
    # TrackReminders
    api_response = api_instance.post_workspace_track_reminders(workspace_id, track_reminder_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_workspace_track_reminders: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **track_reminder_post** | [**RemindersPayload**](RemindersPayload.md)| Reminder parameters. | 

### Return type

[**ModelsTrackReminder**](ModelsTrackReminder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
user_id = 56 # int | Numeric ID of the user

try:
    # Change a lost password
    api_response = api_instance.post_workspace_users_lost_password(workspace_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_workspace_users_lost_password: %s\n" % e)
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

## `post_workspaces`
> WorkspaceWorkspace post_workspaces(post)

Workspaces

Change a workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
post = toggl.WorkspacePayload() # WorkspacePayload | Change parameters

try:
    # Workspaces
    api_response = api_instance.post_workspaces(post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_workspaces: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | [**WorkspacePayload**](WorkspacePayload.md)| Change parameters | 

### Return type

[**WorkspaceWorkspace**](WorkspaceWorkspace.md)

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
workspace_id = 56 # int | Numeric ID of the workspace within the organization
post = toggl.UserAssignmentsPayload() # UserAssignmentsPayload | Describes the change in assignment

try:
    # Change assignments of users within a workspace.
    api_response = api_instance.put_organization_workspaces_assignments(organization_id, workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_organization_workspaces_assignments: %s\n" % e)
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

## `put_timesheet_setups`
> TimesheetsetupsAPITimesheetSetup put_timesheet_setups(workspace_id, setup_id, payload)

Update a timesheet setup

Updates a timesheet setups.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup
payload = toggl.TimesheetsetupsUpdatePayload() # TimesheetsetupsUpdatePayload | Setup update parameters.

try:
    # Update a timesheet setup
    api_response = api_instance.put_timesheet_setups(workspace_id, setup_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_timesheet_setups: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **setup_id** | **int**| Numeric ID of the timesheet setup | 
 **payload** | [**TimesheetsetupsUpdatePayload**](TimesheetsetupsUpdatePayload.md)| Setup update parameters. | 

### Return type

[**TimesheetsetupsAPITimesheetSetup**](TimesheetsetupsAPITimesheetSetup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_timesheets_handler`
> TimesheetsAPITimesheet put_workspace_timesheets_handler(workspace_id, setup_id, start_date, payload)

Update timesheets

Updates a timesheet.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup.
start_date = 'start_date_example' # str | Start date (YYYY-MM-DD) of the timesheet.
payload = toggl.TimesheetsPutTimesheetPayload() # TimesheetsPutTimesheetPayload | Timesheet status and rejection comment.

try:
    # Update timesheets
    api_response = api_instance.put_workspace_timesheets_handler(workspace_id, setup_id, start_date, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspace_timesheets_handler: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **setup_id** | **int**| Numeric ID of the timesheet setup. | 
 **start_date** | **str**| Start date (YYYY-MM-DD) of the timesheet. | 
 **payload** | [**TimesheetsPutTimesheetPayload**](TimesheetsPutTimesheetPayload.md)| Timesheet status and rejection comment. | 

### Return type

[**TimesheetsAPITimesheet**](TimesheetsAPITimesheet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_track_reminder`
> ModelsTrackReminder put_workspace_track_reminder(workspace_id, reminder_id, track_reminder_post)

TrackReminder

Updates a workspace tracking reminder.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
reminder_id = 56 # int | Reminder ID.
track_reminder_post = toggl.RemindersPayload() # RemindersPayload | Reminder parameters.

try:
    # TrackReminder
    api_response = api_instance.put_workspace_track_reminder(workspace_id, reminder_id, track_reminder_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspace_track_reminder: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **reminder_id** | **int**| Reminder ID. | 
 **track_reminder_post** | [**RemindersPayload**](RemindersPayload.md)| Reminder parameters. | 

### Return type

[**ModelsTrackReminder**](ModelsTrackReminder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
user_id = 56 # int | Numeric ID of the user

try:
    # Update workspace user
    api_response = api_instance.put_workspace_users(workspace_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspace_users: %s\n" % e)
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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
workspace_user_id = 56 # int | Numeric ID of the workspace user
post = toggl.UserPayload() # UserPayload | Changes that need to be applied to the user data.

try:
    # Update workspace-user
    api_response = api_instance.put_workspace_workspace_users(workspace_id, workspace_user_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspace_workspace_users: %s\n" % e)
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

## `put_workspaces`
> WorkspaceWorkspace put_workspaces(workspace_id, post)

Update workspace

Update a specific workspace.

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
api_instance = toggl.WorkspacesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric Workspace ID
post = toggl.WorkspacePayload() # WorkspacePayload | Workspace parameters

try:
    # Update workspace
    api_response = api_instance.put_workspaces(workspace_id, post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspaces: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric Workspace ID | 
 **post** | [**WorkspacePayload**](WorkspacePayload.md)| Workspace parameters | 

### Return type

[**WorkspaceWorkspace**](WorkspaceWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

