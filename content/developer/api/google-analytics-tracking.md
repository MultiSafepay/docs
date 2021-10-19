---
title: "Google Analytics tracking via our API"
weight: 2
meta_title: "Google Analytics tracking via our API - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/google-analytics-tracking
    - /faq/general/tracking-payment-metrics-in-google-analytics/
---

You can track the behavior of your customers through Google Analytics [tracking](/api/#create-an-order).  

This only applies to [redirect](/developer/api/difference-between-direct-and-redirect/) requests. When the customer reaches the MultiSafepay payment page, the UA-code is generated and appears in the HTML.

Tracking isn't available for [direct](/developer/api/difference-between-direct-and-redirect/) requests because the customer doesn't go to a [MultiSafepay payment page](/payment-pages/) between your checkout and success page. 
