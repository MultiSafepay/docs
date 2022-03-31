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
    Mu->>Me: Matches payment and settles funds
    
{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to your success page and receives our bank details by email. | 
| **Redirect flow** | The customer is redirected first to a [payment page](/payment-pages/), where they confirm their bank account number and (optionally) bank country. {{< br >}} MultiSafepay's bank account details are then displayed. | 

## 1. Email payment details

MultiSafepay emails the customer the following payment details to include when transfering the funds, or your can [email them yourself](/payment-methods/bank-transfer/payment-flow/#emailing-payment-instructions-yourself).

{{< screen src="/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius" >}}

You can view the payment details for a transaction in your MultiSafepay dashboard, in the relevant **Transaction details** page under **Offline actions**.

### Emailing payment instructions yourself

You may prefer to email the customer the payment details yourself, e.g. for consistent, branded communications. Make sure you include clear instructions about what details the customer needs to provide and the required format (see&nbsp;2.&nbsp;below).

To prevent us from emailing the customer, see API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder) > Banking order. Set the `disable_send_email` parameter to `true`. 

## 2. Customer transfers funds

The customer must only pay for **one** order per bank transfer. When transferring the funds, they must correctly input:  
    
- The amount
- Their bank account number
- The payment reference number (**not** the order number)  
    **Format:** 16 digits, numbers only, no words

## 3. MultiSafepay matches the payment

When we receive payment from the customer (1–3 business days later), we automatically match it to the corresponding transaction in our system based on the payment details provided. If auto-matching fails, we try to match the payment manually.

If we cannot match the payment:

- For smaller amounts, we refund the customer.
- For larger amounts, we contact you for information to help identify the correct transaction.

This costs all parties time and effort, and creates a negative customer experience. 

See [Resolving unmatched payments](/bank-transfer/unmatched-payments/).

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| Awaiting the customer to transfer the funds. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete  payment within 60 days. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
