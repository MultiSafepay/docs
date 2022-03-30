---
title: "Google Analytics tracking via our API"
weight: 2
meta_title: "Google Analytics tracking via our API - MultiSafepay Docs"
read_more: "."
url: '/developer/google-analytics-tracking-api/'
aliases:
    - /developer/api/google-analytics-tracking/
    - /faq/api/google-analytics-tracking
    - /faq/general/tracking-payment-metrics-in-google-analytics/
---

You can track the behavior of your customers through Google Analytics [tracking](/api/#create-an-order).  

This only applies to [redirect](/developer/direct-vs-redirect/) requests. When the customer reaches the payment page, the UA-code is generated and appears in the HTML.

Tracking isn't available for [direct](/developer/direct-vs-redirect/) requests because the customer doesn't go to a [payment page](/payment-pages/) between your checkout and success page. 
