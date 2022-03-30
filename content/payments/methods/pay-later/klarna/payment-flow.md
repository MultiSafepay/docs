---
title: 'Klarna payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Klarna payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
url: '/payment-methods/klarna/payment-flow/'
aliases:
    - /payments/methods/billing-suite/klarna/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant K as Klarna
    participant Me as Merchant

    C->>Mu: Selects Klarna at checkout
    Mu->>C: Connects to Klarna (direct/redirect)
    K->>Mu: Authorizes the payment
    Mu->>K: Captures the funds
    Note over Mu,K: Settlement is now guaranteed!
    Me->>C: Ships the order (within 28 days, or extend the shipping period)
    Note over Me,C: Manually change the order status to Shipped! 
    K->>C: Sends invoice 
    Note over K,C: You can customize the invoice. 
    C->>K: Completes payment with preferred payment method
    K->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 21 days)

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to Klarna. | 
| **Redirect flow** | The customer is redirected to a [payment page](/payment-pages/) to provide their birth date, email address, and phone number, and accept the term and conditions. {{< br >}} They are then redirected to your success page. | 

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Klarna. {{< br >}} You can still cancel with Klarna (see [Reservation number](/payment-methods/klarna/reservation-invoice-numbers/)). | Initialized   | Initialized  |
| Klarna has authorized the transaction and the funds are awaiting capture. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} See: {{< br >}} - [Extend the shipping period](/payment-methods/klarna/extending-shipping-period/) {{< br >}} - [Invoice number](/payment-methods/klarna/reservation-invoice-numbers/) (for queries to Klarna) {{< br >}} **Note:** The billing and shipping addresses must be the **same**. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| The transaction expired after 1 hour or you didn't [change the order status to Shipped](/about-payments/pay-later-shipped-status/) within 28 days. {{< br >}} See [Handling expired orders](/payment-methods/klarna/handling-expired-orders/).  | Expired    | Expired    |
| Klarna authorized the transaction, but either you or the customer cancelled it before capture. | Void   | Void |
| Klarna declined the transaction. {{< br >}} Only the customer can contact Klarna to find out why they declined the transaction. {{< br >}} For merchant support, email <klarna@multisafepay.com> {{< br >}} | Declined | Declined |

## Refund statuses

| Description  | Order status      | Transaction status |
|-----|----|------|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund is complete.  | Completed      | Completed   |


