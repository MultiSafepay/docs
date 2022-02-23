---
weight: 338
meta_title: "API reference - Create a WeChat Pay order - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"WECHAT",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
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
  "gateway":"WECHAT",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "manual":false,
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"cn_CN",
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
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": 0.3,
        "description": "Test order description",
        "transaction_id": 123456789,
        "type": "SYSTEM"
      }
    ],
    "created": "2021-09-16T14:39:50",
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
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "cn_CN",
      "phone1": "0208500500",
      "phone2": "",
      "state": null,
      "zip_code": "1033SC"
    },
    "description": "Test order description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2021-09-16T14:39:50",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": 123456789,
      "account_id": "wx<string>",
      "external_transaction_id": "wx<string>",
      "recurring_flow": null,
      "recurring_id": null,
      "recurring_model": null,
      "type": "WECHAT"
    },
    "payment_methods": [
      {
        "account_holder_name": 123456789,
        "account_id": "wx<string>",
        "amount": 1000,
        "currency": "EUR",
        "description": "Test order description",
        "external_transaction_id": "wx<string>",
        "payment_description": "WeChat Pay",
        "status": "initialized",
        "type": "WECHAT"
      }
    ],
    "qr_url": "weixin://wxpay/bizpayurl?pr=<string>",
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789,
    "var1": null,
    "var2": null,
    "var3": null,
    "payment_url": "http://www.example.com/client/notification?type=redirect&transactionid=my-order-id-1",
    "cancel_url": "http://www.example.com/client/notification?type=cancel"
  }
}

```

{{< /code-block >}}

{{< description >}}
## WeChat Pay
See also Payment methods – [WeChat Pay](/payment-methods/wechat-pay/).

Displaying the WeChat QR code:

- Redirect orders redirect the customer to a [MultiSafepay payment page](/payment-pages/) where the QR code is displayed under **Payment methods**.

- Direct orders retrieve the `qr_url` and render the QR code in your system to display it to the customer.

### WeChat Pay - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`, `paymentlink`.

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Fixed value: `WECHAT`. 

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

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

---------------- 

### WeChat Pay - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`, `paymentlink`.

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Fixed value: `WECHAT`. 

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

Fixed value: `false`.

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
`description` | string

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   

----------------
`fastcheckout` | string 

Fixed value: `NO`.

----------------
`financial_status` | string

The [transaction status](/about-payments/multisafepay-statuses/) of the order.

----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

----------------
`items` | object 

See [items (object)](/api/#items-object).


----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`qr_url` | string 

The URL of the QR code.

----------------
`reason` | string

----------------
`related_transactions` | string

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
