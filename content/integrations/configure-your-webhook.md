---
title: 'Configure your webhook endpoint'
category: 62962dd7e272a6002ebbbbc5
order: 402
hidden: false
parentDoc: 62a9a54a66018200436bdb74
excerpt: 'Configure a webhook to receive updates about orders.'
slug: 'configure-your-webhook'
next:
  description: Handle notifications
  pages:
    - type: doc
      icon: file-text-o
      name: Handle notifications
      slug: handle-notifications
      category: integrations
---

MultiSafepay uses a webhook to send updates about orders and other notifications to your web server.

You can configure the webhook at site level or at order level.

# How it works

The webhook is triggered when we have data to send you, or when the <<glossary:order status>> or <<glossary:transaction status>> changes, e.g. when:

- A customer completes payment
- A customer's payment is declined or fails
- An order has shipped
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the `POST` method to inform your web server when there is an update, and shares details on what has changed. This is more efficient than a poll-based `GET` method where your web server must continually check for updates. We do support `GET` as a `notification_method`, but we strongly recommend `POST` because it's more efficient.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/webhook-flow.svg" alt="Webhook communication flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

> ℹ Note
> International bank account numbers (IBANs) are sensitive data. For security reasons, we mask them by default in POST webhook notifications so that only the last 4 digits are visible, e.g. *** 1234. 
>
> To unmask them, see [IBANs](/docs/ibans/).

# Prerequisites

You must set a webhook endpoint, which is a URL that:

- Doesn't include port numbers
- Is publicly accessible, or has MultiSafepay on your allow list
- Uses HTTPS - We don't accept HTTP for security reasons.

For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

# Configuration

You can configure the webhook endpoint at:

<details id="site-level">
<summary>Site level</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Integrations** > **Sites**, and then click the relevant site.
3. On the **Site profile** page, under **Functionality**, in the **Webhook URL** field, set your webhook endpoint.

**Note:** These instructions apply to your `notification_url` for order updates. For [FastCheckout shipping options updates](/docs/fastcheckout-shipping-options), see Order level below.

</details>

<details id="order-level">
<summary>Order level</summary>
<br>

1. [Create an order](/reference/createorder/) via our API.
2. In the request body, set:
	- For order updates: 
    - `payment_options.notification_url` to your webhook endpoint 
	  - `payment_options.notification_method` to `POST`
  - For [FastCheckout shipping options](/docs/fastcheckout-shipping-options) updates:
    - `payment_options.feed_url` to your other notifications endpoint (defaults to `POST`)

---

</details>

> ℹ Note
>
> If you configure your webhook endpoint at site **and** order level, the order level endpoint is used by default.

### Example

``` javascript
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 1000,
  "description": "product description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}'
```

> ✅ Success!
> Now that you have configured your webhook endpoint, you need to configure your web server to handle notifications correctly.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)