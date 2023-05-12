---
title: ''
category: 6477597e0e2961004638cd5d
order: 5
hidden: false
parentDoc: 64674fbc74bc4007521ebbcb 
slug: 'smartPOS-solutions'
---

Our SmartPOS solutions lets you to initiate payments via:

- Manual input 
- Cloud-based POS  
- On-same device third-party applications
  - Web applications 
  - Native applications 

# Manual input

To start processing payments manually:

1. Enter **Amount due** and select **Pay**.
2. The customer can either tap or insert their card to make the payment.
3. Once the payment is completed, a notification is displayed.

# Cloud-based POS

 Cloud-based <<glossary:POS>> lets you initiate payments through external applications.

This diagram shows a successful cloud-based POS payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/cloud-POS.svg" alt="cloud-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>


Before initiating payments, you must ensure manual input is disabled. To disable manual input - see [SmartPOS features](docs/smartpos-features).

Create an order - see [Recipes](/recipes/cloud-payment-notifications).

To receive order payments updates subscribe to [Event notifications.](/docs/event-notifications)

<br>

***

<br>

# On-same device third-party applications

## Web application

Web applications let you initiate payments on-same devices from a browser to the payment app.

This diagram shows a successful web application payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/web-app-POS.svg" alt="web-app-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>


Before you start initiating payments, ensure manual input is disabled. To disable manual input - see [SmartPOS features](docs/smartpos-features).

Use the following URL to initiate order payments:

```Text URL
msp://?amount={$amount}&order_id={$order_id}&callback={$callback_url}&notification_url={$notification_url}
```

- `amount`: the amount specified in EUR cents. 
- `order_id`: Your unique identifier for order ID.
- `callback_url`: This URL redirects the customer to receive payment status notifications.
- Optionally, you can set `notification_url` to receive order payment updates notifications.

Payment status received can either be  **Completed** or **Cancelled**.

<br>

***

<br>

## Native application

This diagram shows a successful native application payment flow. Click to magnify.


<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/static/diagrams/svg/native-app-POS.svg" alt="native-app-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>

Before initiating payments, you must ensure manual input is disabled. To disable manual input - see [SmartPOS features](docs/smartpos-features).

To initiate payments - see <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">MultiSafepay Android POS integration </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<br>

# Handle notifications

The table below sets out ways you can choose to receive updates on order payments through our POS solutions.

| POS Solution        | Required                                                                                           | Optional                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| Cloud-based POS     | Subscribe to the [event notifications.](/docs/event-notifications#event-notifications)             | Configure [webhook notification](/docs/webhook#configure-your-webhook-endpoint.).                               |
| Web applications    | Set `callback_url` in the [ link.](/docs/solutions#web-applications-pos)                           | Set `notification_url` in the [ link](/docs/solutions#web-applications-pos), to configure webhook notification. |
| Native applications | Set `package_name` in your <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">intent call.</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | Configure [webhook notification.](/docs/webhook#configure-your-webhook-endpoint.).                              |

# User guide

## Cancellation

If payments haven't yet been completed, you can try to cancel an order. See  API reference - [Cancel an order](/reference/updateorder).

## Refunds

<details id="refunds">

<summary>How to process refunds</summary>
<br>

**Via the API** 

See API reference – [Refund order](/reference/refundorder).

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and click the relevant transaction.
3. On the **Transaction details** page, click **Refund order**.
4. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
5. In the **Comment** field, enter any additional information.
6. In the **Amount** fields, enter the amount to refund. 
7. Click **Continue**.
8. Review **Refund confirmation**, and then click **Confirm**.

</details>

## Updates

To get updates on a specific order, make a [Get order](/reference/getorder/) request, using the `order_id`.

## Testing

You can't test terminals in your MultiSafepay test account.
***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#