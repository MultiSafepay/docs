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

    C->>Mu: Selects Bank Transfer at checkout
    Mu->>C: Provides the payment details (direct/redirect)
    C->>Mu: Transfers funds (online or with teller)
    Note over C,Mu: Takes 1–3 business days 
    Mu->>Me: Matches payment and settles funds
    
{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | 1. The customer is redirected to your success page. {{< br >}} 2. MultiSafepay emails them the payment details to transfer the funds. {{< br >}} **Or** you can email them the payment details yourself, e.g. for consistent, branded communications. {{< br >}} To prevent us from emailing the customer, in your `POST /orders` request, set the `disable_send_email` parameter to `true`. | [API reference](/api/#bank-transfer---direct) |
| **Redirect flow** | 1. The customer is redirected first to a [MultiSafepay payment page](/payment-pages/). {{< br >}} 2. They confirm their bank account number (helps us match payments correctly) and (optionally) bank country. {{< br >}} 3. The customer clicks **Confirm**. {{< br >}}**Note:** Required to successfully create the transaction in our system. {{< br >}} 4. The payment details are displayed for the customer to transfer the funds. | [API reference](/api/#bank-transfer---redirect) |

### Example payment details

You can view the payment details for a transaction in your MultiSafepay account, in the relevant **Transaction details** page under **Offline actions**.

{{< screen src="/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius" >}}

## Customers transfering funds

When transfering the funds, the customer must correctly input:  

- The amount
- The payment reference number (16 digits, numbers only, no words)
- Their bank account number (optional, but recommended to help us match payments correctly)

## Matching payments

We match incoming payments to the correct outstanding transactions in our system.

If the payment details or amount are missing or incorrect and we can't match the payment, we refund it to the customer. 

To help avoid this, see [Unmatched payments](/bank-transfer/unmatched-payments/).

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment within 60 days and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).