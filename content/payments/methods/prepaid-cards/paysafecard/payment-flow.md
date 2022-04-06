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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as Paysafecard
    participant Me as Merchant

    C->>Mu: Selects a Paysafecard at checkout
    Mu->>C: Connects to Paysafecard (redirect)
    C->>P: Enters card PIN and completes payment
    P->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
**Redirect flow:** The customer is redirected to a [payment page](/payment-pages/) to enter the 16-digit PIN on the card. 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Paysafecard. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction at Paysafecard. | Void   | Void   |
| The customer didn't complete payment within 3&nbsp;hours. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |

