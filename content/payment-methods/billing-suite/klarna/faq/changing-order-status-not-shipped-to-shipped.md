---
title : "Changing order status from Not shipped to Shipped"
meta_title: "Klarna - Changing order status from Not shipped to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---

When the customer chooses to pay with Klarna, MultiSafepay creates a Klarna transaction with **Not shipped** status. 

Klarna does not support auto-ship functionality, so after you ship the order to the customer, you need to change the order status to **Shipped** to start communicating with the customer. There are 3 ways to do this:

- Change the status manually in your MultiSafepay Control.
- Use our API to automatically change the status in your custom integration.
- Some ecommerce integrations change the status automatically. Check in your integration.

To change the order status manually, follow these steps:

- Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
- Go to **Transactions** > **Transactions overview**.
- Search for the transaction, and click to open the **Transaction details** page. 
- Under **Order details**, click **Change order status**. 
- Change the status to **Shipped**.
- Send the customer the Track & Trace details, if relevant.

After 14 business days, MultiSafepay receives the funds from Klarna and makes them available to merchants. After 18-19 days, MultiSafepay adds the funds to your MultiSafepay balance when the transaction status changes to **Completed**.