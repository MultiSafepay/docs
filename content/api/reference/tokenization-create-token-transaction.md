---
weight: 606
meta_title: "API Reference - Tokenization - Create token transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> POST - /orders

```json
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

```json
{
    "success": true,
    "data": {
        "amount": 1000,
        "amount_refunded": 0,
        "costs": [
            {
                "amount": 0.6,
                "description": " Tokenization Generate token transaction ",
                "transaction_id": 123456789
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
            "phone2": "00310000001",
            "reference": "AutoQAReference",
            "state": "NH",
            "zip_code": "1033SC"
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
        "transaction_id": 123456789
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

* All of the following parameters are required fields.

**Parameters**

__type__ | string

The payment flow for the checkout process.  Options: `direct`.     

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.     

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

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

A text which will be shown with the order in your MultiSafepay account. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is not supported. Use the ‘items’ or ‘shopping_cart’ objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).                                

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails. 

----------------
__customer__ | 

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

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

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/payments/features/tokenization)

{{< /description >}}