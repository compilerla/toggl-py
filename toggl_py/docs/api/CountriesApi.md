# toggl.CountriesApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](CountriesApi.md#get_countries) | **GET** /countries | Countries
[**get_countries_country_id_subdivisions**](CountriesApi.md#get_countries_country_id_subdivisions) | **GET** /countries/{country_id}/subdivisions | CountrySubdivisions


## `get_countries`
> list[ModelsCountry] get_countries()

Countries

Returns a list of existing countries

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.CountriesApi()

try:
    # Countries
    api_response = api_instance.get_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_countries: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsCountry]**](ModelsCountry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_countries_country_id_subdivisions`
> list[ModelsSubdivision] get_countries_country_id_subdivisions(country_id)

CountrySubdivisions

Returns a list of subdivisions for a specific country.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.CountriesApi()
country_id = 56 # int | country id

try:
    # CountrySubdivisions
    api_response = api_instance.get_countries_country_id_subdivisions(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_countries_country_id_subdivisions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **int**| country id | 

### Return type

[**list[ModelsSubdivision]**](ModelsSubdivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

