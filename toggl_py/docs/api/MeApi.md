# toggl.MeApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_push_services**](MeApi.md#delete_push_services) | **DELETE** /me/push_services | PushServices
[**get_clients**](MeApi.md#get_clients) | **GET** /me/clients | Clients
[**get_lost_password**](MeApi.md#get_lost_password) | **GET** /me/lost_passwords | LostPassword
[**get_me**](MeApi.md#get_me) | **GET** /me | Me
[**get_me_features**](MeApi.md#get_me_features) | **GET** /me/features | Features
[**get_me_flags**](MeApi.md#get_me_flags) | **GET** /me/flags | Flags
[**get_me_location**](MeApi.md#get_me_location) | **GET** /me/location | User&#39;s last known location
[**get_me_notifications**](MeApi.md#get_me_notifications) | **GET** /me/notifications | Notifications
[**get_me_projects**](MeApi.md#get_me_projects) | **GET** /me/projects | Projects
[**get_me_projects_paginated**](MeApi.md#get_me_projects_paginated) | **GET** /me/projects/paginated | ProjectsPaginated
[**get_me_timesheets**](MeApi.md#get_me_timesheets) | **GET** /me/timesheets | User&#39;s Timesheets
[**get_me_track_reminders**](MeApi.md#get_me_track_reminders) | **GET** /me/track_reminders | TrackReminders
[**get_organizations**](MeApi.md#get_organizations) | **GET** /me/organizations | Organizations that a user is part of
[**get_push_services**](MeApi.md#get_push_services) | **GET** /me/push_services | PushServices
[**get_tags**](MeApi.md#get_tags) | **GET** /me/tags | Tags
[**get_tasks**](MeApi.md#get_tasks) | **GET** /me/tasks | Tasks
[**get_web_timer**](MeApi.md#get_web_timer) | **GET** /me/web-timer | WebTimer
[**get_workspaces**](MeApi.md#get_workspaces) | **GET** /me/workspaces | Workspaces
[**me_logged_get**](MeApi.md#me_logged_get) | **GET** /me/logged | Logged
[**post_close_account**](MeApi.md#post_close_account) | **POST** /me/close_account | CloseAccount
[**post_lost_password**](MeApi.md#post_lost_password) | **POST** /me/lost_passwords | LostPassword
[**post_lost_password_confirm**](MeApi.md#post_lost_password_confirm) | **POST** /me/lost_passwords/confirm | LostPassword conformation
[**post_me_accept_tos**](MeApi.md#post_me_accept_tos) | **POST** /me/accept_tos | AcceptTOS
[**post_me_disable_product_emails**](MeApi.md#post_me_disable_product_emails) | **POST** /me/disable_product_emails/{disable_code} | Disable product emails
[**post_me_disable_weekly_report**](MeApi.md#post_me_disable_weekly_report) | **POST** /me/disable_weekly_report/{weekly_report_code} | Disable weekly report
[**post_me_flags**](MeApi.md#post_me_flags) | **POST** /me/flags | Flags
[**post_push_services**](MeApi.md#post_push_services) | **POST** /me/push_services | PushServices
[**put_me**](MeApi.md#put_me) | **PUT** /me | Me
[**put_notifications**](MeApi.md#put_notifications) | **POST** /me/notifications/{notification_id}/seen | Notifications


## `delete_push_services`
> str delete_push_services(delete_push_services_unsubscribe)

PushServices

Unregister Firebase token for current user

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
delete_push_services_unsubscribe = toggl.PushDeletePushServicesUnsubscribe() # PushDeletePushServicesUnsubscribe | FirebaseToken

try:
    # PushServices
    api_response = api_instance.delete_push_services(delete_push_services_unsubscribe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->delete_push_services: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_push_services_unsubscribe** | [**PushDeletePushServicesUnsubscribe**](PushDeletePushServicesUnsubscribe.md)| FirebaseToken | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_clients`
> list[ModelsClient] get_clients(since=since)

Clients

Get Clients.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve clients created/modified/deleted since this date using UNIX timestamp. (optional)

try:
    # Clients
    api_response = api_instance.get_clients(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_clients: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve clients created/modified/deleted since this date using UNIX timestamp. | [optional] 

### Return type

[**list[ModelsClient]**](ModelsClient.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_lost_password`
> str get_lost_password(token_code)

LostPassword

Verifies the user request to reset the password.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()
token_code = 'token_code_example' # str | Token code

try:
    # LostPassword
    api_response = api_instance.get_lost_password(token_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_lost_password: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_code** | **str**| Token code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me`
> RelatedUserWithRelated get_me(with_related_data=with_related_data)

Me

Returns details for the current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
with_related_data = true # bool | Retrieve user related data (clients, projects, tasks, tags, workspaces, time entries, etc.) (optional)

try:
    # Me
    api_response = api_instance.get_me(with_related_data=with_related_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_related_data** | **bool**| Retrieve user related data (clients, projects, tasks, tags, workspaces, time entries, etc.) | [optional] 

### Return type

[**RelatedUserWithRelated**](RelatedUserWithRelated.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_features`
> list[MeWorkspace] get_me_features()

Features

Get features.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # Features
    api_response = api_instance.get_me_features()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_features: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[MeWorkspace]**](MeWorkspace.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_flags`
> UserFlags get_me_flags()

Flags

Returns flags for the current user. They will be represented by an object with dynamic string keys, where the value can be of any type.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # Flags
    api_response = api_instance.get_me_flags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_flags: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UserFlags**](UserFlags.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_location`
> MeUserLocationResponse get_me_location()

User's last known location

Returns the client's IP-based location. If no data is present, empty response will be yielded.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()

try:
    # User's last known location
    api_response = api_instance.get_me_location()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_location: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**MeUserLocationResponse**](MeUserLocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_notifications`
> list[ModelsUserNotification] get_me_notifications()

Notifications

Get notifications.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # Notifications
    api_response = api_instance.get_me_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_notifications: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsUserNotification]**](ModelsUserNotification.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_projects`
> list[ModelsProject] get_me_projects(include_archived=include_archived, since=since)

Projects

Get projects

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
include_archived = 'include_archived_example' # str | Include archived projects. (optional)
since = 56 # int | Retrieve projects modified since this date using UNIX timestamp, including deleted ones. (optional)

try:
    # Projects
    api_response = api_instance.get_me_projects(include_archived=include_archived, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_projects: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **str**| Include archived projects. | [optional] 
 **since** | **int**| Retrieve projects modified since this date using UNIX timestamp, including deleted ones. | [optional] 

### Return type

[**list[ModelsProject]**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_projects_paginated`
> list[ModelsProject] get_me_projects_paginated(start_project_id=start_project_id, since=since, per_page=per_page)

ProjectsPaginated

Get paginated projects.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
start_project_id = 56 # int | Project ID to resume the next pagination from. (optional)
since = 56 # int | Retrieve projects created/modified/deleted since this date using UNIX timestamp. (optional)
per_page = 56 # int | Number of items per page, default 201. (optional)

try:
    # ProjectsPaginated
    api_response = api_instance.get_me_projects_paginated(start_project_id=start_project_id, since=since, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_projects_paginated: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_project_id** | **int**| Project ID to resume the next pagination from. | [optional] 
 **since** | **int**| Retrieve projects created/modified/deleted since this date using UNIX timestamp. | [optional] 
 **per_page** | **int**| Number of items per page, default 201. | [optional] 

### Return type

[**list[ModelsProject]**](ModelsProject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_timesheets`
> list[ModelsTimesheet] get_me_timesheets()

User's Timesheets

Returns the timehseets for the current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # User's Timesheets
    api_response = api_instance.get_me_timesheets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_timesheets: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsTimesheet]**](ModelsTimesheet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_me_track_reminders`
> list[ModelsTrackReminder] get_me_track_reminders()

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # TrackReminders
    api_response = api_instance.get_me_track_reminders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_me_track_reminders: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsTrackReminder]**](ModelsTrackReminder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organizations`
> list[ModelsMeOrganization] get_organizations()

Organizations that a user is part of

Get all organizations a given user is part of.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()

try:
    # Organizations that a user is part of
    api_response = api_instance.get_organizations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_organizations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsMeOrganization]**](ModelsMeOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_push_services`
> list[str] get_push_services()

PushServices

Get list of firebase tokens registered for current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # PushServices
    api_response = api_instance.get_push_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_push_services: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_tags`
> list[ModelsTag] get_tags(since=since)

Tags

Returns tags for the current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve tags modified/deleted since this date using UNIX timestamp. (optional)

try:
    # Tags
    api_response = api_instance.get_tags(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_tags: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve tags modified/deleted since this date using UNIX timestamp. | [optional] 

### Return type

[**list[ModelsTag]**](ModelsTag.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_tasks`
> list[ModelsTask] get_tasks(since=since, include_not_active=include_not_active)

Tasks

Returns tasks from projects in which the user is participating.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve tasks created/modified/deleted since this date using UNIX timestamp. (optional)
include_not_active = 'include_not_active_example' # str | Include tasks marked as done. (optional)

try:
    # Tasks
    api_response = api_instance.get_tasks(since=since, include_not_active=include_not_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_tasks: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve tasks created/modified/deleted since this date using UNIX timestamp. | [optional] 
 **include_not_active** | **str**| Include tasks marked as done. | [optional] 

### Return type

[**list[ModelsTask]**](ModelsTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_web_timer`
> str get_web_timer()

WebTimer

Get web timer.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # WebTimer
    api_response = api_instance.get_web_timer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_web_timer: %s\n" % e)
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

## `get_workspaces`
> list[WorkspaceWorkspace] get_workspaces(since=since)

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve workspaces created/modified/deleted since this date using UNIX timestamp, including the dates a workspace member got added, removed or updated in the workspace. (optional)

try:
    # Workspaces
    api_response = api_instance.get_workspaces(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_workspaces: %s\n" % e)
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

## `me_logged_get`
> me_logged_get()

Logged

Used to check if authentication works.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()

try:
    # Logged
    api_instance.me_logged_get()
except ApiException as e:
    print("Exception when calling MeApi->me_logged_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_close_account`
> str post_close_account()

CloseAccount

Close Account

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # CloseAccount
    api_response = api_instance.post_close_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_close_account: %s\n" % e)
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

## `post_lost_password`
> str post_lost_password(post_lost_password)

LostPassword

Handles the users request to reset the password.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()
post_lost_password = toggl.ModelsLostPassword() # ModelsLostPassword | Lost Password Parameters

try:
    # LostPassword
    api_response = api_instance.post_lost_password(post_lost_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_lost_password: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_lost_password** | [**ModelsLostPassword**](ModelsLostPassword.md)| Lost Password Parameters | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_lost_password_confirm`
> str post_lost_password_confirm(post_new_password)

LostPassword conformation

Handles lost password request confirmation.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()
post_new_password = toggl.MeLostPasswordPayload() # MeLostPasswordPayload | New Password Data

try:
    # LostPassword conformation
    api_response = api_instance.post_lost_password_confirm(post_new_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_lost_password_confirm: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_new_password** | [**MeLostPasswordPayload**](MeLostPasswordPayload.md)| New Password Data | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_me_accept_tos`
> str post_me_accept_tos()

AcceptTOS

Accepts the last version of the Terms of Service for the current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))

try:
    # AcceptTOS
    api_response = api_instance.post_me_accept_tos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_me_accept_tos: %s\n" % e)
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

## `post_me_disable_product_emails`
> str post_me_disable_product_emails(disable_code)

Disable product emails

Disable product emails.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()
disable_code = 'disable_code_example' # str | Disable Code

try:
    # Disable product emails
    api_response = api_instance.post_me_disable_product_emails(disable_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_me_disable_product_emails: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_code** | **str**| Disable Code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_me_disable_weekly_report`
> str post_me_disable_weekly_report(weekly_report_code)

Disable weekly report

Disable weekly report.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.MeApi()
weekly_report_code = 'weekly_report_code_example' # str | Weekly report code

try:
    # Disable weekly report
    api_response = api_instance.post_me_disable_weekly_report(weekly_report_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_me_disable_weekly_report: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weekly_report_code** | **str**| Weekly report code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_me_flags`
> UserFlags post_me_flags(post_flags)

Flags

Add flags for the current user. The current limits are 4 flags per request, 128 flags in total. Keys and values can be up to 32 and 64 characters, respectively.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
post_flags = toggl.UserFlags() # UserFlags | flags

try:
    # Flags
    api_response = api_instance.post_me_flags(post_flags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_me_flags: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_flags** | [**UserFlags**](UserFlags.md)| flags | 

### Return type

[**UserFlags**](UserFlags.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_push_services`
> str post_push_services(post_push_services_subscribe)

PushServices

Register Firebase token for current user

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
post_push_services_subscribe = toggl.PushPostPushServicesSubscribe() # PushPostPushServicesSubscribe | FirebaseToken

try:
    # PushServices
    api_response = api_instance.post_push_services(post_push_services_subscribe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->post_push_services: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_push_services_subscribe** | [**PushPostPushServicesSubscribe**](PushPostPushServicesSubscribe.md)| FirebaseToken | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_me`
> ModelsTogglUser put_me(payload)

Me

Updates details for the current user.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
payload = toggl.MePayload() # MePayload | Update user parameters

try:
    # Me
    api_response = api_instance.put_me(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->put_me: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**MePayload**](MePayload.md)| Update user parameters | 

### Return type

[**ModelsTogglUser**](ModelsTogglUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_notifications`
> str put_notifications(notification_id)

Notifications

Mark notification seen.

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
api_instance = toggl.MeApi(toggl.ApiClient(configuration))
notification_id = 56 # int | Notification ID.

try:
    # Notifications
    api_response = api_instance.put_notifications(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->put_notifications: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| Notification ID. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

