---
title: "Mastercard payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Mastercard payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/mastercard/how-does-mastercard-work
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant Ma as Mastercard
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects Mastercard at checkout
    Mu->>C: Connects to Mastercard <br> (embedded/redirect)
    C->>Ma: Enters payment details, verifies identity with SecureCode, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds
       

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Embedded solution** | The customer selects Mastercard and enters their payment details at checkout. | [Payment Components](/payment-components/) |
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to enter their payment details. | [API reference](/api/#mastercard) |

**Note:** SecureCode is the Mastercard version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/).

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| [Manually authorize or decline the transaction](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/). | Uncleared | Uncleared |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 1&nbsp;hour and the transaction expired. | Expired | Expired |
| The customer's bank has declined the transaction (see possible reasons below). | Declined | Declined   |

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
| The refund is complete.  | Completed      | Completed   |
| The customer requested a [chargeback](/payments/chargebacks/). | Chargeback | Completed   |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

