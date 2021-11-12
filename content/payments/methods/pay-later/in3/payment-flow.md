---
title: 'in3 payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "in3 payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/svgs/in3.svg'
url: '/payment-methods/in3/payment-flow/'
aliases:
    - /payments/methods/billing-suite/in3/payment-flow/
    - /payments/methods/billing-suite/in3/user-guide/changing-order-status-to-shipped/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as in3
    participant Me as Merchant

    C->>Mu: Selects in3 at checkout
    Mu->>C: Connects to in3 (direct/redirect)
    C->>I: Selects their bank, accepts the payment periods, and terms & conditions
    I->>Mu: Authorizes the payment
    Mu->>I: Captures the funds
    C->>I: Pays 1st instalment within 5 mins
    Note over C,I: Settlement is now guaranteed!
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 15 days of 1st instalment)
    C->>I: Pays 2nd instalment within 30 days, and 3rd within 60 days 

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to in3 to select their bank, and accept the payment periods and terms and conditions. | 
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to provide their birth date, title, and phone number. {{< br >}} They are then redirected to your success page. | 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. {{< br >}} You can still cancel it. | Initialized   | Initialized  |
| in3 is authorizing the payment or waiting for the customer to pay the first installment. {{< br >}} The customer has 5 minutes to pay the first installment, or The transaction was cancelled. {{< br >}} The first installment is required to create the order. | Uncleared  | Initialized  |
| The customer has paid the first installment. {{< br >}} Settlement is now guaranteed. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/).  | Shipped | Uncleared | 
| The transaction is complete. | Completed | Completed |
| in3 has declined the payment. {{< br >}} No order was created. | Declined | Declined |
| The transaction was cancelled. | Void | Void |
| The transaction expired after 2 hours. | Expired | Expired |

## Refund statuses

| Description  | Order status      | Transaction status |
|----|-----|-----|
| in3 has successfully processed a full or partial refund. | Completed    | Completed   |
| The refund was declined.  | Declined      | Declined   |


