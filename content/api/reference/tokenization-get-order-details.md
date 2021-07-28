---
weight: 605
meta_title: "API Reference - Tokenization - Get order details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> GET - /orders/{order_id}

> JSON Response
```json
{
    "success": true,
    "data": {
        "amount": 10000,
        "amount_refunded": 0,
        "costs": [
            {
                "amount": ,
                "description": "Tokenization Test Order",
                "transaction_id": 123456789
                "type": "SYSTEM"
            }
        ],
        "created": "2019-10-24T13:19:08",
        "currency": "EUR",
        "custom_info": {
            "custom_1": null,
            "custom_2": null,
            "custom_3": null
        },
        "customer": {
            "address1": "Kraanspoor",
            "address2": "",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": "The Netherlands",
            "email": "simonsmit@example.com",
            "first_name": "Simon",
            "house_number": "39C",
            "last_name": "Smit",
            "locale": "nl_NL",
            "phone1": "0208500500",
            "reference": "AutoQAReference",
            "zip_code": "1033SC"
        },
        "description": "Tokenization Test Order",
        "fastcheckout": "NO",
        "financial_status": "completed",
        "items": null,
        "modified": "2019-10-24T13:19:08",
        "order_id": "AutoQA-1571915948-481",
        "payment_details": {
            "account_holder_name": "Testperson-nl",
            "account_id": null,
            "card_expiry_date": 1612,
            "external_transaction_id": null,
            "last4": 1111,
            "recurring_id": " azbkvsE0up4",
            "recurring_model": "unscheduled",
            "type": "VISA"
        },
        "payment_methods": [
            {
                "account_holder_name": "Testperson-nl",
                "amount": 10000,
                "card_expiry_date": 4412,
                "currency": "EUR",
                "description": "Tokenization – Test Order",
                "external_transaction_id": 234374824,
                "payment_description": "Visa CreditCards",
                "status": "completed",
                "type": "VISA"
            }
        ],
        "reason": "Successful approval/completion",
        "reason_code": "",
        "related_transactions": null,
        "status": "completed",
        "transaction_id": 123456789
    }
}
```

{{< /code-block >}}

{{< description >}}

###  Get order details 

This API call allows you to retreive the order details while listing the recurring id and recurring model.

* All of the following parameters are required fields.

**Parameter**

__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.     

----------------

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/payments/features/tokenization)

{{< /description >}}
