---
title: "TrustPay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "TrustPay payment flow - MultiSafepay Docs"

short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/trustpay/payment-flow/'
aliases: 
    - /payment-methods/trustpay/trustpay-how-does-it-work/
    - /payments/methods/banks/trustpay/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="Order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects TrustPay at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/). | Initialized | Initialized |
| 2. | The customer authenticates their account and completes payment. | | |
| 3. | MultiSafepay collects the funds and settles them in your MultiSafepay balance.| Completed | Completed |

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
