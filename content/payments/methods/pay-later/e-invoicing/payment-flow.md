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

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects E-Invoicing at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to provide <br> birth date, bank account, email address, and phone number, <br> then redirects to your success page
    else Direct flow
    Mu->>MF: Sends order details
    end
    MF->>Mu: Authorizes the payment
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped. 
    MF->>C: Sends invoice (settlement is now guaranteed)
    C->>MF: Completes payment 
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| MultiSafepay's risk analysis is in progress. {{< br >}} You can still cancel. | Initialized   | Initialized  |
| E-Invoicing has authorized the transaction. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Initialized  |
| **Important**: [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} You must ship to receive payment. | Shipped | Initialized |
| MultiSafepay has collected payment. | Completed    | Completed  |
| E-Invoicing declined the transaction. | Declined | Declined |
| The transaction has been cancelled. | Void/Cancelled | Void/Cancelled |
| The customer didn't complete payment. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete.  | Completed | Completed |

## See also

- [Viewing transactions](/payments/methods/billing-suite/e-invoicing/user-guide/viewing-transactions/)
- [Batching transactions for subscriptions](/payments/methods/billing-suite/e-invoicing/user-guide/batching-transactions/)




