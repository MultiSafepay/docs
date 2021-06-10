---
title: "Synchronizing MultiSafepay payment links"
meta_title: "Lightspeed app - Synchronizing MultiSafepay payment links - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/lightspeed_app/faq/lightspeed-orderid/
---

When a payment link is generated in your [MultiSafepay Control](https://merchant.multisafepay.com), an order ID is required to link the transaction to the corresponding order ID in the Lightspeed platform. 

However, users often mistake Lightspeed's reference number `ORD` for the order ID. As a result, payments received via the MultiSafepay payment link are not linked to the Lightspeed order ID.

The correct Lightspeed order ID to use when generating a payment link in your MultiSafepay Control appears in the Lightspeed URL on the relevant **Order details** page, e.g. https://yourdomain.webshop.com/admin/dmin/orders/994152471?offset=7 Order ID = 94152471.
