---
title: "Trustly payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Trustly payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/trustly.svg'
url: '/payment-methods/trustly/payment-flow/'
aliases: 
    - /payment-methods/trustly/how-does-trustly-work/
    - /payments/methods/banks/trustly/payment-flow/
---
## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Trustly at checkout
    Mu->>C: Connects to customer's bank (redirect only)
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Redirect flow">}}
&nbsp;  
The customer selects Trustly at checkout and is redirected first to a MultiSafepay payment page to select their country and bank, and then to their online banking environment. 

{{< /details>}}

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
| The transaction is complete.| Completed | Completed |
| Trustly has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment and the transaction expired. | Expired | Expired |
| In rare cases, the transaction is marked as **Uncleared**. {{< br >}} Trustly then informs MultiSafepay of the correct status, which may be **Completed**, **Declined**, or **Expired**. {{< br >}} **Uncleared** status automatically expires after 5 days. | Uncleared | Uncleared   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is complete. | Completed | Completed |





