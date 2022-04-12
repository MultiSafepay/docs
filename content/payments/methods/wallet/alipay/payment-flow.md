---
title: "Alipay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Alipay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/alipay/payment-flow/'
aliases: 
    - /payment-methods/wallet/alipay/alipay-how-does-it-work
    - /payments/methods/wallet/alipay/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Alipay
    participant Me as Merchant

    C->>Mu: Selects Alipay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page
    else Direct flow
    Mu->>A: Payment is processed with Alipay
    end
    A->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Alipay. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 5&nbsp;hours, or it was cancelled. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed      | Completed   |



