---
weight: 204
meta_title: "API Reference - Get order details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#retrieve-an-order
---
{{< code-block >}}
> GET - /orders/{order_id}


> JSON response

```json
{
  "success": true,
  "data": {
    "transaction_id": 123456789,
    "order_id": "{order_id}",
    "created": "2019-03-01T16:12:47",
    "currency": "EUR",
    "amount": 200,
    "description": "Test order description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": null,
    "amount_refunded": 200,
    "status": "refunded",
    "financial_status": "completed",
    "reason": "Successful approval/completion",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-01T16:13:14",
    "customer": {
      "locale": "nl_NL",
      "first_name": "Simon",
      "last_name": "Smit",
      "address1": "Kraanspoor",
      "address2": "",
      "house_number": "39C",
      "zip_code": "1033SC",
      "city": "Amsterdam",
      "state": "NH",
      "country": "NL",
      "country_name": "The Netherlands",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "email": "simonsmit@example.com"
    },
    "payment_details": {
      "recurring_id": "133761993_gTp2",
      "type": "VISA",
      "account_id": null,
      "account_holder_name": "Testperson-nl approved",
      "external_transaction_id": 906015000050,
      "last4": "1234",
      "card_expiry_date": 1904
    },
    "costs": [
      {
        "transaction_id": 123456789,
        "amount": 0.19,
        "description": "Refund order 258655825 for TEST TEST",
        "type": "internal",
        "created": "2019-03-01T16:14:02",
        "status": "completed"  
      }
    ],
    "related_transactions": [
      {
        "amount": 200,
        "costs": [
          {
            "amount": 19,
            "description": "EURO 0.19 per refund",
            "type": "SYSTEM",
            "currency": "EUR",
            "status": "reserved"
          }
        ],
        "created": "2019-03-01T16:14:02",
        "currency": "EUR",
        "description": "Refund order 258655825 for TEST TEST",
        "modified": "2019-03-01T16:14:02",
        "status": "completed",
        "transaction_id": 123456789
      }
    ],
    "payment_methods": [
      {
        "account_holder_name": "Testperson-nl approved",
        "amount": 200,
        "card_expiry_date": 1904,
        "currency": "EUR",
        "description": "Test order description",
        "external_transaction_id": 906015000050,
        "last4": 1234,
        "payment_description": "Visa",
        "status": "completed",
        "type": "VISA"
      }
    ]
  }
}
```
{{< /code-block >}}

{{< description >}}
### Get order details

Retrieve the status of and information about a specific order. The structure may differ depending on the order type or method.

**Parameters**

----------------
`order_id` | integer / string | required

The unique identifier of the requested order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.                                      
Format: Maximum 50 characters.


**Response**

----------------
`transaction_id` | integer

The payment service provider identifier.

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string 

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | 

The amount (in cents) for the customer to pay. 

----------------
`description` | string | 

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`var1` / `var2` / `var3` | string | 

Variables for storing additional data. 

----------------
`items` | object 

See [items (object)](/api/#items-object/).

----------------
`status` | string

The [order status](/api/multisafepay-statuses/) of the order. 

----------------
`financial_status` | string

The [transaction status](/api/multisafepay-statuses/) of the order. 

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment_details-object).

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment_methods-object).

----------------

{{% /description %}}
