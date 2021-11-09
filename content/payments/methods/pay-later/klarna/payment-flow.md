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
    Note over K,C: You can customize the invoice! 
    C->>K: Completes payment with preferred payment method
    K->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 21 days)

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to Klarna. | [API reference](/api/#klarna---direct) |
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to provide their birthdate, email address, and phone number, and accepts the term and conditions. {{< br >}} They are then redirected to your success page. | [API reference](/api/#klarna---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. {{< br >}} You can cancel the transation at this stage. {{< br >}} See [Reservation number](/payment-methods/klarna/reservation-invoice-numbers/) (for queries to Klarna) | Uncleared   | Initialized  |
| Klarna has authorized the payment. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| Manually [change the order status to Shipped](/payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/). {{< br >}} See: {{< br >}} - [Extend the shipping period](/payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/) {{< br >}} - [Supported addresses](/payments/methods/billing-suite/klarna/user-guide/supported-addresses/) {{< br >}} - [Invoice number](/payment-methods/klarna/reservation-invoice-numbers/) (for queries to Klarna) | Shipped | Uncleared |
| The transaction is complete. | Shipped    | Completed  |
| Klarna declined the transaction, or it was cancelled. {{< br >}} For more information, email <klarna@multisafepay.com> {{< br >}}    | Void   | Cancelled |
| You did not [change the order status to Shipped](/payment-methods/klarna/changing-order-status-to-shipped/) within 28 days. {{< br >}} See [Handling expired orders](/payment-methods/klarna/handling-expired-orders/).  | Expired    | Expired    |

## Refund statuses

| Description  | Order status      | Transaction status |
|-----|----|------|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund is complete.  | Completed      | Completed   |


