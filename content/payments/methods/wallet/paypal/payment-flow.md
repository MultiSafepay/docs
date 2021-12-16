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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant P as PayPal
    participant Me as Merchant

    C->>Mu: Selects PayPal at checkout
    Mu->>C: Connects to PayPal (direct/redirect)
    C->>P: Authenticates account, completes payment 
    P->>Me: Settles funds in your <br> PayPal business account

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to their PayPal account. | 
| **Redirect flow** | The customer is redirected briefly to a [MultiSafepay payment page](/payment-pages/) and then to PayPal. | 

**Note:** MultiSafepay does **not** collect funds for PayPal transactions.

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. {{< br >}} **Note:** The transaction status doesn't change because MultiSafepay doesn't collect the funds. | Completed | Initialized |
| The currency is not enabled in your PayPal business account. {{< br >}} To change the order status to **Completed**, enable the relevant currency. {{< br >}} You can only decline or authorize **Uncleared** transactions in your PayPal account. | Uncleared | Initialized |
| PayPal has declined the transaction. | Declined | Declined   |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 14 days and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Initialized |
| The refund is complete.  | Completed | Initialized |
| The customer has requested a refund but there are not enough funds in your PayPal business account. | Uncleared | Initialized   |




