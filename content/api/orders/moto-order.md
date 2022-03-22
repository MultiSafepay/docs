---
weight: 224
meta_title: "API reference - MOTO orders - MultiSafepay Docs"
url: '/api/moto-orders/'
---

{{< code-block >}}
> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"apitool_13015375",
  "currency":"EUR",
  "amount":1000,
  "gateway":"CREDITCARD",
  "description":"product description",
  "payment_options":{
    "notification_url":"http://10.1.10.111/testtool/client/json-test/notification?type=notification",
    "redirect_url":"http://10.1.10.111/testtool/client/json-test/notification?type=redirect",
    "cancel_url":"http://10.1.10.111/testtool/client/json-test/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl",
    "ip_address":"62.195.130.40",
    "forwarded_ip":"",
    "first_name":"Testperson-nl",
    "last_name":"Approved",
    "address1":"Neherkade",
    "address2":"",
    "house_number":"XI",
    "zip_code":"2521VA",
    "city":"Gravenhage",
    "state":"",
    "country":"NL",
    "birthday":"10071970",
    "gender":"male",
    "phone":"0612345678",
    "email":"example@multisafepay.com",
    "referrer":"http://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "gateway_info":{
    "moto":true
  }
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "order_id":"my-order-id-1",
    "created":"2019-03-04T13:52:07",
    "currency":"EUR",
    "amount":1000,
    "description":"Test order description",
    "var1":null,
    "var2":null,
    "var3":null,
    "items":null,
    "amount_refunded":0,
    "status":"initialized",
    "financial_status":"initialized",
    "reason":"",
    "reason_code":"",
    "fastcheckout":"NO",
    "modified":"2019-03-04T13:52:07",
    "customer":{
      "locale":"en_US",
      "first_name":"Simon",
      "last_name":"Smit",
      "company_name":null,
      "address1":"Kraanspoor",
      "address2":"",
      "house_number":"39C",
      "zip_code":"1033SC",
      "city":"Amsterdam",
      "state":"NH",
      "country":"NL",
      "country_name":"The Netherlands",
      "phone1":"0208500500",
      "phone2":"00310000001",
      "email":"simonsmit@example.com"
    },
    "payment_details":{
      "recurring_id":null,
      "type":"IDEAL",
      "account_id":null,
      "account_holder_name":null,
      "external_transaction_id":"0050003729272772",
      "account_iban":"*** 1234",
      "isser_id":"0021"
    },
    "costs":[
      {
        "transaction_id":123456789,
        "amount":0,
        "description":"iDEAL Transactions",
        "type":"SYSTEM"
      }
    ],
    "payment_url":"https://betalen.rabobank.nl/ideal-betaling/landingpage?random=44b2dcf080f29f6f52d05802fd76e31285ac564dc974319f0109e1d978234770&trxid=0050003729272772"
  }
}
```

{{< /code-block >}}

{{< description >}}

## MOTO orders

Process a card payment with payment details provided by phone or email.  
See [MOTO](/features/moto/).

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency of the payment.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | required

The payment amount in the currency's smallest unit:  

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10 

----------------
`gateway` | string | required

The gateway identifier for the payment method.  
Options: `AMEX`, `CREDITCARD`, `MASTERCARD`, `VISA`.

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`gateway_info` | object

Contains:  

`moto` | boolean | required

To create a MOTO order, set to `true`.

----------------

**Response**

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`order_id` | string 

Your unique identifier for the order.  

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string 

The currency of the payment.  

----------------
`amount` | integer 

The payment amount.

----------------
`description` | string

The order description. 

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.  

----------------
`items` | object 

See [items (object)](/api/#items-object).

----------------
`amount_refunded` | integer

The amount refunded to the customer. 

----------------
`status` | string 

The [order status](/about-payments/multisafepay-statuses/). 

----------------
`financial_status` | string

The [transaction status](/about-payments/multisafepay-statuses/) of the order. 

----------------
`reason` | string 

The reason for any modifications to the order. 

----------------
`reason_code` | string 

The reason code for any modifications to the order. 

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

{{< /description >}}
