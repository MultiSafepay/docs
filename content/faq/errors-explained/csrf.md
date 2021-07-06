---
title: 'CSRF'
weight: 10
meta_title: "FAQ CSRF - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

CSRF, also known as Cross-Site Request Forgery.
 
The warning CSRF is displayed on our payment page when the customer is reaching it through a POST request.
This can occur when you are having an HTML form through which you send the customer to `https://payv2.multisafepay.com` with a POST request.
 
* `https://api.multisafepay.com` will accept POST and GET requests
* `https://payv2.multisafepay.com` will only accept GET requests.
 
If you are seeing this issue and are having difficulties resolving this error, do not hesitate to contact us at <integration@multisafepay.com>

For more information, see our full [API Documentation](/api)

