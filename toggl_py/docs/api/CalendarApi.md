# toggl.CalendarApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_calendar_calendars_selected_get**](CalendarApi.md#integrations_calendar_calendars_selected_get) | **GET** /integrations/calendar/calendars/selected | Get all selected calendars for a given user.
[**integrations_calendar_callback_provider_get**](CalendarApi.md#integrations_calendar_callback_provider_get) | **GET** /integrations/calendar/callback/{provider} | Callback for provider OAuth setup.
[**integrations_calendar_events_details_suggestion_post**](CalendarApi.md#integrations_calendar_events_details_suggestion_post) | **POST** /integrations/calendar/events/details-suggestion | Get details suggestion for given events.
[**integrations_calendar_events_event_id_details_suggestion_get**](CalendarApi.md#integrations_calendar_events_event_id_details_suggestion_get) | **GET** /integrations/calendar/events/{event_id}/details-suggestion | Get details suggestion for a given event.
[**integrations_calendar_events_get**](CalendarApi.md#integrations_calendar_events_get) | **GET** /integrations/calendar/events | Get all events for the caller user.
[**integrations_calendar_events_update_post**](CalendarApi.md#integrations_calendar_events_update_post) | **POST** /integrations/calendar/events/update | Update all events from selected calendars for a user.
[**integrations_calendar_get**](CalendarApi.md#integrations_calendar_get) | **GET** /integrations/calendar | Get all integrations a user has.
[**integrations_calendar_integration_id_calendars_calendar_id_patch**](CalendarApi.md#integrations_calendar_integration_id_calendars_calendar_id_patch) | **PATCH** /integrations/calendar/{integration_id}/calendars/{calendar_id} | Sets whether a calendar is or not selected by the user.
[**integrations_calendar_integration_id_calendars_get**](CalendarApi.md#integrations_calendar_integration_id_calendars_get) | **GET** /integrations/calendar/{integration_id}/calendars | Get all calendars for a given integration.
[**integrations_calendar_integration_id_calendars_id_calendar_events_get**](CalendarApi.md#integrations_calendar_integration_id_calendars_id_calendar_events_get) | **GET** /integrations/calendar/{integration_id}/calendars/{id_calendar}/events | (DEPRECATED) Get all events for a given calendar in a given integration.
[**integrations_calendar_integration_id_calendars_update_post**](CalendarApi.md#integrations_calendar_integration_id_calendars_update_post) | **POST** /integrations/calendar/{integration_id}/calendars/update | Updates calendar data according to provider API.
[**integrations_calendar_integration_id_delete**](CalendarApi.md#integrations_calendar_integration_id_delete) | **DELETE** /integrations/calendar/{integration_id} | Delete a given integration.
[**integrations_calendar_setup_get**](CalendarApi.md#integrations_calendar_setup_get) | **GET** /integrations/calendar/setup | Get URL for setting up a calendar integration with given provider.


## `integrations_calendar_calendars_selected_get`
> HandlercalendarCalendarsResponse integrations_calendar_calendars_selected_get(limit=limit, page_token=page_token)

Get all selected calendars for a given user.

Get all selected calendars for a given user that was previously saved in the database.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
limit = 'limit_example' # str | Max results per page (optional)
page_token = 'page_token_example' # str | Token for next page. Used in pagination when the number of results exceed 'limit' (optional)

try:
    # Get all selected calendars for a given user.
    api_response = api_instance.integrations_calendar_calendars_selected_get(limit=limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_calendars_selected_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max results per page | [optional] 
 **page_token** | **str**| Token for next page. Used in pagination when the number of results exceed &#39;limit&#39; | [optional] 

### Return type

[**HandlercalendarCalendarsResponse**](HandlercalendarCalendarsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_callback_provider_get`
> integrations_calendar_callback_provider_get(provider, state, code)

Callback for provider OAuth setup.

Callback endpoint used only by the Calendar Service Provider, which fetches the code

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
provider = 'provider_example' # str | Calendar service provider
state = 'state_example' # str | state string to verify user authenticity
code = 'code_example' # str | Temporary code which will be used to fetch credentials

try:
    # Callback for provider OAuth setup.
    api_instance.integrations_calendar_callback_provider_get(provider, state, code)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_callback_provider_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Calendar service provider | 
 **state** | **str**| state string to verify user authenticity | 
 **code** | **str**| Temporary code which will be used to fetch credentials | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_events_details_suggestion_post`
> HandlercalendarPostDetailsSuggestionResponse integrations_calendar_events_details_suggestion_post(request)

Get details suggestion for given events.

Given one or more event IDs, this endpoint responds with the most probable event details (and its accuracy) to assign to the to-be-created time entry for each event ID. This endpoint will only suggests time entries with description and project not empty, because it uses the description to tell if the TE is similar and the project as the main detail to be suggested.  If the description is equal, as well as all the other details, the accuracy will be 100%, in the case the description is equal but the other details differs, the most frequent will be suggested and the accuracy will be given based on the frequency. In the case there is no TE with the same description the most similar will be suggested based on the Jaro-Winkler algorithm, and the accuracy will be the similarity rating.  This endpoint returns status 200 OK with only the successful suggestions. Any event ID that is invalid or the user does not have access to will be ignored, as well as any event that has no available suggestion.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
request = toggl.HandlercalendarPostDetailsSuggestionRequest() # HandlercalendarPostDetailsSuggestionRequest | Request body containing the event IDs we want to get the suggestion for

try:
    # Get details suggestion for given events.
    api_response = api_instance.integrations_calendar_events_details_suggestion_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_events_details_suggestion_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HandlercalendarPostDetailsSuggestionRequest**](HandlercalendarPostDetailsSuggestionRequest.md)| Request body containing the event IDs we want to get the suggestion for | 

### Return type

[**HandlercalendarPostDetailsSuggestionResponse**](HandlercalendarPostDetailsSuggestionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_events_event_id_details_suggestion_get`
> ModelsSuggestion integrations_calendar_events_event_id_details_suggestion_get(event_id)

Get details suggestion for a given event.

Given an event ID, this endpoint responds with the most probable event details (and the accuracy) to assign to the to-be-created time entry. This endpoint will only suggests time entries with description and project not empty, because it uses the description to tell if the TE is similar and the project as the main detail to be suggested.  If the description is equal, as well as all the other details, the accuracy will be 100%, in the case the description is equal but the other details differs, the most frequent will be suggested and the accuracy will be given based on the frequency. In the case there is no TE with the same description the most similar will be suggested based on the Jaro-Winkler algorithm, and the accuracy will be the similarity rating.  This endpoint returns status 200 OK and a \"null\" string in case no suggestion was found.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
event_id = 56 # int | Calendar event ID which we want to get a possible project to match

try:
    # Get details suggestion for a given event.
    api_response = api_instance.integrations_calendar_events_event_id_details_suggestion_get(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_events_event_id_details_suggestion_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Calendar event ID which we want to get a possible project to match | 

### Return type

[**ModelsSuggestion**](ModelsSuggestion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_events_get`
> HandlercalendarEventsResponse integrations_calendar_events_get(start_date, end_date, limit=limit, page_token=page_token)

Get all events for the caller user.

Get all events from selected calendars for the caller user. This endpoint will only return events if events were fetched from provider before the request is made. Check which is the endpoint for the events.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
start_date = 'start_date_example' # str | Smallest boundary date to search for calendar events
end_date = 'end_date_example' # str | Biggest boundary date to search for calendar events
limit = 'limit_example' # str | Max results per page (optional)
page_token = 'page_token_example' # str | Token for next page. Used in pagination when the number of results exceed 'limit' (optional)

try:
    # Get all events for the caller user.
    api_response = api_instance.integrations_calendar_events_get(start_date, end_date, limit=limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_events_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Smallest boundary date to search for calendar events | 
 **end_date** | **str**| Biggest boundary date to search for calendar events | 
 **limit** | **str**| Max results per page | [optional] 
 **page_token** | **str**| Token for next page. Used in pagination when the number of results exceed &#39;limit&#39; | [optional] 

### Return type

[**HandlercalendarEventsResponse**](HandlercalendarEventsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_events_update_post`
> HandlercalendarResponse integrations_calendar_events_update_post()

Update all events from selected calendars for a user.

Fetch all events from a user's selected calendars and save in database.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))

try:
    # Update all events from selected calendars for a user.
    api_response = api_instance.integrations_calendar_events_update_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_events_update_post: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlercalendarResponse**](HandlercalendarResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_get`
> list[ModelsIntegration] integrations_calendar_get()

Get all integrations a user has.

Get all integrations a user has. Each user may have at most one integration per provider.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))

try:
    # Get all integrations a user has.
    api_response = api_instance.integrations_calendar_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsIntegration]**](ModelsIntegration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_integration_id_calendars_calendar_id_patch`
> list[ModelsCalendar] integrations_calendar_integration_id_calendars_calendar_id_patch(integration_id, calendar_id, payload=payload)

Sets whether a calendar is or not selected by the user.

This endpoint is used to set updatable fields of a calendar like selected field.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
integration_id = 56 # int | Integration ID as saved in the database
calendar_id = 56 # int | Calendar ID as saved in the database
payload = toggl.HandlercalendarPatchCalendar() # HandlercalendarPatchCalendar | Calendar fields to be updated (optional)

try:
    # Sets whether a calendar is or not selected by the user.
    api_response = api_instance.integrations_calendar_integration_id_calendars_calendar_id_patch(integration_id, calendar_id, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_integration_id_calendars_calendar_id_patch: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Integration ID as saved in the database | 
 **calendar_id** | **int**| Calendar ID as saved in the database | 
 **payload** | [**HandlercalendarPatchCalendar**](HandlercalendarPatchCalendar.md)| Calendar fields to be updated | [optional] 

### Return type

[**list[ModelsCalendar]**](ModelsCalendar.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_integration_id_calendars_get`
> HandlercalendarCalendarsResponse integrations_calendar_integration_id_calendars_get(integration_id, limit=limit, selected=selected, page_token=page_token)

Get all calendars for a given integration.

Get all calendars for a given integration that was previously saved in the database.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
integration_id = 56 # int | Integration ID as saved in the database
limit = 56 # int | Max results per page (optional)
selected = true # bool | if we should get the selected or not calendars, or all calendars, in case of omission (optional)
page_token = 'page_token_example' # str | Token for next page. Used in pagination when the number of results exceed 'limit' (optional)

try:
    # Get all calendars for a given integration.
    api_response = api_instance.integrations_calendar_integration_id_calendars_get(integration_id, limit=limit, selected=selected, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_integration_id_calendars_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Integration ID as saved in the database | 
 **limit** | **int**| Max results per page | [optional] 
 **selected** | **bool**| if we should get the selected or not calendars, or all calendars, in case of omission | [optional] 
 **page_token** | **str**| Token for next page. Used in pagination when the number of results exceed &#39;limit&#39; | [optional] 

### Return type

[**HandlercalendarCalendarsResponse**](HandlercalendarCalendarsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_integration_id_calendars_id_calendar_events_get`
> HandlercalendarEventsResponse integrations_calendar_integration_id_calendars_id_calendar_events_get(integration_id, id_calendar, start_date, end_date, limit=limit, page_token=page_token)

(DEPRECATED) Get all events for a given calendar in a given integration.

Get all events for a given calendar in a given integration.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
integration_id = 56 # int | Integration ID as saved in the database
id_calendar = 'id_calendar_example' # str | Calendar ID as returned by the provider, it may be an e-mail address, for instance
start_date = 'start_date_example' # str | Smallest boundary date to search for calendar events
end_date = 'end_date_example' # str | Biggest boundary date to search for calendar events
limit = 'limit_example' # str | Max results per page (optional)
page_token = 'page_token_example' # str | Token for next page. Used in pagination when the number of results exceed 'limit' (optional)

try:
    # (DEPRECATED) Get all events for a given calendar in a given integration.
    api_response = api_instance.integrations_calendar_integration_id_calendars_id_calendar_events_get(integration_id, id_calendar, start_date, end_date, limit=limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_integration_id_calendars_id_calendar_events_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Integration ID as saved in the database | 
 **id_calendar** | **str**| Calendar ID as returned by the provider, it may be an e-mail address, for instance | 
 **start_date** | **str**| Smallest boundary date to search for calendar events | 
 **end_date** | **str**| Biggest boundary date to search for calendar events | 
 **limit** | **str**| Max results per page | [optional] 
 **page_token** | **str**| Token for next page. Used in pagination when the number of results exceed &#39;limit&#39; | [optional] 

### Return type

[**HandlercalendarEventsResponse**](HandlercalendarEventsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_integration_id_calendars_update_post`
> HandlercalendarFetchedCalendarsResponse integrations_calendar_integration_id_calendars_update_post(integration_id)

Updates calendar data according to provider API.

This endpoint uses the passed integration to get a provider and update all the calendars from that

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
integration_id = 56 # int | Integration ID as saved in the database

try:
    # Updates calendar data according to provider API.
    api_response = api_instance.integrations_calendar_integration_id_calendars_update_post(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_integration_id_calendars_update_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Integration ID as saved in the database | 

### Return type

[**HandlercalendarFetchedCalendarsResponse**](HandlercalendarFetchedCalendarsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_integration_id_delete`
> str integrations_calendar_integration_id_delete(integration_id)

Delete a given integration.

Executes logic deletion of an integration.

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
integration_id = 56 # int | Integration ID as saved in the database

try:
    # Delete a given integration.
    api_response = api_instance.integrations_calendar_integration_id_delete(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_integration_id_delete: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Integration ID as saved in the database | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `integrations_calendar_setup_get`
> integrations_calendar_setup_get(provider, return_to=return_to)

Get URL for setting up a calendar integration with given provider.

Set up an integration with a given provider, returning a URL to the said provider in order to

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
api_instance = toggl.CalendarApi(toggl.ApiClient(configuration))
provider = 'provider_example' # str | Calendar service provider which the calendars will be retrieved
return_to = 'return_to_example' # str | Page to which the user will be redirected after authenticating (optional)

try:
    # Get URL for setting up a calendar integration with given provider.
    api_instance.integrations_calendar_setup_get(provider, return_to=return_to)
except ApiException as e:
    print("Exception when calling CalendarApi->integrations_calendar_setup_get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Calendar service provider which the calendars will be retrieved | 
 **return_to** | **str**| Page to which the user will be redirected after authenticating | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

