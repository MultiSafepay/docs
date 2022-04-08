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

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant G as Gift card issuer
    participant Me as Merchant

    C->>Mu: Selects a gift card at checkout
    Mu->>C: Redirects customer to payment page
    C->>G: Enters gift card details and completes payment
    G->>Mu: Processes payment and transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| For partial payment with another method: The customer didn't complete payment. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |

