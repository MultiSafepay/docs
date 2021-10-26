---
title: "Difference between direct and redirect API requests"
weight: 1
meta_title: "API Documentation - Difference between direct and redirect - MultiSafepay Docs"
read_more: "."
aliases:
    - /faq/api/difference-between-direct-and-redirect
---

In our API, you can make direct and redirect requests.

### Direct requests

Direct requests connect directly to the specified payment method and either:

- Generate a direct link to the payment method, e.g. specifying iDEAL in the `gateway` parameter takes the customer to the payment page of their bank. 
- Complete the transaction immediately without the customer having to do anything. 

You can make direct requests repeatedly, e.g. for [recurring payments](/features/recurring-payments/).

### Redirect requests

Redirect requests send the customer to a [MultiSafepay payment page](/payment-pages/) where they complete payment.

If you specify the payment method [`gateway`](/api/#gateways), the page is tailored to the selected payment method. For example, if the `gateway` is set to `VISA`, the page includes fields for the customer to enter their credit card details.  
If you leave the `gateway` parameter empty, all payment methods enabled in your MultiSafepay account appear on the payment page.

If you provide a [redirect URL](/developer/api/redirect-url/), after completing payment, the customer is then directed to your success/thank you page.


