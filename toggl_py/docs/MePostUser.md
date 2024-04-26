# MePostUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **int** | User&#39;s country ID, if not provided will be United States | [optional] 
**created_with** | **str** | Should describe the application/service that is using the API | [optional] 
**email** | **str** | Email for new user account | 
**full_name** | **str** | User&#39;s full name, if not provided will be derived from the email address | [optional] 
**invitation_code** | **str** | Optional, used when creating account through an invitation | [optional] 
**password** | **str** | Password for new user account | 
**timezone** | **str** | User&#39;s timezone, if not provided will be UTC | [optional] 
**tos_accepted** | **bool** | Whether the Terms of Service have been accepted | 
**workspace** | [**MePostInitialWorkspace**](MePostInitialWorkspace.md) | Optional workspace settings, used when creating account not through an invitation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


