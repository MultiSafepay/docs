---
title: 'Event notifications'
category: 6477597e0e2961004638cd5d
order: 6
hidden: false
parentDoc: 64674fbc74bc4007521ebbcb
slug: 'event-notifications'
---

To receive payment order status updates, subscribe to event notifications.

## 1. Add the HTML elements

1. Add CSS to the `<head>` of your checkout page:  
   ```html
     <link href="static/tailwind.min.css" rel="stylesheet">
   ```

2. Add the event notifications script to `<head>` of your checkout page:  

```html
<script src="https://testapi.multisafepay.com/events/static/message-bus.min.js"></script>
```

1. Add the DOM element for the event notifications in the `<body>` of your checkout page:

```html
<div id="eventNotifications" class="p-10 grid grid-cols-2">
```

1. Add the form element  in the `<body>` of your checkout page:

```Text HTML
 <div class="space-y-2">
                <h1 class="text-lg font-bold mb-5">Event notifications</h1>

                <form>
                <div>
                    <div>endpoint</div>
                    <input v-model="endpoint" class="border-2 rounded p-1 w-80" />
                </div>

                <div>
                    <div>events token</div>
                    <input v-model="token" class="border-2 rounded p-1 w-96" required />
                </div>

                <div class="py-3">
                    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="subscribe($event)">Subscribe</button>
                </div>
                </form>
            </div>
```

## 2. Initiate payments

[Create an order](/reference/createorder/), include in your request `gateway_info`. See - [Recipe](/recipes/cloud-payment-notifications)

## 3. Subscribe to event notifications

1. In response to your request in the previous step, you receive `event_tokens` and `event_url`.
2. Pass the `event_url` and `event_demo` in your demo fields.
3. Select the **Subscribe** button.
4. Once you subscribe to the event, you will receive payment notifications.

The following table outlines the order payment statuses that are to be received.

| Description                  | Payment status |
| ---------------------------- | -------------- |
| Payment has been initialized | Initialized    |
| Payment has been canceled.   | Cancelled.     |
| Payment has been finalized.  | Completed      |
| Payment has been declined.   | Declined.      |

**Note:** **Declined** status doesn't mean a final status, the customer can still try to make the payment, or you can choose to cancel the payment.

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#