---
title: "PayPal payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "PayPal payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/paypal/payment-flow/'
aliases: 
    - /payment-methods/wallet/paypal/how-does-paypal-work
    - /payments/methods/wallet/paypal/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as PayPal
    participant Me as Merchant

    C->>Mu: Selects PayPal at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> then to their PayPal account
    else Direct flow
    Mu->>C: Redirects to PayPal account
    end
    C->>P: Authenticates account, and completes payment 
    P->>Me: Settles funds in your <br> PayPal business account

{{< /mermaid >}}
&nbsp;  

**Note:** MultiSafepay does **not** collect funds for PayPal transactions.

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to PayPal. | Initialized | Initialized |
| - Awaiting the customer to pay in their PayPal account **or** {{< br >}} - PayPal is authorizing the transaction **or** {{< br >}} - You may need to enable the currency and then authorize the payment in your PayPal business account.  | Uncleared | Initialized |
| PayPal has collected payment. | Completed | Initialized |
| The customer cancelled the payment in PayPal. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 14 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Initialized |
| Refund complete.  | Completed | Initialized |
| Refund declined. | Declined | Declined |
| - PayPal is authorizing the refund. {{< br >}} **Or** {{< br >}} - There are not enough funds in your PayPal business account to process the refund. {{< br >}} For more information, see your PayPal business account. | Uncleared | Initialized   |