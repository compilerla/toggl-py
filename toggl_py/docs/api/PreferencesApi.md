# toggl.PreferencesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_preferences**](PreferencesApi.md#get_preferences) | **GET** /me/preferences | Preferences for the current user
[**get_preferences_client**](PreferencesApi.md#get_preferences_client) | **GET** /me/preferences/{client} | Preferences for an specific client of the current user
[**get_workspace_preferences**](PreferencesApi.md#get_workspace_preferences) | **GET** /workspaces/{workspace_id}/preferences | Get workspace preferences
[**post_preferences**](PreferencesApi.md#post_preferences) | **POST** /me/preferences | Update the preferences for the current user
[**post_preferences_client**](PreferencesApi.md#post_preferences_client) | **POST** /me/preferences/{client} | Update the preferences for an specific client of the current user
[**post_workspace_preferences**](PreferencesApi.md#post_workspace_preferences) | **POST** /workspaces/{workspace_id}/preferences | Get workspace preferences


## `get_preferences`
> ModelsAllPreferences get_preferences()

Preferences for the current user

Returns user preferences and alpha features. The list of alpha features contains a full list of feature codes (every feature that exists in database) and the `enabled` flag specifying if that feature should be enabled or disabled for the user.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))

try:
    # Preferences for the current user
    api_response = api_instance.get_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->get_preferences: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsAllPreferences**](ModelsAllPreferences.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_preferences_client`
> ModelsAllPreferences get_preferences_client(client, since=since)

Preferences for an specific client of the current user

Returns user preferences and alpha features. The list of alpha features contains a full list of feature codes (every feature that exists in database) and the `enabled` flag specifying if that feature should be enabled or disabled for the user.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))
client = 'client_example' # str | Client type
since = 56 # int | Retrieve preference modified since this date using UNIX timestamp. (optional)

try:
    # Preferences for an specific client of the current user
    api_response = api_instance.get_preferences_client(client, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->get_preferences_client: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| Client type | 
 **since** | **int**| Retrieve preference modified since this date using UNIX timestamp. | [optional] 

### Return type

[**ModelsAllPreferences**](ModelsAllPreferences.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_preferences`
> ModelsLogo get_workspace_preferences(workspace_id)

Get workspace preferences

Get the preferences for a given workspace.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace preferences
    api_response = api_instance.get_workspace_preferences(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->get_workspace_preferences: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsLogo**](ModelsLogo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_preferences`
> str post_preferences(preferences)

Update the preferences for the current user

With this endpoint, preferences can be modified and alpha features can be enabled or disabled.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))
preferences = toggl.ModelsAllPreferences() # ModelsAllPreferences | Preferences

try:
    # Update the preferences for the current user
    api_response = api_instance.post_preferences(preferences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->post_preferences: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferences** | [**ModelsAllPreferences**](ModelsAllPreferences.md)| Preferences | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_preferences_client`
> str post_preferences_client(client, preferences)

Update the preferences for an specific client of the current user

With this endpoint, preferences can be modified and alpha features can be enabled or disabled.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))
client = 'client_example' # str | Client type
preferences = toggl.ModelsAllPreferences() # ModelsAllPreferences | Preferences

try:
    # Update the preferences for an specific client of the current user
    api_response = api_instance.post_preferences_client(client, preferences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->post_preferences_client: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| Client type | 
 **preferences** | [**ModelsAllPreferences**](ModelsAllPreferences.md)| Preferences | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_preferences`
> ModelsLogo post_workspace_preferences(workspace_id, preferences)

Get workspace preferences

Get the preferences for a given workspace.

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
api_instance = toggl.PreferencesApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
preferences = toggl.ModelsWorkspacePreferences() # ModelsWorkspacePreferences | Input data of the preferences.

try:
    # Get workspace preferences
    api_response = api_instance.post_workspace_preferences(workspace_id, preferences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->post_workspace_preferences: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **preferences** | [**ModelsWorkspacePreferences**](ModelsWorkspacePreferences.md)| Input data of the preferences. | 

### Return type

[**ModelsLogo**](ModelsLogo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

