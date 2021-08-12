---
weight: 203
meta_title: "API Reference - Create a direct order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
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
  "description":"product description",
  "gateway_info":{
    "issuer_id":"0021"
  },
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
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
    "description":"product description",
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

Supported payment methods:   
ALIPAY, BANKTRANS, BELFIUS, CBC, CREDITCARD, DIRDEB, DIRECTBANK, EINVOICE, IDEAL, ING, KBC, KLARNA, PAYAFTER, PAYPAL

For additional **required** information, see the relevant [payment method](/api/#payment-methods).

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
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

----------------
`amount_refunded` | integer

The amount refunded to the customer. 

----------------
`status` | string 

The [order status](/payments/multisafepay-statuses/) of the order. 

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order. 

----------------
`reason` | string 

The capture reason for the order.

----------------
`fastcheckout` | string 

Whether this is a [FastCheckout](/payments/methods/fastcheckout/) transaction.  
Options: `YES`, `NO`.

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment_details-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
