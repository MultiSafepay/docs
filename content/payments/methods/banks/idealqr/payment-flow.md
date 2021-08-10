---
title: "iDEAL QR payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "iDEAL QR payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/iDeal-qr.svg'
read_more: '.'
aliases: 
    - /payment-methods/idealqr/how-does-idealqr-work/
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
| 4. | The transaction is successful. {{< br >}} It cannot be reversed by the customer and settlement is guaranteed. | Completed | Completed |
| 5. | MultiSafepay collects the funds and adds them to your MultiSafepay balance.| | |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been canceled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |


