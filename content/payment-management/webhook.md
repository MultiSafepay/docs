---
title: 'Webhook'
category: 6278c92bf4ad4a00361431b0
order: 9
hidden: false
excerpt: 'Configure a webhook to receive notifications about orders.'
slug: 'webhook'
---

MultiSafepay uses a webhook to send updates about orders and other notifications to your web server.

You can configure the webhook at website level or at <<glossary:order>> level.

# How it works

The webhook is triggered when we have data to send you, or when the <<glossary:order status>> or <<glossary:transaction status>> changes, e.g. when:

- A customer completes payment
- A customer's payment is declined or fails
- A customer begins the payment process but does not finalize it
- An order has shipped
- A refund is processed

MultiSafepay uses HTTPS to send notifications securely to the webhook endpoint configured for your web server.

Our webhook uses the `POST` method to inform your web server when there is an update, and shares details on what has changed. This is more efficient than a poll-based `GET` method where your web server must continually check for updates. We do support `GET` as a `notification_method`, but we strongly recommend `POST`.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/webhook-flow.svg" alt="Webhook communication flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

**⚠️ Note:** International bank account numbers (IBANs) are sensitive data. For security reasons, we mask them by default in POST webhook notifications so that only the last 4 digits are visible, e.g. *** 1234. 
To unmask them, see [IBANs](/docs/ibans/).

# Prerequisites

You must set a webhook endpoint, which is a URL that:

- Doesn't include port numbers.
- Is publicly accessible, or has MultiSafepay on your allow list.
- Uses HTTPS - We don't accept HTTP for security reasons.
- Only contains a specific set of ASCII characters (alphanumeric, -, _, ., :, /).

For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

# Configure your webhook endpoint

You can configure the webhook endpoint at:

<details id="site-level">
<summary>Site level</summary>
<br>

For websites:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**, and then click the relevant website.
3. Under **Functionality** > **Webhook URL**, set your webhook endpoint.

**⚠️ Note:** These instructions apply to your `notification_url` for order updates. For [FastCheckout shipping options updates](/docs/fastcheckout-shipping-options), see Order level below.

For terminal groups:

You can add a **Webhook URL** for a **terminal group** from your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. For more information, see **Activation** - <a href="https://docs.multisafepay.com/docs/smartpos-activation#activation" target="_blank">SmartPOS activation</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> or <a href="https://docs.multisafepay.com/docs/traditional-ctap-terminal#activation" target="_blank">Traditional (CTAP) terminal</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, depending on your terminal.

</details>

<details id="order-level">
<summary>Order level</summary>
<br>

1. [Create an order](/reference/createorder/) via our API.
2. In the request body, set:
	- For order updates: 
    - `payment_options.notification_url` to your webhook endpoint 
	  - `payment_options.notification_method` to `POST`
  - For [FastCheckout shipping options](/docs/fastcheckout-shipping-options) updates:
    - `payment_options.feed_url` to your other notifications endpoint (defaults to `POST`)

---

</details>

**⚠️ Note:** If you configure your webhook endpoint at site **and** order level, the order level endpoint is used by default.

### Example request

``` javascript
curl -X POST \
"https://api.multisafepay.com/v1/json/orders?api_key={your-api-key}"
-d '{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 1000,
  "description": "product description",
  "payment_options": {
      "notification_url": "https://www.example.com/paymentnotification",
      "notification_method": "POST"
  }
}'

```
<details id="example-get-response">
<summary><b>Example response</b></summary>

