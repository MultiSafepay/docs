---
weight: 604
meta_title: "API - Tokenization - Original transaction - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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

MultiSafepay offers the following recurring models: __Card on file (COF), Subscription, Unscheduled__


* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: direct, redirect.        |
| gateway                         | string | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways). E.g. CREDITCARD. |
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| recurring_model                        | string | The function of the recurring model e.g. Card on file, Subscription, Unscheduled  |
| amount                          | integer | The amount (in cents) that the customer needs to pay.                                   |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
|  payment_options 	|   object	 | 
| notification_url            | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                | string    | Customer will be redirected to this page after a successful payment. |
| cancel_url                  | string    | Customer will be redirected to this page after a failed payment.  |
| customer	| object	 | 

Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/tools/tokenization/).

{{< /description >}}
