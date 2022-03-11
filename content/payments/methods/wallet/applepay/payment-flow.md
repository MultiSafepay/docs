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

This diagram shows the flow for a successful transaction.

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
    C->>A: Authorizes payment on an iOS device with Touch ID or Face ID
    alt is Direct integration
    A->>Me: Sends the customer's payment details as an encrypted token
    Me->>Mu: Sends the customer's payment details as an encrypted token
    else is Redirect integration
    A->>Mu: Sends the customer's payment details as an encrypted token
    end
    Mu->>CS: Decrypts token and processes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    CS->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer selects Apple Pay and completes payment on your checkout page. | 
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) and then to Apple to complete payment. | 

For more information about using Apple Pay, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| [Manually authorize or decline the transaction](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| The transaction is complete. | Completed | Completed |
| The transaction was cancelled or the customer requested a chargeback. | Void   | Void   |
| The customer didn't complete payment within 1&nbsp;hour and the transaction expired. | Expired | Expired |
| The issuer has declined the transaction. {{< br >}} See [Declined credit card payments](/about-payments/declined-status/). | Declined | Declined   |


## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed  | Completed  |





