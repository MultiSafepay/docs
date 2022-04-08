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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    C->>Mu: Selects Sofort at checkout
    alt Direct flow
    Mu->>C: Redirects customer to their online banking environment
    else Redirect flow
    Mu->>C: Redirects customer to payment page, <br> and then to their online banking environment
    end
    C->>CB: Authenticates account and completes payment
    CB->>Mu: Transfers funds 
    Note over CB,Mu: May take 3 business days <br> Don't ship yet!
    Me->>C: Ships order
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| The customer's bank has authorized the transaction and is transfering the funds.  {{< br >}} May take up to 3 business days for all amounts. {{< br >}} Do **not** ship yet! MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via Sofort. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 1 day. | Expired | Expired |

**Note:** Amounts less than 100 EUR are completed immediately. The status of orders over 100 EUR changes to **Uncleared** and then to **Completed** after 24 hours.

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |













