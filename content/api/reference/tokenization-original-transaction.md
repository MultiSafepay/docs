---
weight: 604
meta_title: "API - Tokenization - Original transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> POST - /orders

```shell
{
        "type": "redirect",
        "gateway": "CREDITCARD",
        "order_id": "my-order-id-1",
        "currency": "EUR",
        "recurring_model": "unscheduled",
        "amount": 10000,
        "description": "Tokenization - ALL - Original unscheduled",
        "payment_options": {
                "notification_url": "http://www.example.com/client/notification?type=notification",
                "redirect_url": "http://www.example.com/client/notification?type=redirect",
                "cancel_url": "http://www.example.com/client/notification?type=cancel",
                "close_window": true
        },
        "customer": {
                "locale": "nl_NL",
                "ip_address": "85.149.25.196",
                "forwarded_ip": "",
                "first_name": "Testperson-nl",
                "last_name": "Approved",
                "address1": "Kraanspoor",
                "house_number": "39",
                "zip_code": "1033 SC",
                "city": "Amsterdam",
                "country": "NL",
                "birthday": "10071970",
                "gender": "male",
                "phone": "0208500500",
                "email": "example@multisafepay.com",
                "referrer": "http://example.com",
                "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "reference": "AutoQAReference"
        }
}
```
> JSON response

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```

{{< /code-block >}}


{{< description >}}

### Original Tokenization transaction

This API call allows you to create an original order using a specific recurring model.

MultiSafepay offers the following recurring models: 

1. __Card on file (COF)__: transaction where a cardholder authorized a merchant to store the cardholder's details 

2. __Subscription__: agreement or services that are billed at the end of a merchant’s billing cycle

3. __Unscheduled__: event triggered for application (for example a mobile top up when no credit is left on the phone)




* All parameters shown are required field(s)

**Parameters**

__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.     

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) E.g. CREDITCARD.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.     

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

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
Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization)

{{< /description >}}
