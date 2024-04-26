# RequestsProjectProfitability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **bool** | Whether the project is set as billable, optional, premium feature. | [optional] 
**client_ids** | **list[int]** | Client IDs, optional. A nil entry on this list means that only projects without client will be selected. | [optional] 
**currency** | **str** | Currency, example: \&quot;usd\&quot;. | 
**end_date** | **str** | End date, optional, example: time.DateOnly. Should be greater than Start date. | [optional] 
**project_ids** | **list[int]** | Project IDS, optional. | [optional] 
**resolution** | **str** | Resolution, optional. Can be \&quot;day\&quot;, \&quot;week\&quot; or \&quot;month\&quot;. | [optional] 
**rounding** | **int** | Rounding, optional, duration rounding settings, premium feature. | [optional] 
**rounding_minutes** | **int** | RoundingMinutes, optional, duration rounding minutes settings, premium feature. | [optional] 
**start_date** | **str** | Start date, optional, example: time.DateOnly. Should be less than End date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


