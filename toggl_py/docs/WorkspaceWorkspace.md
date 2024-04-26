# WorkspaceWorkspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** | Current user is workspace admin | [optional] 
**api_token** | **str** | deprecated | [optional] 
**at** | **str** | Timestamp of last workspace change | [optional] 
**business_ws** | **bool** | Workspace on Premium subscription | [optional] 
**csv_upload** | [**ModelsCsvUpload**](ModelsCsvUpload.md) | CSV upload data | [optional] 
**default_currency** | **str** | Default currency, premium feature, optional, only for existing WS, will be &#39;USD&#39; initially | [optional] 
**default_hourly_rate** | **float** | The default hourly rate, premium feature, optional, only for existing WS, will be 0.0 initially | [optional] 
**hide_start_end_times** | **bool** |  | [optional] 
**ical_enabled** | **bool** | Calendar integration enabled | [optional] 
**ical_url** | **str** | URL of calendar | [optional] 
**id** | **int** | Identifier of the workspace | [optional] 
**last_modified** | **str** | Last modification of data in the workspace | [optional] 
**logo_url** | **str** | URL of workspace logo | [optional] 
**max_data_retention_days** | **int** | How far back free workspaces can access data. | [optional] 
**name** | **str** | Name of the workspace | [optional] 
**only_admins_may_create_projects** | **bool** | Only admins will be able to create projects, optional, only for existing WS, will be false initially | [optional] 
**only_admins_may_create_tags** | **bool** | Only admins will be able to create tags, optional, only for existing WS, will be false initially | [optional] 
**only_admins_see_billable_rates** | **bool** | Whether only admins will be able to see billable rates, premium feature, optional, only for existing WS. Will be false initially | [optional] 
**only_admins_see_team_dashboard** | **bool** | Only admins will be able to see the team dashboard, optional, only for existing WS, will be false initially | [optional] 
**organization_id** | **int** | Identifier of the organization | [optional] 
**permissions** | **str** | Permissions list | [optional] 
**premium** | **bool** | Workspace on Starter subscription | [optional] 
**profile** | **int** | deprecated | [optional] 
**projects_billable_by_default** | **bool** | New projects billable by default | [optional] 
**projects_private_by_default** | **bool** | Workspace setting for default project visbility. | [optional] 
**rate_last_updated** | **str** | Timestamp of last workspace rate update | [optional] 
**reports_collapse** | **bool** | Whether reports should be collapsed by default, optional, only for existing WS, will be true initially | [optional] 
**role** | **str** | Role of the current user in the workspace | [optional] 
**rounding** | **int** | Default rounding, premium feature, optional, only for existing WS. 0 - nearest, 1 - round up, -1 - round down | [optional] 
**rounding_minutes** | **int** | Default rounding in minutes, premium feature, optional, only for existing WS | [optional] 
**server_deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**subscription** | [**ModelsSubscription**](ModelsSubscription.md) | deprecated | [optional] 
**suspended_at** | **datetime** | Timestamp of suspension | [optional] 
**te_constraints** | [**ModelsTimeEntryConstraints**](ModelsTimeEntryConstraints.md) | Time entry constraints setting | [optional] 
**working_hours_in_minutes** | **int** | Working hours in minutes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


