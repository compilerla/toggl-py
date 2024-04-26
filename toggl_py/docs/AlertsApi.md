# toggl.AlertsApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alerts**](AlertsApi.md#delete_alerts) | **DELETE** /workspaces/{workspace_id}/alerts/{alert_id} | Alerts
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /workspaces/{workspace_id}/alerts | Alerts
[**post_alerts**](AlertsApi.md#post_alerts) | **POST** /workspaces/{workspace_id}/alerts | Alerts
[**put_alerts**](AlertsApi.md#put_alerts) | **PUT** /workspaces/{workspace_id}/alerts/{alert_id} | Alerts


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
api_instance = toggl.AlertsApi(toggl.ApiClient(configuration))

try:
    # Alerts
    api_response = api_instance.delete_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alerts: %s\n" % e)
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

## `get_alerts`
> list[ModelsAlert] get_alerts()

Alerts

Returns a list of existing alerts

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AlertsApi()

try:
    # Alerts
    api_response = api_instance.get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alerts: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsAlert]**](ModelsAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = toggl.AlertsApi(toggl.ApiClient(configuration))
request = NULL # object | Alert data

try:
    # Alerts
    api_response = api_instance.post_alerts(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->post_alerts: %s\n" % e)
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

## `put_alerts`
> ModelsAlert put_alerts(request)

Alerts

Handles PUT alert requests.

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
api_instance = toggl.AlertsApi(toggl.ApiClient(configuration))
request = NULL # object | Alert data

try:
    # Alerts
    api_response = api_instance.put_alerts(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->put_alerts: %s\n" % e)
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

