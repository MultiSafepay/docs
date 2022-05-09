---
title: 'Handle notifications'
breadcrumb_title: "Handle notifications"
layout: 'single'
meta_title: 'Build your integration – Handle notifications - MultiSafepay Docs'
logo: '/svgs/Wrappers.svg'
short_description: 'Handle notifications successfully.'
weight: 1
url: '/integrations/self-made/handle-notifications/'
---

When there is an update to your order, we notify your web server at the following URL through a `POST` request:  
`{your-webhook-endpoint}?transactionid=12345&timestamp=140292929`

This URL is your webhook endpoint combined with two additional parameters:

- `transactionid`: Your unique identifier for the order, previously set as `order_id` in your API request.
- `timestamp`: The time the notification was triggered.

The updated order details make up the payload of the request. 

### Check the status

Check the order status in the `status` field. If necessary, update your backend.

**Note:** You can ignore notifications that:

- Don't have the `timestamp` parameter in the URL  
- Have the same [order status](/about-payments/multisafepay-statuses/) 

### Validate the request

Every `POST` notification request includes an HMAC signature that you must use to validate its authenticity. To validate the request, you can either:

{{< two-buttons href-2="https://github.com/MultiSafepay/php-sdk/blob/master/src/Util/Notification.php" text-2="Use our PHP SDK" description-2="Use the notification function from our PHP SDK." img-2="/logo/Integrations/PHP.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/integrations/self-made/handle-notifications/validate-hmac-signatures" text-2="Validate with your own solution" description-2="Create your own solution to validate HMAC signatures." img-2="/svgs/Wrappers.svg" alt-2="Right arrow" >}}

### Acknowledge the notification

Acknowledge that you have successfully received a valid notification by returning:

- HTTP status code `200` with `OK` at the start or end of the message body, **or**
- HTTP status code `200` with `MULTISAFEPAY_OK` anywhere in the message body.

Until we receive your acknowledgement, we resend the notification 4 times at 15 minute intervals, each with a new timestamp.

### Troubleshooting notifications

If for some reason you don't receive a notification:

1. In your MultiSafepay test account, go to **Transactions** > **Transaction overview** > **Transaction details**. Scroll to the bottom to find **Offline actions**.
2. Click <img src='/img/offline-actions-webhookendpoint.png'> and check that the URL displayed is the correct webhook endpoint.
3. If the webhook endpoint is correct, click <img src='/img/offline-actions-resend.png'> to resend the notification.

If you **still** don't receive a notification, you may need to authorize MultiSafepay servers' IP addresses on your web server. For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

You have successfully configured your web server to handle notifications received from our webhook.

## Next steps

{{< two-buttons
href-1="/integrations/self-made/configure-your-webhook" header-1="Previous" text-1="Configure your webhook endpoint" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/integrations/self-made/next-steps" header-2="Next" text-2="Next steps" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}