---
title : "Notification URL"
meta_title: "Notification URL - MultiSafepay Docs"
weight: 3
read_more: "."
aliases:
    - /faq/api/how-does-the-notification-url-work
    - /faq/api/notification-url
---

Notifications are webhooks where the API notifies your web server when the status of a transaction changes. They are triggered by actions by:

- Customers, e.g. completing a payment
- Merchants, e.g. processing a refund

## GET vs POST notification
The advantage of using the `POST` notification is it saves your web server trips. It doesn't have to request the [transaction status](/payments/multisafepay-statuses/) from our API again, and receive the updated transaction status directly in the notification payload.

## GET notification example
We recieve the following request from your web server:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
}
```

When the status of this transaction changes, we notify your web server at the following URL through a `GET` request: https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

**Note:** In the notification url, the `transaction_id` value should be the same as the `order_id`.

In your [backend](/getting-started/glossary/#backend), follow these steps: 

1. Send a [get order details request](/api/#get-order-details) using the `transaction_id` provided.
2. Check the `status` field in the response and update the status of the order in your backend.
3. Return an OK message. We expect an empty page with with an HTTP 200 OK in the header and the word `OK` in the response body.
