---
title: "Postepay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Postepay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/postepay/payment-flow/'
aliases:
    - /payments/methods/credit-and-debit-cards/postepay/payment-flow/
    - /postepay/payment-flow/
---

The table below shows a successful transaction flow from start to finish.  

{{< details title="Order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects Postepay at checkout and is redirected to a MultiSafepay payment page.  | Initialized | Initialized |
| 2. | The customer enters their card details, verifies their identify via [Verified by Visa](/security-and-legal/payment-regulations/about-3d-secure/) or Mastercard [SecureCode](/security-and-legal/payment-regulations/about-3d-secure/), and completes the payment. | | |
| 3. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 4. | You need to manually [authorize or decline the transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). | Uncleared | Uncleared |
| 5. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer's bank has declined the transaction (see possible reasons below). {{< br >}} For more information, see [Declined status](/faq/general/declined-status/). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 1-hour period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |



