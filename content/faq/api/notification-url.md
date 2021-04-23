---
title : "Notification URL"
meta_title: "FAQ API - Notification URL - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/api/how-does-the-notification-url-work
---
Notifications are webhooks where the API notifies your web server when the status of a transaction changes. They are triggered by actions by:

- Customers, e.g. completing a payment
- Merchants, e.g. initiating a refund
  
We add 2 parameters to the notification request:

- `transactionid`  
- `timestamp`

For `POST` requests, we add the order data to the request body.

You can ignore requests if:

- We request the `notification_url` without the `timestamp` parameter.  
- You receive the same `order status`. 

Our API provides a GET and POST notification.

## GET notification example
We recieve the following request from your web server:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
}
```

When the status of this transaction changes, we notify your web server at the following URL through a `GET` request: https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

**Note:** In the notification url, the `transaction_id` should have the same value as the `order_id`.

In your backend, follow these steps: 

1. Send a [status request](/api/#retrieve-an-order) on the order using the `transaction_id` provided.
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
2. Explode/split the resulting string using the colon as separator. The first part is the timestamp, the second part is sha512hex of the payload.
3. Concatenate the timestamp, colon, and original payload.
4. Calculate hmac/sha512 of step 4 using your [API key](/faq/general/glossary/#api-key) as the HMAC key.
5. Only allow the request if this hash matches the sha512hex from step 2 and the timestamp is recent enough.

## GET vs POST notification
The advantage of using the `POST` notification is it saves your web server trips. It doesn't have to request the transaction status from our API again, and receive the updated transaction status directly in the notification payload.

For security reasons, you must always validate the payload to make the `POST` notification comes from MultiSafepay and hasn't been tampered with.

### Response
For the response, we expect an empty page with either:

- "OK" as the first two characters in the response body **or**
- "MULTISAFEPAY_OK" anywhere in the reponse body

If we don't receive "OK" or "MULTISAFEPAY_OK" in the response body, we resend the notification with a timestamp. Notifications are repeated twice within 15 minutes. 


### Note:

- Always use **https** in the `notification_url`.
- Notification URLs in your [MultiSafepay Control](https://merchant.multisafepay.com) are _leading_, that is we use the notification URL under **Website settings** in your MultiSafepay Control first.
- If the notification URL field in your MultiSafepay Control is empty or not returning an OK response (for any reason), we use the notification URL from the transaction.
- Never include port numbers in your notification URL. For security reasons, we only process standard ports.
- Make sure you authorize our [IP ranges](/faq/general/ip-ranges) to access the notification URL.
