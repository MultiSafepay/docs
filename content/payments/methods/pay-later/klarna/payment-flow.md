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
    Mu->>K: Sends a capture
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    K->>C: Sends invoice (standard period of 14 days) 
    Note over K,C: Settlement is now guaranteed!
    C->>K: Completes payment with preferred method
    K->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#afterpay---direct)  
The customer selects AfterPay at checkout and is redirected straight to AfterPay.  

[Redirect flow](/api/#afterpay---redirect)  
The customer:

- Selects AfterPay at checkout and is redirected to a MultiSafepay payment page 
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
| 1. | The customer selects Klarna at checkout and is redirected to the Klarna payment page to initiate a transaction. {{< br >}} See also [Reservation and invoice numbers](/payments/methods/billing-suite/klarna/user-guide/reservation-and-invoice-number/). | Uncleared   | Initialized  |
| 2. | Klarna authorizes the payment. Settlement is now guaranteed, but not received until after you ship the order. | Completed  | Uncleared  |
| 3. | Ship the order within 28 days, or [extend the shipping period](/payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/). {{< br >}} You **must**: {{< br >}} - Ship the order to receive payment. {{< br >}} - Manually [change the order status to Shipped](/payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/). {{< br >}} See also [Supported addresses](/payments/methods/billing-suite/klarna/user-guide/supported-addresses/). | Shipped | Uncleared |
| 4. | Klarna invoices the customer. {{< br >}} See also [Customizing invoices](/payments/methods/billing-suite/klarna/user-guide/customizing-invoices/). | | |
| 5. | Klarna settles the funds with MultiSafepay, and we add them to your MultiSafepay balance within 21 days. | Shipped    | Completed  |

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|------|----|----|
| Klarna did not authorize the transaction. For more information, email <klarna@multisafepay.com> {{< br >}} **Or** {{< br >}} The customer or merchant cancelled the payment.    | Void   | Cancelled |
| You did not [change the order status to Shipped](/payment-methods/klarna/changing-order-status-to-shipped/) within 28 days. {{< br >}} See [Handling expired orders](/payment-methods/klarna/handling-expired-orders/).  | Expired    | Expired    |

## Refund statuses

| Description  | Order status      | Transaction status |
|-----|----|------|
| The customer requests a refund. | Initialized    | Completed   |
| The refund is successfully processed.  | Completed      | Completed   |

{{< details title="Get support" >}} 

**Merchants**: Email MultiSafepay at <klarna@multisafepay.com>

**Customers**:

- See Klarna – [Contact customer service](https://www.klarna.com/international/contact-customer-service).
- Email the Support Team at <support@multisafepay.com>

{{< /details >}}
