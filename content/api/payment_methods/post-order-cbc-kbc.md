---
weight: 309
meta_title: "API reference - Create a CBC order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"CBC",
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
    "locale":"nl_BE"
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
  "gateway":"CBC",
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
    "locale":"nl_BE",
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

> JSON Response
```json
{
  "success":true,
  "data":{
    "amount":1000,
    "amount_refunded":0,
    "costs":[
      {
        "amount":500,
        "description":"",
        "transaction_id":123456789,
        "type":"SYSTEM"
      },
      {
        "transaction_id":123456789,
        "amount":500,
        "description":"",
        "type":"SYSTEM"
      }
    ],
    "created":"2019-03-08T10:15:37",
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
      "phone1":"0208500500",
      "locale":"nl_BE",
      "zip_code":"1033SC"
    },
    "description":"Test order description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2019-03-08T10:15:37",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":null,
      "account_id":null,
      "external_transaction_id":325062361,
      "recurring_id":null,
      "recurring_model":null,
      "type":"CBC"
    },
    "payment_methods":[
      {
        "amount":1000,
        "currency":"EUR",
        "description":"Test order description",
        "external_transaction_id":325062361,
        "payment_description":"CBC",
        "status":"initialized",
        "type":"CBC"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":123456789,
    "payment_url":"https://www.cbc.be/olpayment?langWebSite=N&olpId=S132&olpCtx=%2FH8s4RM8GN%2FSKLOcUoTBBPus%2BWBbXCz9ChR12y5ozVDe8Rc70DjFQNQy2TaiSnTOEQkziFEQmgQy%2BHDxrqqzB%2F8I1yk5zE0%"
  }
}
```

{{< /code-block >}}

{{< description >}}
## CBC/KBC
See also Payment methods – [CBC/KBC](/payments/methods/banks/cbc-kbc/).

**Note:** Ensure you provide the relevant `gateway`.

### CBC/KBC - redirect

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
Options: `CBC`, `KBC`.

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
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------    
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------  

### CBC/KBC - direct

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
Value: `CBC`, `KBC`.

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

----------------    
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`amount_refunded` | integer

The amount refunded to the customer.

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

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

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
