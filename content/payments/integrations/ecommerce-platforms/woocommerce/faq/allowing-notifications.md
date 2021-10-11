---
title : "Allowing notifications"
meta_title: "WooCommerce plugin - Allowing notifications - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
url: '/woo-commerce/notifications/'
aliases:
    - /integrations/ecommerce-integrations/woocommerce/faq/rest-endpoint-is-blocked/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/allowing-notifications/
---

Notifications are webhooks our API uses to notify your server when the status of a transaction changes. They are triggered by actions like:

- Customers completing a payment
- Merchants processing a refund

From WooCommerce version 4.7.0, notifications via `POST` requests, instead of `GET` requests.  

However, sometimes the REST endpoint used to process notifications may be blocked by a firewall at server level or by some WordPress plugins at application level. In this case, ensure you include MultiSafepay requests on your safelist. 

For more information, see [Notification URL](/developer/api/notification-url/).