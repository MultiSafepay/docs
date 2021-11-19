---
title: 'CSRF errors'
weight: 3
meta_title: "CSRF errors - MultiSafepay Docs"
read_more: "."
aliases:
    - /faq/errors-explained/csrf
    - /faq/errors-explained/csrf-errors
---

The cross-site request forgery (CSRF) warning appears on payment pages when customers access them through POST requests.

This can occur when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a POST request.
 
* `https://api.multisafepay.com` accepts POST and GET requests
* `https://payv2.multisafepay.com` only accepts GET requests.
 
For support, email the Integration Team at <integration@multisafepay.com>

