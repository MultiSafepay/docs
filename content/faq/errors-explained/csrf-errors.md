---
title: 'CSRF errors'
weight: 3
meta_title: "FAQ Errors - CSRF errors - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/errors-explained/csrf
---

The cross-site request forgery (CSRF) warning appears on payment pages when customers access them through POST requests.

This can occur when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a POST request.
 
* `https://api.multisafepay.com` accepts POST and GET requests
* `https://payv2.multisafepay.com` only accepts GET requests.
 
For support, email the Integration Team at <integration@multisafepay.com>

