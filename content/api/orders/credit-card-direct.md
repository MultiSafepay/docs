---
weight: 314
meta_title: "API reference - Credit card – direct - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"direct",
  "gateway":"MASTERCARD",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "forwarded_ip":"",
    "first_name":"Simon",
    "last_name":"Smit",
    "address1":"Kraanspoor",
    "address2":"",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0208500500",
    "email":"simonsmit@example.com",
    "referrer":"https://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "gateway_info":{
    "card_number":"5555555555554444",
    "card_holder_name":"MasterCard-Test-Order",
    "card_expiry_date":"2512",
    "card_cvc":"123",
    "moto":false
  }
}
```

> JSON response     

```json
{
  "success":true,
  "data":{
    "amount":100,
    "amount_refunded":0,
    "costs":[
      
    ],
    "created":"2022-01-31T14:37:26",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":"Neherkade",
      "address2":null,
      "city":"Gravenhage",
      "country":"NL",
      "country_name":null,
      "email":"example@multisafepay.com",
      "first_name":"Testperson-nl",
      "house_number":"XI",
      "last_name":"Approved",
      "locale":"nl",
      "phone1":"0612345678",
      "phone2":"",
      "state":null,
      "zip_code":"2521VA"
    },
    "description":"Test order description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2022-01-31T14:37:26",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":"Test Holder Name",
      "account_id":null,
      "card_expiry_date":2512,
      "external_transaction_id":null,
      "last4":4444,
      "recurring_flow":null,
      "recurring_id":null,
      "recurring_model":null,
      "type":"MASTERCARD"
    },
    "payment_methods":[
      {
        "account_holder_name":"Test Holder Name",
        "amount":100,
        "card_expiry_date":2512,
        "currency":"EUR",
        "description":"product description",
        "payment_description":"MASTERCARD",
        "status":"initialized",
        "type":"MASTERCARD"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":5437731,
    "var1":null,
    "var2":null,
    "var3":null,
    "customer_verification":{
      "html":"<html>\n  <head>\n    <title>PaReq Form Submission</title>\n    <script type=\"text/javascript\">        function onLoadHandler() {\n            document.getElementById('PaReqForm').submit();\n        }\n    </script>\n  </head>\n  <body onLoad=\"onLoadHandler();\">\n    <form id=\"PaReqForm\" action=\"https://testpay.multisafepay.com/3ds2/sim/acs\" method=\"post\">\n      <noscript>\n        <center>\n          <br/>\n          <h1>Processing your Transaction</h1>\n          <h2>JavaScript is currently disabled or not supported by your browser.</h2><br/>\n          <h3>Please click Proceed to continue the processing of your transaction.</h3>\n          <input type=\"submit\" value=\"Proceed\"/>\n        </center>\n      </noscript>\n      <input type=\"hidden\" name=\"PaReq\" value=\"eJxUUttu4jAU/JWoH4BjJ0BAp5bYpcv2IZR2kbrty8rYp8TbxEmdG/Tra4fSi+SHGY91xjM2bDOLuPyDsrXIIcW6FnsMtLq8UDiLnsZJ+DSZhXEsdrNQsmS3U8lEJkrQ6ILDZnGHLxw6tLUuDaejcMSAnKmbZmUmTMNByJcf12tOWRSPJ0DeKRRor5echqFfQE4UjCiQp1pmGvOgEya4R/uclR0aIIMGsmxNY498ymIgZwKtzXnWNNWckL7vR702HWK+x1yNTE6AeB3I56U2rUe1m3fQij8Ut/G6SOPH1dUhfb06pq+3dP1fxjfbxSUQfwKUaJCzkLGQRjSg0TyazpmLM+yDKPxFfBoX8ISh8haLL8LXDXCdWzTyyGfTxOU4M8BDVRp0J1yZHxgU1pJXtlStbAJPrK4a17Pz9wqQzzw/f/vKZePaxMWvuGr/bbeivX82K0v1+m/a+ycYZO+lXXlsTE9mngDxA8j767rGhk/h0LfP8gYAAP//BcCBAAAAAACQ/2sAvRu/iw==\"/>\n      <input type=\"hidden\" name=\"TermUrl\" value=\"https://testpay.multisafepay.com/direct/complete/?mspid=5437731\"/>\n      <input type=\"hidden\" name=\"MD\" value=\"bd86c8da131234567890,de93f580f69044ab90c28bbd86c8da13\"/>\n    </form>\n  </body>\n</html>\n",
      "type":"form"
    },
    "payment_url":"https://testpay.multisafepay.com/customer-verification?sessionid=82CF5wMcW8JP93heDwzfrYbjJJCcJhQv3iN&type=3ds&md=bd86c8da131234567890%2Cde93f580f69044ab90c28bbd86c8da13&lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}

### Credit card – direct 

**Note:** To make credit card – direct requests, you need to handle cardholder data on your server, which requires PCI DSS certification. Instead, we recommend accepting credit card payments using a [payment page](/payment-pages/) or [payment component](/payment-components/). 

See [Handling cardholder data](/features/handling-cardholder-data/). 

**Parameters**

----------------
`type` | string | required

The payment flow.  
Options: `direct`.  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Options: `AMEX`, `CREDITCARD`, `MAESTRO`, `MASTERCARD`, `MISTERCASH` (Bancontact), `VISA`. 

----------------
`order_id` | string | required

Your unique identifier for the order.   
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency of the transaction.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The payment amount in the currency's smallest unit:  

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10 

----------------
`description` | string | required

The description of the customer's order. Also appears on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`gateway_info` | object

Contains:  

`card_number` | string | required

The customer's full credit card number.

`card_holder_name` | string | required

The name of the cardholder on the credit card.

`card_expiry_date` | string | required

The expiry date on the credit card.  
Format: YYMM

`card_cvc` | string | required for most cards, except Maestro and recurring payments.

The card verification code (CVC) is a 3 or 4 digit number used as an additional security feature for card-not-present transactions.  

`moto`  | boolean | optional

Processes a [MOTO](/features/moto/) transaction.


**Response**

----------------
`amount` | integer

The amount of the transaction. 

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created. 

----------------
`currency` | string

The currency of the transaction.

----------------
`custom_info`  | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`description` | string | required

The description of the customer's order.

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`financial_status` | string

The [transaction status](/about-payments/multisafepay-statuses/) of the order.

----------------
`items` | object 

See [items (object)](/api/#items-object).

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`order_id` | string 

Your unique identifier for the order. 

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`reason` | string 

----------------
`reason_code` | string 

----------------
`related_transactions` | object

Information about linked transactions.

----------------
`status` | string 

The [order status](/about-payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.

----------------
`customer_verification` | object

Contains: 

`html` | string

If [3D Secure](/glossaries/multisafepay-glossary/#3d-secure) authentication is:

- Required: An HTML form is returned. You can either render the form and redirect the customer to it to pass authentication, or redirect them to the payment_url (recommended).
- Not required: The [transaction status](/about-payments/multisafepay-statuses/) response is processed directly and no HTML form is returned.

`type` | string

Value: `form`.

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{% /description %}}

