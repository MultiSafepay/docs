---
title: "Dankort payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Dankort payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant V as Visa
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects Dankort at checkout
    Mu->>C: Connects to Visa (redirect only)
    C->>V: Enters payment details, verifies identity, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

**Redirect flow:** The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter their payment details. 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The transaction is initiated and the customer has been redirected to 3D Secure. | Initialized | Initialized |
| 3D Secure authorization was sucessful, but the transaction is flagged for potential fraud risk. [Manually capture or decline the transaction](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The transaction was cancelled. | Void   | Cancelled   |
| Payment wasn't captured manually or within 5 days. | Void | Void |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| 3D Secure authorization failed or was cancelled, and the transaction was declined. {{< br >}} See [About Declined status](/credit-cards-user-guide/declined-status/). | Declined | Declined   |

## Refund/chargeback statuses

| Description | Order status | Transaction status |
|---|---|---|
| The refund/chargeback is initiated. | Reserved    | Reserved   |
| The refund/chargeback is complete.  | Completed      | Completed   |



