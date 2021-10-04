---
title: "TrustPay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "TrustPay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/trustpay/trustpay-how-does-it-work/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer authenticates their account and completes the payment. | | |
| 4. | The transaction is successful.  |  |  |
| 5. | MultiSafepay collects the funds and settles them in your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 10-day period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |








## How it works
If the transaction is approved by TrustPay, the transaction status will change to _completed_ and MultiSafepay will add the funds to the balance of your MultiSafepay account.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status | Transaction Status | Description                                                                                                          |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                             | 
| Completed    | Completed        | A successful Trustpay transaction has been received and the funds will be added to your MultiSafepay account balance.  | 
| Declined     | Declined         | Transaction has been rejected.                                                                                       | 
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                       | 
| Void         | Cancelled        | Transaction has been cancelled.                                                                                       | 


#### Refund flow

| Order Status   | Transaction Status | Description                              |
|----------------|------------------|------------------------------------------|
| Reserved       | Reserved         | A refund has been requested.             | 
| Completed      | Completed        | Refund has been successfully processed.  | 

The full API reference for TrustPay can be found [here](/api/#trustpay)

### Product Rules
Some rules may apply to certain payment methods. For TrustPay, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with TrustPay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful TrustPay transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* As a direct banking payment method, TrustPay has a different payment flow and therefore the setting of days or seconds active will have no influence. The customer processes the payment from his/her own banking environment. Full documentation can be found on our [lifetime of a payment link](/api/#adjust-payment-link-lifetimes) FAQ page

* As it is a standard bank transfer method, an expiry date exception for TrustPay transactions has been set to 10 days

* TrustPay transactions are processed in [Czech Koruna (CZK)](/faq/general/which-currencies-are-supported-by-multisafepay) 
   
 