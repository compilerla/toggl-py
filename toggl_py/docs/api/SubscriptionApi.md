# toggl.SubscriptionApi

All URIs are relative to *https://localhost:8080/api/v9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organization_subscription**](SubscriptionApi.md#delete_organization_subscription) | **DELETE** /organizations/{organization_id}/subscription | Subscription
[**delete_workspace_subscription**](SubscriptionApi.md#delete_workspace_subscription) | **DELETE** /workspaces/{workspace_id}/subscription/{subscription_id} | Subscription
[**get_currencies**](SubscriptionApi.md#get_currencies) | **GET** /currencies | Currencies
[**get_organization_invoice**](SubscriptionApi.md#get_organization_invoice) | **GET** /organizations/{organization_id}/invoices/{invoice_uid}.pdf | InvoicePdf
[**get_organization_invoice_summary**](SubscriptionApi.md#get_organization_invoice_summary) | **GET** /organizations/{organization_id}/subscription/invoice_summary | Invoice Summary
[**get_organization_subscription**](SubscriptionApi.md#get_organization_subscription) | **GET** /organizations/{organization_id}/subscription | Subscription
[**get_public_subscription_plans**](SubscriptionApi.md#get_public_subscription_plans) | **GET** /workspaces/plans | Public Subscription Plans
[**get_workspace_currencies**](SubscriptionApi.md#get_workspace_currencies) | **GET** /workspaces/{workspace_id}/currencies | Get workspace currencies
[**get_workspace_customer**](SubscriptionApi.md#get_workspace_customer) | **GET** /workspaces/{workspace_id}/customer | Customer
[**get_workspace_features**](SubscriptionApi.md#get_workspace_features) | **GET** /workspaces/{workspace_id}/subscription/features | Features
[**get_workspace_features_selected**](SubscriptionApi.md#get_workspace_features_selected) | **GET** /workspaces/{workspace_id}/subscription/selected_features | SelectedFeatures
[**get_workspace_invoices**](SubscriptionApi.md#get_workspace_invoices) | **GET** /workspaces/{workspace_id}/invoices/{invoice_id}.pdf | InvoicePdf
[**get_workspace_payment_receipts**](SubscriptionApi.md#get_workspace_payment_receipts) | **GET** /workspaces/{workspace_id}/payment_receipts/{payment_id}.pdf | PaymentReceipts
[**get_workspace_payment_records**](SubscriptionApi.md#get_workspace_payment_records) | **GET** /workspaces/{workspace_id}/payment_records | PaymentRecords
[**get_workspace_plans**](SubscriptionApi.md#get_workspace_plans) | **GET** /workspaces/{workspace_id}/plans | WorkspacePlans
[**get_workspace_plans_pricing**](SubscriptionApi.md#get_workspace_plans_pricing) | **GET** /workspaces/{workspace_id}/plans/{plan_id} | WorkspacePlan
[**get_workspace_purchase_order_pdf**](SubscriptionApi.md#get_workspace_purchase_order_pdf) | **GET** /workspaces/{workspace_id}/subscription/purchase_orders/{purchase_order_id}.pdf | PurchaseOrderPdf
[**get_workspace_subscription**](SubscriptionApi.md#get_workspace_subscription) | **GET** /workspaces/{workspace_id}/subscription | Subscription
[**post_organization_plans_pricing_feedback**](SubscriptionApi.md#post_organization_plans_pricing_feedback) | **POST** /organizations/{organization_id}/pricing_plans/{pricing_plan_id}/feedback | Feedback
[**post_organization_purchase_order**](SubscriptionApi.md#post_organization_purchase_order) | **POST** /organizations/{organization_id}/subscription/purchase_orders | PurchaseOrders
[**post_organization_subscription**](SubscriptionApi.md#post_organization_subscription) | **POST** /organizations/{organization_id}/subscription | Subscription
[**post_organization_subscription_0**](SubscriptionApi.md#post_organization_subscription_0) | **POST** /organizations/{organization_id}/subscription/trial | Subscription
[**post_workspace_customer**](SubscriptionApi.md#post_workspace_customer) | **POST** /workspaces/{workspace_id}/customer/contact_detail | ContactDetails
[**post_workspace_plans_pricing_feedback**](SubscriptionApi.md#post_workspace_plans_pricing_feedback) | **POST** /workspaces/{workspace_id}/pricing_plans/{pricing_plan_id}/feedback | Feedback
[**post_workspace_purchase_order**](SubscriptionApi.md#post_workspace_purchase_order) | **POST** /workspaces/{workspace_id}/subscription/purchase_orders | PurchaseOrders
[**post_workspace_subscription**](SubscriptionApi.md#post_workspace_subscription) | **POST** /workspaces/{workspace_id}/subscription | Subscription
[**post_workspace_subscription_calculate**](SubscriptionApi.md#post_workspace_subscription_calculate) | **POST** /workspaces/{workspace_id}/subscription/calculate | SubscriptionCalculation
[**post_workspace_subscription_inc_accept**](SubscriptionApi.md#post_workspace_subscription_inc_accept) | **POST** /workspaces/{workspace_id}/subscription/inc_accept | IncAccept
[**put_organization_subscription**](SubscriptionApi.md#put_organization_subscription) | **PUT** /organizations/{organization_id}/subscription | Subscription
[**put_workspace_profile**](SubscriptionApi.md#put_workspace_profile) | **PUT** /workspaces/{workspace_id}/profile/{profile_id} | Profile


## `delete_organization_subscription`
> str delete_organization_subscription(organization_id, immediate_cancel)

Subscription

Cancels an existing subscription.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
immediate_cancel = 'immediate_cancel_example' # str | If true, the subscription is canceled immediately otherwise canceled at period end

try:
    # Subscription
    api_response = api_instance.delete_organization_subscription(organization_id, immediate_cancel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_organization_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **immediate_cancel** | **str**| If true, the subscription is canceled immediately otherwise canceled at period end | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `delete_workspace_subscription`
> str delete_workspace_subscription(workspace_id, subscription_id, feedback_data)

Subscription

Cancels the subscription and saves feedback if present.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
subscription_id = 56 # int | Numeric ID of the subscription.
feedback_data = toggl.ModelsPlanChangeFeedback() # ModelsPlanChangeFeedback | Feedback data.

try:
    # Subscription
    api_response = api_instance.delete_workspace_subscription(workspace_id, subscription_id, feedback_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_workspace_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **subscription_id** | **int**| Numeric ID of the subscription. | 
 **feedback_data** | [**ModelsPlanChangeFeedback**](ModelsPlanChangeFeedback.md)| Feedback data. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_currencies`
> list[ModelsCurrency] get_currencies()

Currencies

Returns a list of available currencies.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.SubscriptionApi()

try:
    # Currencies
    api_response = api_instance.get_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_currencies: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ModelsCurrency]**](ModelsCurrency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_invoice`
> str get_organization_invoice(organization_id, invoice_uid)

InvoicePdf

Returns a Invoice document in PDF form.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
invoice_uid = 'invoice_uid_example' # str | Numeric ID or string ID of the invoice.

try:
    # InvoicePdf
    api_response = api_instance.get_organization_invoice(organization_id, invoice_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_organization_invoice: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **invoice_uid** | **str**| Numeric ID or string ID of the invoice. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_invoice_summary`
> str get_organization_invoice_summary(organization_id, quantity=quantity, pricing_plan_tag=pricing_plan_tag)

Invoice Summary

Returns a summary of the next invoice for an Organization

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
quantity = 56 # int | Quantity of the subscription (optional)
pricing_plan_tag = 'pricing_plan_tag_example' # str | Pricing plan tag (optional)

try:
    # Invoice Summary
    api_response = api_instance.get_organization_invoice_summary(organization_id, quantity=quantity, pricing_plan_tag=pricing_plan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_organization_invoice_summary: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **quantity** | **int**| Quantity of the subscription | [optional] 
 **pricing_plan_tag** | **str**| Pricing plan tag | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_organization_subscription`
> SubscriptionOutData get_organization_subscription(organization_id)

Subscription

Returns subscription data.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.

try:
    # Subscription
    api_response = api_instance.get_organization_subscription(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_organization_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 

### Return type

[**SubscriptionOutData**](SubscriptionOutData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_public_subscription_plans`
> list[BillingFancyPlan] get_public_subscription_plans()

Public Subscription Plans

Lists Public subscription plans.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = toggl.SubscriptionApi()

try:
    # Public Subscription Plans
    api_response = api_instance.get_public_subscription_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_public_subscription_plans: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[BillingFancyPlan]**](BillingFancyPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_currencies`
> list[str] get_workspace_currencies(workspace_id)

Get workspace currencies

Get the currencies for a given workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Get workspace currencies
    api_response = api_instance.get_workspace_currencies(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_currencies: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

**list[str]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_customer`
> ModelsCustomer get_workspace_customer(workspace_id)

Customer

Allows to fetch customer data.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # Customer
    api_response = api_instance.get_workspace_customer(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**ModelsCustomer**](ModelsCustomer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_features`
> SubscriptionFeatureReturn get_workspace_features(workspace_id)

Features

Returns list of the features available for a workspace

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.

try:
    # Features
    api_response = api_instance.get_workspace_features(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_features: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 

### Return type

[**SubscriptionFeatureReturn**](SubscriptionFeatureReturn.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_features_selected`
> SubscriptionFeatureReturn get_workspace_features_selected(workspace_id)

SelectedFeatures

Returns list of the features assigned to the workspace

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.

try:
    # SelectedFeatures
    api_response = api_instance.get_workspace_features_selected(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_features_selected: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 

### Return type

[**SubscriptionFeatureReturn**](SubscriptionFeatureReturn.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_invoices`
> str get_workspace_invoices(workspace_id, invoice_id)

InvoicePdf

Returns an Invoice document in PDF form.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
invoice_id = 56 # int | Numeric ID of the invoice.

try:
    # InvoicePdf
    api_response = api_instance.get_workspace_invoices(workspace_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_invoices: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **invoice_id** | **int**| Numeric ID of the invoice. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_payment_receipts`
> str get_workspace_payment_receipts(workspace_id, payment_id)

PaymentReceipts

Returns payment receipt pdf file.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
payment_id = 56 # int | Numeric ID of the receipt

try:
    # PaymentReceipts
    api_response = api_instance.get_workspace_payment_receipts(workspace_id, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_payment_receipts: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **payment_id** | **int**| Numeric ID of the receipt | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_payment_records`
> list[ModelsPaymentRecord] get_workspace_payment_records(workspace_id)

PaymentRecords

Returns payment records.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # PaymentRecords
    api_response = api_instance.get_workspace_payment_records(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_payment_records: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

[**list[ModelsPaymentRecord]**](ModelsPaymentRecord.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_plans`
> str get_workspace_plans(workspace_id)

WorkspacePlans

Returns pricing plans for a workspace.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace

try:
    # WorkspacePlans
    api_response = api_instance.get_workspace_plans(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_plans: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_plans_pricing`
> list[BillingFancyPlan] get_workspace_plans_pricing(workspace_id, plan_id)

WorkspacePlan

Returns plans fitered by plan ID.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
plan_id = 56 # int | Numeric ID of the plan to get

try:
    # WorkspacePlan
    api_response = api_instance.get_workspace_plans_pricing(workspace_id, plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_plans_pricing: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **plan_id** | **int**| Numeric ID of the plan to get | 

### Return type

[**list[BillingFancyPlan]**](BillingFancyPlan.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_purchase_order_pdf`
> str get_workspace_purchase_order_pdf(workspace_id, purchase_order_id)

PurchaseOrderPdf

Returns a Purchase Order document in PDF form.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
purchase_order_id = 56 # int | Numeric ID of the purchase order.

try:
    # PurchaseOrderPdf
    api_response = api_instance.get_workspace_purchase_order_pdf(workspace_id, purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_purchase_order_pdf: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **purchase_order_id** | **int**| Numeric ID of the purchase order. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `get_workspace_subscription`
> SubscriptionOutData get_workspace_subscription(workspace_id)

Subscription

Returns subscription data.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.

try:
    # Subscription
    api_response = api_instance.get_workspace_subscription(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_workspace_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 

### Return type

[**SubscriptionOutData**](SubscriptionOutData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_plans_pricing_feedback`
> str post_organization_plans_pricing_feedback(organization_id, pricing_plan_id, comment=comment)

Feedback

Endpoint for client's feedback on change of a pricing plan. It triggers an e-mail message with comment content to support.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization
pricing_plan_id = 56 # int | Numeric ID of the old pricing_plan_id
comment = toggl.ModelsPlanChangeFeedback() # ModelsPlanChangeFeedback | Comment from the client on the pricing plan change (optional)

try:
    # Feedback
    api_response = api_instance.post_organization_plans_pricing_feedback(organization_id, pricing_plan_id, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_organization_plans_pricing_feedback: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization | 
 **pricing_plan_id** | **int**| Numeric ID of the old pricing_plan_id | 
 **comment** | [**ModelsPlanChangeFeedback**](ModelsPlanChangeFeedback.md)| Comment from the client on the pricing plan change | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_purchase_order`
> AccountingPurchaseOrderListItem post_organization_purchase_order(organization_id, organization_purchase_order_request)

PurchaseOrders

Create a Purchase Order document for an organization and send an email to the customer with a reference to the document.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
organization_purchase_order_request = toggl.PurchaseordersPayload() # PurchaseordersPayload | Input data for purchase order creation.

try:
    # PurchaseOrders
    api_response = api_instance.post_organization_purchase_order(organization_id, organization_purchase_order_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_organization_purchase_order: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **organization_purchase_order_request** | [**PurchaseordersPayload**](PurchaseordersPayload.md)| Input data for purchase order creation. | 

### Return type

[**AccountingPurchaseOrderListItem**](AccountingPurchaseOrderListItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_subscription`
> post_organization_subscription(organization_id, organization_subscription_request)

Subscription

Allows to create a new unified subscription for an organization.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
organization_subscription_request = toggl.SubscriptionCreateUnifiedSubsRequest() # SubscriptionCreateUnifiedSubsRequest | Input data for subscription creation.

try:
    # Subscription
    api_instance.post_organization_subscription(organization_id, organization_subscription_request)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_organization_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **organization_subscription_request** | [**SubscriptionCreateUnifiedSubsRequest**](SubscriptionCreateUnifiedSubsRequest.md)| Input data for subscription creation. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_organization_subscription_0`
> post_organization_subscription_0(organization_id)

Subscription

Allows to create a new unified subscription on initial 30-day trial for an organization.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.

try:
    # Subscription
    api_instance.post_organization_subscription_0(organization_id)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_organization_subscription_0: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_customer`
> ModelsContactDetail post_workspace_customer(workspace_id, contact_detail_request)

ContactDetails

Allows to save contact details.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
contact_detail_request = toggl.SubscriptionContactDetailRequest() # SubscriptionContactDetailRequest | Input data for contact details.

try:
    # ContactDetails
    api_response = api_instance.post_workspace_customer(workspace_id, contact_detail_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_customer: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **contact_detail_request** | [**SubscriptionContactDetailRequest**](SubscriptionContactDetailRequest.md)| Input data for contact details. | 

### Return type

[**ModelsContactDetail**](ModelsContactDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_plans_pricing_feedback`
> str post_workspace_plans_pricing_feedback(workspace_id, pricing_plan_id, comment=comment)

Feedback

Endpoint for client's feedback on change of a pricing plan. It triggers an e-mail message with comment content to support.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace
pricing_plan_id = 56 # int | Numeric ID of the old pricing_plan_id
comment = toggl.ModelsPlanChangeFeedback() # ModelsPlanChangeFeedback | Comment from the client on the pricing plan change (optional)

try:
    # Feedback
    api_response = api_instance.post_workspace_plans_pricing_feedback(workspace_id, pricing_plan_id, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_plans_pricing_feedback: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace | 
 **pricing_plan_id** | **int**| Numeric ID of the old pricing_plan_id | 
 **comment** | [**ModelsPlanChangeFeedback**](ModelsPlanChangeFeedback.md)| Comment from the client on the pricing plan change | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_purchase_order`
> AccountingPurchaseOrderListItem post_workspace_purchase_order(workspace_id, workspace_purchase_order_request)

PurchaseOrders

Create a Purchase Order document for a workspace and send an email to the customer with a reference to the document.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
workspace_purchase_order_request = toggl.PurchaseordersPayload() # PurchaseordersPayload | Input data for purchase order creation.

try:
    # PurchaseOrders
    api_response = api_instance.post_workspace_purchase_order(workspace_id, workspace_purchase_order_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_purchase_order: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **workspace_purchase_order_request** | [**PurchaseordersPayload**](PurchaseordersPayload.md)| Input data for purchase order creation. | 

### Return type

[**AccountingPurchaseOrderListItem**](AccountingPurchaseOrderListItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_subscription`
> ModelsSubscription post_workspace_subscription(workspace_id, workspace_subscription_request)

Subscription

Allows to create a new subscription, cancel existing one or change the pricing plan.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
workspace_subscription_request = toggl.SubscriptionPayload() # SubscriptionPayload | Input data for purchase order creation.

try:
    # Subscription
    api_response = api_instance.post_workspace_subscription(workspace_id, workspace_subscription_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **workspace_subscription_request** | [**SubscriptionPayload**](SubscriptionPayload.md)| Input data for purchase order creation. | 

### Return type

[**ModelsSubscription**](ModelsSubscription.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_subscription_calculate`
> SubscriptionCalculatedData post_workspace_subscription_calculate(workspace_id, calculation_data_request)

SubscriptionCalculation

Returns calculation of the subscription price for given pricing plan, period count, user count, currency, taxes etc.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
calculation_data_request = toggl.SubscriptionCalculateRequest() # SubscriptionCalculateRequest | Input data for calculation.

try:
    # SubscriptionCalculation
    api_response = api_instance.post_workspace_subscription_calculate(workspace_id, calculation_data_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_subscription_calculate: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **calculation_data_request** | [**SubscriptionCalculateRequest**](SubscriptionCalculateRequest.md)| Input data for calculation. | 

### Return type

[**SubscriptionCalculatedData**](SubscriptionCalculatedData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `post_workspace_subscription_inc_accept`
> str post_workspace_subscription_inc_accept(workspace_id)

IncAccept

Records user acceptance of Terms of Service.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.

try:
    # IncAccept
    api_response = api_instance.post_workspace_subscription_inc_accept(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->post_workspace_subscription_inc_accept: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_organization_subscription`
> put_organization_subscription(organization_id, organization_subscription_request)

Subscription

Allows to update existing unified subscription for an organization.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
organization_id = 56 # int | Numeric ID of the organization.
organization_subscription_request = toggl.SubscriptionUpdateUnifiedSubsRequest() # SubscriptionUpdateUnifiedSubsRequest | Input data for updating subscription.

try:
    # Subscription
    api_instance.put_organization_subscription(organization_id, organization_subscription_request)
except ApiException as e:
    print("Exception when calling SubscriptionApi->put_organization_subscription: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Numeric ID of the organization. | 
 **organization_subscription_request** | [**SubscriptionUpdateUnifiedSubsRequest**](SubscriptionUpdateUnifiedSubsRequest.md)| Input data for updating subscription. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## `put_workspace_profile`
> str put_workspace_profile(workspace_id, profile_id, feedback_data=feedback_data)

Profile

Allows to change profile (subscription). This endpoint will be deprecated.

### Example

```python
from __future__ import print_function
import time
import toggl
from toggl.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization: BasicAuth
configuration = toggl.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = toggl.SubscriptionApi(toggl.ApiClient(configuration))
workspace_id = 56 # int | Numeric ID of the workspace.
profile_id = 56 # int | Numeric ID of the profile (pricing plan).
feedback_data = toggl.ModelsPlanChangeFeedback() # ModelsPlanChangeFeedback | Feedback data. (optional)

try:
    # Profile
    api_response = api_instance.put_workspace_profile(workspace_id, profile_id, feedback_data=feedback_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->put_workspace_profile: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Numeric ID of the workspace. | 
 **profile_id** | **int**| Numeric ID of the profile (pricing plan). | 
 **feedback_data** | [**ModelsPlanChangeFeedback**](ModelsPlanChangeFeedback.md)| Feedback data. | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

