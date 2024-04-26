# WorkspacePayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins** | **list[int]** | List of admins, optional | [optional] 
**default_currency** | **str** | Default currency, premium feature, optional, only for existing WS, will be &#39;USD&#39; initially | [optional] 
**default_hourly_rate** | **float** | The default hourly rate, premium feature, optional, only for existing WS, will be 0.0 initially | [optional] 
**initial_pricing_plan** | **int** | The subscription plan for the workspace, deprecated | [optional] 
**name** | **str** | Workspace name | [optional] 
**only_admins_may_create_projects** | **bool** | Only admins will be able to create projects, optional, only for existing WS, will be false initially | [optional] 
**only_admins_may_create_tags** | **bool** | Only admins will be able to create tags, optional, only for existing WS, will be false initially | [optional] 
**only_admins_see_billable_rates** | **bool** | Whether only admins will be able to see billable rates, premium feature, optional, only for existing WS. Will be false initially | [optional] 
**only_admins_see_team_dashboard** | **bool** | Only admins will be able to see the team dashboard, optional, only for existing WS, will be false initially | [optional] 
**projects_billable_by_default** | **bool** | Whether projects will be set as billable by default, premium feature, optional, only for existing WS. Will be true initially | [optional] 
**projects_private_by_default** | **bool** | Whether projects will be set to private by default, optional. Will be true initially. | [optional] 
**rate_change_mode** | **str** | The rate change mode, premium feature, optional, only for existing WS. Can be \&quot;start-today\&quot;, \&quot;override-current\&quot;, \&quot;override-all\&quot; | [optional] 
**reports_collapse** | **bool** | Whether reports should be collapsed by default, optional, only for existing WS, will be true initially | [optional] 
**rounding** | **int** | Default rounding, premium feature, optional, only for existing WS | [optional] 
**rounding_minutes** | **int** | Default rounding in minutes, premium feature, optional, only for existing WS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


