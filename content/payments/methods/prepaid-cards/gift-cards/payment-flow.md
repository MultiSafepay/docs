---
title: "Gift cards payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Gift cards payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/gift-cards/how-do-gift-cards-work
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer enters the gift card details, and completes the payment. | | |
| 4. | The card issuer processes the payment and sends a **Completed** notification to MultiSafepay. | | |
| 5. | MultiSafepay collects the funds and adds them to your MultiSafepay balance. {{< br >}} If the customer paid the full amount using the gift card, the transaction status remains **Initialized**. {{< br >}} If they paid with the gift card and another payment method, the transaction status changes to **Completed**. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |
