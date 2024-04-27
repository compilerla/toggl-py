# toggl.SavedReportsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_shared_report_token_csv_post**](SavedReportsApi.md#reports_api_v3_shared_report_token_csv_post) | **POST** /reports/api/v3/shared/{report_token}.csv | Export CSV for saved report
[**reports_api_v3_shared_report_token_pdf_post**](SavedReportsApi.md#reports_api_v3_shared_report_token_pdf_post) | **POST** /reports/api/v3/shared/{report_token}/pdf | Export saved report in pdf format
[**reports_api_v3_shared_report_token_post**](SavedReportsApi.md#reports_api_v3_shared_report_token_post) | **POST** /reports/api/v3/shared/{report_token} | Load the previously saved report
[**reports_api_v3_shared_report_token_xlsx_post**](SavedReportsApi.md#reports_api_v3_shared_report_token_xlsx_post) | **POST** /reports/api/v3/shared/{report_token}.xlsx | Export XSLX saved report


## `reports_api_v3_shared_report_token_csv_post`
> str reports_api_v3_shared_report_token_csv_post(report_token, start_date=start_date, end_date=end_date)

Export CSV for saved report

<p>Downloads a previously saved report in csv.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.SavedReportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)

try:
    # Export CSV for saved report
    api_response = api_instance.reports_api_v3_shared_report_token_csv_post(report_token, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedReportsApi->reports_api_v3_shared_report_token_csv_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_pdf_post`
> str reports_api_v3_shared_report_token_pdf_post(report_token, start_date=start_date, end_date=end_date, display_mode=display_mode)

Export saved report in pdf format

<p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.SavedReportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)
display_mode = 'display_mode_example' # str | Display mode for time data, only for detailed reports. Possible values: 'date_only', 'time_only', 'date_time'. Default value: 'date_and_time' (optional)

try:
    # Export saved report in pdf format
    api_response = api_instance.reports_api_v3_shared_report_token_pdf_post(report_token, start_date=start_date, end_date=end_date, display_mode=display_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedReportsApi->reports_api_v3_shared_report_token_pdf_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 
 **display_mode** | **str**| Display mode for time data, only for detailed reports. Possible values: &#39;date_only&#39;, &#39;time_only&#39;, &#39;date_time&#39;. Default value: &#39;date_and_time&#39; | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_post`
> SavedReportOutput reports_api_v3_shared_report_token_post(report_token, start_date=start_date, first_timestamp=first_timestamp, end_date=end_date, group_ids=group_ids, user_ids=user_ids, client_ids=client_ids, project_ids=project_ids, task_ids=task_ids, tag_ids=tag_ids, description=description, billable=billable, rounding=rounding, rounding_minutes=rounding_minutes, grouped=grouped, grouping=grouping, sub_grouping=sub_grouping)

Load the previously saved report

<p>Returns the previously saved report.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

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
api_instance = toggl.SavedReportsApi(toggl.ApiClient(configuration))
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
first_timestamp = 56 # int | Unix timestamp(UTC) or null for proper pagination. This parameter only works in Detailed and Summary reports. (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD. This parameter only works in Detailed and Summary reports. (optional)
group_ids = [toggl.list[int]()] # list[int] | Integer array with group_ids (optional)
user_ids = [toggl.list[int]()] # list[int] | Integer array with user_ids (optional)
client_ids = [toggl.list[int]()] # list[int] | Integer array with client_ids (optional)
project_ids = [toggl.list[int]()] # list[int] | Integer array with project_ids (optional)
task_ids = [toggl.list[int]()] # list[int] | Integer array with task_ids (optional)
tag_ids = [toggl.list[int]()] # list[int] | Integer array with tag_ids (optional)
description = 'description_example' # str | Case insensitive pattern that matches `.*(description).*` (optional)
billable = true # bool | Is billable filter on (optional)
rounding = 56 # int | How the rounding is done: 1 is rounding up, -1 down, 0 for no rounding. (optional)
rounding_minutes = 56 # int | Rounding amount in minutes (optional)
grouped = true # bool | If it is grouped or not. This parameter only works for Detailed report. (optional)
grouping = 'grouping_example' # str | Criteria to group by. This parameter only works for Summary report. (optional)
sub_grouping = 'sub_grouping_example' # str | Criteria to subgroup. This parameter only works for Summary report. (optional)

try:
    # Load the previously saved report
    api_response = api_instance.reports_api_v3_shared_report_token_post(report_token, start_date=start_date, first_timestamp=first_timestamp, end_date=end_date, group_ids=group_ids, user_ids=user_ids, client_ids=client_ids, project_ids=project_ids, task_ids=task_ids, tag_ids=tag_ids, description=description, billable=billable, rounding=rounding, rounding_minutes=rounding_minutes, grouped=grouped, grouping=grouping, sub_grouping=sub_grouping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedReportsApi->reports_api_v3_shared_report_token_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **first_timestamp** | **int**| Unix timestamp(UTC) or null for proper pagination. This parameter only works in Detailed and Summary reports. | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD. This parameter only works in Detailed and Summary reports. | [optional] 
 **group_ids** | **list[int]**| Integer array with group_ids | [optional] 
 **user_ids** | **list[int]**| Integer array with user_ids | [optional] 
 **client_ids** | **list[int]**| Integer array with client_ids | [optional] 
 **project_ids** | **list[int]**| Integer array with project_ids | [optional] 
 **task_ids** | **list[int]**| Integer array with task_ids | [optional] 
 **tag_ids** | **list[int]**| Integer array with tag_ids | [optional] 
 **description** | **str**| Case insensitive pattern that matches &#x60;.*(description).*&#x60; | [optional] 
 **billable** | **bool**| Is billable filter on | [optional] 
 **rounding** | **int**| How the rounding is done: 1 is rounding up, -1 down, 0 for no rounding. | [optional] 
 **rounding_minutes** | **int**| Rounding amount in minutes | [optional] 
 **grouped** | **bool**| If it is grouped or not. This parameter only works for Detailed report. | [optional] 
 **grouping** | **str**| Criteria to group by. This parameter only works for Summary report. | [optional] 
 **sub_grouping** | **str**| Criteria to subgroup. This parameter only works for Summary report. | [optional] 

### Return type

[**SavedReportOutput**](SavedReportOutput.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_shared_report_token_xlsx_post`
> str reports_api_v3_shared_report_token_xlsx_post(report_token, start_date=start_date, end_date=end_date)

Export XSLX saved report

<p>Downloads a previously saved report in xlsx.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.SavedReportsApi()
report_token = 'report_token_example' # str | Token for the saved report
start_date = 'start_date_example' # str | Starting date in the format YYYY-MM-DD (optional)
end_date = 'end_date_example' # str | End date in the format YYYY-MM-DD (optional)

try:
    # Export XSLX saved report
    api_response = api_instance.reports_api_v3_shared_report_token_xlsx_post(report_token, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedReportsApi->reports_api_v3_shared_report_token_xlsx_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_token** | **str**| Token for the saved report | 
 **start_date** | **str**| Starting date in the format YYYY-MM-DD | [optional] 
 **end_date** | **str**| End date in the format YYYY-MM-DD | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

