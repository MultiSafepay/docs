---
weight: 231
meta_title: "API reference - Direct: Flexible 3D enabled - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders 

```json 
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":10,
  "gateway":"CREDITCARD",
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
    "flexible_3d":true,
    "card_number":"",
    "card_holder_name":"",
    "card_expiry_date":"",
    "card_cvc":""
  }
}
```


> JSON response


```json
{
  "success":true,
  "data":{
    "amount":10,
    "amount_refunded":0,
    "costs":[
      
    ],
    "created":"2020-02-24T15:11:23",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":"Kraanspoor",
      "city":"Amsterdam",
      "country":"NL",
      "country_name":"The Netherlands",
      "email":"simonsmit@example.com",
      "first_name":"Simon",
      "house_number":"39C",
      "last_name":"Smit",
      "locale":"nl_NL",
      "phone1":"0208500500",
      "zip_code":"1033SC"
    },
    "description":"Test Product Description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2020-02-24T15:11:23",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":"",
      "account_id":null,
      "card_expiry_date":,
      "external_transaction_id":null,
      "last4":,
      "recurring_id":null,
      "recurring_model":null,
      "type":"MASTERCARD"
    },
    "payment_methods":[
      {
        "account_holder_name":"",
        "amount":10,
        "card_expiry_date":,
        "currency":"EUR",
        "description":"Test Product Description",
        "payment_description":"MasterCard",
        "status":"initialized",
        "type":"MASTERCARD"
      }
    ],
    "reason":"3DS Enrolled",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":123456789,
    "var1":null,
    "var2":null,
    "var3":null,
    "customer_verification":{
      "html":"<html>\n <head>\n <title>PaReq Form Submission</title>\n <script type=\"text/javascript\">\n function onLoadHandler(){ document.getElementById('PaReqForm').submit(); }\n </script>\n </head>\n <body onLoad=\"onLoadHandler();\">\n <form id=\"PaReqForm\" action=\"https://www.securesuite.co.uk/ing_retail/tdsecure/opt_in_dispatcher.jsp?VAA=B\" method=\"post\">\n <noscript>\n <center><br/>\n <h1>Processing your Transaction</h1>\n <h2>JavaScript is currently disabled or not supported by your browser.</h2><br/>\n <h3>Please click Proceed to continue the processing of your transaction.</h3>\n <input type=\"submit\" value=\"Proceed\"/>\n </center>\n </noscript>\n <input type=\"hidden\" name=\"PaReq\" value=\"eJxVkslu2zAQhl/FyL3iKss0JgTSOkhzUBEkvrg3mhrbCqwlFNXaefoOvdQtIAjzDZf5/xnCchcQ\r\nF2/ox4AWShwGt8VJXd3feZ1XxUZzqaZGy02+LtTaOOlm1bQQSvE7Cy8Pr/hh4ReGoe5aKzKeSWBX\r\npNuC37k2WnD+4+vzDyunRmracUFoMDwvrOA8fcDOCK1r0C4f35aT9AN2YvDd2MZwtLmcAbsCjGFv\r\ndzH2c8aacR/rwW2wd8cvFTZd5ruG9ftxW7fb0I09izhEillDFtvYMZEVZ8XpFmA3uS9jigaqeqgr\r\nu3r3n6v3/a5sHvXPxUqVy/KzfMrF+un3PbC0AyoX0UouOZdST4SeCzGXCtgpD65JcsknOT+H0KcK\r\nD7f8vww0i4CtP1pTJK9XAjz0XUvKLUn+G0OFg7d96KrRx0mCUPeR+k/V0wqwm5tv39MofKQua14I\r\nYZSQxmjNc5OGclpIVWpqrVSckhcAlo6yy7ypU6dnQtF/z+cPnVPCWQ==\"/>\n <input type=\"hidden\" name=\"TermUrl\" value=\"https://pay.multisafepay.com/direct/complete/?mspid=335263060\"/>\n <input type=\"hidden\" name=\"MD\" value=\"b73b9a2a8d671330null,c45d7f40236942f5b73b9a2a8d671330\"/>\n </form>\n </body>\n</html>\n",
      "type":"form"
    },
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL",
    "cancel_url":"https://www.example.com/client/notification?type=cancel&transactionid=apitool_"
  }
}
```
{{< /code-block >}}

{{< description >}}

### Direct: Flexible 3D enabled

Use [Flexible 3D](/payments/features/flexible-3ds/) to set whether or not to complete the transaction with [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/) verification.

To enable 3D Secure, in the `POST /orders` request > `gateway_info` object, set the `flexible_3d` parameter to `true`.

**Notes:**  

- Activating Flexible 3D Secure overrides Dynamic 3D settings, so that payments are not enrolled with a 3D authentication.

- We no longer support [Flexible 3D](https://docs.multisafepay.com/tools/flexible_3d) for merchants based in Europe due to PSD2 regulations.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10 

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Option: `CREDITCARD`.

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).  

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`gateway_info` | object | required

Contains:  

`flexible_3d` | boolean | required

- `true`: Enables 3D Secure verification. The payment is classified as **3D Secure Result: Enrolled Liability**.
- `false`: Disables 3D Secure verification. The payment is classified as **"Not Enrolled, Liability".**

**Response**

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

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
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`reason` | string 

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
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{< /description >}}
