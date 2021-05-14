---
title : "Displaying all payment methods"
weight: 43
meta_title: "Payment pages - Displaying all payment methods - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases:
    - /tools/payment-pages/show-all-methods
---

If a customer's country is unclear or your backend doesn't let you provide the correct country code, consider displaying all your enabled payment methods on the payment page. This is only supported for [PayV2 payment pages](/tools/payment-pages/activating-payv2/).

To display all payment methods on the payment page, follow these steps:

1. [Create an order](/api/#create-an-order) to retrieve the payment link.
2. Put `&methods=all` behind the payment link, e.g.:

``` https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL ```

3. Redirect the customer to the adapted link.

**Note:** This is not a standard option in our [ecommerce integrations](/integrations/ecommerce-integrations). 

