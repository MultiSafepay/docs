---
title : "Changing the order status to Shipped"
meta_title: "Shopware 5 plugin - Changes to the new pluginChanging the order status to Shipped  - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---

For [Billing Suite](/payment-methods/billing-suite/) payment methods, after you ship the order to the customer, you need to change the order status from **Completed** to **Shipped**. This prevents the order expiring, and lets the payment method initiate the billing process with the customer and pay the transaction out to your MultiSafepay balance. 

If you change the order status to **Delivered** in your backend, the updated status is passed to your MultiSafepay account automatically.