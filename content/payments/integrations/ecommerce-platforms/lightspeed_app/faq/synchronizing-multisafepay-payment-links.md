---
title: "Synchronizing MultiSafepay payment links"
meta_title: "Lightspeed app - Synchronizing MultiSafepay payment links - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/lightspeed_app/faq/lightspeed-orderid/
---

When you generate a payment link in your [MultiSafepay account](https://merchant.multisafepay.com), you cannot update the transaction status or link it to a transaction in Lightspeed via our app. This is by design in Lightspeed. 

To link the transaction to the corresponding order ID in the Lightspeed platform, provide the Lightspeed order ID from the URL on the relevant **Order details** page, e.g. https://yourdomain.webshop.com/admin/dmin/orders/994152471?offset=7 Order ID = 94152471.

**Note:** Do **not** provide the Lightspeed `ORD` reference number. 

