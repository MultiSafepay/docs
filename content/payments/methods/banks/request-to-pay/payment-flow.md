---
title: "Request to Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Request to Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
url: '/payment-methods/request-to-pay/payment-flow/'
aliases: 
    - /payment-methods/bancontact/how-does-request-to-pay-work/
    - /payments/methods/banks/request-to-pay/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant D as Deutsche Bank
    participant Me as Merchant

    C->>Mu: Selects Request to Pay at checkout
    Mu->>C: Connects to Deutsche Bank (direct/redirect)
    C->>D: Authenticates account and authorizes SEPA bank transfer
    D->>Mu: Transfers funds 
    Note over D,Mu: Within 24 hours <br> (if Instant SEPA not supported)
    Mu->>Me: Settles funds
    
{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to their online banking environment. | 
| **Redirect flow** | The customer is redirected first to a [payment page](/payment-pages/), and then to their online banking environment. |

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Deutsche Bank. | Initialized | Initialized |
| Deutsche Bank has authorized the transaction and is transfering the funds. | Completed  | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Deutsche Bank declined the transaction. | Declined | Declined   |
| The customer cancelled the transaction at Deutsche Bank. | Void | Void |
| The customer didn't complete payment within 1 hour. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
| The refund was declined. | Declined | Declined |



        


