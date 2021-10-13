---
title : "Changing order status to Shipped"
meta_title: "Betaal per Maand - Changing order status to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 3
url: '/payment-methods/betaal-per-maand/changing-order-status-to-shipped/'
aliases:
    - /payments/methods/billing-suite/betaalpermaand/user-guide/changing-order-status-to-shipped/
---

Changing the order status from **Completed** to **Shipped** prevents the order expiring, and triggers Betaal per Maand to invoice the customer and transfer the funds to MultiSafepay. 

## In your MultiSafepay account

To change the order status in your MultiSafepay account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the Track & Trace details, if relevant.

At this point, you also need to [provide the track-and-trace code](/payments/methods/billing-suite/betaalpermaand/faq/providing-track-and-trace/).

## In your backend

If you change the order status to **Shipped** in your [backend](/getting-started/glossary/#backend), some MultiSafepay plugins can pass the updated status to your MultiSafepay account automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other MultiSafepay plugins, you can forward the status via our API by making a `PATCH /orders` request. 

Some third-party plugins may not support forwarding the status via our API. 

See API reference – [Update an order](/api/#update-an-order).


