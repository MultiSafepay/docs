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

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as Apple Pay
    participant CS as Card scheme
    participant Me as Merchant
    
    C->>Mu: Selects Apple Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page, <br> and then to Apple
    else Direct flow
    Mu->>C: Redirects to Apple
    end
    C->>A: Authorizes payment on an iOS device with Touch ID or Face ID
    alt Redirect integration
    A->>Mu: Sends token
    else Direct integration
    A->>Me: Sends the customer's payment details as an encrypted token
    Me->>Mu: Sends token
    end
    Mu->>CS: Decrypts token and processes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    CS->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;   

For more information about using Apple Pay, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

## Payment statuses

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the card scheme is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. {{< br >}} Review it and then [manually capture or decline](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D&nbsp;Secure authentication. | Expired | Expired |
| The customer failed 3D&nbsp;Secure authentication or cancelled payment. {{< br >}} See [Declined credit card payments](/about-payments/declined-status/). | Declined | Declined   |
|**Refunds**|||
| Refund initiated. | Reserved    | Reserved   |
| Refund complete.  | Completed  | Completed  |





