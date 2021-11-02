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

flowchart TD
    id1(["Customer selects iDEAL (QR) at checkout"]) --> id2(["Direct: {{< br >}} Customer is redirected straight to their online banking page"]) & id3(["Redirect: {{< br >}} Customer is redirected to a MultiSafepay payment page to select their bank, and then to the online banking page"])--> id4([Customer authenticates their account or scans the QR code and completes payment]) --> id5(["MultiSafepay collects the funds from the customer's bank and settles them in your MultiSafepay balance"]) 

{{< /mermaid >}}


{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as Issuer
    participant Me as Merchant

    C->>Mu: Selects iDEAL (QR) at checkout
    Mu->>C: Connects to issuer
    C->>I: Completes payment
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

1. The customer selects iDEAL (QR) at checkout.  
2. We connect the customer with the [issuer](/getting-started/glossary/#issuer) directly or redirect them to a MultiSafepay payment page. 
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
| The funds are in your MultiSafepay balance. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is pending (banking only).  | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |
