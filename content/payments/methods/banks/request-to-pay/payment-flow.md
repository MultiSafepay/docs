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

## How it works

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

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#request-to-pay---direct)  
The customer selects Request to Pay at checkout and is redirected straight to the Deutsche Bank online banking environment.  

[Redirect flow](/api/#request-to-pay---redirect)  
The customer selects Request to Pay at checkout and is redirected first to a [MultiSafepay payment page](/payment-pages/), and then to the Deutsche  online banking environment. 

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
| The transaction is successful and settlement is pending. | Uncleared  | Completed |
| The transaction is complete. | Completed | Completed |
| Deutsche Bank has declined the transaction. | Declined | Declined   |
| The customer cancelled the payment. | Void | Void |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
| Deutsche Bank has declined the refund. | Declined | Declined |


        


