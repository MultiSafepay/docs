---
title: "iDEAL payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "iDEAL payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/iDeal.svg'
url: '/payment-methods/ideal/payment-flow/'
aliases: 
    - /payment-methods/ideal/how-does-ideal-work/
    - /payments/methods/banks/ideal/payment-flow/
    - /payments/methods/banks/idealqr/payment-flow/
---
This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects iDEAL (QR) at checkout
    Mu->>C: Connects to customer's bank (direct/redirect)
    C->>CB: Authenticates account/scans QR code and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer selects iDEAL and their bank at checkout and is redirected to their online banking environment. | [API reference](/api/#ideal---direct) |
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/) to select their bank, and then to their online banking environment. | [API reference](/api/#ideal---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is pending (banking only).  | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
