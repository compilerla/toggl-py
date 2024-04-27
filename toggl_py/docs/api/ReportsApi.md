# toggl.ReportsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_saved_report_resource**](ReportsApi.md#delete_saved_report_resource) | **DELETE** /workspaces/{workspace_id}/reports/shared/{report_id} | models.SavedReport
[**delete_workspace_scheduled_reports**](ReportsApi.md#delete_workspace_scheduled_reports) | **DELETE** /workspaces/{workspace_id}/scheduled_reports/{report_id} | ScheduledReport
[**get_saved_report_resource**](ReportsApi.md#get_saved_report_resource) | **GET** /workspaces/{workspace_id}/reports/shared/{report_id} | models.SavedReport
[**get_shared_report**](ReportsApi.md#get_shared_report) | **GET** /workspaces/{workspace_id}/reports/shared | workspace.SharedReport
[**get_workspace_scheduled_reports**](ReportsApi.md#get_workspace_scheduled_reports) | **GET** /workspaces/{workspace_id}/scheduled_reports | ScheduledReports
[**post_shared_report**](ReportsApi.md#post_shared_report) | **POST** /workspaces/{workspace_id}/reports/shared | workspace.SharedReport
[**post_workspace_scheduled_reports**](ReportsApi.md#post_workspace_scheduled_reports) | **POST** /workspaces/{workspace_id}/scheduled_reports | ScheduledReports
[**put_saved_report_resource**](ReportsApi.md#put_saved_report_resource) | **PUT** /workspaces/{workspace_id}/reports/shared/{report_id} | models.SavedReport
[**put_shared_report**](ReportsApi.md#put_shared_report) | **PUT** /workspaces/{workspace_id}/reports/shared | workspace.SharedReport


## `delete_saved_report_resource`
> ModelsSavedReport delete_saved_report_resource(workspace_id, report_id)

models.SavedReport

Delete saved report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
report_id = 56 # int | Numeric ID of the report.

try:
    # models.SavedReport
    api_response = api_instance.delete_saved_report_resource(workspace_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_saved_report_resource: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **report_id** | **int**| Numeric ID of the report. | 

### Return type

[**ModelsSavedReport**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_scheduled_reports`
> str delete_workspace_scheduled_reports(workspace_id, report_id)

ScheduledReport

Endpoint for delete a scheduled report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
report_id = 56 # int | Numeric ID of the report

try:
    # ScheduledReport
    api_response = api_instance.delete_workspace_scheduled_reports(workspace_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_workspace_scheduled_reports: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **report_id** | **int**| Numeric ID of the report | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_saved_report_resource`
> ModelsSavedReport get_saved_report_resource(workspace_id, report_id)

models.SavedReport

Get saved report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
report_id = 56 # int | Numeric ID of the report.

try:
    # models.SavedReport
    api_response = api_instance.get_saved_report_resource(workspace_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_saved_report_resource: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **report_id** | **int**| Numeric ID of the report. | 

### Return type

[**ModelsSavedReport**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_shared_report`
> list[ModelsSavedReport] get_shared_report(workspace_id, fixed_dates=fixed_dates, name=name, page=page, per_page=per_page, public=public, scheduled=scheduled, sort_direction=sort_direction, sort_field=sort_field)

workspace.SharedReport

Get shared report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
fixed_dates = true # bool |  (optional)
name = 'name_example' # str |  (optional)
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
public = true # bool |  (optional)
scheduled = true # bool |  (optional)
sort_direction = 'sort_direction_example' # str |  (optional)
sort_field = 'sort_field_example' # str |  (optional)

try:
    # workspace.SharedReport
    api_response = api_instance.get_shared_report(workspace_id, fixed_dates=fixed_dates, name=name, page=page, per_page=per_page, public=public, scheduled=scheduled, sort_direction=sort_direction, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_shared_report: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **fixed_dates** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **public** | **bool**|  | [optional] 
 **scheduled** | **bool**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**list[ModelsSavedReport]**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_scheduled_reports`
> list[ModelsScheduledReport] get_workspace_scheduled_reports(workspace_id)

ScheduledReports

Lists scheduled reports.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # ScheduledReports
    api_response = api_instance.get_workspace_scheduled_reports(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_workspace_scheduled_reports: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsScheduledReport]**](ModelsScheduledReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_shared_report`
> ModelsSavedReport post_shared_report(workspace_id, saved_report_payload)

workspace.SharedReport

Add shared report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
saved_report_payload = toggl.SavedPayload() # SavedPayload | Saved Report Payload

try:
    # workspace.SharedReport
    api_response = api_instance.post_shared_report(workspace_id, saved_report_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->post_shared_report: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **saved_report_payload** | [**SavedPayload**](SavedPayload.md)| Saved Report Payload | 

### Return type

[**ModelsSavedReport**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_scheduled_reports`
> ModelsScheduledReport post_workspace_scheduled_reports(workspace_id, workspace_id2)

ScheduledReports

Endpoint for setting up a scheduled report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
workspace_id2 = toggl.ScheduledPayload() # ScheduledPayload | Comment from the client on the pricing plan change

try:
    # ScheduledReports
    api_response = api_instance.post_workspace_scheduled_reports(workspace_id, workspace_id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->post_workspace_scheduled_reports: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **workspace_id2** | [**ScheduledPayload**](ScheduledPayload.md)| Comment from the client on the pricing plan change | 

### Return type

[**ModelsScheduledReport**](ModelsScheduledReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_saved_report_resource`
> ModelsSavedReport put_saved_report_resource(workspace_id, report_id, saved_report_payload)

models.SavedReport

Change saved report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
report_id = 56 # int | Numeric ID of the report.
saved_report_payload = toggl.SavedPayload() # SavedPayload | Saved Report Payload

try:
    # models.SavedReport
    api_response = api_instance.put_saved_report_resource(workspace_id, report_id, saved_report_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->put_saved_report_resource: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **report_id** | **int**| Numeric ID of the report. | 
 **saved_report_payload** | [**SavedPayload**](SavedPayload.md)| Saved Report Payload | 

### Return type

[**ModelsSavedReport**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_shared_report`
> ModelsSavedReport put_shared_report(workspace_id, report_id, saved_report_payload)

workspace.SharedReport

Change shared report.

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
api_instance = toggl.ReportsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
report_id = 56 # int | Numeric ID of the report.
saved_report_payload = [toggl.SavedPayload()] # list[SavedPayload] | Saved Report Payload

try:
    # workspace.SharedReport
    api_response = api_instance.put_shared_report(workspace_id, report_id, saved_report_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->put_shared_report: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **report_id** | **int**| Numeric ID of the report. | 
 **saved_report_payload** | [**list[SavedPayload]**](SavedPayload.md)| Saved Report Payload | 

### Return type

[**ModelsSavedReport**](ModelsSavedReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

