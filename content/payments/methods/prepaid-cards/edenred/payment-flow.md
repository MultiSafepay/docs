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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant E as Edenred
    participant Me as Merchant

    C->>Mu: Selects Edenred at checkout
    Mu->>C: Connects to Edenred (redirect)
    C->>E: Authenticates account, authorizes MultiSafepay access
    E->>Mu: Confirms authorization and sufficient funds on voucher
    E->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
**Redirect flow:** The customer is redirected first to a [MultiSafepay payment page](/payment-pages/) to select the relevant voucher, and then to their Edenred account. 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |


