# toggl.InvitationsApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invitations**](InvitationsApi.md#get_invitations) | **GET** /invitations/{invitation_code} | Get an invitation
[**post_organization_accept_invitation**](InvitationsApi.md#post_organization_accept_invitation) | **POST** /organizations/invitations/{invitation_code}/accept | Accepts invitation
[**post_organization_invitation**](InvitationsApi.md#post_organization_invitation) | **POST** /organizations/{organization_id}/invitations | Creates a new invitation for the user
[**post_reject_invitation**](InvitationsApi.md#post_reject_invitation) | **POST** /organizations/invitations/{invitation_code}/reject | Rejects invitation
[**put_invitation**](InvitationsApi.md#put_invitation) | **PUT** /organizations/{organization_id}/invitations/{invitation_code}/resend | Resends user their invitation


## `get_invitations`
> ModelsSSOInvitation get_invitations(invitation_code)

Get an invitation

Returns an invitation data by code.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.InvitationsApi()
invitation_code = 'invitation_code_example' # str | Invitation code

try:
    # Get an invitation
    api_response = api_instance.get_invitations(invitation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->get_invitations: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_code** | **str**| Invitation code | 

### Return type

[**ModelsSSOInvitation**](ModelsSSOInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_accept_invitation`
> str post_organization_accept_invitation(inviutation_code)

Accepts invitation

User connected with invitation is marked as joined, email is sent to the inviter.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.InvitationsApi()
inviutation_code = 'inviutation_code_example' # str | Invitation code

try:
    # Accepts invitation
    api_response = api_instance.post_organization_accept_invitation(inviutation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->post_organization_accept_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inviutation_code** | **str**| Invitation code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_invitation`
> InvitationResult post_organization_invitation(organization_id, post_invitation_request)

Creates a new invitation for the user

Creates a new invitation for the user.

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
api_instance = toggl.InvitationsApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
post_invitation_request = toggl.InvitationPost() # InvitationPost | Input data for invitation creation

try:
    # Creates a new invitation for the user
    api_response = api_instance.post_organization_invitation(organization_id, post_invitation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->post_organization_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **post_invitation_request** | [**InvitationPost**](InvitationPost.md)| Input data for invitation creation | 

### Return type

[**InvitationResult**](InvitationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_reject_invitation`
> str post_reject_invitation(inviutation_code)

Rejects invitation

User connected with invitation is marked as deleted.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.InvitationsApi()
inviutation_code = 'inviutation_code_example' # str | Invitation code

try:
    # Rejects invitation
    api_response = api_instance.post_reject_invitation(inviutation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->post_reject_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inviutation_code** | **str**| Invitation code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_invitation`
> str put_invitation(organization_id, invitation_code)

Resends user their invitation

Resend invitation email to user.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.InvitationsApi()
organization_id = 56 # int | Organization ID
invitation_code = 'invitation_code_example' # str | Invitation code

try:
    # Resends user their invitation
    api_response = api_instance.put_invitation(organization_id, invitation_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->put_invitation: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization ID | 
 **invitation_code** | **str**| Invitation code | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

