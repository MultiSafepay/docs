---
title : "How does shipping work within Shopware 5?"
meta_title: "How does shipping work within Shopware 5? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

In the Shopware 5 plugin, it is mandatory to _ship_ goods in order to be paid.

Shipping within Shopware 5 works by __changing__ the order status to _Shipped_ in the order details. If your Shopware 5 plugin is older than version 2.5.0, you can ship the order by __clicking__ on the _Ship_ button in the order details.

The track-and-trace code will be issued when goods are shipped.