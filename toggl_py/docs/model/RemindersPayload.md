# RemindersPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Frequency of the reminder in days, should be either 1 or 7 | [optional] 
**group_ids** | **list[int]** | Group IDs to send the reminder to, can be omitted if user_ids is provided | [optional] 
**threshold** | **float** | Threshold is the number of hours after which the reminder will be sent | [optional] 
**user_ids** | **list[int]** | User IDs to send the reminder to, can be omitted if group_ids is provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


