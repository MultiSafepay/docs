---
title : "Allowing notifications"
meta_title: "WooCommerce plugin - Allowing notifications - MultiSafepay Docs"

read_more: "."
url: '/woo-commerce/notifications/'
aliases:
    - /integrations/ecommerce-integrations/woocommerce/faq/rest-endpoint-is-blocked/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/allowing-notifications/
---

MultiSafepay provides a webhook you can use to receive notifications about updates to your orders.

The webhook is triggered when the order or transaction status changes, e.g. when:
- A customer completes payment
- A customer's attempt to pay fails 
- You process a refund

From WooCommerce version 4.7.0, notifications are sent via `POST` requests, instead of `GET` requests.  

However, sometimes the REST endpoint used to process notifications may be blocked by a firewall at server level or by some WordPress plugins at application level. In this case, ensure you include MultiSafepay requests on your safelist. 

For more information, see [Webhooks](/developer/api/webhooks/).