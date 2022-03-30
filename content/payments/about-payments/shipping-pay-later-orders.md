---
title: "Shipping pay later orders"
weight: 50
meta_title: "Shipping pay later orders - MultiSafepay Docs"
read_more: "."
url: '/about-payments/pay-later-shipped-status/'
---

For [pay later methods](/payment-methods/pay-later/), you must manually change the [order status](/about-payments/multisafepay-statuses/) from **Completed** to **Shipped**. This triggers the payment method to invoice the customer and transfer the funds to MultiSafepay. It also prevents the order from expiring. 

## In your MultiSafepay dashboard

To change the order status in your MultiSafepay dashboard, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the track and trace details, if relevant.

## In your backend

If you change the order status in your [backend](/glossaries/multisafepay-glossary/#backend), the following [ready-made integrations](/integrations/ready-made/) can pass the updated status to your MultiSafepay dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, you can update the status via our API. See API reference – [Update order](https://api-docs.multisafepay.com/reference/updateorder).

**Note:** Some third-party plugins may not support updating the status via our API. 

