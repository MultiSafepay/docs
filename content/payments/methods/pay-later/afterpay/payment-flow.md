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

The table below shows a successful payment flow from start to finish.  

{{< details title="Order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|  | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects AfterPay at checkout. |  |  |
| 2. | AfterPay authorizes the payment. | Uncleared | Uncleared |
| 3. | Once authorized, MultiSafepay sends a capture to AfterPay.  | Completed  | Uncleared  |
| 4. | Ship the order. {{< br >}} You **must**: {{< br >}} - Manually change the order status to **Shipped** (see below). {{< br >}} - Ship the order to receive payment. | Shipped | Uncleared |
| 6. | AfterPay invoices the customer with a standard payment period of 14 days. Settlement is now guaranteed. | | |
| 7. | The customer completes the payment with AfterPay via [iDEAL](/payments/methods/banks/ideal/) or online banking, within 14 days unless otherwise agreed in writing. |  |  |
| 8. | AfterPay settles the funds with MultiSafepay. | Shipped | Completed |
| 9. | MultiSafepay settles the funds in your MultiSafepay balance.|  |  |

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

### Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| AfterPay has declined the payment. AfterPay only provides the reason directly to the customer, for privacy and compliance reasons. {{< br >}} **Or** {{< br >}} The payment was cancelled. | Void | Cancelled |
| You did not ship the order within 90 days of creating the transaction and it expired. | Expired | Expired |

### Return process
If the customer returns some items from the order and this takes a long time to verify, you can pauze the collection period for 2 to 4 weeks. 

Phone +31 207230230 or email <merchant@afterpay.com> 

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized    | Completed   |
| The refund was successfully processed.  | Completed      | Completed   |
