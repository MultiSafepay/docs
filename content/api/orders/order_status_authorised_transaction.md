---
weight: 222
meta_title: "API Reference - Set order status of authorized transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#order-status-authorized-transaction
---
{{< code-block >}}

> GET - /orders/{order_id}

> JSON response

```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
        "order_id": "my-order-id-1",
        "created": "2019-03-22T10:32:52",
        "currency": "EUR",
        "amount": 9743,
        "description": "",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2019-03-22T10:32:52",
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
            "recurring_id": 57876598769,
            "type": "VISA",
            "account_id": null,
            "account_holder_name": "MultiSafepay",
            "external_transaction_id": 234374824,
            "last4": 1111,
            "card_expiry_date": 4412,
            "capture": "manual",
            "capture_expiry": "2020-06-06T05:53:44",
            "capture_remain": 9743
        },
        "costs": [
            {
                "transaction_id": 123456789,
                "amount": 2.83,
                "description": "",
                "type": "SYSTEM",   
            }
        ],
        "related_transactions": null,
        "payment_methods": [
            {
                "account_holder_name": "MultiSafepay",
                "amount": 9743,
                "card_expiry_date": 4412,
                "currency": "EUR",
                "description": "MultiSafepay Test",
                "external_transaction_id": 234374824,
                "last4": 1111,
                "payment_description": "Visa CreditCards",
                "status": "initialized",
                "type": "VISA"
            }
        ]
    }
}
```
{{< /code-block >}}
{{< description >}}
### Set order status of authorized transaction

**Parameter**

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment_methods-object).

----------------

{{% /description %}}