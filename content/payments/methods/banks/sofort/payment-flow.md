---
title: "Sofort payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Sofort payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
url: '/payment-methods/sofort/payment-flow/'
aliases: 
    - /payment-methods/sofort-banking/how-does-sofort-banking-work/
    - /payments/methods/banks/sofort-banking/payment-flow/
    - /payments/methods/banks/sofort/payment-flow/
---

## How it works

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Sofort at checkout
    Mu->>C: Connects to customer's bank (direct/redirect)
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Note over CB,Mu: May take 3 business days <br> Don't ship yet!
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#ideal---direct)  
The customer selects iDEAL and their bank at checkout and is redirected straight to their online banking environment.  

[Redirect flow](/api/#ideal---redirect)  
The customer selects iDEAL at checkout and is redirected first to a MultiSafepay payment page to select their bank, and then to their online banking environment. 

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
| The customer's bank is processing the transaction and transfering the funds.  {{< br >}} May take up to 3 business days for all amounts. {{< br >}} Do **not** ship during this status. MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete  payment and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund was successful. | Completed | Completed |













