---
title: "PayPal payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "PayPal payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/paypal/payment-flow/'
aliases: 
    - /payment-methods/wallet/paypal/how-does-paypal-work
    - /payments/methods/wallet/paypal/payment-flow/
---

The table below shows a successful transaction flow from start to finish. 

**Note:** MultiSafepay does **not** collect funds for PayPal.

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects PayPal at checkout and is redirected to PayPal. | Initialized | Initialized |
| 2. | The customer authenticates their account and completes payment. |   |  |
| 3. | PayPal adds the funds to your PayPal business account. {{< br >}} **Note:** The transaction status is not updated because MultiSafepay doesn't collect the funds. | Completed | Initialized |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The payment was made in a currency that is not enabled in your PayPal business account. Enable the currency for the order status to change to completed. {{< br >}} You can only decline or authorize **Uncleared** transactions in your PayPal account. | Uncleared | Initialized |
| PayPal has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 14-day period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Initialized   |
| The refund was successfully processed.  | Completed      | Initialized   |
| The customer has requested a refund but there are not enough funds in your PayPal business account. | Uncleared | Initialized   |




