---
title: 'Event notifications'
parentDoc: 64674fbc74bc4007521ebbcb
category: 6477597e0e2961004638cd5d
order: 4
hidden: false
slug: 'event-notifications'
excerpt: 'Receive status updates for SmartPOS terminal transactions.'


---

MultiSafepay offers the possibility to subscribe to event notifications. This allows you to receive order payments updates using an event stream URL.

# How it works

Once subscribed to event notifications, you will receive order payment updates when: 

- A customer completes the payment.
- A payment is reversed.
- The payment has been cancelled or declined.

The terminal make a `GET` request using an event stream **URL**. Once the connection has been set, it remains open until the payment process is complete. Any events triggered on the terminal will be detected by our backend and an update will be sent. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d9319259aa70fc594e26a315cb6bfc46130fa4d47c96bd0b2759a23faf4b5734-Untitled_diagram___Mermaid_Chart-2025-07-08-092557.svg",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


# Prerequisites

- SmartPOS terminal must be [activated in your MultiSafepay account](/docs/getting-started-guide/).
- Payments must be initiated via [cloud <<glossary:POS>> payment](/docs/smartpos-solutions#cloud-pos-payment).

In other scenarios, you can make use of our <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">webhook </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>notifications.

**⚠️Note:** When making requests locally, you might encounter **CORS** (**Cross-Origin Resource Sharing**) errors. We recommend using a **backend proxy** to handle the API requests, bypassing browser CORS restrictions.

# User guide

Follow the steps below to learn how to subscribe to our event notifications.

## 1. Initiate a Cloud POS payment

1. [Create an order](/reference/createorder/), and set`terminal_id` in your request. See Recipe - <a href="https://docs.multisafepay.com/recipes/cloud-pos-payment" target="_blank">Cloud POS payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. In response, you receive an `events_token` and an `event_stream_url`.

#### Example request

```curl
curl --location --request POST \
'https://api.multisafepay.com/v1/json/orders?api_key={terminal_group_api_key}' \
--header 'Content-Type: application/json' \
--data '{
    "type": "redirect",
    "order_id": "example_order_id",
    "gateway": "",
    "currency": "EUR",
    "amount": 1,
    "description": "example description",
    "payment_options": {
        "notification_url": "https://example.webhook.com"
    },
    "gateway_info": {
        "terminal_id": "00000ABC"
    }
}'
```

#### Example response

```json
{
    "success": true,
    "data": {
        "order_id": "example_order_id",
        "session_id": "d5MrwfDyPY36t8XAb2aMh5s6nH1XHOwqrOA00Ei",
        "payment_url": "https://payv2.multisafepay.com/connect/d5MrwfDyPY36t8XAb2aMh5s6nH1XHOwqrOA00Ei/?					lang=nl_NL",
        "events_token": "WkYyQBSMvjg3nJ7dtneQT7jd-								BsyAwFlMHoqwL7FNbMuC0xkpkF.bVjgMzRRDezylsixMegHEnVFW:tnWrRblQeJNy8ZAv_x4QfOoRruySEQa2U3aZPmBcLWKVFYLDAHVKzP1YpaBykMA0u9xCD7ZRHBiznkb.FmpOsHtsOPU7o_A4.eFK2LvMhg9Pad6BbLC2x4SdczFT1RKLHcQwkVPfBPMEGcOfedQNr",
        "events_stream_url": "https://api.multisafepay.com/events/stream/"
    }
}
```

## 2. Subscribe to the event notifications

To subscribe to event notifications make a `GET` request, using the `events_token` and the `events_stream_url` from your response. See recipe - [Subscribe to Event notifications](/recipes/subscribe-to-event-notifications) 

#### Example request

```curl
curl --location --request GET \
'https://api.multisafepay.com/events/stream/' \
--header 'Authorization: WkYyQBSMvjg3nJ7dtneQT7jd-								BsyAwFlMHoqwL7FNbMuC0xkpkF.bVjgMzRRDezylsixMegHEnVFW:tnWrRblQeJNy8ZAv_x4QfOoRruySEQa2U3aZPmBcLWKVFYLDAHVKzP1YpaBykMA0u9xCD7ZRHBiznkb.FmpOsHtsOPU7o_A4.eFK2LvMhg9Pad6BbLC2x4SdczFT1RKLHcQwkVPfBPMEGcOfedQNr'
```

#### Example response

```json
event: session.order
data: {"financial_status":"initialized","order_id":"example_order_id","session_id":"d5MrwfDyPY36t8XAb2aMh5s6nH1XHOwqrOA00Ei","status":"initialized","transaction_id":"89000000"}
event: session.order
data: {"financial_status":"completed","order_id":"example_order_id","session_id":"d5MrwfDyPY36t8XAb2aMh5s6nH1XHOwqrOA00Ei","status":"completed","transaction_id":"890000000"}
```

**⚠️Note:** You cannot initiate another payment until the current payment is **Cancelled** or **Completed**.

## Payment statuses

The table below sets out possible payment statuses and what they commonly mean.

[block:parameters]
{
  "data": {
    "h-0": "Description",
    "h-1": "Payment status",
    "0-0": "The <<glossary:card scheme>> is processing your payment request.",
    "0-1": "Initialized",
    "1-0": "The payment has been cancelled on the terminal or via API, or has expired after 60 seconds of inactivity. For more information - see [Cancellation.](/docs/smartpos-solutions#cancellation)  <br>**Note:**  You can now initiate another cloud POS payment.",
    "1-1": "Cancelled",
    "2-0": "The customer has completed the payment.  <br>**Note:**  You can now initiate another cloud POS payment.",
    "2-1": "Completed",
    "3-0": "The <<glossary:card scheme>> has declined the payment. The customer will be redirected to the payment screen to retry the payment.  \n  \nIn certain cases, a payment may be **soft declined**, meaning the customer must authenticate to proceed with the transaction. For more information, see <a href=\"https://docs.multisafepay.com/docs/smartpos-solutions#soft-declines\" target=\"_blank\">Soft declines</a> <i class=\"fa fa-external-link\" style=\"font-size:12px;color:#8b929e\"></i> - SmartPOS solutions.",
    "3-1": "Declined"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


***

[Top of page](#)

***