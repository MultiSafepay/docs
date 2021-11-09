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
## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Belfius at checkout
    Mu->>C: Connects to customer's bank (direct/redirect)
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#belfius---direct)  
The customer selects Belfius and their bank at checkout and is redirected straight to their online banking environment.  

[Redirect flow](/api/#belfius---redirect)  
The customer selects Belfius at checkout and is redirected first to a [MultiSafepay payment page](/payment-pages/) to select their bank, and then to their online banking environment. 

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
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

**Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and finalize all incoming payments.

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
















