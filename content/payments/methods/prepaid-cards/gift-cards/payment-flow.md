---
title: "Gift cards payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Gift cards payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/gift-cards/payment-flow/'
aliases: 
    - /payment-methods/gift-cards/how-do-gift-cards-work
    - /payments/methods/prepaid-cards/gift-cards/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects the relevant gift card at checkout and is redirected to a [MultiSafepay payment page](/payments/checkout/payment-pages/). | Initialized | Initialized |
| 2. | The customer enters the gift card details, and completes the payment. | | |
| 3. | The card issuer processes the payment and sends a **Completed** notification to MultiSafepay. | | |
| 4. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. {{< br >}} If the customer paid the full amount using the gift card, the transaction status remains **Initialized**. {{< br >}} If they paid with the gift card and another payment method, the transaction status changes to **Completed**. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |
