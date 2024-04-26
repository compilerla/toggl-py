# toggl.AuthenticationApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_sso**](AuthenticationApi.md#delete_workspace_sso) | **DELETE** /workspaces/{workspace_id}/sso | Erase a workspace SSO configuration
[**get_saml2_login_url**](AuthenticationApi.md#get_saml2_login_url) | **GET** /auth/saml2/login | SAML2 Identity Provider URL
[**get_workspace_sso**](AuthenticationApi.md#get_workspace_sso) | **GET** /workspaces/{workspace_id}/sso | Workspace SSO configuration
[**me_sessions_delete**](AuthenticationApi.md#me_sessions_delete) | **DELETE** /me/sessions | Delete session
[**me_sessions_post**](AuthenticationApi.md#me_sessions_post) | **POST** /me/sessions | Create session
[**patch_workspace_sso**](AuthenticationApi.md#patch_workspace_sso) | **PATCH** /workspaces/{workspace_id}/sso | Enable/disable the Workspace SSO configuration
[**post_enable_sso**](AuthenticationApi.md#post_enable_sso) | **POST** /me/enable_sso | Confirm SSO enabling for user account
[**post_reset_token**](AuthenticationApi.md#post_reset_token) | **POST** /me/reset_token | ResetToken
[**post_saml2_callback**](AuthenticationApi.md#post_saml2_callback) | **POST** /auth/saml2/login/{workspace_id} | SAML2 Identity Provider Callback
[**post_signup**](AuthenticationApi.md#post_signup) | **POST** /signup | Signup
[**post_workspace_sso**](AuthenticationApi.md#post_workspace_sso) | **POST** /workspaces/{workspace_id}/sso | Workspace SSO configuration


## `delete_workspace_sso`
> str delete_workspace_sso(workspace_id)

Erase a workspace SSO configuration

Remove the SSO configuration for a workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Erase a workspace SSO configuration
    api_response = api_instance.delete_workspace_sso(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->delete_workspace_sso: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_saml2_login_url`
> Saml2LoginResponse get_saml2_login_url(email, client=client, state=state)

SAML2 Identity Provider URL

Returns the SSO URL given an email address for authenticating in an Identity Provider.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
email = 'email_example' # str | User email
client = 'client_example' # str | Client identification (webapp/toggl-button/client) TODO: add desktop identification (optional)
state = 'state_example' # str | State to be preserved when redirecting to Accounts API (optional)

try:
    # SAML2 Identity Provider URL
    api_response = api_instance.get_saml2_login_url(email, client=client, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_saml2_login_url: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User email | 
 **client** | **str**| Client identification (webapp/toggl-button/client) TODO: add desktop identification | [optional] 
 **state** | **str**| State to be preserved when redirecting to Accounts API | [optional] 

### Return type

[**Saml2LoginResponse**](Saml2LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_sso`
> SsoConfigResult get_workspace_sso(workspace_id)

Workspace SSO configuration

Returns the SSO configuration for a workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Workspace SSO configuration
    api_response = api_instance.get_workspace_sso(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_workspace_sso: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**SsoConfigResult**](SsoConfigResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `me_sessions_delete`
> me_sessions_delete()

Delete session

Deletes a session used for authenticating the current request

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()

try:
    # Delete session
    api_instance.me_sessions_delete()
except ApiException as e:
    print("Exception when calling AuthenticationApi->me_sessions_delete: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `me_sessions_post`
> ModelsUser me_sessions_post(session_post=session_post)

Create session

Creates a session and sets a cookie in the response header which can be used for authentication in API requests

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
session_post = toggl.MePostSessionHandlerRequestBody() # MePostSessionHandlerRequestBody | Session preferences (optional)

try:
    # Create session
    api_response = api_instance.me_sessions_post(session_post=session_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->me_sessions_post: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_post** | [**MePostSessionHandlerRequestBody**](MePostSessionHandlerRequestBody.md)| Session preferences | [optional] 

### Return type

[**ModelsUser**](ModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `patch_workspace_sso`
> SsoState patch_workspace_sso(workspace_id, settings)

Enable/disable the Workspace SSO configuration

Enable/Disable the SSO configuration for a workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
workspace_id = 56 # int | Numeric ID of the workspace
settings = toggl.SsoState() # SsoState | SAML2 enable flag

try:
    # Enable/disable the Workspace SSO configuration
    api_response = api_instance.patch_workspace_sso(workspace_id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->patch_workspace_sso: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **settings** | [**SsoState**](SsoState.md)| SAML2 enable flag | 

### Return type

[**SsoState**](SsoState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_enable_sso`
> str post_enable_sso(enable_sso_post)

Confirm SSO enabling for user account

Confirm SSO enabling in existing Toggl account after successful SSO

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
api_instance = toggl.AuthenticationApi(toggl.ApiClient(configuration))
enable_sso_post = toggl.SsoConfirmation() # SsoConfirmation | SSO enabling confirmation data

try:
    # Confirm SSO enabling for user account
    api_response = api_instance.post_enable_sso(enable_sso_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_enable_sso: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_sso_post** | [**SsoConfirmation**](SsoConfirmation.md)| SSO enabling confirmation data | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_reset_token`
> str post_reset_token()

ResetToken

Resets API token for the current user.

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
api_instance = toggl.AuthenticationApi(toggl.ApiClient(configuration))

try:
    # ResetToken
    api_response = api_instance.post_reset_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_reset_token: %s\n" % e)
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

## `post_saml2_callback`
> post_saml2_callback(workspace_id, saml_response, relay_state=relay_state)

SAML2 Identity Provider Callback

Receives the IdP Callback containing the SAML2 assertion with response of user authentication in the IdP.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
workspace_id = 56 # int | Numeric ID of the workspace
saml_response = 'saml_response_example' # str | SAML2 assertion with authentication response
relay_state = 'relay_state_example' # str | Encoded string containing client and host which originated the requests (optional)

try:
    # SAML2 Identity Provider Callback
    api_instance.post_saml2_callback(workspace_id, saml_response, relay_state=relay_state)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_saml2_callback: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **saml_response** | **str**| SAML2 assertion with authentication response | 
 **relay_state** | **str**| Encoded string containing client and host which originated the requests | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_signup`
> ModelsTogglUser post_signup(post_user)

Signup

Sign up as a new user.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
post_user = toggl.MePostUser() # MePostUser | authorization data

try:
    # Signup
    api_response = api_instance.post_signup(post_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_signup: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user** | [**MePostUser**](MePostUser.md)| authorization data | 

### Return type

[**ModelsTogglUser**](ModelsTogglUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_sso`
> ModelsSSOConfig post_workspace_sso(workspace_id, settings)

Workspace SSO configuration

Save the SSO configuration for a workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.AuthenticationApi()
workspace_id = 56 # int | Numeric ID of the workspace
settings = toggl.ModelsSSOConfig() # ModelsSSOConfig | SAML2 config parameters

try:
    # Workspace SSO configuration
    api_response = api_instance.post_workspace_sso(workspace_id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_workspace_sso: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **settings** | [**ModelsSSOConfig**](ModelsSSOConfig.md)| SAML2 config parameters | 

### Return type

[**ModelsSSOConfig**](ModelsSSOConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

