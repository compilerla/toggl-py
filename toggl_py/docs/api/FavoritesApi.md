# toggl.FavoritesApi

All URIs are relative to `https://https://api.track.toggl.com/api/v9`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_favorite**](FavoritesApi.md#create_favorite) | **POST** /me/favorites | Create a favorite
[**delete_favorite**](FavoritesApi.md#delete_favorite) | **DELETE** /me/favorites/{favorite_id} | Deletes a given favorite
[**get_favorites**](FavoritesApi.md#get_favorites) | **GET** /me/favorites | Get a list of favorites
[**post_favorites_suggestions**](FavoritesApi.md#post_favorites_suggestions) | **POST** /me/favorites/suggestions | Generates and returns a list of suggested favorites.
[**update_favorite**](FavoritesApi.md#update_favorite) | **PUT** /me/favorites | Update an array of favorites


## `create_favorite`
> ModelsFavorite create_favorite(favorite, meta=meta)

Create a favorite

This endpoint allows the creation of a favorite given some parameters. The workspace is required, as well as either description or project (no favorite without both will be accepted). The user is also required, but it already goes in the authentication. Also, the user must have access to all resources being referenced in the favorite attributes, and these resources should have valid relationships. For instance, if you want a favorite in a given workspace and with some tags, the tags must belong to that workspace. In case of user having no access to an attribute, a 403 status is returned, if the attributes don't relate correctly between themselves the status returned will be 400.

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
api_instance = toggl.FavoritesApi(toggl.ApiClient(configuration))
favorite = toggl.HandlerfavoritesPayload() # HandlerfavoritesPayload | Favorite details
meta = true # bool | Should the response contain data for meta entities (optional)

try:
    # Create a favorite
    api_response = api_instance.create_favorite(favorite, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->create_favorite: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite** | [**HandlerfavoritesPayload**](HandlerfavoritesPayload.md)| Favorite details | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 

### Return type

[**ModelsFavorite**](ModelsFavorite.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_favorite`
> delete_favorite()

Deletes a given favorite

Deletes a given favorite logically from database, as well as its tags.

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
api_instance = toggl.FavoritesApi(toggl.ApiClient(configuration))

try:
    # Deletes a given favorite
    api_instance.delete_favorite()
except ApiException as e:
    print("Exception when calling FavoritesApi->delete_favorite: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_favorites`
> list[ModelsFavorite] get_favorites(since=since)

Get a list of favorites

Gets all favorites for the requesting user

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
api_instance = toggl.FavoritesApi(toggl.ApiClient(configuration))
since = 56 # int | Retrieve favorites created/deleted since this date using UNIX timestamp. (optional)

try:
    # Get a list of favorites
    api_response = api_instance.get_favorites(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->get_favorites: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Retrieve favorites created/deleted since this date using UNIX timestamp. | [optional] 

### Return type

[**list[ModelsFavorite]**](ModelsFavorite.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_favorites_suggestions`
> list[ModelsFavorite] post_favorites_suggestions()

Generates and returns a list of suggested favorites.

It will create 3 favorites based on past user's TE activity and return them. Suggested favorites will be created only once for a given user, and only if the user has never created a favorite before (either manually or by a previous suggestion request). If there is no past TE data there won't be suggested favorites either.

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
api_instance = toggl.FavoritesApi(toggl.ApiClient(configuration))

try:
    # Generates and returns a list of suggested favorites.
    api_response = api_instance.post_favorites_suggestions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->post_favorites_suggestions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsFavorite]**](ModelsFavorite.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `update_favorite`
> ModelsFavorite update_favorite(favorite, meta=meta)

Update an array of favorites

This endpoint allows updating an array of favorites. It follow all the requirements and behavior from the [post] (Create Favorite) counterpart.

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
api_instance = toggl.FavoritesApi(toggl.ApiClient(configuration))
favorite = toggl.HandlerfavoritesPayload() # HandlerfavoritesPayload | Favorite details
meta = true # bool | Should the response contain data for meta entities (optional)

try:
    # Update an array of favorites
    api_response = api_instance.update_favorite(favorite, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->update_favorite: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite** | [**HandlerfavoritesPayload**](HandlerfavoritesPayload.md)| Favorite details | 
 **meta** | **bool**| Should the response contain data for meta entities | [optional] 

### Return type

[**ModelsFavorite**](ModelsFavorite.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

