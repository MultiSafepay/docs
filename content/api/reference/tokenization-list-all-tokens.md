---
weight: 607
meta_title: "API - Tokenization - List all tokens - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}

> JSON Response

```shell
{
    "success": true,
    "data": {
        "amount": 1000,
        "amount_refunded": 0,
        "costs": [
            {
                "amount": 0.6,
                "description": " Tokenization Generate token transaction ",
                "transaction_id": 767288,
                "type": "SYSTEM"
            }
        ],
        "created": "2019-10-24T13:22:45",
        "currency": "EUR",
        "custom_info": {
            "custom_1": null,
            "custom_2": null,
            "custom_3": null
        },
        "customer": {
            "address1": null,
            "address2": null,
            "city": null,
            "country": null,
            "country_name": null,
            "email": "",
            "first_name": null,
            "house_number": null,
            "last_name": null,
            "locale": "nl_NL",
            "phone1": null,
            "phone2": "",
            "reference": "AutoQAReference",
            "state": null,
            "zip_code": null
        },
        "description": "Tokenization - ALL - Trx with previous token with unscheduled model when is disabled",
        "fastcheckout": "NO",
        "financial_status": "completed",
        "items": null,
        "modified": "2019-10-24T13:22:45",
        "order_id": "my-order-id",
        "payment_details": {
            "account_holder_name": "Testperson-nl",
            "account_id": null,
            "card_expiry_date": 1112,
            "external_transaction_id": 929711011483,
            "last4": 1111,
            "recurring_id": "azbkvsE0up4",
            "recurring_model": "unscheduled",
            "type": "VISA"
        },
        "payment_methods": [
            {
                "account_holder_name": "Testperson-nl",
                "amount": 1000,
                "card_expiry_date": 1112,
                "currency": "EUR",
                "description": "Tokenization - ALL - Trx with previous token with unscheduled model when is disabled",
                "external_transaction_id": 929711011483,
                "last4": 0,
                "payment_description": "Visa CreditCards",
                "status": "completed",
                "type": "VISA"
            }
        ],
        "reason": "Successful approval/completion",
        "reason_code": "",
        "related_transactions": null,
        "status": "completed",
        "transaction_id": 2728879,
        "payment_url": " https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL ",
        "cancel_url": " http://www.example.com/client/notification?type=cancel "
    }
}
```

{{< /code-block >}}

{{< description >}}

### List all tokens for a customer reference

This API call allows you to list all tokens related to a single customer reference.

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
|token                            | string   | The unique token linked to the customer reference. |

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization/)

{{< /description >}}