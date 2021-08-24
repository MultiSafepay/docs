---
title : "Notification URL"
meta_title: "Notification URL - MultiSafepay Docs"
weight: 5
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/how-does-the-notification-url-work
    - /faq/api/notification-url
---

Notifications are webhooks where the API notifies your web server when the status of a transaction changes. They are triggered by actions by:

- Customers, e.g. completing a payment
- Merchants, e.g. processing a refund
  
We add 2 parameters to the notification request:

- `transaction_id`  
- `timestamp`

For `POST` requests, we add the order data to the request body.

You can ignore requests if:

- We request the `notification_url` without the `timestamp` parameter.  
- You receive the same [order status](/payments/multisafepay-statuses/). 

Our API provides a `GET` and `POST` notification.

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

## POST notification example
We recieve the following request from your web server:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
    "notification_method": "POST",
}
```

When the status of this transaction changes, we notify your web server at the following URL through a `POST` request: https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

In your backend, follow these steps: 

1. Validate the `POST` request.
2. Check the `status` field in the response and update the status of the order in your backend.
3. Return an OK message. We expect an empty page with with an HTTP 200 OK in the header and the word `OK` in the response body.

## Validating POST notifications
Before accepting the order data, you need to validate the `POST` notification request by comparing the provided and calculated signature/hash.

To calculate the signature/hash, follow these steps:

1. Base64 decode the Auth header.
2. Split the decoded Auth header using the colon (`:`) as separator. The first string is the timestamp, the second string is a SHA512 hash of the payload.
3. Concatenate the timestamp, colon, and (non-hashed) payload of the notification.
4. SHA512 hash the concatenated string that resulted from step 3 using your [website API key](/tools/multisafepay-account/get-your-api-key) as HMAC key.
5. Check whether the the SHA512 hash that resulted from step 4 matches the SHA512 hash from step 2.

Additionally, check whether the timestamp is recent and the originating IP address is MultiSafepay's.

## GET vs POST notification
The advantage of using the `POST` notification is it saves your web server trips. It doesn't have to request the [transaction status](/payments/multisafepay-statuses/) from our API again, and receive the updated transaction status directly in the notification payload.

For security reasons, you must always validate the payload to make the `POST` notification comes from MultiSafepay and hasn't been tampered with.

### Response
For the response, we expect an empty page with either:

- "OK" as the first two characters in the response body **or**
- "MULTISAFEPAY_OK" anywhere in the response body

If we don't receive "OK" or "MULTISAFEPAY_OK" in the response body, we resend the notification with a timestamp. Notifications are repeated twice within 15 minutes. 


### Note:

- Always use **https** in the `notification_url`.
- Specifying a `notification_url` in the `POST /orders` request overrides the Notification URL set in your [MultiSafepay account](https://merchant.multisafepay.com).
- Never include port numbers in your notification URL. For security reasons, we only process standard ports.
- Make sure you authorize our [IP ranges](/faq/general/ip-ranges) to access the notification URL.

