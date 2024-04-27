# toggl.GoalsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**goals_cadences_get**](GoalsApi.md#goals_cadences_get) | **GET** /goals/cadences | Get a list of goal cadences
[**goals_get**](GoalsApi.md#goals_get) | **GET** /goals | Get a list of goals
[**goals_goal_id_delete**](GoalsApi.md#goals_goal_id_delete) | **DELETE** /goals/{goal_id} | Delete one goal
[**goals_goal_id_get**](GoalsApi.md#goals_goal_id_get) | **GET** /goals/{goal_id} | Get one goal
[**goals_goal_id_patch**](GoalsApi.md#goals_goal_id_patch) | **PATCH** /goals/{goal_id} | Update a Goal
[**goals_goal_id_stats_get**](GoalsApi.md#goals_goal_id_stats_get) | **GET** /goals/{goal_id}/stats | Get stats for a goal
[**goals_insight_post**](GoalsApi.md#goals_insight_post) | **POST** /goals/insight | Get a insight
[**goals_post**](GoalsApi.md#goals_post) | **POST** /goals | Create a Goal


## `goals_cadences_get`
> list[GoalsCadenceResponse] goals_cadences_get(amount=amount, archived=archived, goal=goal, offset=offset)

Get a list of goal cadences

Gets all cadences for the goals requested for the asking user.

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
amount = 56 # int |  (optional)
archived = 'archived_example' # str |  (optional)
goal = [56] # list[int] |  (optional)
offset = 56 # int |  (optional)

try:
    # Get a list of goal cadences
    api_response = api_instance.goals_cadences_get(amount=amount, archived=archived, goal=goal, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_cadences_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **int**|  | [optional] 
 **archived** | **str**|  | [optional] 
 **goal** | [**list[int]**](int.md)|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**list[GoalsCadenceResponse]**](GoalsCadenceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_get`
> list[ModelsPlainGoal] goals_get(archived=archived, workspace_id=workspace_id)

Get a list of goals

Gets all goals for the requesting user. The returned Goal will have only one type, but may have multiple on the same type, like 3 projects, or more than one task. Billable will always be one.

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
archived = 'false' # str |  (optional) (default to false)
workspace_id = 56 # int |  (optional)

try:
    # Get a list of goals
    api_response = api_instance.goals_get(archived=archived, workspace_id=workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archived** | **str**|  | [optional] [default to false]
 **workspace_id** | **int**|  | [optional] 

### Return type

[**list[ModelsPlainGoal]**](ModelsPlainGoal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_goal_id_delete`
> goals_goal_id_delete(goal_id)

Delete one goal

Delete a goal that belongs to the calling user

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal_id = 56 # int | Goal ID

try:
    # Delete one goal
    api_instance.goals_goal_id_delete(goal_id)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_goal_id_delete: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **int**| Goal ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_goal_id_get`
> ModelsPlainGoal goals_goal_id_get(goal_id)

Get one goal

Gets a goal that belongs to the calling user

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal_id = 56 # int | Goal ID

try:
    # Get one goal
    api_response = api_instance.goals_goal_id_get(goal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_goal_id_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **int**| Goal ID | 

### Return type

[**ModelsPlainGoal**](ModelsPlainGoal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_goal_id_patch`
> ModelsGoal goals_goal_id_patch(goal)

Update a Goal

Update a goal with the updateable parameters given by UpdateParams

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal = toggl.GoalsUpdateParams() # GoalsUpdateParams | Goal details

try:
    # Update a Goal
    api_response = api_instance.goals_goal_id_patch(goal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_goal_id_patch: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal** | [**GoalsUpdateParams**](GoalsUpdateParams.md)| Goal details | 

### Return type

[**ModelsGoal**](ModelsGoal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_goal_id_stats_get`
> ModelsGoalStats goals_goal_id_stats_get(goal_id)

Get stats for a goal

Gets stats for a given goal that must belong to the calling user

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal_id = 56 # int | Goal ID

try:
    # Get stats for a goal
    api_response = api_instance.goals_goal_id_stats_get(goal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_goal_id_stats_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **int**| Goal ID | 

### Return type

[**ModelsGoalStats**](ModelsGoalStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_insight_post`
> GoalsInsightResponse goals_insight_post(goal)

Get a insight

Get data insight for user simulating how much the user would accomplish for a given Goal

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal = toggl.GoalsParamsInsight() # GoalsParamsInsight | Insight details

try:
    # Get a insight
    api_response = api_instance.goals_insight_post(goal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_insight_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal** | [**GoalsParamsInsight**](GoalsParamsInsight.md)| Insight details | 

### Return type

[**GoalsInsightResponse**](GoalsInsightResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `goals_post`
> GoalsParamsCreate goals_post(goal)

Create a Goal

Create a Goal object with its parameters. `goal_type` field must contain either `projects` or `billable` object, not both, or `null` if the goal has `workspace` type.

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
api_instance = toggl.GoalsApi(toggl.ApiClient(configuration))
goal = toggl.ModelsPlainGoal() # ModelsPlainGoal | Goal details

try:
    # Create a Goal
    api_response = api_instance.goals_post(goal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal** | [**ModelsPlainGoal**](ModelsPlainGoal.md)| Goal details | 

### Return type

[**GoalsParamsCreate**](GoalsParamsCreate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

