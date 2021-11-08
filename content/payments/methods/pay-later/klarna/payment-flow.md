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

## How it works

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

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#klarna---direct)  
The customer selects Klarna at checkout and is redirected straight to Klarna.  

[Redirect flow](/api/#klarna---redirect)  
The customer:

- Selects Klarna at checkout and is redirected to a MultiSafepay payment page 
- Provides their birthdate, email address, and phone number, and accepts the terms and conditions
- Is redirected to your success page

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
| The refund has been successfully processed.  | Completed      | Completed   |


