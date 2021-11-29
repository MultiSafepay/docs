---
title : "Webhooks"
meta_title: "Webhooks - MultiSafepay Docs"
weight: 3
read_more: "."
logo: '/svgs/Wrappers.svg'
aliases:
    - /faq/api/how-does-the-notification-url-work
    - /faq/api/notification-url
    - /developer/api/notification-url
---

MultiSafepay uses a webhook to notify you about updates to your orders.

The webhook is triggered when the [order or transaction status](/payments/multisafepay-statuses/) changes, e.g. when:
- A customer completes payment
- A customer's attempt to pay fails (order status **Initialized**, transaction status **Void**)
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the POST method to inform your web server when there is an update and shares details on what has changed. This is more efficient than a poll-based method where your web server must continually check for updates.

{{< mermaid class="text-center" >}}

sequenceDiagram
    participant C as Customer
    participant Mu as MultiSafepay
    participant Me as Merchant

    C-->>Mu: Completes payment
    Mu->>Me: Sends notification
    Me-->>Me: Updates order in system

{{< /mermaid >}}
&nbsp;  

## Integration requirements

If you use one of our [ready-made integrations](/getting-started/create-your-integration/#ready-made-integrations) this is set up automatically for you and you don't need to do anything.

If you use one of our [wrappers or SDKs](/developer/wrappers/) then you need to configure this as part of your integration. For more information, read the documentation that comes with the wrapper or SDK.

If you are creating your own custom integration, you need to configure this yourself. See - [Build your own](/getting-started/create-your-integration/build-your-own/).