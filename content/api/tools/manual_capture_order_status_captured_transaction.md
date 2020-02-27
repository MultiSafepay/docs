---
weight: 1353
---
{{< code-block >}}

> GET - /orders/<capture_order_id>

> JSON Response

```shell
{
    "success": true,
    "data": {
        "transaction_id": 001,
        "order_id": "my-order-id-1",
        "created": "2019-03-22T12:03:56",
        "currency": "EUR",
        "amount": 1000,
        "description": "Manual Capture Test",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "completed",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2019-03-22T12:03:58",
        "customer": {
            "locale": "nl_NL",
            "first_name": "Testperson-nl",
            "last_name": "Approved",
            "address1": "Kraanspoor",
            "address2": null,
            "house_number": 39C,
            "zip_code": "1033SC",
            "city": "Amsterdam",
            "state": null,
            "country": "NL",
            "country_name": null,
            "phone1": "0208500500",
            "phone2": "",
            "email": "test@example.com"
        },
        "payment_details": {
            "recurring_id": null,
            "type": "VISA",
            "account_id": null,
            "account_holder_name": "MultiSafepay",
            "external_transaction_id": null,
            "last4": 1111,
            "card_expiry_date": 4412
        },
        "costs": [
            {
                "transaction_id": 001,
                "description": "",
                "type": "SYSTEM",
                "amount":
            }
        ],
        "related_transactions": null,
        "payment_methods": [
            {
                "account_holder_name": "MultiSafepay",
                "amount": 1000,
                "card_expiry_date": 4412,
                "currency": "EUR",
                "description": "Manual Capture Test",
                "last4": 1111,
                "payment_description": "Visa CreditCards",
                "status": "completed",
                "type": "VISA"
            }
        ]
    }
}
```
{{< /code-block >}}
{{< description >}}
### Order Status Captured Transaction
| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
|  order_id	| integer / string	|    The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string (max. 50 chars) |

Read more about [Manual Capture](/tools/manual-capture/) on our documentation page.
{{% /description %}}