---
weight: 1354
---
{{% code %}}

> GET - /orders/<order_id>

> JSON Response

```shell
{
    "success": true,
    "data": {
        "transaction_id": 001,
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
            "first_name": "Testperson-nl",
            "last_name": "Approved",
            "address1": "Kraanspoor",
            "address2": null,
            "house_number": "39C",
            "zip_code": "1033 SC",
            "city": "Amsterdam",
            "state": null,
            "country": "NL",
            "country_name": null,
            "phone1": "0208500500",
            "phone2": "",
            "email": "test@example.com"
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
                "transaction_id": 001,
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
{{% /code %}}
{{% description %}}
### Order Status Authorized Transaction
| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
|  order_id	|  integer / string	|    The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string. Required. Max 50 char.| 

Please make sure you check out our dedicated documentation for [Manual Capture](/tools/manual-capture/)
{{% /description %}}