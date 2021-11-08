---
weight: 333
meta_title: "API reference - Create a Sofort order - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"DIRECTBANK",
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
    "locale":"de_DE"
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=de_DE"
  }
}
```
> POST - /orders
```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"DIRECTBANK",
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
    "locale":"de_DE",
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
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "amount":9743,
    "amount_refunded":0,
    "costs":[
      {
        "transaction_id":123456789,
        "amount":743,
        "description":"",
        "type":"SYSTEM"
      },
      {
        "amount":900,
        "description":"",
        "transaction_id":123456789,
        "type":"SYSTEM"
      }
    ],
    "created":"2020-01-30T10:43:39",
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
      "locale":"de_DE",
      "phone1":"0208500500",
      "zip_code":"1033SC"
    },
    "description":"Test order description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2020-01-30T10:43:39",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":null,
      "account_id":10071970,
      "external_transaction_id":null,
      "recurring_id":null,
      "recurring_model":null,
      "type":"DIRECTBANK"
    },
    "payment_methods":[
      {
        "account_id":10071970,
        "amount":9743,
        "currency":"EUR",
        "description":"Test order description",
        "payment_description":"SOFORT Banking",
        "status":"initialized",
        "type":"DIRECTBANK"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":123456789,
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=de_DE",
    "cancel_url":"https://www.example.com/client/notification?type=cancel"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Sofort

See also Payment methods – [Sofort](/payment-methods/sofort).

### Sofort - redirect

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
Value: `DIRECTBANK`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  
For supported currencies, see [Sofort product rules](/payments/methods/banks/sofort-banking/about/).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | optional

See [customer (object)](/api/#customer-object).

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

The [transaction status](/payments/multisafepay-statuses/) of the order.

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
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

### Sofort - direct

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
Value: `DIRECTBANK`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  
For supported currencies, see [About SOFORT Banking](/payments/methods/banks/sofort-banking/about/).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | optional

See [customer (object)](/api/#customer-object).   

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

Whether this is a FastCheckout transaction.
Options: `YES`, `NO`.

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

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

The [order status](/payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{< /description >}}
