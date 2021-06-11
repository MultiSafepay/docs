---
title : "How does shipping work within Shopware 6?"
meta_title: "How does shipping work within Shopware 6? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---
In the Shopware 6 plugin, it is mandatory to _ship_ goods in order to be paid.

Shipping within Shopware 6 works by __changing__ the order status to _Shipped_ in the order details.

The track-and-trace code will be issued when goods are shipped.