---
title : "Changing order status from Completed to Shipped"
meta_title: "Klarna - Changing order status from Completed to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---

When you agree with an order and ship it, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets Klarna initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance.

You can do this:

- Automatically using our [API](https://docs.multisafepay.com/api/#update-an-order), which updates your MultiSafepay Control 
- Automatically in your [ecommerce integration](/integrations/ecommerce-integrations)
- Manually in your [MultiSafepay Control](https://merchant.multisafepay.com)

To change the order status manually, follow these steps:

1. Go to **Transactions** > **Transactions overview**.
2. Search for the transaction and click to open the **Transaction details** page.
3. Use the **Change order status** field.