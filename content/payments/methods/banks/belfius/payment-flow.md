---
title: "Belfius payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Belfius payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/belfius.svg'
url: '/payment-methods/belfius/payment-flow/'
aliases: 
    - /payment-methods/belfius/how-does-belfius-work/
    - /payments/methods/banks/belfius/payment-flow/
---
This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant B as Belfius
    participant Me as Merchant

    C->>Mu: Selects Belfius at checkout
    Mu->>C: Connects to Belfius (direct/redirect)
    C->>B: Authenticates account and completes payment
    B->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to their online banking environment. | 
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/), and then to their online banking environment. | 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Belfius. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 5 days. | Expired | Expired |

{{< blue-notice >}} **Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and finalize all incoming payments. {{< /blue-notice >}}

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
















