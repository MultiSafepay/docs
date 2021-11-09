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

## How it works

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
| AfterPay is authorizing the payment. {{< br >}} You can still cancel the transaction at this point. | Uncleared | Uncleared |
| MultiSafepay has sent a capture to AfterPay. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| Manually change the order status to **Shipped** (see below). {{< br >}} You must ship to receive payment. | Shipped | Uncleared |
| The transaction is complete. | Shipped | Completed |
| AfterPay has declined the payment. AfterPay only provides the reason directly to the customer, for privacy and compliance reasons. {{< br >}} **or** the payment was cancelled. | Void | Cancelled |
| You did not ship the order within 90 days of creating the transaction and it expired. | Expired | Expired |

{{< details title="Changing order status to Shipped" >}}
 
Changing the order status from **Completed** to **Shipped** prevents the order expiring, and triggers AfterPay to invoice customer and transfer the funds to MultiSafepay. 

**In your MultiSafepay account**

To change the order status in your MultiSafepay account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status to **Shipped** in your [backend](/getting-started/glossary/#backend), some MultiSafepay plugins can pass the updated status to your MultiSafepay account automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other MultiSafepay plugins, you can forward the status via our API by making a `PATCH /orders` request. 

Some third-party plugins may not support forwarding the status via our API. 

See API reference – [Update an order](/api/#update-an-order).
{{< /details >}}


### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone +31 207230230 or email <merchant@afterpay.com> 

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund is complete.  | Completed      | Completed   |
