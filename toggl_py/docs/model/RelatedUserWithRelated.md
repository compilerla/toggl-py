# RelatedUserWithRelated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | will be omitted if empty | [optional] 
**at** | **datetime** |  | [optional] 
**authorization_updated_at** | **str** | AuthorizationUpdatedAt timestamp when the authorization user session object was last updated. | [optional] 
**beginning_of_week** | **int** |  | [optional] 
**clients** | [**list[ModelsClient]**](ModelsClient.md) | Clients, null if with_related_data was not set to true or if the user does not have any clients | [optional] 
**country_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**default_workspace_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**has_password** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**intercom_hash** | **str** | will be omitted if empty | [optional] 
**oauth_providers** | **list[str]** |  | [optional] 
**openid_email** | **str** |  | [optional] 
**openid_enabled** | **bool** |  | [optional] 
**options** | [**ModelsOptions**](ModelsOptions.md) | will be omitted if empty | [optional] 
**projects** | [**list[ModelsProject]**](ModelsProject.md) | Projects, null if with_related_data was not set to true or if the user does not have any projects | [optional] 
**tags** | [**list[ModelsTag]**](ModelsTag.md) | Tags, null if with_related_data was not set to true, or if the user does not have any tags | [optional] 
**tasks** | [**list[ModelsTask]**](ModelsTask.md) | Tasks, null if with_related_data was not set to true or if the user does not have any tasks | [optional] 
**time_entries** | [**list[ModelsTimeEntry]**](ModelsTimeEntry.md) | TimeEntries, null if with_related_data was not set to true or if the user does not have any time entries | [optional] 
**timezone** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**workspaces** | [**list[WorkspaceWorkspace]**](WorkspaceWorkspace.md) | Workspaces, null if with_related_data was not set to true or if the user does not have any workspaces | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


