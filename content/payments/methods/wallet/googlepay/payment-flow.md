---
title: "Google Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Google Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/google-pay/payment-flow'
noindex: '.'
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant G as Google Pay
    participant CS as Card scheme
    participant Me as Merchant
    participant CB as Customer's bank
    
    C->>Mu: Selects Google Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects customer to payment page, <br> and then to Google account
    else Direct flow
    Mu->>C: Redirects customer to Google account
    end
    C->>G: Completes payment 
    alt Direct integration
    G->>Me: Sends the customer's payment details as an encrypted token
    Me->>Mu: Sends token
    else Redirect integration
    G->>Mu: Sends token
    end
    Mu->>CS: Decrypts token and processes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes (or declines) transaction
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

For more information about the Google Pay™ payment flow, see Google Pay – [Overview](https://developers.google.com/pay/api/web/overview).

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
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |


