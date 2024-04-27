# toggl.ApprovalsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_timesheet_setups**](ApprovalsApi.md#delete_timesheet_setups) | **DELETE** /workspaces/{workspace_id}/timesheet_setups/{setup_id} | Delete a timesheet setup
[**get_timesheet_setups**](ApprovalsApi.md#get_timesheet_setups) | **GET** /workspaces/{workspace_id}/timesheet_setups | Get timesheet setups
[**get_workspace_timesheet_hours_handler**](ApprovalsApi.md#get_workspace_timesheet_hours_handler) | **POST** /workspaces/{workspace_id}/timesheets/hours | Get timesheets hours
[**get_workspace_timesheet_time_entries_handler**](ApprovalsApi.md#get_workspace_timesheet_time_entries_handler) | **GET** /workspaces/{workspace_id}/timesheets/{setup_id}/{start_date} | Get timesheet time entries
[**get_workspace_timesheets_handler**](ApprovalsApi.md#get_workspace_timesheets_handler) | **GET** /workspaces/{workspace_id}/timesheets | Get timesheets
[**post_timesheet_setups**](ApprovalsApi.md#post_timesheet_setups) | **POST** /workspaces/{workspace_id}/timesheet_setups | Create a timesheet setup
[**put_timesheet_setups**](ApprovalsApi.md#put_timesheet_setups) | **POST** /workspaces/{workspace_id}/timesheet_setups/{setup_id} | Update a timesheet setup
[**put_workspace_timesheets_handler**](ApprovalsApi.md#put_workspace_timesheets_handler) | **PUT** /workspaces/{workspace_id}/timesheets/{setup_id}/{start_date} | Update timesheets


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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup

try:
    # Delete a timesheet setup
    api_response = api_instance.delete_timesheet_setups(workspace_id, setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->delete_timesheet_setups: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
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
    print("Exception when calling ApprovalsApi->get_timesheet_setups: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
payload = toggl.TimesheetsPostTimesheetHoursPayload() # TimesheetsPostTimesheetHoursPayload | Array of timesheet setup IDs and start dates.

try:
    # Get timesheets hours
    api_response = api_instance.get_workspace_timesheet_hours_handler(workspace_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->get_workspace_timesheet_hours_handler: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup.
start_date = 'start_date_example' # str | Start date (YYYY-MM-DD) of the timesheet.

try:
    # Get timesheet time entries
    api_response = api_instance.get_workspace_timesheet_time_entries_handler(workspace_id, setup_id, start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->get_workspace_timesheet_time_entries_handler: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
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
    print("Exception when calling ApprovalsApi->get_workspace_timesheets_handler: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
payload = toggl.TimesheetsetupsCreatePayload() # TimesheetsetupsCreatePayload | Arrays of setup creation parameters.

try:
    # Create a timesheet setup
    api_response = api_instance.post_timesheet_setups(workspace_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->post_timesheet_setups: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup
payload = toggl.TimesheetsetupsUpdatePayload() # TimesheetsetupsUpdatePayload | Setup update parameters.

try:
    # Update a timesheet setup
    api_response = api_instance.put_timesheet_setups(workspace_id, setup_id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->put_timesheet_setups: %s\n" % e)
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
api_instance = toggl.ApprovalsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
setup_id = 56 # int | Numeric ID of the timesheet setup.
start_date = 'start_date_example' # str | Start date (YYYY-MM-DD) of the timesheet.
payload = toggl.TimesheetsPutTimesheetPayload() # TimesheetsPutTimesheetPayload | Timesheet status and rejection comment.

try:
    # Update timesheets
    api_response = api_instance.put_workspace_timesheets_handler(workspace_id, setup_id, start_date, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->put_workspace_timesheets_handler: %s\n" % e)
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

