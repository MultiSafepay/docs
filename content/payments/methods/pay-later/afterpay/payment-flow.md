---
title: 'AfterPay payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "AfterPay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
url: '/payment-methods/afterpay/payment-flow/'
aliases:
    - /payments/methods/billing-suite/afterpay/payment-flow/
    - /payments/methods/pay-later/afterpay/user-guide/changing-order-status-to-shipped/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as AfterPay
    participant Me as Merchant

    C->>Mu: Selects AfterPay at checkout
    Mu->>C: Connects to AfterPay (direct/redirect)
    A->>Mu: Authorizes the payment
    Mu->>A: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    A->>C: Sends invoice (standard period of 14 days) 
    Note over A,C: Settlement is now guaranteed!
    C->>A: Completes payment with preferred method
    A->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to AfterPay. | 
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to accept the terms and conditions and provide their birth date, email address, and phone number. {{< br >}} They are then redirected to your success page. |

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| AfterPay is authorizing the payment. {{< br >}} You can still cancel it. | Uncleared | Uncleared |
| MultiSafepay has sent a capture to AfterPay. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} You must ship to receive payment. | Shipped | Uncleared |
| The transaction is complete. | Shipped | Completed |
| AfterPay has declined the payment **or** the payment was cancelled. {{< br >}} AfterPay only provides the reason directly to the customer, for privacy and compliance reasons.  | Void | Cancelled |
| You did not ship within 90 days of creating the transaction and it expired. | Expired | Expired |

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund is complete.  | Completed      | Completed   |

