---
weight: 223
meta_title: "API reference - Fetch order status of captured transaction - MultiSafepay Docs"

---
{{< code-block >}}

> GET - /orders/<capture_order_id>

> JSON response

```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "order_id":"my-order-id-1",
    "created":"2019-03-22T12:03:56",
    "currency":"EUR",
    "amount":1000,
    "description":"Manual Capture Test",
    "var1":null,
    "var2":null,
    "var3":null,
    "items":null,
    "amount_refunded":0,
    "status":"completed",
    "financial_status":"completed",
    "reason":"",
    "reason_code":"",
    "fastcheckout":"NO",
    "modified":"2019-03-22T12:03:58",
    "customer":{
      "locale":"nl_NL",
      "first_name":"Simon",
      "last_name":"Smit",
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
      "type":"VISA",
      "account_id":null,
      "account_holder_name":"MultiSafepay",
      "external_transaction_id":null,
      "last4":1111,
      "card_expiry_date":4412
    },
    "costs":[
      {
        "transaction_id":123456789,
        "amount":0,
        "description":"",
        "type":"SYSTEM"
      }
    ],
    "related_transactions":null,
    "payment_methods":[
      {
        "account_holder_name":"MultiSafepay",
        "amount":1000,
        "card_expiry_date":4412,
        "currency":"EUR",
        "description":"Manual Capture Test",
        "last4":1111,
        "payment_description":"Visa CreditCards",
        "status":"completed",
        "type":"VISA"
      }
    ]
  }
}
```
{{< /code-block >}}
{{< description >}}
### Fetch order status of captured transaction

**Parameter**

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

**Response**

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string 

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer 

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string 

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.  
Format: Maximum 500 characters.

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
`reason` | string | required

The reason for capturing the order. 

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`related_transactions` | string

Information about linked transactions.

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------

{{% /description %}}