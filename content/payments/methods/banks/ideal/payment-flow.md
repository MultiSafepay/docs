---
title: "iDEAL payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "iDEAL payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/iDeal.svg'
url: '/payment-methods/ideal/payment-flow/'
aliases: 
    - /payment-methods/ideal/how-does-ideal-work/
    - /payments/methods/banks/ideal/payment-flow/
    - /payments/methods/banks/idealqr/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as Issuer
    participant Me as Merchant

    C->>Mu: Initiates payment
    Mu->>C: Connects to issuer
    C->>I: Completes payment
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

1. The customer selects iDEAL (QR) at checkout.  
2. We connect the customer with the issuer directly or redirect them to a MultiSafepay payment page. 
3. The customer authenticates their account or scans the QR code and completes payment.  
4. The issuer transfers the funds to MultiSafepay.  
5. We settle the funds in your MultiSafepay balance. 

## Payment statuses

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The customer has completed payment. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is pending (banking only).  | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |






