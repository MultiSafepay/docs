---
title: 'SmartPOS solutions'
parentDoc: 64674fbc74bc4007521ebbcb 
category: 6477597e0e2961004638cd5d
order: 2
hidden: false
slug: 'smartpos-solutions'
---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in the following countries:
> 
> - Netherlands
> - Belgium
> 
> Please note that in this stage, you cannot request terminals yet to use POS services.  
> If you are interested in participating in the next stage of our pilot, email <sales@multisafepay.com>
>

Our SmartPOS solutions let you initiate payments through:

- Manual input 
- Cloud POS payment
- On-same device third-party applications
  - Web application
  - Native application

# Manual input

To start processing payments manually:

1. Enter **Amount due** and select **Pay**.
2. The customer can either tap or insert their card to make the payment.
3. Once the payment is completed, a notification is displayed.

# Cloud POS payment

With cloud <<glossary:POS>> payment, you can initiate payments from an external application.

This diagram shows a successful cloud-based POS payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/cloud-POS-flow.svg" alt="cloud-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>

  📘 **Note:** Before you start initiating payments, you must ensure **cloud mode** is enabled - see [SmartPOS features](/docs/smartpos-features).

Create an order. See Recipe - <a href="https://docs.multisafepay.com/recipes/cloud-pos-payment" target="_blank">Cloud POS payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

To receive payments updates subscribe to [Event notifications.](/docs/event-notifications)

<br>

***

# On-same device third-party applications

## Web applications

Web applications let you initiate payments on-same devices from a browser to the payment app. 

This diagram shows a successful web application payment flow. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/web-flow.svg" alt="web-app-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>

### Initiate payments 

1. Before initiating web application payments, you need to create an order.

**Example**

```
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "redirect",
  "order_id": "my_order_id",
  "gateway": "",
  "currency": "EUR",
  "amount": 10,
  "description": "Order Description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}'
```

2. Initiate a payment using the URL below:

``` URL
msp://?amount={$amount}&order_id={$order_id}&callback={$callback_url}&notification_url={$notification_url}
```

- `amount`: the amount specified in EUR cents. 
- `order_id`: Your unique identifier for order ID.
- `callback_url`: This URL redirects the customer to receive payment status notifications.
- Optionally, you can set `notification_url` to receive order payment updates notifications.

Payment status received can either be  **Completed** or **Cancelled**.

<br>

***

## Native applications

Native applications let you initiate payments on-same devices from app to payment app.

This diagram shows a successful native application payment flow. Click to magnify.


<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/native-flow.svg" alt="native-app-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>

### Initiate payments 

1. Before initiating native application payments, you need to create an order.

**Example**

```
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "redirect",
  "order_id": "my_order_id",
  "gateway": "",
  "currency": "EUR",
  "amount": 10,
  "description": "Order Description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}'
```

2. To initiate payments - see <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">MultiSafepay Android POS integration </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<br>

# Handle notifications

The table below sets out options available for receiving updates on the payments.

| POS Solutions       | Required     | Optional            |
| :------------ |:---------------- | :--------------|
| Cloud POS payment   | Subscribe to the [event notifications.](/docs/event-notifications)             | Configure a [webhook](/docs/webhook#configure-your-webhook-endpoint.).                              |
| Web applications    | Set `callback_url` in the [ link.](/docs/solutions#web-applications-pos)                           | Set `notification_url` in the [ link](/docs/solutions#web-applications-pos) to configure a webhook. |
| Native applications | Set `package_name` in your <a href="https://github.com/MultiSafepay/pos-android-integration" target="_blank">intent call.</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | Configure a [webhook.](/docs/webhook#configure-your-webhook-endpoint.)                              |

# User guide

## Cancellation

To cancel an order, make a POST request using the `order_id`.

```
curl -X POST 'https://testapi.multisafepay.com/v1/json/orders/{order_id}/cancel?api_key={your-api-key}'
```

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

Make a [Get order](/reference/getorder) request to get updates on a specific order.

## Testing

You cannot test terminals in your MultiSafepay test account.

<br>

***

[Top of page](#)