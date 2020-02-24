---
title : "How can I show all payment methods directly?"
weight: 43
meta_title: "Payment pages - Show all payment methods - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

When the country of your customer is not fully clear or your backend does not allow you to provide for the correct country code, you might want to offer all available payment methods directly on our payment page. This is done by following these steps:

1. Retrieve the payment link by [creating an order](/api/#create-an-order)
2. Put _&methods=all_ behind the payment link
3. Redirect your customer to this adapted link.

* The payment link should now look like: 
``` https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL ```
_Please note that this an example, the link might not work_

Notes:
_This is not a standard option in our plugins. 
This will only work on our new payment pages which start with payv2. If you see no option to switch to our [new payment pages](/tools/payment-pages/what-is-payv2/), please contact us at <integration@multisafepay.com>_.
