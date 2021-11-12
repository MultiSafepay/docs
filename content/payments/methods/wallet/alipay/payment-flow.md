---
title: "Alipay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Alipay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/alipay/payment-flow/'
aliases: 
    - /payment-methods/wallet/alipay/alipay-how-does-it-work
    - /payments/methods/wallet/alipay/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Alipay
    participant Me as Merchant

    C->>Mu: Selects Alipay at checkout
    Mu->>C: Connects to Alipay (direct/redirect)
    C->>A: Completes payment
    A->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The payment is processed directly with Alipay. | [API reference](/api/#alipay---direct) |
| **Redirect flow** | The customer is briefly redirected to a [MultiSafepay payment page](/payment-pages/) before the payment is processed directly with Alipay. | [API reference](/api/#alipay---redirect) | 

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| Alipay has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 5&nbsp;hours and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

