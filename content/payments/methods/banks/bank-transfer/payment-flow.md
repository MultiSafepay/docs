---
title: "Bank Transfer payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Bank Transfer payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
url: '/payment-methods/bank-transfer/payment-flow/'
aliases: 
    - /payment-methods/bank-transfer/how-does-bank-transfer-work/
    - /payments/methods/banks/bank-transfer/payment-flow/
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

1. The customer selects Bank transfer at checkout and provides an email address.  
2. MultiSafepay connects the customer with the [issuer](/getting-started/glossary/#issuer) directly or redirects them to a MultiSafepay payment page, where they confirm their bank account number. 
3. The customer:  
    - Receives MultiSafepay's bank account details by email, sent by MultiSafepay or yourself. 
{{< details title="Emailing payment instructions yourself" >}}

If emailing your own payment instructions to the customer, in your `POST /orders` API request, set the `disable_send_email` parameter to `true`. 

This prevents us from emailing the customer.

For more information, see API reference – [Bank Transfer: Direct](/api/#request-to-pay).

{{< /details >}}
    - Completes payment to our account, either online or with a teller.  
This may take 1-3 business days. 
4. The issuer transfers the funds to MultiSafepay.  
5. MultiSafepay:  
    - Collects the funds and matches them to the outstanding transaction.  
    - Settles the funds in your MultiSafepay balance.  

**Note:** If the customer provides incorrect payment details and/or pays the wrong amount and we can't match the payment correctly, we refund it to the customer. 


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
| The customer didn't complete  payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |