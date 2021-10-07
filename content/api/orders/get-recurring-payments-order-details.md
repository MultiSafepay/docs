---
weight: 236
meta_title: "API reference - Get recurring payments order details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> GET - /orders/{order_id}

> JSON response
```json
{
  "success":true,
  "data":{
    "amount":10000,
    "amount_refunded":0,
    "costs":[
      {
        "transaction_id":123456789,
        "amount":0,
        "description":"Tokenization Test Order",
        "type":"SYSTEM"
      }
    ],
    "created":"2019-10-24T13:19:08",
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
      "reference":"AutoQAReference",
      "zip_code":"1033SC"
    },
    "description":"Tokenization Test Order",
    "fastcheckout":"NO",
    "financial_status":"completed",
    "items":null,
    "modified":"2019-10-24T13:19:08",
    "order_id":"AutoQA-1571915948-481",
    "payment_details":{
      "account_holder_name":"Testperson-nl",
      "account_id":null,
      "card_expiry_date":1612,
      "external_transaction_id":null,
      "last4":1111,
      "recurring_id":" azbkvsE0up4",
      "recurring_model":"unscheduled",
      "type":"VISA"
    },
    "payment_methods":[
      {
        "account_holder_name":"Testperson-nl",
        "amount":10000,
        "card_expiry_date":4412,
        "currency":"EUR",
        "description":"Test tokenization order",
        "external_transaction_id":234374824,
        "payment_description":"Visa CreditCards",
        "status":"completed",
        "type":"VISA"
      }
    ],
    "reason":"Successful approval/completion",
    "reason_code":"",
    "related_transactions":null,
    "status":"completed",
    "transaction_id":123456789
  }
}
```

{{< /code-block >}}

{{< description >}}

### Get recurring payment order details 

Retreive details about a [recurring payment](/features/recurring-payments) order.

**Parameter**

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.   

**Response**

----------------
`amount` | integer 

The amount (in cents) for the customer to pay.

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
`currency` | string 

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

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
`reason` | string | required


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

{{< /description >}}
