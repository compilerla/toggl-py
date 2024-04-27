# SubscriptionContactDetailRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_address** | **str** |  | 
**company_city** | **str** |  | [optional] 
**company_name** | **str** |  | 
**contact_email** | **str** |  | 
**contact_person** | **str** |  | [optional] 
**country_id** | **int** |  | 
**country_subdivision_id** | **int** | CountrySubdivisionID is the ID of the country subdivision (state in USA) This field is required if country_id &#x3D;&#x3D; 235 (United states) | [optional] 
**sub_division** | [**ModelsSubdivision**](ModelsSubdivision.md) |  | [optional] 
**tax_number** | **str** |  | [optional] 
**zip_code** | **str** | ZIPCode field is required if country_id &#x3D;&#x3D; 235 (United states) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


