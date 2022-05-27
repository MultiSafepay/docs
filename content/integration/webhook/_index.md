---
title : "Webhook"
meta_title: "Webhook - MultiSafepay Docs"
weight: 60
read_more: "."
layout: single
logo: "/svgs/General.svg"
url: "/integrations/webhooks/"
short_description: 'Receive updates about orders and other notifications.'
aliases:
    - /faq/api/how-does-the-notification-url-work
    - /faq/api/notification-url
    - /developer/api/notification-url
    - /integration/webhooks/
---

MultiSafepay uses a webhook to send you updates about orders and other notifications.

The webhook is triggered when the [order or transaction status](/about-payments/multisafepay-statuses/) changes, e.g. when:

- A customer completes payment
- A customer's payment is declined or fails
- An order has shipped
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the `POST` method to inform your web server when there is an update, and shares details on what has changed. This is more efficient than a poll-based method where your web server must continually check for updates.

{{< mermaid class="text-center" >}}

sequenceDiagram
    participant C as Customer
    participant Mu as MultiSafepay
    participant Me as Merchant

    C-->>Mu: Completes payment
    Mu->>Me: Sends notification
    Me-->>Me: Updates order in system
    Me->>Mu: Sends acknowledgement

{{< /mermaid >}}
&nbsp;  

## Integration requirements

If you use one of our [ready-made integrations](/integrations/ready-made/), this is set up automatically for you and you don't need to do anything.

If you use one of our [wrappers or SDKs](/developer/wrappers/), then you need to configure this as part of your integration. For more information, read the documentation that comes with the wrapper or SDK.

If you are building your own integration, you need to configure this yourself. See [Configure your webhook endpoint](/integrations/self-made/configure-your-webhook/).