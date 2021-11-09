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
    participant Me as Merchant

    C->>Mu: Selects Bank Transfer at checkout
    Mu->>C: Emails MultiSafepay's bank account details
    Note over Mu,C: Or email the details yourself
    C->>Mu: Transfers funds (online or with teller)
    Note over C,Mu: Takes 1–3 business days 
    Mu->>Me: Matches transaction and settles funds
    
{{< /mermaid >}}

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#bank-transfer---direct)  
The customer selects Bank Transfer at checkout and is redirected to your success page.  

[Redirect flow](/api/#bank-transfer---redirect)  
The customer selects Bank Transfer at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/), where they confirm their bank account number and (optionally) the bank country.  
MultiSafepay's bank account details are then displayed. 

{{< /details>}}

{{< details title="Emailing payment instructions yourself" >}}

MultiSafepay automatically emails our bank account details to the customer. Alternatively, you can email them yourself, e.g. for consistent, branded communications.

To prevent MultiSafepay from emailing the customer, in your `POST /orders` API request, set the `disable_send_email` parameter to `true`. 

For more information, see API reference – [Bank Transfer: Direct](/api/#request-to-pay).

{{< /details >}}

{{< details title="Matching transactions">}}
&nbsp;  
If the customer provides incorrect payment details and/or pays the wrong amount and we can't match the payment correctly, we refund it to the customer. 

{{< /details >}}

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
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |