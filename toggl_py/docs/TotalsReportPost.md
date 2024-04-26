# TotalsReportPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | Whether the time entry is set as billable, optional, premium feature. | [optional] 
**client_ids** | **list[int]** | Client IDs, optional, filtering attribute. To filter records with no clients, use [null]. | [optional] 
**description** | **str** | Description, optional, filtering attribute. | [optional] 
**end_date** | **str** | End date, example time.DateOnly. Should be greater than Start date. | [optional] 
**granularity** | **str** | Totals granularity, optional, overrides resolution values. Possible values: day, week and month. | [optional] 
**group_ids** | **list[int]** | Group IDs, optional, filtering attribute. | [optional] 
**grouped** | **bool** | Whether time entries should be grouped, optional, default false. | [optional] 
**max_duration_seconds** | **int** | Max duration seconds, optional, filtering attribute. Time Audit only, should be greater than MinDurationSeconds. | [optional] 
**min_duration_seconds** | **int** | Min duration seconds, optional, filtering attribute. Time Audit only, should be less than MaxDurationSeconds. | [optional] 
**posted_fields** | **list[str]** |  | [optional] 
**project_ids** | **list[int]** | Project IDs, optional, filtering attribute. To filter records with no projects, use [null]. | [optional] 
**resolution** | **str** | Graph resolution, optional. Allow clients to explicitly request a resolution. | [optional] 
**rounding** | **int** | Whether time should be rounded, optional, default from workspace settings. | [optional] 
**rounding_minutes** | **int** | Rounding minutes value, optional, default from workspace settings. Should be 0, 1, 5, 6, 10, 12, 15, 30, 60 or 240. | [optional] 
**start_time** | **str** |  | [optional] 
**start_date** | **str** | Start date, example time.DateOnly. Should be less than End date. | [optional] 
**tag_ids** | **list[int]** | Tag IDs, optional, filtering attribute. To filter records with no tags, use [null]. | [optional] 
**task_ids** | **list[int]** | Task IDs, optional, filtering attribute. To filter records with no tasks, use [null]. | [optional] 
**time_entry_ids** | **list[int]** | Time entry IDs, optional. | [optional] 
**user_ids** | **list[int]** | User IDs, optional, filtering attribute. | [optional] 
**with_inline_rates** | **bool** | Whether results should be returned in line, optional, default false. | [optional] 
**with_graph** | **bool** | Whether Graph information should be loaded, optional,  default false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


