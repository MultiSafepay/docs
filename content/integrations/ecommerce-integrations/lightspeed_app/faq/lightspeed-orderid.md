---
title: "How do I synchronise a generated payment link with Lightspeed?"
meta_title: "Lightspeed plugin - How do I synchronise a generated payment link with Lightspeed? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
draft: true
---

When a payment link is generated in your [MultiSafepay Control](https://merchant.multisafepay.com), an _orderID_ is required. This is necessary to link the transaction to the correct _orderID_ in the Lightspeed ecommerce platform.

However, Lightspeed is displaying a reference number _ORD_ which is often mistaken for an order ID.
Due to this confusion, when a payment link is generated from the MultiSafepay Control without an order ID, the reference number is used instead of the order ID.
In this case, a payment received through a payment link is not linked to the order ID of the Lightspeed ecommerce platform.

The order ID that should be used when generating a payment link in your MultiSafepay Control is displayed in the URL of the Lightspeed ecommerce platform.

On the order detail page of the Lightspeed ecommerce platform, the correct order ID will be displayed in the URL.

_Example: https://yourdomain.webshop.com/admin/dmin/orders/994152471?offset=7
In this case the order ID is 94152471._
