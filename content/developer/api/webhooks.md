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

MultiSafepay provides a webhook that you can use to receive notifications when there are updates to your orders.

Webhooks send notifications in real-time when an event occurs. For MultiSafepay this can be when:
- A customer completes payment
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the POST method to inform your web server when there is an update and shares details on what has changed. This is more efficient than a poll-based method where your web server must continually check for updates.

{{< mermaid class="text-center" >}}

sequenceDiagram
    participant C as Customer
    participant Mu as MultiSafepay
    participant Me as Merchant

    C-->>Mu: Customer completes payment
    Mu->>Me: Notification
    Me-->>Me: Updates order in system

{{< /mermaid >}}
&nbsp;  

If you use one of our [ready-made integrations](/getting-started/create-your-integration/#ready-made-integrations) this is set up automatically for you and you don't need to do anything.

If you use one of our [wrappers or SDKs](/developer/wrappers/) then you need to configure this as part of your integration. For more information, read the documentation that comes with the wrapper or SDK.

If you are creating your own custom integration, you need to configure this yourself. See - [Build your own](/getting-started/create-your-integration/build-your-own/).