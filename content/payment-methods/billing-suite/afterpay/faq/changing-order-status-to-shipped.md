---
title : "Changing order status to Shipped"
meta_title: "AfterPay - Changing order status from Completed to Shipped - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 3
---

After you ship the order to the customer, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets AfterPay initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance. You can do this:

- Automatically using our [API](https://docs.multisafepay.com/api/#update-an-order), which updates your MultiSafepay Control 
- Automatically in your [ecommerce integration](/integrations/ecommerce-integrations)
- Manually in your [MultiSafepay Control](https://merchant.multisafepay.com)

To change the order status manually, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transactions overview**.
3. Search for the transaction, and click to open the **Transaction details** page. 
4. Under **Order details**, click **Change order status**. 
5. Change the status to **Shipped**.
6. Send the customer the Track & Trace details, if relevant.