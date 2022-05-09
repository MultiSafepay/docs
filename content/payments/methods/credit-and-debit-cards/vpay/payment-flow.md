---
title: "V Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "V Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/vpay/payment-flow/'
aliases: 
    - /payment-methods/vpay/how-does-vpay-work/
    - /payments/methods/credit-and-debit-cards/vpay/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant V as Visa
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects V Pay at checkout
    Mu->>C: Redirects to payment page
    C->>V: Enters payment details, authenticates, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
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
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. {{< br >}} Review it and then [manually capture or decline](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D&nbsp;Secure authentication. | Expired | Expired |
| The customer failed 3D&nbsp;Secure authentication or cancelled payment. {{< br >}} See [Declined credit card payments](/about-payments/declined-status/). | Declined | Declined   |
|**Refunds/chargebacks**|||
| Refund/chargeback initiated. | Reserved    | Reserved   |
| Refund/chargeback complete.  | Completed      | Completed   |


