# WeeklyExportPDFPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | Whether the time entry is set as billable, optional, premium feature. | [optional] 
**calculate** | **str** | Calculate option, optional. Can be by time or amounts. | [optional] 
**cents_separator** | **str** |  | [optional] 
**client_ids** | **list[int]** | Client IDs, optional, filtering attribute. To filter records with no clients, use [null]. | [optional] 
**date_format** | **str** | Date format, optional, default \&quot;MM/DD/YYYY\&quot;. Can be \&quot;MM/DD/YYYY\&quot;, \&quot;DD-MM-YYYY\&quot;, \&quot;MM-DD-YYYY\&quot;, \&quot;YYYY-MM-DD\&quot;, \&quot;DD/MM/YYYY\&quot; or \&quot;DD.MM.YYYY\&quot;. | [optional] 
**description** | **str** | Description, optional, filtering attribute. | [optional] 
**duration_format** | **str** | Duration format, optional, default \&quot;classic\&quot;. Can be \&quot;classic\&quot;, \&quot;decimal\&quot; or \&quot;improved\&quot;. | [optional] 
**end_date** | **str** | End date, example time.DateOnly. Should be greater than Start date. | [optional] 
**group_by_task** | **bool** | GroupByTask tells the weekly report to return the data grouped by all the usual groups plus planned task. | [optional] 
**group_ids** | **list[int]** | Group IDs, optional, filtering attribute. | [optional] 
**grouping** | **str** | Grouping option, optional. | [optional] 
**max_duration_seconds** | **int** | Max duration seconds, optional, filtering attribute. Time Audit only, should be greater than MinDurationSeconds. | [optional] 
**min_duration_seconds** | **int** | Min duration seconds, optional, filtering attribute. Time Audit only, should be less than MaxDurationSeconds. | [optional] 
**posted_fields** | **list[str]** |  | [optional] 
**project_ids** | **list[int]** | Project IDs, optional, filtering attribute. To filter records with no projects, use [null]. | [optional] 
**rounding** | **int** | Whether time should be rounded, optional, default from workspace settings. | [optional] 
**rounding_minutes** | **int** | Rounding minutes value, optional, default from workspace settings. Should be 0, 1, 5, 6, 10, 12, 15, 30, 60 or 240. | [optional] 
**start_time** | **str** |  | [optional] 
**start_date** | **str** | Start date, example time.DateOnly. Should be less than End date. | [optional] 
**tag_ids** | **list[int]** | Tag IDs, optional, filtering attribute. To filter records with no tags, use [null]. | [optional] 
**task_ids** | **list[int]** | Task IDs, optional, filtering attribute. To filter records with no tasks, use [null]. | [optional] 
**time_entry_ids** | **list[int]** | TimeEntryIDs filters by time entries. This was added to support retro-compatibility with reports v2. | [optional] 
**user_ids** | **list[int]** | User IDs, optional, filtering attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


