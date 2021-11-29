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

MultiSafepay provides a [webhook](/developer/api/webhooks/) that sends notifications to your web server when the status of an order changes.

## Configuring the webhook

You can configure the webhook at website level or for specific orders.

### Requirements

To use this webhook, you need to set a webhook endpoint. The webhook endpoint must **not** include port numbers and must be:
- A URL that can be accessed [from the public web](/developer/errors-explained/multisafepay-ip-ranges/)
- A HTTPS endpoint - HTTP endpoints aren't accepted for security reasons.

### Website level

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Select the relevant website.
4. In the **Notification URL** field, set your webhook endpoint.

### Order level

1. [Create an order](/api/#orders) via our API.
2. In the request body, set:
	- `payment_options.notification_url` to your webhook endpoint
	- `payment_options.notification_method` to `POST`

**Example**:

```
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "direct",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 1000,
  "gateway": "PAYAFTER",
  "description": "product description",
  // This request is truncated
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}'
```

**Note:**
If you set the **Notification URL** in your [MultiSafepay account](https://merchant.multisafepay.com) then this overrides anything set in `payment_options.notification_url` as part of an API request.

## Handling notifications

### Step 1: Receive notification

When the status of an order changes, we notify your web server at the following URL through a `POST` request:  
`{your-webhook-endpoint}?transactionid=12345&timestamp=140292929`

This URL is your webhook endpoint combined with two additional parameters:

- `transactionid`: Your unique identifier for the order
- `timestamp`: The time the notification was triggered

We add the current order details to the request body. 

### Step 2: Check the order status

Check the order status in the `status` field, and update the status of the order in your backend.

**Note:** You can ignore notifications that:

- Don't have the `timestamp` parameter in the URL.  
- Have the same [order status](/payments/multisafepay-statuses/). 

### Step 3: Validate the request

Every `POST` notification request includes a signature that you must use to validate its authenticity. To validate the request:

1. Base64 decode the `Auth` header value of the request.
2. Split the decoded `Auth` header value using the colon (`:`) as separator.
    - The first string is the timestamp.
    - The second string is the hash-based signature. 
3. Concatenate the:
    - Timestamp
    - Colon (`:`)
    - Payload of the request
4. SHA512 hash the concatenated string that resulted from step 3, using your API key as HMAC key.

If the request is valid, the hashed value from step 4 matches the hash-based signature from step 2.

Additionally, check whether the timestamp is recent and the originating IP address is MultiSafepay's. For a list of MultiSafepay's IP addresses, contact <integration@multisafepay.com>

{{< details title="Sample notification validation in Python" >}}

``` python
#!/usr/bin/python

import argparse
import base64
import hashlib
import hmac
import sys

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--apikey", help="API key", required=True)
parser.add_argument("-p", "--payload", help="Payload", required=True)
parser.add_argument("-a", "--authheader", help="Auth header", required=True)
args = parser.parse_args()

# Step 1: Base64 decode the auth header
encoded_auth_bytes = args.authheader.encode("ascii")
decoded_auth_bytes = base64.b64decode(encoded_auth_bytes)
decoded_auth = decoded_auth_bytes.decode("ascii")

# Step 2: Split the decoded auth header
timestamp = decoded_auth.split(':')[0]
signature = decoded_auth.split(':')[1]

# Step 3: Concatenate the timestamp, colon, and payload
concatenated_string = timestamp + ":" + args.payload

# Step 4: SHA512 hash the concatenated string
hashed_value = hmac.new(args.apikey.encode(), concatenated_string.encode(), hashlib.sha512).hexdigest()

# Step 5: Compare the hashed value with the signature
if hashed_value == signature:
	print("The notification is authentic")
	sys.exit(0)
else:
	print("Error: The notification is not authentic")
	sys.exit(1)
```
{{< /details >}}

### Step 4: Acknowledge the notification

Acknowledge that you have successfully received a valid notification by returning:

- HTTP status code `200` 
- HTTP message body starting with `OK`, **or**
- HTTP message body containing `MULTISAFEPAY_OK`

Until we receive your acknowledgement, we resend the notification 4 times at 15 minute intervals, each with a new timestamp.

## Next steps

You've successfully configured your webhook endpoint and web server to handle notifications. For next steps, either review our API reference documentation or test your integration.

{{< two-buttons href-2="/api/" text-2="API reference" description-2="Our comprehensive API reference documentation." img-2="/svgs/API.svg" alt-2="Right arrow" >}}

{{< two-buttons
href-1="/getting-started/build-your-integration" header-1="Previous" text-1="Build your integration" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/getting-started/test-your-integration" header-2="Next" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
