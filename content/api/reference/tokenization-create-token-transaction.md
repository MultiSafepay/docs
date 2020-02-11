---
weight: 606
meta_title: "API - Tokenization - Create token transaction - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}

> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "recurring_id": "azbkvsE0up4",
    "recurring_model": "unscheduled",
    "amount": 1000,
    "description": "Tokenization Generate token transaction",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "reference": "AutoQAReference"
    }
}
```
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

### Create token transaction

This API call allows you to generate a token transaction by using the recurring id and recurring model in the request.

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
| type                           | string  | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
| order_id                       | integer / string  | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                    |
| currency                       | string  | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| recurring_id                        | string | The unique recurring id used for recurring payments. |
| recurring_model                        | string | The function of the recurring model e.g. Card on file, Subscription, Unscheduled  |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                   |
| description                    | string  | A free text description which will be shown with the order in MultiSafepay Control. If the customers bank supports it this description will also be shown on the customer`s bank statement. |
|  payment_options 	|   object	 | 
| notification_url            | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                | string    | Customer will be redirected to this page after a successful payment. |
| cancel_url                  | string    | Customer will be redirected to this page after a failed payment.  |
| customer	| object	 | 
| locale	|  string | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. | 
| account_holder_name		| string	 | The customer’s name here if provided in transaction request. |
| card_expiry_date		| string	 | Card expiry date. |
| reason		| string	 | Add a short text memo based on the capture reason of the order. |


Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization/)

{{< /description >}}