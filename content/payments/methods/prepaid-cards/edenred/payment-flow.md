---
title: "Edenred payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Edenred payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/edenred/payment-flow/'
aliases:
    - /payments/methods/prepaid-cards/edenred/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant E as Edenred
    participant Me as Merchant

    C->>Mu: Selects Edenred at checkout
    Mu->>C: Connects to Edenred (redirect only)
    C->>E: Authenticates account, authorizes MultiSafepay access
    E->>Mu: Confirms authorization and sufficient funds on voucher
    E->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Redirect flow">}}

The customer is redirected first to a [MultiSafepay payment page](/payment-pages/) to select the relevant voucher, and then to their Edenred account. 

See API reference – [Edenred](/api/#edenred).

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
| The transaction is complete. | Completed | Completed |


