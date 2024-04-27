# toggl.DefaultApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_api_v3_workspace_workspace_id_comparative_post**](DefaultApi.md#reports_api_v3_workspace_workspace_id_comparative_post) | **POST** /reports/api/v3/workspace/{workspace_id}/comparative | Load comparative report
[**reports_api_v3_workspace_workspace_id_data_trends_clients_post**](DefaultApi.md#reports_api_v3_workspace_workspace_id_data_trends_clients_post) | **POST** /reports/api/v3/workspace/{workspace_id}/data_trends/clients | Load clients&#39; data trends
[**reports_api_v3_workspace_workspace_id_data_trends_projects_post**](DefaultApi.md#reports_api_v3_workspace_workspace_id_data_trends_projects_post) | **POST** /reports/api/v3/workspace/{workspace_id}/data_trends/projects | Load projects&#39; data trends
[**reports_api_v3_workspace_workspace_id_data_trends_users_post**](DefaultApi.md#reports_api_v3_workspace_workspace_id_data_trends_users_post) | **POST** /reports/api/v3/workspace/{workspace_id}/data_trends/users | Load users&#39; data trends
[**reports_api_v3_workspace_workspace_id_profitability_projects_post**](DefaultApi.md#reports_api_v3_workspace_workspace_id_profitability_projects_post) | **POST** /reports/api/v3/workspace/{workspace_id}/profitability/projects | Load profitability projects report


## `reports_api_v3_workspace_workspace_id_comparative_post`
> ComparativeReport reports_api_v3_workspace_workspace_id_comparative_post(workspace_id, comparative_post=comparative_post)

Load comparative report

Returns comparative report.

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
api_instance = toggl.DefaultApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
comparative_post = toggl.ComparativeComparativePost() # ComparativeComparativePost | Comparative reports conditions (optional)

try:
    # Load comparative report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_comparative_post(workspace_id, comparative_post=comparative_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_api_v3_workspace_workspace_id_comparative_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **comparative_post** | [**ComparativeComparativePost**](ComparativeComparativePost.md)| Comparative reports conditions | [optional] 

### Return type

[**ComparativeReport**](ComparativeReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_data_trends_clients_post`
> ClientsDataTrendsReport reports_api_v3_workspace_workspace_id_data_trends_clients_post(workspace_id, data_trends_post)

Load clients' data trends

Returns the clients' data trends.

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
api_instance = toggl.DefaultApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
data_trends_post = toggl.BaseDataTrendsPost() # BaseDataTrendsPost | Report data trends conditions

try:
    # Load clients' data trends
    api_response = api_instance.reports_api_v3_workspace_workspace_id_data_trends_clients_post(workspace_id, data_trends_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_api_v3_workspace_workspace_id_data_trends_clients_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **data_trends_post** | [**BaseDataTrendsPost**](BaseDataTrendsPost.md)| Report data trends conditions | 

### Return type

[**ClientsDataTrendsReport**](ClientsDataTrendsReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_data_trends_projects_post`
> ProjectsDataTrendsReport reports_api_v3_workspace_workspace_id_data_trends_projects_post(workspace_id, data_trends_post=data_trends_post)

Load projects' data trends

Returns projects' data trends.

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
api_instance = toggl.DefaultApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
data_trends_post = toggl.BaseDataTrendsPost() # BaseDataTrendsPost | Data trends conditions (optional)

try:
    # Load projects' data trends
    api_response = api_instance.reports_api_v3_workspace_workspace_id_data_trends_projects_post(workspace_id, data_trends_post=data_trends_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_api_v3_workspace_workspace_id_data_trends_projects_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **data_trends_post** | [**BaseDataTrendsPost**](BaseDataTrendsPost.md)| Data trends conditions | [optional] 

### Return type

[**ProjectsDataTrendsReport**](ProjectsDataTrendsReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_data_trends_users_post`
> UsersDataTrendsReport reports_api_v3_workspace_workspace_id_data_trends_users_post(workspace_id, data_trends_post)

Load users' data trends

Returns users' data trends.

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
api_instance = toggl.DefaultApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
data_trends_post = toggl.BaseDataTrendsPost() # BaseDataTrendsPost | Report data trends conditions

try:
    # Load users' data trends
    api_response = api_instance.reports_api_v3_workspace_workspace_id_data_trends_users_post(workspace_id, data_trends_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_api_v3_workspace_workspace_id_data_trends_users_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **data_trends_post** | [**BaseDataTrendsPost**](BaseDataTrendsPost.md)| Report data trends conditions | 

### Return type

[**UsersDataTrendsReport**](UsersDataTrendsReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `reports_api_v3_workspace_workspace_id_profitability_projects_post`
> ProjectsReport reports_api_v3_workspace_workspace_id_profitability_projects_post(workspace_id, project_profitability_post=project_profitability_post)

Load profitability projects report

Returns profitability projects report.

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
api_instance = toggl.DefaultApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Workspace ID
project_profitability_post = toggl.RequestsProjectProfitability() # RequestsProjectProfitability | Profitability projects report conditions (optional)

try:
    # Load profitability projects report
    api_response = api_instance.reports_api_v3_workspace_workspace_id_profitability_projects_post(workspace_id, project_profitability_post=project_profitability_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_api_v3_workspace_workspace_id_profitability_projects_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **project_profitability_post** | [**RequestsProjectProfitability**](RequestsProjectProfitability.md)| Profitability projects report conditions | [optional] 

### Return type

[**ProjectsReport**](ProjectsReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

