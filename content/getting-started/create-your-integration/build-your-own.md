---
title: 'Build your own'
breadcrumb_title: 'Build your own'
weight: 10
meta_title: "Getting Started - Build your own integration - MultiSafepay Docs"

read_more: "."
logo: '/svgs/Wrappers.svg'
layout: 'single'
weight: 30
short_description: "Build your own custom integration."
---

## Set up webhooks

- Always use **https** in the `notification_url`.

We recieve the following request from your web server:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
    "notification_method": "POST",
}
```

When the status of this transaction changes, we notify your web server at the following URL through a `POST` request: https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

## Handle event notifications

We add 2 parameters to the notification request:

- `transaction_id`  
- `timestamp`

For `POST` requests, we add the order data to the request body.

You can ignore requests if:

- We request the `notification_url` without the `timestamp` parameter.  
- You receive the same [order status](/payments/multisafepay-statuses/). 

## Validate event notifications

Before accepting the order data, you need to validate the `POST` notification request by comparing the provided and calculated signature/hash.

To calculate the signature/hash, follow these steps:

1. Base64 decode the Auth header.
2. Split the decoded Auth header using the colon (`:`) as separator. The first string is the timestamp, the second string is a SHA512 hash of the payload.
3. Concatenate the timestamp, colon, and (non-hashed) payload of the notification.
4. SHA512 hash the concatenated string that resulted from step 3 using your [website API key](/account/site-id-api-key-secure-code/) as HMAC key.
5. Check whether the the SHA512 hash that resulted from step 4 matches the SHA512 hash from step 2.

Additionally, check whether the timestamp is recent and the originating IP address is MultiSafepay's.

Check the `status` field in the response and update the status of the order in your backend.

## Send event notification responses

For the response, we expect an empty page with either:

- "OK" as the first two characters in the response body **or**
- "MULTISAFEPAY_OK" anywhere in the response body

If we don't receive "OK" or "MULTISAFEPAY_OK" in the response body, we resend the notification with a timestamp. Notifications are repeated twice within 15 minutes. 

---

### Note:

- Specifying a `notification_url` in the `POST /orders` request overrides the Notification URL set in your [MultiSafepay account](https://merchant.multisafepay.com).
- Never include port numbers in your notification URL. For security reasons, we only process standard ports.
- Make sure you authorize our [IP ranges](/developer/errors-explained/multisafepay-ip-ranges/) to access the notification URL.



{{< two-buttons href-2="/api/" text-2="API reference" description-2="Our comprehensive API reference documentation." img-2="/svgs/API.svg" alt-2="Right arrow" >}}

## Next steps

{{< two-buttons
href-1="/getting-started/build-your-integration" header-1="Previous" text-1="Build your integration" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/getting-started/test-your-integration" header-2="Next" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
