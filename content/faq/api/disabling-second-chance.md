---
title: "Disabling Second Chance emails"
weight: 4
meta_title: "FAQ API - Disabling Second Chance emails - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/api/disable-second-chance
---

You can disable Second Chance emails through an API call. In the transaction request when you [create an order](/api/#create-an-order), enter the value `false` instead of `true`.