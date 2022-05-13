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

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as in3
    participant Me as Merchant

    C->>Mu: Selects in3 at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, title, and phone number, <br> then redirects to your success page
    else Direct flow
    Mu->>C: Redirects to in3 to select their bank, <br> and accept the payment periods and terms & conditions
    end
    I->>Mu: Authorizes the payment
    Mu->>I: Captures the funds
    C->>I: Pays 1st instalment within 5 mins (settlement is now guaranteed)
    Me->>C: Ships the order 
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 15 days of 1st instalment)
    C->>I: Pays 2nd instalment within 30 days, and 3rd within 60 days 

{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| in3's credit check is in progress. {{< br >}} You can still cancel. | Initialized   | Initialized  |
| in3 is waiting for the customer to pay the first installment (within 5 mins). | Uncleared  | Initialized  |
| The customer has paid the first installment. {{< br >}} Settlement is now guaranteed. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| You can [manually change the order status to Shipped](/about-payments/pay-later-shipped-status/) for your records, but this is not required to trigger invoicing. | Shipped | Uncleared | 
| MultiSafepay has collected payment. | Completed | Completed |
| in3 declined the transaction. | Declined | Declined |
| The customer cancelled the transaction or abandoned payment of the first installment. | Void | Void |
| The customer didn't pay the first installment. | Expired | Expired |
|**Refunds**|||
| in3 has successfully processed a full or partial refund. | Completed | Completed |
| The refund was declined. | Declined | Declined   |


