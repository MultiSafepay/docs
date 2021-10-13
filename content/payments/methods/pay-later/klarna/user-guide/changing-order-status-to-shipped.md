---
title : "Changing order status to Shipped"
meta_title: "Klarna - Changing order status to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 1
url: '/payment-methods/klarna/changing-order-status-to-shipped/'
aliases:
    - /payment-methods/billing-suite/klarna/faq/changing-order-status-completed-to-shipped/
    - /payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/
---

Changing the order status from **Completed** to **Shipped** prevents the order expiring, and triggers Klarna to invoice the customer and transfer the funds to MultiSafepay. 

## In your MultiSafepay account

To change the order status in your MultiSafepay account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the Track & Trace details, if relevant.

## In your backend

Some MultiSafepay plugins can pass the updated status to your MultiSafepay account automatically when you set the order status in your [backend](/getting-started/glossary/#backend) to:

- Magento 2: **Shipped** 
- Shopware 5: **Completed**
- WooCommerce: **Completed**

For other MultiSafepay plugins, you can forward the status via our API by making a `PATCH /orders` request. Some third-party plugins may not support this. 

See API reference – [Update an order](/api/#update-an-order).


