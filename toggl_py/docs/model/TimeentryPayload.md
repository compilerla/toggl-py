# TimeentryPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | Whether the time entry is marked as billable, optional, default false | [optional] 
**created_with** | **str** | Must be provided when creating a time entry and should identify the service/application used to create it | [optional] 
**description** | **str** | Time entry description, optional | [optional] 
**duration** | **int** | Time entry duration. For running entries should be negative, preferable -1 | [optional] 
**duronly** | **bool** | Deprecated: Used to create a time entry with a duration but without a stop time. This parameter can be ignored. | [optional] 
**pid** | **int** | Project ID, legacy field | [optional] 
**project_id** | **int** | Project ID, optional | [optional] 
**shared_with_user_ids** | **list[int]** | List of user IDs to share this time entry with | [optional] 
**start** | **str** | Start time in UTC, required for creation. Format: 2006-01-02T15:04:05Z | [optional] 
**start_date** | **str** | If provided during creation, the date part will take precedence over the date part of \&quot;start\&quot;. Format: 2006-11-07 | [optional] 
**stop** | **str** | Stop time in UTC, can be omitted if it&#39;s still running or created with \&quot;duration\&quot;. If \&quot;stop\&quot; and \&quot;duration\&quot; are provided, values must be consistent (start + duration &#x3D;&#x3D; stop) | [optional] 
**tag_action** | **str** | Can be \&quot;add\&quot; or \&quot;delete\&quot;. Used when updating an existing time entry | [optional] 
**tag_ids** | **list[int]** | IDs of tags to add/remove | [optional] 
**tags** | **list[str]** | Names of tags to add/remove. If name does not exist as tag, one will be created automatically | [optional] 
**task_id** | **int** | Task ID, optional | [optional] 
**tid** | **int** | Task ID, legacy field | [optional] 
**uid** | **int** | Time Entry creator ID, legacy field | [optional] 
**user_id** | **int** | Time Entry creator ID, if omitted will use the requester user ID | [optional] 
**wid** | **int** | Workspace ID, legacy field | [optional] 
**workspace_id** | **int** | Workspace ID, required | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


