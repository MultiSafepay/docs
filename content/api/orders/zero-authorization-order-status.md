---
weight: 239
meta_title: "API reference - Get zero authorization order details - MultiSafepay Docs"

---
{{< code-block >}}
> GET - /orders/{order_id}

> JSON response

```json
{
  "success":true,
  "data":{
    "amount":0,
    "amount_refunded":0,
    "costs":[
      
    ],
    "created":"2019-10-17T10:44:59",
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
      "state":"NH",
      "zip_code":"1033SC"
    },
    "description":"MultiSafepay Test",
    "fastcheckout":"NO",
    "financial_status":"completed",
    "items":null,
    "modified":"2019-09-17T10:44:59",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":"MultiSafepay",
      "account_id":null,
      "card_expiry_date":4412,
      "external_transaction_id":234374824,
      "last4":1111,
      "recurring_id":"57876598769",
      "recurring_model":null,
      "type":"VISA"
    },
    "payment_methods":[
      {
        "account_holder_name":"MultiSafepay",
        "amount":9743,
        "card_expiry_date":2203,
        "currency":"EUR",
        "description":"MultiSafepay Test",
        "external_transaction_id":234374824,
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
    "var1":null,
    "var2":null,
    "var3":null
  }
}
```
{{< /code-block >}}
{{< description >}}
### Get zero authorization order details

**Parameter**

----------------
`order_id` | integer | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

**Response**

----------------
`amount` | integer

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

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

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

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
`var1` / `var2` / `var3` | string | optional

Variables for storing additional data.

----------------

{{% /description %}}