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

<details id="webhook">
<summary>Webhook</summary>
<br>

The webhook is triggered when the [order or transaction status](/payments-statuses/) changes, e.g. when:

- A customer completes payment
- A customer's payment is declined or fails
- An order has shipped
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the `POST` method to inform your web server when there is an update, and shares details on what has changed. This is more efficient than a poll-based method where your web server must continually check for updates.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/webhook-flow.svg" alt="Webhook communication flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

</details>

# Requirements

You must set a webhook endpoint, which is a URL that:

- Doesn't include port numbers.
- Is publicly accessible, or has MultiSafepay on your allow list.
- Uses HTTPS - We don't accept HTTP for security reasons.

For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

# Site level

To configure the webhook endpoint at site level:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Select the relevant site.
4. In the **Notification URL** field, set your webhook endpoint.

# Order level

To configure the webhook endpoint at order level:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) via our API.
2. In the request body, set:
	- `payment_options.notification_url` to your webhook endpoint
	- `payment_options.notification_method` to `POST`

<details id="note">
<summary>Note</summary>
<br>

We do support `GET` as a `notification_method`, but we strongly recommend to use `POST`, which is the most efficient.
</details>

**Example**:

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

Now that you have configured your webhook endpoint, you need to configure your web server to handle notifications correctly.