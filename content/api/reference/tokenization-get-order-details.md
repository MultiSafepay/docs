---
weight: 605
meta_title: "API - Tokenization - Get order details - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> GET - /orders/{order_id}

> JSON Response
```shell
{
    "success": true,
    "data": {
        "amount": 10000,
        "amount_refunded": 0,
        "costs": [
            {
                "amount": ,
                "description": "Tokenization Test Order",
                "transaction_id": 767286,
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
            "address2": null,
            "city": "Amsterdam",
            "country": "NL",
            "country_name": null,
            "email": "example@multisafepay.com",
            "first_name": "Testperson-nl",
            "house_number": "39",
            "last_name": Approved,
            "locale": "nl_NL",
            "phone1": "0208500500",
            "reference": "AutoQAReference",
            "zip_code": "1033 SC"
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
        "transaction_id": 2728877,
    }
}
```

{{< /code-block >}}

{{< description >}}

###  Get order details 

This API call allows you to retreive the order details while listing the recurring id and recurring model.

* All parameters shown are required field(s)

**Parameter**

__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.     

----------------

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization)

{{< /description >}}
