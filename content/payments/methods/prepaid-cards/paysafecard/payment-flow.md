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

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as Paysafecard
    participant Me as Merchant

    C->>Mu: Selects a Paysafecard at checkout
    Mu->>C: Connects to Paysafecard (redirect only)
    C->>P: Enters card PIN and completes payment
    P->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Redirect flow">}}
&nbsp;  
The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter the 16-digit PIN on the card. 

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
| The transaction is complete.| Completed | Completed |
| The transaction was declined. | Declined   | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 3 hours and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |
