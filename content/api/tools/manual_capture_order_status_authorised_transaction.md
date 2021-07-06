---
weight: 1354
---
{{< code-block >}}

> GET - /orders/{order_id}

> JSON Response

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
                "transaction_id": 123456789
                "description": "",
                "type": "SYSTEM",
                "amount": 2.83
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
### Order Status Authorized Transaction

**Parameter**

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string. Required. Max 50 char.

----------------

Read more about [Manual Capture](/tools/manual-capture) on our documentation page.
{{% /description %}}