---
title: 'Configure your webhook endpoint'
breadcrumb_title: "Configure your webhook endpoint"
layout: 'single'
meta_title: 'Build your integration – Configure your webhook endpoint - MultiSafepay Docs'
logo: '/svgs/Wrappers.svg'
short_description: 'Configure a webhook to receive updates about orders'
weight: 1
url: '/integrations/self-made/configure-your-webhook/'
---

MultiSafepay uses a [webhook](/integration/webhooks/) to send updates about orders and other notifications to your web server.

You can configure the webhook at website level or at order level.

### Requirements

You must set a webhook endpoint, which is a URL that:

- Doesn't include port numbers.
- Is publicly accessible, or has MultiSafepay on your allow list.
- Uses HTTPS - We don't accept HTTP for security reasons.

For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

### Website level

To configure the webhook endpoint at website level:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Select the relevant website.
4. In the **Notification URL** field, set your webhook endpoint.

### Order level

To configure the webhook endpoint at order level:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) via our API.
2. In the request body, set:
	- `payment_options.notification_url` to your webhook endpoint
	- `payment_options.notification_method` to `POST`

    {{< collapse title="Note" size="h3" >}}
We do support `GET` as a `notification_method`, but we strongly recommend to use `POST`, which is the most efficient.
{{< /collapse >}}

**Example**:

```
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

## Next steps

{{< two-buttons
href-1="/integrations/self-made/manage-orders" header-1="Previous" text-1="Manage orders" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/integrations/self-made/handle-notifications" header-2="Next" text-2="Handle notifications" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}