---
title: "Dotpay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Dotpay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Dotpay.svg'
url: '/payment-methods/dotpay/payment-flow/'
aliases: 
    - /payment-methods/dotpay/dotpay-how-does-it-work/
    - /payments/methods/banks/dotpay/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Dotpay at checkout
    Mu->>C: Connects to customer's bank (redirect only)
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Redirect flow">}}

The customer is redirected first to a MultiSafepay payment page to select their bank, and then to their online banking environment. 

See API reference – [Dotpay](/api/#dotpay).

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
| The transaction is complete. | Completed | Completed |
| Dotpay has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund was successful. | Completed | Completed |



