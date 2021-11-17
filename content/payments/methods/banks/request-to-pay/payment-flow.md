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
    D->>Me: Settles funds
    Note over D,Me: Within 24 hours <br> (if Instant SEPA not supported)

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to their online banking environment. | [API reference](/api/#request-to-pay---direct) |
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/), and then to their online banking environment. | [API reference](/api/#request-to-pay---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is successful and settlement is pending. | Uncleared  | Completed |
| The transaction is complete. | Completed | Completed |
| Deutsche Bank has declined the transaction. | Declined | Declined   |
| The transaction is cancelled. | Void | Void |
| The customer didn't complete payment within 1 hour and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
| Deutsche Bank has declined the refund. | Declined | Declined |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

        


