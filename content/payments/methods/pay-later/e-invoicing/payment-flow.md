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

This diagram shows the flow for a successful transaction.

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
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    MF->>C: Sends invoice 
    Note over MF,C: Settlement is now guaranteed!
    C->>MF: Completes payment 
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The order details are sent directly to MultiFactor. | 
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to provide their birthdate, bank account, email address, and phone number. {{< br >}} They are then redirected to your success page. | 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. {{< br >}} You can still cancel it. | Initialized   | Initialized  |
| E-Invoicing has authorized the payment. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Initialized  |
| **Important**: [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} You must ship to receive payment. | Shipped | Initialized |
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
| The refund is complete.  | Completed | Completed |

