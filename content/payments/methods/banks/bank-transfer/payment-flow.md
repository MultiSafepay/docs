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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant Me as Merchant

    C->>Mu: Selects Bank Transfer at checkout (direct/redirect)
    Mu->>C: Emails MultiSafepay's bank account details
    Note over Mu,C: Or email the details yourself
    C->>Mu: Transfers funds (online or with teller)
    Note over C,Mu: Takes 1–3 business days 
    Mu->>Me: Matches transaction and settles funds
    
{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to your success page and receives our bank details by email. | 
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/), where they confirm their bank account number and (optionally) bank country. {{< br >}} MultiSafepay's bank account details are then displayed. | 

**Note:** If the customer provides incorrect payment details and/or pays the wrong amount and we can't match the payment correctly, we refund it to the customer. 

{{< details title="Emailing bank details yourself" >}}

MultiSafepay automatically emails our bank account details to the customer. Alternatively, you can email them yourself, e.g. for consistent, branded communications.

To prevent MultiSafepay from emailing the customer, in your `POST /orders` request, set the `disable_send_email` parameter to `true`. 

For more information, see API reference – [Bank Transfer: Direct](/api/#request-to-pay).

{{< /details >}}

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment within 60 days and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |

