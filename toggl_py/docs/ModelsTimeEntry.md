# ModelsTimeEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | When was last updated | [optional] 
**billable** | **bool** | Whether the time entry is marked as billable | [optional] 
**client_name** | **str** | Related entities meta fields - if requested | [optional] 
**description** | **str** | Time Entry description, null if not provided at creation/update | [optional] 
**duration** | **int** | Time entry duration. For running entries should be negative, preferable -1 | [optional] 
**duronly** | **bool** | Used to create a TE with a duration but without a stop time, this field is deprecated for GET endpoints where the value will always be true. | [optional] 
**id** | **int** | Time Entry ID | [optional] 
**permissions** | **list[str]** | Permission list | [optional] 
**pid** | **int** | Project ID, legacy field | [optional] 
**project_active** | **bool** |  | [optional] 
**project_color** | **str** |  | [optional] 
**project_id** | **int** | Project ID. Can be null if project was not provided or project was later deleted | [optional] 
**project_name** | **str** |  | [optional] 
**server_deleted_at** | **str** | When was deleted, null if not deleted | [optional] 
**shared_with** | [**list[ModelsTimeEntrySharedWith]**](ModelsTimeEntrySharedWith.md) | Indicates who the time entry has been shared with | [optional] 
**start** | **str** | Start time in UTC | [optional] 
**stop** | **str** | Stop time in UTC, can be null if it&#39;s still running or created with \&quot;duration\&quot; and \&quot;duronly\&quot; fields | [optional] 
**tag_ids** | **list[int]** | Tag IDs, null if tags were not provided or were later deleted | [optional] 
**tags** | **list[str]** | Tag names, null if tags were not provided or were later deleted | [optional] 
**task_id** | **int** | Task ID. Can be null if task was not provided or project was later deleted | [optional] 
**task_name** | **str** |  | [optional] 
**tid** | **int** | Task ID, legacy field | [optional] 
**uid** | **int** | Time Entry creator ID, legacy field | [optional] 
**user_id** | **int** | Time Entry creator ID | [optional] 
**wid** | **int** | Workspace ID, legacy field | [optional] 
**workspace_id** | **int** | Workspace ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


