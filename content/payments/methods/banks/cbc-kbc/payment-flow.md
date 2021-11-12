---
title: "CBC/KBC payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "CBC/KBC payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/cbc.svg'
url: '/payment-methods/cbc-kbc/payment-flow/'
aliases: 
    - /payment-methods/cbc/how-does-cbc-work/
    - /payments/methods/banks/cbc/payment-flow/
    - /payments/methods/banks/kbc/payment-flow/
    - /payments/methods/banks/cbc-kbc/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CK as CBC/KBC
    participant Me as Merchant

    C->>Mu: Selects CBC/KBC at checkout
    Mu->>C: Connects to CBC/KBC (direct/redirect)
    C->>CK: Authenticates account and completes payment
    CK->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to their online banking environment. | [API reference](/api/#cbckbc---direct) |
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/), and then to their online banking environment. | [API reference](/api/#cbckbc---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete.| Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 5 days and the transaction expired. | Expired | Expired |

{{< blue-notice >}} **Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and match all incoming payments. {{< /blue-notice >}}

## Refund statuses

 Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).




