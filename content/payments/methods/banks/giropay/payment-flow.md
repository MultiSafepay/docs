---
title: "Giropay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Giropay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Giropay.svg'
url: '/payment-methods/giropay/payment-flow/'
aliases: 
    - /payment-methods/giropay/how-does-giropay-work/
    - /payments/methods/banks/giropay/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Giropay at checkout
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
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
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction. | Void   | Void   |
| The customer didn't complete payment within 10 minutes. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |



