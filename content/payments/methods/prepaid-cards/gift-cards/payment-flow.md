---
title: "Gift cards payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Gift cards payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/gift-cards/payment-flow/'
aliases: 
    - /payment-methods/gift-cards/how-do-gift-cards-work
    - /payments/methods/prepaid-cards/gift-cards/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant G as Gift card issuer
    participant Me as Merchant

    C->>Mu: Selects a gift card at checkout
    Mu->>C: Connects to the card issuer (redirect only)
    C->>G: Enters gift card details and completes payment
    G->>Mu: Processes payment and transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter the gift card details. | [API reference](/api/#gift-cards) | 

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. {{< br >}}  | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

{{< blue-notice >}} If the customer paid the full amount using the gift card, the transaction status remains **Initialized**. {{< br >}} If they paid with the gift card and another payment method, the transaction status changes to **Completed**. {{< /blue-notice >}}

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).