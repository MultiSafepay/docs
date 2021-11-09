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

## How it works

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

{{< details title="Redirect flow">}}

The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter the gift card details. 

See API reference – [Gift cards](/api/#gift-cards).

{{< /details>}}

## Payment statuses

{{< details title="Order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status**  
The progression of the customer's order with you, independent of the payment

**Transaction status**  
The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The customer enters the gift card details, and completes the payment. | | |
| The transaction is complete. {{< br >}} **Note:** If the customer paid the full amount using the gift card, the transaction status remains **Initialized**. {{< br >}} If they paid with the gift card and another payment method, the transaction status changes to **Completed**. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |
