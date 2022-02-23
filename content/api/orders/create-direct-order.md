---
weight: 203
meta_title: "API reference - Create a direct order - MultiSafepay Docs"

url: '/api/create-direct-order/'
---

{{< code-block >}}
> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "gateway":"IDEAL",
  "description":"Test order description",
  "gateway_info":{
    "issuer_id":"0021"
  },
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
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

### Create a direct order

For additional **required** information, see the relevant [payment method](/api/#payment-method-examples).

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

For a full list of gateway IDs, see [Payment method gateway IDs](/developer/gateway-ids/).
 
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`gateway_info` | object

Contains:  

`issuer_id` | string | required

The unique identifier of the gateway issuer.  
See [Retrieve gateway issuers](/api/#gateway-issuers).

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`shopping_cart.items` | optional

See [shopping_cart.items object](/api/#shopping-cart-items-object).

**Response**

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.  
Format: Maximum 500 characters.

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
