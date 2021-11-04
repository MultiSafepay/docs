---
title: "Visa payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Visa payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/visa/how-does-visa-work
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant V as Visa
    participant Me as Merchant

    C->>Mu: Selects Visa at checkout
    Mu->>C: Connects to Visa <br> (embedded/redirect)
    C->>V: Enters payment details, passes Verified by Visa, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
    V->>Mu: Transfers funds 
    Mu->>Me: Settles funds
       

{{< /mermaid >}}
&nbsp;  

{{< details title="Embedded vs redirect">}}

**Embedded solution**   
The customer selects Cartes Bancaires and enters their payment details at checkout.  
See [Payment Components](/payment-components/).

**Redirect flow**  
The customer selects Cartes Bancaires at checkout and is redirected to a MultiSafepay payment page to enter their payment details.  
See API reference – [Co-branded credit cards](/api/#co-branded-credit-cards). 

{{< /details>}}

**Note:** Verified by Visa is Visa's version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/).

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
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| The customer's bank has declined the transaction. | Declined | Declined   |

{{< details title="Reasons for Declined status">}}

The table below shows possible reasons for **Declined** status. 

Only the customer can contact their credit card issuer to find out the specific reason.

| Reason | Description |
|----------|---------|
| Transaction declined by MultiSafepay | Our automated fraud filter declined the transaction. Email the Support Team at <support@multisafepay.com> |
| Do not honor | The reason is not shared with MultiSafepay. |
| 3D authorisation cancelled | [3D Secure](/features/3d-secure/about/) verification was incomplete or couldn't be validated. |
| Expired card | The credit card has expired. |
| Insufficient funds | The customer has insufficient credit on their card to complete the payment. |
| Merchant only accepts 3D Secure-verified cards | Email requests to accept non-3D Secure verified cards to the Risk Team at <risk@multisafepay.com>  |

For any questions, email the Support Team at <support@multisafepay.com>

{{< /details >}}

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested a [chargeback](/payments/chargebacks/). | Chargeback | Completed   |


