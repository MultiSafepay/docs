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

This diagram shows the flow for a successful transaction.

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
**Redirect flow**: The customer is redirected first to a [payment page](/payment-pages/) to select their bank, and then to their online banking environment.

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 3 days. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |



