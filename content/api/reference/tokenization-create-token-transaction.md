---
weight: 606
meta_title: "API - Tokenization - Create token transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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

_It must be noted that the recurring_id, recurring_model and reference must be specified in the request in order for the transaction to be processed_

* All parameters shown are required field(s)

**Parameters**

__type__ | string

Specifies the payment flow for the checkout process. Options: direct.     

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.     

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__recurring_id__ | string

The unique recurring id used for recurring payments.

----------------
__recurring_model__ | string

The function of the recurring model e.g. Card on file, Subscription, Unscheduled.

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.     

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is not supported. Use the ‘items’ or ‘shopping_cart’ objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)                                

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment. 

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. 

----------------
__account_holder_name__ | string

The customer’s name here if provided in transaction request.

----------------
__card_expiry_date__ | string

Card expiry date.

----------------
__reason__ | string

Add a short text memo based on the capture reason of the order.

----------------

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization)

{{< /description >}}