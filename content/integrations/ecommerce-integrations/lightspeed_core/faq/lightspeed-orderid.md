---
title: "How do I synchronise a generated payment link with Lightspeed?"
meta_title: "Lightspeed plugin core synchronise generated payment link - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: [/integrations/lightspeed/faq/lightspeed-orderid/]
---

When a payment link is generated from [MultiSafepay Control](https://merchant.multisafepay.com), an _orderID_ number is required. This is necessary to link the transaction to the correct _orderID_ in the ecommerce platform of Lightspeed.

However, Lightspeed displays a reference number _ORD_ which is often mistaken for an orderID. Due to this confusion, it happens that when generating a payment link in the MultiSafepay Control, the reference number is used instead of the _orderID_.<br>

Therefore, when using a reference number, a payment received through a payment link generated in your MultiSafepay control is not linked to the _orderID_ of the ecommerce platform of Lightspeed.

The _orderID_ that should be used when generating a payment link in your MultiSafepay Control is displayed in the URL of the ecommerce platform of Lightspeed.  

In the order detail page of the ecommerce platform of Lightspeed, the correct _orderID_ will be displayed in the URL.

_Example: https://yourdomain.webshop.com/admin/dmin/orders/994152471?offset=7
In this case the _orderID_ is 94152471._

For any questions, email Lightspeed at <info.nl@lightspeedhq.com>
