---
title: "Difference between direct and redirect API calls"
weight: 1
meta_title: "FAQ API - Difference between direct and redirect - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---

In our API, you can make direct and redirect calls.

### Direct calls

Direct calls connect directly to the specified payment method and either:

- Generate a direct link to the payment method, e.g. specifying iDEAL in the `gateway` parameter takes the customer to the payment page of their bank. 
- Complete the transaction immediately without the customer having to do anything. 

You can make direct calls repeatedly, e.g. for [recurring payments](/tools/recurring-payments).

### Redirect calls

Redirect calls send the customer to a MultiSafepay payment page for the specified payment method, e.g. specifying Visa in the `gateway` parameter includes fields on the payment page for the customer to fill in their Visa credit card information. The customer doesn't leave the MultiSafepay payment page.

If you leave the `gateway` parameter empty, all payment methods enabled in your MultiSafepay Control appear on the [payment page](/tools/payment-pages/what-is-payv2/).
