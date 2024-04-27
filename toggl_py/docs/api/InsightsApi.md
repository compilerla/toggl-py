# toggl.InsightsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**insights_api_v1_workspace_workspace_id_data_trends_projects_post**](InsightsApi.md#insights_api_v1_workspace_workspace_id_data_trends_projects_post) | **POST** /insights/api/v1/workspace/{workspace_id}/data_trends/projects | Load projects&#39; data trends
[**insights_api_v1_workspace_workspace_id_profitability_employees_extension_post**](InsightsApi.md#insights_api_v1_workspace_workspace_id_profitability_employees_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/profitability/employees.{extension} | Export employee profitability insights
[**insights_api_v1_workspace_workspace_id_profitability_projects_extension_post**](InsightsApi.md#insights_api_v1_workspace_workspace_id_profitability_projects_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/profitability/projects.{extension} | Export profitability project insights
[**insights_api_v1_workspace_workspace_id_trends_projects_extension_post**](InsightsApi.md#insights_api_v1_workspace_workspace_id_trends_projects_extension_post) | **POST** /insights/api/v1/workspace/{workspace_id}/trends/projects.{extension} | Export projects data trends


## `insights_api_v1_workspace_workspace_id_data_trends_projects_post`
> list[ProjectsProjectTrends] insights_api_v1_workspace_workspace_id_data_trends_projects_post(workspace_id, project_trend_post)

Load projects' data trends

Returns the projects' data trends projects from a workspace.

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
api_instance = toggl.InsightsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
project_trend_post = toggl.ProjectsProjectTrend() # ProjectsProjectTrend | Projects filter conditions

try:
    # Load projects' data trends
    api_response = api_instance.insights_api_v1_workspace_workspace_id_data_trends_projects_post(workspace_id, project_trend_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->insights_api_v1_workspace_workspace_id_data_trends_projects_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **project_trend_post** | [**ProjectsProjectTrend**](ProjectsProjectTrend.md)| Projects filter conditions | 

### Return type

[**list[ProjectsProjectTrends]**](ProjectsProjectTrends.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_profitability_employees_extension_post`
> str insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(parameters)

Export employee profitability insights

Downloads employee profitability insights in the specified format: csv or xlsx.

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
api_instance = toggl.InsightsApi(toggl.ApiClient(configuration))
parameters = toggl.RequestsEmployeeProfitability() # RequestsEmployeeProfitability | Parameters for report

try:
    # Export employee profitability insights
    api_response = api_instance.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->insights_api_v1_workspace_workspace_id_profitability_employees_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**RequestsEmployeeProfitability**](RequestsEmployeeProfitability.md)| Parameters for report | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_profitability_projects_extension_post`
> str insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(parameters, extension)

Export profitability project insights

Downloads profitability project insights in the specified format: csv or xlsx.

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
api_instance = toggl.InsightsApi(toggl.ApiClient(configuration))
parameters = toggl.RequestsProjectProfitability() # RequestsProjectProfitability | Parameters for report
extension = 'extension_example' # str | csv,xlsx

try:
    # Export profitability project insights
    api_response = api_instance.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(parameters, extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->insights_api_v1_workspace_workspace_id_profitability_projects_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**RequestsProjectProfitability**](RequestsProjectProfitability.md)| Parameters for report | 
 **extension** | **str**| csv,xlsx | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, text/xlsx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `insights_api_v1_workspace_workspace_id_trends_projects_extension_post`
> list[ProjectsProjectTrends] insights_api_v1_workspace_workspace_id_trends_projects_extension_post(workspace_id, extension, project_trend=project_trend)

Export projects data trends

Downloads projects data trends in the specified format: csv or xlsx.

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
api_instance = toggl.InsightsApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
extension = 'extension_example' # str | csv,xlsx
project_trend = toggl.ProjectsProjectTrend() # ProjectsProjectTrend | Projects filter conditions (optional)

try:
    # Export projects data trends
    api_response = api_instance.insights_api_v1_workspace_workspace_id_trends_projects_extension_post(workspace_id, extension, project_trend=project_trend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->insights_api_v1_workspace_workspace_id_trends_projects_extension_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **extension** | **str**| csv,xlsx | 
 **project_trend** | [**ProjectsProjectTrend**](ProjectsProjectTrend.md)| Projects filter conditions | [optional] 

### Return type

[**list[ProjectsProjectTrends]**](ProjectsProjectTrends.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

