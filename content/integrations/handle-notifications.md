---
title: 'Handle notifications'
category: 62962dd7e272a6002ebbbbc5
order: 403
hidden: false
parentDoc: 62a1d799ab0558004cabb528
slug: 'handle-notifications'
next:
  description: Test your integration
  pages:
    - type: doc
      icon: file-text-o
      name: Test your integration
      slug: testing
      category: payment methods
---

When there is an update to your order, we notify your web server at the following URL through a `POST` request:  
`{your-webhook-endpoint}?transactionid=12345&timestamp=140292929`

This URL is your webhook endpoint combined with two additional parameters:

- `transactionid`: Your unique identifier for the order, previously set as `order_id` in your API request.
- `timestamp`: The time the notification was triggered.

The updated order details make up the payload of the request. 

# Check the status

Check the order status in the `status` field. If necessary, update your backend.

**Note:** You can ignore notifications that:

- Don't have the `timestamp` parameter in the URL  
- Have the same [order status](/payments-statuses/) 

# Validate the request

Every `POST` notification request includes an HMAC signature that you must use to validate its authenticity. To validate the request, you can either:

<details id="use-our-php-sdk">
<summary>Use our PHP SDK</summary>
<br>

Use the notification function from our PHP SDK. [View on GitHub](https://github.com/MultiSafepay/php-sdk/blob/master/src/Util/Notification.php).

</details>

<details id="validate-with-your-own-solution">
<summary>Validate with your own solution</summary>
<br>

Create your own solution to validate HMAC signatures.

To validate the HMAC signature of `POST` notification requests in your own solution, follow these steps:

1. Base64 decode the `Auth` header value of the request.
  <details>
    <summary>Example</summary>
    <br>

    Before: `MTY0MTIxODg4NDowNmNiZjIyNmU3Yzg3M2VmZjk2OTIxZDdmZGUzOTk4ZWI2YmUwZGU3OTE1ZWUxYzFiNTE0OTUxMWZjYTgyZTI2YmIwYWIyZTZkMGUwYWQ5OTdjYmFiMTUxZTRiYTU2MTU0MThkOGUxMjUyODMwMTcyNjE0M2VkMTE0NjI4N2Y5Mw==`

    After:
    `1641218884:06cbf226e7c873eff96921d7fde3998eb6be0de7915ee1c1b5149511fca82e26bb0ab2e6d0e0ad997cbab151e4ba5615418d8e12528301726143ed1146287f93`
  </details>

2. Split the decoded `Auth` header value using the colon (`:`) as separator.
    - The first string is the timestamp.
    - The second string is the HMAC signature. 

    <details>
    <summary>Example</summary>
    <br>

    Timestamp: `1641218884`  
    HMAC signature: `06cbf226e7c873eff96921d7fde3998eb6be0de7915ee1c1b5149511fca82e26bb0ab2e6d0e0ad997cbab151e4ba5615418d8e12528301726143ed1146287f93`
  </details>

3. Concatenate the:

    - Timestamp
    - Colon (`:`)
    - Payload of the request

    <details>
    <summary>Example</summary>
    <br>

    ``` javascript
    1641218884:{"amount":1000,"amount_refunded":0,"costs":[{"amount":0.49,"description":"0.49 For iDEAL Transactions","transaction_id":"123456789","type":"SYSTEM"}],"created":"2022-01-03T15:08:02","currency":"EUR","custom_info":{"custom_1":null,"custom_2":null,"custom_3":null},"customer":{"address1":null,"address2":null,"city":null,"country":null,"country_name":null,"email":"","first_name":null,"house_number":null,"last_name":null,"locale":"en_US","phone1":null,"phone2":"","state":null,"zip_code":null},"description":"product description","fastcheckout":"NO","financial_status":"initialized","items":null,"modified":"2022-01-03T15:08:02","order_id":"my-order-id", "payment_details":{"account_holder_name":null,"account_iban":"https://example.com","account_id":null,"external_transaction_id":"123456789","issuer_id":"3151","recurring_flow":null,"recurring_id":null,"recurring_model":null,"type":"IDEAL"},"payment_methods":[{"amount":1000,"currency":"EUR","description":"product description","external_transaction_id":"123456789","payment_description":"iDEAL","status":"initialized","type":"IDEAL"}],"reason":"","reason_code":"","related_transactions":null,"status":"initialized","transaction_id":"123456789","var1":null,"var2":null,"var3":null}
    ```
  </details>

4. SHA512 hash the concatenated string that resulted from step 3, using your API key as the HMAC key.

    If the request is valid, the hashed value from step 4 matches the HMAC signature from step 2.

    <details>
    <summary>Example</summary>
    <br>

    HMAC key: `8HHhGgRWrA3O7NswjmgwyH7buPPCGnR5AkwAQyqI`

    SHA512 hash: `06cbf226e7c873eff96921d7fde3998eb6be0de7915ee1c1b5149511fca82e26bb0ab2e6d0e0ad997cbab151e4ba5615418d8e12528301726143ed1146287f93`
    </details>

    Additionally, check whether the timestamp is recent and the originating IP address is MultiSafepay's. For a list of MultiSafepay's IP addresses, email <integration@multisafepay.com>

**Sample code**

We provide a code sample in Python for your reference.

  <details>
  <summary>Sample notification validation in Python</summary>
  <br>

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
  </details>
</details>

# Acknowledge the notification

Acknowledge that you have successfully received a valid notification by returning:

- HTTP status code `200` with `OK` at the start or end of the message body, **or**
- HTTP status code `200` with `MULTISAFEPAY_OK` anywhere in the message body.

Until we receive your acknowledgement, we resend the notification 4 times at 15 minute intervals, each with a new timestamp.

# Troubleshooting notifications

If for some reason you don't receive a notification:

1. In your MultiSafepay test account, go to **Transactions** > **Transaction overview** > **Transaction details**. Scroll to the bottom to find **Offline actions**.
2. Click <img src='https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/offline-actions-webhookendpoint.png'> and check that the URL displayed is the correct webhook endpoint.
3. If the webhook endpoint is correct, click <img src='https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/offline-actions-resend.png'> to resend the notification.

If you **still** don't receive a notification, you may need to authorize MultiSafepay servers' IP addresses on your web server. For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

You have successfully configured your web server to handle notifications received from our webhook.

___

:tada: Congratulations! You've successfully created an order, configured your webhook endpoint, and set up your web server to handle notifications.