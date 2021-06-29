---
title : "Why notifications are not being processed?"
meta_title: "WooCommerce plugin - Why notifications are not being processed - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
- /integrations/ecommerce-integrations/woocommerce/faq/rest-endpoint-is-blocked/
---

Notifications are webhooks where the MultiSafepay API notifies your web server when the status of a transaction changes. They are triggered by actions like:

- Customers, e.g. completing a payment
- Merchants, e.g. initiating a refund

In the MultiSafepay plugin for WooCommerce version 4.7.0, we introduced a change to process notifications via POST request, instead of GET request.

You can read more about this in the following article: 

  - https://docs.multisafepay.com/faq/api/notification-url/#get-vs-post-notification

However, sometimes the REST endpoint used to process the notifications could be blocked by a firewall at server level or by some WordPress plugins at application level. 

If this is the case, most of the plugins provide a way to include the notification url in a whitelist. 
Check this with your developers to include our request in a whitelist. 

