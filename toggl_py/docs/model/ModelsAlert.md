# ModelsAlert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[ModelsAlertError]**](ModelsAlertError.md) |  | [optional] 
**id** | **int** |  | [optional] 
**object_type** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**receiver_groups** | **str** |  | [optional] 
**receiver_roles** | **str** |  | [optional] 
**receiver_users** | **str** |  | [optional] 
**receivers** | **int** |  | [optional] 
**source_kind** | **str** |  | [optional] 
**threshold** | **int** |  | [optional] 
**threshold_type** | **str** |  | [optional] 
**thresholds** | **str** | using pq types is a workaround to enable reading postgres arrays into go types we should wrap these pq types to avoid polluting our domain | [optional] 
**wid** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


