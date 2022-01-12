---
weight: 331
meta_title: "API reference - Create a Request to Pay transaction - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders 

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"DBRTP",
  "currency":"EUR",
  "amount":9743,
  "description":"Test order description",
  "manual":false,
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
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/12SV72okI6zR23ofq5gdEnaFYZ4qLZ3aFLj/?lang=nl_NL"
  }
}
```

> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"DBRTP",
  "currency":"EUR",
  "amount":9743,
  "description":"Test order description",
  "manual":false,
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
    "amount":9743,
    "amount_refunded":0,
    "costs":[
      {
        "transaction_id":123456789,
        "amount":50,
        "description":"",
        "type":"SYSTEM"
      }
    ],
    "created":"2020-03-25T12:07:00",
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
    "modified":"2020-03-25T12:07:00",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":null,
      "account_id":null,
      "external_transaction_id":"P-26660200325-0935",
      "recurring_id":null,
      "recurring_model":null,
      "type":"DBRTP"
    },
    "payment_methods":[
      {
        "amount":9743,
        "currency":"EUR",
        "description":"Test order description",
        "external_transaction_id":"P-26660200325-0935",
        "payment_description":"Request to Pay",
        "status":"initialized",
        "type":"DBRTP"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":123456789,
    "payment_url":"https://pushpayments.db.com/flow/eyJwYXlsb2FkIjp7ImlwaSI6IjE2QjIwREREMjE1NjE0QTc2Rjg0OTMwMDV="
  }
}
```

{{< /code-block >}}

{{< description >}}

## Request to Pay
See also Payment methods – [Request to Pay](/payment-methods/request-to-pay).

### Request to Pay - redirect

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
Value: `DBRTP`.

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

**Response** 

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

### Request to Pay - direct

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
Value: `DBRTP`.

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
`customer` | object 

See [customer (object)](/api/#customer-object).

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
`reason` | string


----------------
`related_transactions` | object

Information about linked transactions.

----------------
`status` | string

The [order status](/about-payments/multisafepay-statuses/).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

{{< /description >}}
