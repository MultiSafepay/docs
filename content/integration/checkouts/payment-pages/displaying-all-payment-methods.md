---
title : "Displaying all payment methods on payment pages"
weight: 50
meta_title: "Displaying all payment methods on payment pages - MultiSafepay Docs"
read_more: "."
url: "/payment-pages/displaying-payment-methods/"
aliases:
    - /tools/payment-pages/show-all-methods
    - /payments/checkout/payment-pages/displaying-all-payment-methods/
---

If a customer's country is unclear or your [backend](/glossaries/multisafepay-glossary/#backend) doesn't let you provide the correct country code, consider displaying all your enabled payment methods on the payment page. This is not supported for [deprecated payment pages](/payment-pages/deprecated/).

To display all payment methods on the payment page, follow these steps:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) to retrieve the payment link.
2. Add `&methods=all` at the end of the payment link, e.g.: `https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL&methods=all`
3. Redirect the customer to the adapted link.

**Note:** This is not a standard option in our [ready-made integrations](/integrations/ready-made/). 

