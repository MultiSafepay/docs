---
title : "Changing order status to Shipped"
meta_title: "in3 - Changing order status to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 20
---

After you ship the order to the customer, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets in3 initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance. 

## In your MultiSafepay account

To change the order status in your MultiSafepay account, follow these steps:

1. Log in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the Track & Trace details, if relevant.

## In your backend

If you change the order status to **Shipped** in your backend, some MultiSafepay plugins can pass the updated status to your MultiSafepay account automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other MultiSafepay plugins, you can forward the status via our API by making a PATCH `/orders` request. 

Some third-party plugins may not support forwarding the status via our API. 

See API Reference – [Update an order](/api/#update-an-order).