```json
{
  "success": true,
  "data": {"amount":1000,
  "amount_refunded":0,
  "costs":[
    {"amount":0.44,
  "description":"0.44 For iDEAL Transactions",
  "transaction_id":"8009375",
  "type":"SYSTEM"}
  ],
  "created":"2022-09-07T11:19:59",
  "currency":"EUR",
  "custom_info":
  {
  "custom_1":null,
  "custom_2":null,
  "custom_3":null
  },
  "customer": {
  "address1":"Neherkade",
  "address2":null,
  "city":"Gravenhage",
  "country":"NL",
  "country_name":"Netherlands",
  "email":"example@multisafepay.com",
  "first_name":"Testperson-nl",
  "house_number":"XI",
  "last_name":"Approved",
  "locale":"nl_NL",
  "phone1":"0612345678",
  "phone2":null,
  "state":null,
  "zip_code":"2521VA"
  },
  "description":"Product description",
  "fastcheckout":"NO",
  "financial_status":"initialized",
  "items":null,
  "modified":"2022-09-07T11:19:59",
  "order_id":"my-order-id-1",
  "payment_details":{
    "account_holder_name":null,
    "account_iban":"https://testpayv2.multisafepay.com/simulator/ideal?trxid=3924195754138182&ideal=prob&issuerid=0031&merchantReturnURL=https%3A%2F%2Ftestpayv2%2Emultisafepay%2Ecom%2Fconnect%2Fredirect%3Flang%3Dnl%5FNL%26mspid%3D8996625",
    "account_id":null,
    "card_authentication_result":null,
    "external_transaction_id":"3924195754138182",
    "issuer_id":"0031",
    "recurring_flow":null,
    "recurring_id":null,
    "recurring_model":null,
    "type":"IDEAL"
    },
    "payment_methods":[
      {"amount":1000,
      "currency":"EUR",
      "description":"Product description",
      "external_transaction_id":"3924195754138182",
      "payment_description":"iDEAL",
      "status":"initialized",
      "type":"IDEAL"}
      ],
      "reason":null,
      "reason_code":null,
      "related_transactions":null,
      "status":"initialized",
      "transaction_id":8996625,
      "var1":null,
      "var2":null,
      "var3":null
      }
}
```
</details>
<br>

✅ **Success!** You have configured your webhook endpoint Now you need to configure your web server to handle notifications correctly.

# Handle notifications

When there is an update to your order, we notify your web server at the following URL via a `POST` request:  
`{your-webhook-endpoint}?transactionid=12345&timestamp=140292929`

This URL is your webhook endpoint combined with two additional parameters:

- `transactionid`: Your unique identifier for the order, previously set as `order_id` in your API request.
- `timestamp`: The time the notification was triggered.
- `identifier=shipping`: For [FastCheckout shipping options updates](/docs/fastcheckout-shipping-options).

The updated order details make up the payload of the request. 

## 1. Check the status

Check the <<glossary:order status>> in the `status` field. If necessary, update your <<glossary:backend>>.

**⚠️ Note:** You can ignore notifications that:
- Don't have the `timestamp` parameter in the URL  
- Have the same <<glossary:order status>> 

**⚠️ Note:** When using **webhook notifications** on POS terminals, you might encounter **soft declines** when processing payments. For more information, see <a href="https://docs.multisafepay.com/docs/smartpos-solutions#soft-declines" target="_blank">Soft declines</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> - SmartPOS solutions.
=======
### Pre-transactions

If a customer initiates a payment process but does not finalize it, and no **PSP ID** (transaction reference number) is associated with the payment session, the corresponding order status will be updated to **Canceled** in your <<glossary:backend>>.

## 2. Validate the request

Every `POST` notification request includes an HMAC signature that you must use to validate its authenticity. To validate the request, you can either:

- Use the notification function from our PHP SDK. <a href="https://github.com/MultiSafepay/php-sdk/blob/master/src/Util/Notification.php" target="_blank">View on GitHub</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, **or**
- Create your own solution to validate HMAC signatures.

### Own solution

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

#### Example

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

## 3. Acknowledge the notification

Acknowledge that you have successfully received a valid notification by returning:

- HTTP status code `200` with `OK` within the first 100 characters of the message body, **or**
- HTTP status code `200` with `MULTISAFEPAY_OK` anywhere within the first 100 characters of the message body.

Until we receive your acknowledgment, we resend the notification 3 times at 15 minute intervals, each with a new timestamp.

## 4. Resend failed notifications

If a notification fails or we don't receive your acknowledgment, we resend the notification 3 times at 15 minute intervals, each with a new timestamp.

If for some reason you don't receive the notification, you can retry it manually in your dashboard.

<details id="how-to-retry-notifications-in-your-dashboard">
<summary>How to retry notifications in your dashboard</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Notification history**, click <img src='https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/offline-actions-webhookendpoint.png'> and check that the URL displayed is the correct webhook endpoint.
4. If the webhook endpoint is correct, to resend the notification, click the **Resend** icon.

</details>

If you **still** don't receive a notification, you may need to authorize MultiSafepay servers' IP addresses on your web server. 
For a list of MultiSafepay IP addresses, email <integration@multisafepay.com>

✅ **Success!** You have configured your webhook endpoint and set up your web server to handle notifications.

### Notifications overview

To see a filterable overview of all notifications you've received:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Notifications**.

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
