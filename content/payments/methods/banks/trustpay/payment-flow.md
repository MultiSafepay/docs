---
title: "TrustPay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "TrustPay payment flow - MultiSafepay Docs"

short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/trustpay/payment-flow/'
aliases: 
    - /payment-methods/trustpay/trustpay-how-does-it-work/
    - /payments/methods/banks/trustpay/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects TrustPay at checkout
    Mu->>C: Connects to customer's bank (redirect only)
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/) to select their bank, and then to their online banking environment. | [API reference](/api/#trustpay) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete.| Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 10 days and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).