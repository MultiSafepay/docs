---
title: "Postepay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Postepay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/postepay/payment-flow/'
aliases:
    - /payments/methods/credit-and-debit-cards/postepay/payment-flow/
    - /postepay/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CS as Card scheme
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects Postepay at checkout
    Mu->>C: Connects to card scheme <br> (redirect only)
    C->>CS: Enters payment details, verifies identity with  3D Secure, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

**Redirect flow:** The customer is redirected to a [payment page](/payment-pages/) to enter their payment details.

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. Review it and then [manually capture or decline](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. {{< br >}} See [Declined credit card payments](/about-payments/declined-status/). | Declined | Declined   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The refund is initiated | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |



