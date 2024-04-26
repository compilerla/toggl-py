# ModelsOrganizationWorkspaceUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Flag indicating if user accepted the invitation | [optional] 
**admin** | **bool** | Flag indicating if user is admin | [optional] 
**at** | **str** | Timestamp of the last update | [optional] 
**avatar_file_name** | **str** | URL of avatar | [optional] 
**email** | **str** | Email of the user | [optional] 
**group_ids** | [**UtilsInt64Slice**](UtilsInt64Slice.md) | List of groups the user belongs to | [optional] 
**id** | **int** | Identifier of the user inside workspace | [optional] 
**inactive** | **bool** | Flag indicating if user was deactivated by admin of the workspace | [optional] 
**invitation_code** | **str** | internal | [optional] 
**invite_url** | **str** | internal | [optional] 
**is_direct** | **bool** | Flag indicating if user is a direct member of the workspace (is not assigned to the workspace using the group) | [optional] 
**labour_cost** | **int** | Labour cost assigned to the user | [optional] 
**name** | **str** | Name of the user | [optional] 
**organization_admin** | **bool** | Flag indicating if user is admin inside organization | [optional] 
**rate** | **float** | Rate assigned to the user | [optional] 
**rate_last_updated** | **str** | Timestamp of the last rate update | [optional] 
**role** | **str** | Role of the user | [optional] 
**timezone** | **str** | Timezone of the user | [optional] 
**user_id** | **int** | Global user identifier | [optional] 
**working_hours_in_minutes** | **int** | Working hours value in minutes | [optional] 
**workspace_admin** | **bool** | Flag indicating if user is admin inside workspace | [optional] 
**workspace_id** | **int** | Workspace identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


