---
title: "American Express payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "American Express payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/credit-and-debit-cards/american-express/how-does-american-express-work/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as American Express
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects American Express at checkout
    Mu->>C: Connects to American Express (redirect only)
    C->>A: Enters payment details, verifies identity, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    alt MultiSafepay collects
        CB->>Mu: Transfers funds 
        Mu->>Me: Settles funds
    else With American Express MID
        CB->>A: Transfers funds
        A->>Me: Settles funds
    end
    

{{< /mermaid >}}
&nbsp;  
**Redirect flow:** The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter their payment details. 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| [Manually authorize or decline the transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). | Uncleared | Uncleared |
| The transaction is completed. | Completed | Completed |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer has requested a refund. | Void | Void |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| The customer's bank has declined the transaction. {{< br >}} See [About Declined status](/credit-cards-user-guide/declined-status/). | Declined | Declined   |

## Refund/chargeback statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund/chargeback. | Reserved    | Reserved   |
| The refund/chargeback is complete.  | Completed      | Completed   |



