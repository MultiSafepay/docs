---
title: "Google Analytics tracking via the API"
weight: 5
meta_title: "FAQ API - Google Analytics tracking - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

You can track the behavior of your customers through Google Analytics [tracking](/api/#create-an-order).  

This only applies to redirect calls. When the customer reaches the MultiSafepay payment page, the UA-code is generated and appears in the HTML.

Tracking isn't available for direct calls because the customer doesn't go to a MultiSafepay page between checkout and the successful payment page. 

For more information, see [Difference between direct and redirect calls](/faq/api/difference-between-direct-and-redirect).