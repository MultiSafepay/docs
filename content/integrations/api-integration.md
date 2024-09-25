---
title: 'API integration'
category: 62962dd7e272a6002ebbbbc5
hidden: false
order: 1
excerpt: 'Build your own payments integration using our API, wrappers, or SDKs.'
slug: 'api-integration'
---

This tutorial explains how to build your own integration using our API, and how to create orders and track their progress via our webhook.

# Prerequisites

You must first:

1. [Create a test account](/docs/getting-started-guide#1-create-a-free-test-account).
2. [Set up your account](/docs/getting-started-guide#2-set-up-your-account).
3. [Get your site API key](/docs/sites#site-id-api-key-and-security-code).


To authenticate requests, you must include your API key as a query parameter in the request URL.  

&nbsp; **💡 Tip!** While building your integration we recommend using the [test environment](/reference/environments/): `https://testapi.multisafepay.com/v1/json`.

Before continuing with this tutorial, see if you can save development time with our range of [wrappers and SDKs](/docs/wrappers-sdks/).

# 1. Create an order

MultiSafepay provides a RESTful API you can access with HTTP requests to manage your data. We support data in JSON format only.

The most important data element in our API is the <<glossary:order>>, which can be linked to multiple <<glossary:transactions>>. 

**1.** Test the most common operation with our API which is to [create an order](/reference/createorder/). To specify which payment flow the customer experiences, set the order `type` to <<glossary:direct>> or <<glossary:redirect>>.

#### Example request
This is an example request for a <<glossary:redirect>> order.

``` javascript
curl -X POST "https://testapi.multisafepay.com/v1/json/orders?api_key={your-test-api-key}" \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
-d '{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "gateway": "",
  "currency": "EUR",
  "amount": 1000,
  "description": "Test order description",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "notification_method": "POST",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Test Company Name",
    "address1": "Kraanspoor",
    "house_number": "39C",
    "zip_code": "1033SC",
    "city": "Amsterdam",
    "country": "NL",
    "phone": "0208500500",
    "email": "jdoe@example.com",
    "referrer": "https://example.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  }
}'
```

**2.** Check that you receive a response with `success` set to `true`.

#### Example response
``` javascript
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://example.com/?lang=nl_NL"
  }
}
```

**3.** Open the `payment_url` to complete payment on the payment page. 

**⚠️ Note:** If you receive an error in the response, see [Troubleshooting](/docs/troubleshooting/).

✅ **Success!** You have successfully created an order. Now learn how to track orders via our webhook as they progress.

# 2. Set up webhook

The most important parameters in the <<glossary:order>> are `status`(the <<glossary:order status>>) and `financial_status` (the <<glossary:transaction status>>).

To understand how orders are progressing, we recommend tracking their `status`. So that you don't have to continually poll our server to check for updates to your orders, we provide a webhook to send you notifications automatically. 

To learn how to configure your webhook endpoint and handle notifications, see [Webhook](/docs/webhook/).

For information about all possible statuses, see [Payment statuses](/docs/payment-statuses/).

✅ **Success!** You have configured your webhook endpoint. Now you can test your selected payment methods.

# 3. Test payment methods

For how to test each payment method, see Testing payment methods - [Test payment details](/docs/testing#test-payment-details). 
If this is your first time, we recommend following the steps for [iDEAL](/docs/testing#ideal).

✅ **Success!** You can successfully create orders for your payment mix. 

# GET requests

To fetch information about a specific order, make a [Get order](/reference/getorder/) request, using the `order_id`.

<details id="example-get-request">
<summary>Example GET request</summary>
<br>

``` javascript
curl -X GET 'https://testapi.multisafepay.com/v1/json/orders/my-order-id-1?api_key={your-test-api-key}' \ 
-H 'accept: application/json'
```

</details>

<details id="example-get-response">
<summary>Example GET response</summary>
<br>

``` json
{
  "success": true,
  "data": {
    "amount": 100,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": 0.00,
        "description": "0.00 For iDEAL Transactions",
        "transaction_id": 1234567,
        "type": "SYSTEM"
      }
    ],
    "created": "2021-12-07T15:56:32",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "address2": null,
      "city": "Amsterdam",
      "country": "NL",
      "country_name": null,
      "email": "jdoe@example.com",
      "first_name": "John",
      "house_number": "39C",
      "last_name": "Doe",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "phone2": "",
      "state": null,
      "zip_code": "1033SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "completed",
    "items": null,
    "modified": "2021-12-07T15:56:40",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_bic": "INGBNL2A",
      "account_holder_name": "Jan Jansen",
      "account_iban": "NL87ABNA0000000001",
      "account_id": 1,
      "external_transaction_id": "3749936454986553",
      "issuer_id": "0031",
      "recurring_flow": null,
      "recurring_id": "998107705729622024",
      "recurring_model": null,
      "type": "IDEAL"
    },
    "payment_methods": [
      {
        "account_bic": "INGBNL2A",
        "account_holder_name": "Jan Jansen",
        "account_iban": "NL87ABNA0000000001",
        "account_id": 1,
        "amount": 100,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "3749936454986553",
        "payment_description": "iDEAL",
        "status": "completed",
        "type": "IDEAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "completed",
    "transaction_id": 2345678,
    "var1": null,
    "var2": null,
    "var3": null
  }
}
```
</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)