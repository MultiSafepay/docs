---
title: 'Event notifications'
parentDoc: 64674fbc74bc4007521ebbcb
category: 6477597e0e2961004638cd5d
order: 3
hidden: false
slug: 'event-notifications'
---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in the following countries:
> 
> - Netherlands
> 
> Please note that in this stage, you cannot request terminals yet to use POS services.  
> If you are interested in participating in the next stage of our pilot, email <sales@multisafepay.com>
>

Subscribe to event notifications to receive order payments updates when, e.g.,

- A customer completes the payment.
- The payment has been cancelled or declined.

# Prerequisites

- SmartPOS terminal must be [activated in your MultiSafepay account](/docs/getting-started-guide/).
- Payments must be initiated via [cloud <<glossary:POS>> payment](/docs/solutions).

# 1. Initiate payments

1. [Create an order](/reference/createorder/), and set`terminal_id` in your request. See Recipe - [Event notifications.](/recipes/cloud-payment-notifications)
2. In response to the API request you made, you receive a `event_url` and `event_token`.
3. Copy the `event_url` and `event_token`.

📘 **Note:** You cannot initiate another payment until the current payment is **Cancelled** or **Completed**.

# 2. Subscribe to the event notifications

To subscribe to event notifications, pass the `events_url` and `events_token` to the <a href="https://github.com/MultiSafepay/message-bus" target="_blank">Message-bus-js</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 3. Payment statuses

The table below sets out possible payment statuses and what they commonly mean.

| Description                  | Payment status |
| :---------------------------| :-------------- |
| The <<glossary:card scheme>> is processing your payment request. | Initialized    |
| he payment has been cancelled on the terminal or via API. For more information - see [Cancellation.](/docs/solutions#cancellation)  <br>**Note:**  You can now initiate another cloud POS payment.   | Cancelled.     |
| The customer has completed the payment.  <br>**Note:**  You can now initiate another cloud POS payment.  | Completed      |
| The <<glossary:card scheme>> has declined the payment. The customer will be redirected to the payment screen to retry the payment.  | Declined. |

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]