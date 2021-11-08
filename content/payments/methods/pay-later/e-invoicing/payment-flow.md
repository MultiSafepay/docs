---
title: 'E-Invoicing payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "E-Invoicing payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/e-invoicing/payment-flow/'
aliases:
    - /payments/methods/billing-suite/e-invoicing/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects E-Invoicing at checkout
    Mu->>C: Connects to MultiFactor (direct/redirect)
    MF->>Mu: Authorizes the payment
    Mu->>MF: Sends a capture
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    MF->>C: Sends invoice 
    Note over MF,C: Settlement is now guaranteed!
    C->>MF: Completes payment 
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#e-invoicing---direct)  
The customer selects E-Invoicing at checkout and the order details are sent directly to E-Invoicing.  

[Redirect flow](/api/#e-invoicing---redirect)  
The customer:

- Selects E-Invoicing at checkout and is redirected to a MultiSafepay payment page 
- Provides their birthdate, bank account, email address, and phone number
- Is redirected to your success page

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
| The customer has initiated a transaction. {{< br >}} You can cancel the transaction at this point. | Initialized   | Initialized  |
| E-Invoicing has authorized the payment. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Initialized  |
| Ship the order. {{< br >}} You **must**: {{< br >}} - [Change the order status to Shipped](/payments/methods/billing-suite/e-invoicing/user-guide/changing-order-status-to-shipped/). {{< br >}} - Ship the order to receive payment. | Shipped | Initialized |
| The transaction is complete. | Completed    | Completed  |
| E-Invoicing has declined the payment. | Declined | Declined |
| The payment has been cancelled. | Void | Cancelled |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

See also:

- [Viewing transactions](/payments/methods/billing-suite/e-invoicing/user-guide/viewing-transactions/)
- [Batching transactions for subscriptions](/payments/methods/billing-suite/e-invoicing/user-guide/batching-transactions/)

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund was successful.  | Completed | Completed |

