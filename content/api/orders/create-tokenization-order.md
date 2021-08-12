---
weight: 235
meta_title: "API Reference - Create tokenization order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#create-token-transaction
---

{{< code-block >}}

> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "recurring_id":"azbkvsE0up4",
  "recurring_model":"unscheduled",
  "amount":1000,
  "description":"Create tokenization order",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "reference":"AutoQAReference"
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
      {
        "transaction_id":123456789,
        "amount":0.6,
        "description":"Create tokenization order",
        "type":"SYSTEM"
      }
    ],
    "created":"2019-10-24T13:22:45",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":"Kraanspoor",
      "address2":"",
      "city":"Amsterdam",
      "country":"NL",
      "country_name":"The Netherlands",
      "email":"simonsmit@example.com",
      "first_name":"Simon",
      "house_number":"39C",
      "last_name":"Smit",
      "locale":"nl_NL",
      "phone1":"0208500500",
      "phone2":"00310000001",
      "reference":"AutoQAReference",
      "state":"NH",
      "zip_code":"1033SC"
    },
    "description":"Tokenization - ALL - Trx with previous token with unscheduled model when is disabled",
    "fastcheckout":"NO",
    "financial_status":"completed",
    "items":null,
    "modified":"2019-10-24T13:22:45",
    "order_id":"my-order-id",
    "payment_details":{
      "account_holder_name":"Testperson-nl",
      "account_id":null,
      "card_expiry_date":1112,
      "external_transaction_id":929711011483,
      "last4":1111,
      "recurring_id":"azbkvsE0up4",
      "recurring_model":"unscheduled",
      "type":"VISA"
    },
    "payment_methods":[
      {
        "account_holder_name":"Testperson-nl",
        "amount":1000,
        "card_expiry_date":1112,
        "currency":"EUR",
        "description":"Tokenization - ALL - Trx with previous token with unscheduled model when is disabled",
        "external_transaction_id":929711011483,
        "last4":0,
        "payment_description":"Visa CreditCards",
        "status":"completed",
        "type":"VISA"
      }
    ],
    "reason":"Successful approval/completion",
    "reason_code":"",
    "related_transactions":null,
    "status":"completed",
    "transaction_id":123456789,
    "payment_url":" https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL ",
    "cancel_url":" http://www.example.com/client/notification?type=cancel "
  }
}
```

{{< /code-block >}}

{{< description >}}
### Create tokenization order

Create a [tokenization](/payments/features/tokenization) order.

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
`recurring_id` | string | required

The unique identifier for the recurring payment.

----------------
`recurring_model` | string | required

The recurring model.  
Options: `cardonfile`, `subscription`, `unscheduled`.  
See also [Recurring models](/payments/features/tokenization/#recurring-models).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.     

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
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

See [custom_info (object)](/api/#custom_info).

----------------
`fastcheckout` | string 

Whether this is a [FastCheckout](/payments/methods/fastcheckout/) transaction.  
Options: `YES`, `NO`.

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`items` | object 

See [items (object)](/api/#items-object/).

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment_details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment_methods-object).

----------------
`reason` | string

The capture reason for the order.

----------------
`related_transactions` | object

Information about linked transactions.

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/) of the order.

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------


{{< /description >}}