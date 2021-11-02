---
title: "Paysafecard payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Paysafecard payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/paysafecard/payment-flow/'
aliases: 
    - /payment-methods/paysafecard/how-does-paysafecard-work
    - /payments/methods/prepaid-cards/paysafecard/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects Paysafecard at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/). | Initialized | Initialized |
| 2. | The customer enters the 16-digit PIN code on the Paysafecard voucher, and completes the payment. | | |
| 3. | MultiSafepay collects the funds and settles them in your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been declined. | Declined   | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 3-hour period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |
