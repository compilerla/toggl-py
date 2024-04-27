# SubscriptionOutData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** |  | [optional] 
**billing_period_in_months** | **int** |  | [optional] 
**campaign_available** | **bool** |  | [optional] 
**cancel_date** | **str** |  | [optional] 
**card_details** | [**ModelsCardDetails**](ModelsCardDetails.md) |  | [optional] 
**company_id** | **int** |  | [optional] 
**contact_details** | [**ModelsContactDetail**](ModelsContactDetail.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**current_period_ends_at** | **str** |  | [optional] 
**current_period_starts_at** | **str** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**end_date** | **str** | Deprecated: this field will be replaced by CurrentPeriodEndsAt | [optional] 
**enterprise** | **bool** |  | [optional] 
**is_subscription_beta** | **bool** | temporary flag which is true iff there is at least one admin in the organization, who has the &#x60;multi_workspace_payments&#x60; beta flag enabled | [optional] 
**is_unified** | **bool** |  | [optional] 
**last_invoice** | [**SubscriptionInvoiceInfo**](SubscriptionInvoiceInfo.md) |  | [optional] 
**last_payment** | [**ModelsPaymentInfo**](ModelsPaymentInfo.md) |  | [optional] 
**last_pricing_plan_id** | **int** |  | [optional] 
**new_signup_trial** | **bool** |  | [optional] 
**next_payment_date** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**pricing_plan_id** | **int** | Legacy fields (kept for compatibility with FE) | [optional] 
**renewal_at** | **str** |  | [optional] 
**renewal_date** | **str** |  | [optional] 
**seat_cost_in_cents** | **int** |  | [optional] 
**seats** | **int** |  | [optional] 
**site** | **str** |  | [optional] 
**start_date** | **str** | Deprecated: this field will be replaced by CurrentPeriodStartsAt | [optional] 
**state** | **str** |  | [optional] 
**subscription_created_at** | **str** |  | [optional] 
**subscription_period** | [**ModelsPeriod**](ModelsPeriod.md) |  | [optional] 
**trial_available** | **bool** |  | [optional] 
**trial_end_date** | **str** |  | [optional] 
**trial_start_date** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


