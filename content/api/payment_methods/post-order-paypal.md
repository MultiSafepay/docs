---
weight: 329
meta_title: "API reference - Create a PayPal order - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders 

```json

{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"PAYPAL",
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
    "locale":"nl_NL"
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```

> POST - /orders
```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"PAYPAL",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "manual":false,
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
    "state":"NH",
    "country":"NL",
    "phone":"0208500500",
    "email":"simonsmit@example.com",
    "referrer":"https://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  }
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "amount":1000,
    "amount_refunded":0,
    "costs":[
      
    ],
    "created":"2020-01-30T11:16:11",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":"Kraanspoor",
      "city":"Amsterdam",
      "state":"NH",
      "country":"NL",
      "email":"simonsmit@example.com",
      "first_name":"Simon",
      "house_number":"39C",
      "last_name":"Smit",
      "locale":"nl_NL",
      "phone1":"0208500500",
      "zip_code":"1033SC"
    },
    "description":"Test order description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2020-01-30T11:16:11",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":"Test-person-nl",
      "account_id":"https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
      "external_transaction_id":"8K013819T00365502LLL",
      "paypal_eligibility":"",
      "recurring_id":null,
      "recurring_model":null,
      "type":"PAYPAL"
    },
    "payment_methods":[
      {
        "account_holder_name":"Test-person-nl",
        "account_id":"https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
        "amount":1000,
        "currency":"EUR",
        "description":"Test order description",
        "external_transaction_id":"EC-8K013819T00365502L",
        "payment_description":"PayPal",
        "status":"initialized",
        "type":"PAYPAL"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":123456789,
    "payment_url":"https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp"
  }
}
```

{{< /code-block >}}

{{< description >}}
## PayPal
See also Payment methods – [PayPal](/payment-methods/paypal).

### PayPal - redirect

Once the customer has completed payment, the `status` changes to **Completed**. The `financial_status` remains **Initialized**, and during this status you cannot ship the order. You must first set the order to **Completed** for both the `status` and `financial_status` and then ship the order.

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
`gateway` | string | required

The unique gateway identifier for the payment method.  
Value: `PAYPAL`.

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
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Note:** To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes) the transaction request must include the `state` parameter in the customer's address. 

**Response** 

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

### PayPal - direct 

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`. 

----------------
`order_id` | string | required

Your unique identifier for the order.   
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.   
Value: `PAYPAL`.

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
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Note:** To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes) the transaction request must include the `state` parameter in the customer's address.

**Response**

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
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

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
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

{{< /description >}}
