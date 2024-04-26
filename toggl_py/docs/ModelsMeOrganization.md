# ModelsMeOrganization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** | Whether the requester is an admin of the organization | [optional] 
**at** | **datetime** | Organization&#39;s last modification date | [optional] 
**created_at** | **datetime** | Organization&#39;s creation date | [optional] 
**id** | **int** | Organization ID | [optional] 
**is_multi_workspace_enabled** | **bool** | Is true when the organization option is_multi_workspace_enabled is set | [optional] 
**is_unified** | **bool** |  | [optional] 
**max_data_retention_days** | **int** | How far back free workspaces in this org can access data. | [optional] 
**max_workspaces** | **int** | Maximum number of workspaces allowed for the organization | [optional] 
**name** | **str** | Organization Name | [optional] 
**owner** | **bool** | Whether the requester is a the owner of the organization | [optional] 
**payment_methods** | **str** | Organization&#39;s subscription payment methods. Omitted if empty. | [optional] 
**permissions** | **str** |  | [optional] 
**pricing_plan_id** | **int** | Organization plan ID | [optional] 
**server_deleted_at** | **datetime** | Organization&#39;s delete date | [optional] 
**suspended_at** | **str** | Whether the organization is currently suspended | [optional] 
**trial_info** | [**ModelsTrialInfo**](ModelsTrialInfo.md) |  | [optional] 
**user_count** | **int** | Number of organization users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


