# ModelsProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the project is active or archived | [optional] 
**actual_hours** | **int** | Actual hours | [optional] 
**actual_seconds** | **int** | Actual seconds | [optional] 
**at** | **str** | Last updated date | [optional] 
**auto_estimates** | **bool** | Whether estimates are based on task hours, premium feature | [optional] 
**billable** | **bool** | Whether the project is billable, premium feature | [optional] 
**cid** | **int** | Client ID legacy field | [optional] 
**client_id** | **int** | Client ID | [optional] 
**color** | **str** | Color | [optional] 
**created_at** | **str** | Creation date | [optional] 
**currency** | **str** | Currency, premium feature | [optional] 
**current_period** | [**ModelsRecurringPeriod**](ModelsRecurringPeriod.md) | Current project period, premium feature | [optional] 
**end_date** | **str** | End date | [optional] 
**estimated_hours** | **int** | Estimated hours | [optional] 
**estimated_seconds** | **int** | Estimated seconds | [optional] 
**fixed_fee** | **float** | Fixed fee, premium feature | [optional] 
**id** | **int** | Project ID | [optional] 
**is_private** | **bool** | Whether the project is private | [optional] 
**name** | **str** | Name | [optional] 
**permissions** | **str** |  | [optional] 
**rate** | **float** | Hourly rate | [optional] 
**rate_last_updated** | **str** | Last date for rate change | [optional] 
**recurring** | **bool** | Whether the project is recurring, premium feature | [optional] 
**recurring_parameters** | [**list[ModelsRecurringProjectParameters]**](ModelsRecurringProjectParameters.md) | Project recurring parameters, premium feature | [optional] 
**server_deleted_at** | **str** | Deletion date | [optional] 
**start_date** | **str** | Start date | [optional] 
**status** | **str** | Status of the project (upcoming, active, ended, archived, deleted) | [optional] 
**template** | **bool** | Whether the project is used as template, premium feature | [optional] 
**template_id** | **int** | Template ID | [optional] 
**wid** | **int** | Workspace ID legacy field | [optional] 
**workspace_id** | **int** | Workspace ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


