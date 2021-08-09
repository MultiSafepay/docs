---
title: "Google Analytics tracking via the API"
weight: 5
meta_title: "API Documentation - Google Analytics tracking - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/google-analytics-tracking
    - /faq/general/tracking-payment-metrics-in-google-analytics/
---

You can track the behavior of your customers through Google Analytics [tracking](/api/#create-an-order).  

This only applies to redirect calls. When the customer reaches the MultiSafepay payment page, the UA-code is generated and appears in the HTML.

Tracking isn't available for direct calls because the customer doesn't go to a MultiSafepay page between checkout and the successful payment page. 

For more information, see [Difference between direct and redirect calls](/developer/api/difference-between-direct-and-redirect).