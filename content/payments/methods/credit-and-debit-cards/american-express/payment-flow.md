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

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as American Express
    participant Me as Merchant

    C->>Mu: Selects American Express at checkout
    Mu->>C: Connects to American Express <br> (embedded/redirect)
    C->>A: Enters payment details, verifies identity with Safekey, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
    alt MultiSafepay collects
        A->>Mu: Transfers funds 
        Mu->>Me: Settles funds
    else With American Express MID
        A->>Me: Settles funds
    end
    

{{< /mermaid >}}
&nbsp;  

{{< details title="Embedded vs redirect">}}

**Embedded solution**   
The customer selects American Express and enters their payment details at checkout.  
See [Payment Components](/payment-components/).

**Redirect flow**  
The customer selects American Express at checkout and is redirected to a MultiSafepay payment page to enter their payment details.  
See API reference – [American Express](/api/#american-express). 

{{< /details>}}

**Note:** Safekey is the American Express version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/).

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
| The customer has initiated a transaction. | Initialized | Initialized |
| You need to manually [authorize or decline the transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). | Uncleared | Uncleared |
| The transaction is completed. | Completed | Completed |
| The customer's bank has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status/). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment and the transaction expired. | Expired | Expired |
| The customer requested a [chargeback](/payments/chargebacks/). | Chargeback | Completed   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested a [chargeback](/payments/chargebacks/). | Chargeback | Completed   |



