---
title: "Apple Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Apple Pay payment flow - MultiSafepay Docs"

short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/apple-pay/payment-flow/'
aliases: 
    - /payment-methods/wallet/applepay/apple-pay-how-does-it-work
    - /payments/methods/wallet/applepay/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Apple Pay
    participant CS as Card scheme
    participant Me as Merchant

    C->>Mu: Selects Apple Pay at checkout
    Mu->>C: Connects to Apple Pay (direct/redirect)
    C->>A: Completes payment on an iOS device with Touch ID or Face ID
    A->>Mu: Sends the customer's credit card details as an encrypted token
    Mu->>CS: Decrypts card details and processes credit card transaction
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
    CS->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#apple-pay---direct)  
The customer selects Apple Pay and completes payment on your checkout page.  

[Redirect flow](/api/#apple-pay---redirect)  
The customer is redirected to a [MultiSafepay payment page](/payment-pages/) and then to Apple. 

{{< /details>}}

For more information about using Apple Pay, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

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
| The transaction has been cancelled. | Void   | Void   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| The issuer has declined the transaction (see possible reasons below). | Declined | Declined   |

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
| The refund is complete.  | Completed  | Completed  |
| The customer requested a [chargeback](/payments/chargebacks/). | Chargeback | Completed   |





