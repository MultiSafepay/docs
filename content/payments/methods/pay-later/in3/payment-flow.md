---
title: 'in3 payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "in3 payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/svgs/in3.svg'
url: '/payment-methods/in3/payment-flow/'
aliases:
    - /payments/methods/billing-suite/in3/payment-flow/
    - /payments/methods/billing-suite/in3/user-guide/changing-order-status-to-shipped/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|                       | Flow      | Order status | Transaction status |
|-----|----|---|------|
| 1. | The customer selects in3 at checkout, is redirected to in3, and enters their details. | Initialized   | Initialized  |
| 2. | in3 authorizes the payment. |   |   |
| 3. | The customer has 5 minutes to pay the first installment, or the transaction is cancelled. {{< br >}} The first installment is required to create the order. | Uncleared  | Initialized  |
| 4. | The customer pays the first installment. {{< br >}} Settlement is now guaranteed. | Completed  | Uncleared  |
| 5. | Ship the order. {{< br >}} **Important:** You **must** manually change the order status to **Shipped** (see below).  | Shipped | Uncleared | 
| 6. | MultiSafepay settles the funds in your MultiSafepay balance (within 15 days of the first installment). | Completed | Completed |
| 7. | The customer has 30 days to pay the second installment, and 60 days to pay the third. |  | |

{{< details title="Changing order status to Shipped" >}}

Changing the order status from **Completed** to **Shipped** prevents the order expiring, and triggers in3 to invoice customer and transfer the funds to MultiSafepay. 

**In your MultiSafepay account**

To change the order status in your MultiSafepay account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the Track & Trace details, if relevant.

**In your backend**

If you change the order status to **Shipped** in your [backend](/getting-started/glossary/#backend), some MultiSafepay plugins can pass the updated status to your MultiSafepay account automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other MultiSafepay plugins, you can forward the status via our API by making a `PATCH /orders` request. 

Some third-party plugins may not support forwarding the status via our API. 

See API reference – [Update an order](/api/#update-an-order).
{{< /details >}}

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|----|---|----------|
| in3 has declined the payment. No order was created.    | Declined   | Declined   |
| The payment was cancelled or abandoned. | Void    | Void    |

## Refund statuses

| Description                      | Order status      | Transaction status |
|----|-----|-----|
| in3 has successfully processed a full or partial refund. | Completed    | Completed   |
| in3 has declined a full or partial refund request.  | Declined      | Declined   |


