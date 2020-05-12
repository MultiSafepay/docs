---
weight: 302
meta_title: "API - Create Alipay order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "locale": "cn_CN"
    }
}
```

> JSON Response 

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "cn_CN",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "020 8500 500",
        "email": "example@multisafepay.com",
        "referrer": "http://test.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON Response

```shell
{
    "success": true,
    "data": {
        "transaction_id": 2379429850,
        "order_id": "my-order-id-1",
        "created": "2020-01-08T10:51:04",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test Order Description",
        "items": null,
        "amount_refunded": 0,
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2020-01-08T10:51:04",
        "customer": {
            "first_name": "Testperson-nl",
            "last_name": "",
            "address1": "Kraanspoor",
            "address2": null,
            "house_number": 39C,
            "city": "Amsterdam",
            "country": "NL",
            "country_name": null,
            "zip_code": "1033 SC"
            "email": "example@multisafepay.com",
            "locale": "cn_CN",
            "phone1": "020 8500 500",
        },
        "payment_details": {
            "type": "ALIPAY"
           	 "account_holder_name": null,
            "account_id": "",
            "external_transaction_id": null,
            "recurring_id": null,
            "recurring_model": null,
        },
        "costs": [
            {
                "amount": ,
                "description": "",
                "type": "SYSTEM"
            },
            "payment_methods": [
                {
                    "account_id": "",
                    "amount": 1000,
                    "currency": "EUR",
                    "description": "Test Order Description",
                    "payment_description": "ALIPAY",
                    "status": "initialized",
                    "type": "ALIPAY"
                }
            ],
            "payment_url": "https://excashier.alipay.com/standard/auth.htm?auth_order_id=exc_5fc2c0045b9b455f87fedd6d7f41f021"
        }
    }
```

{{< /code-block >}}

{{< description >}}
## Alipay
### Redirect
Creates a Alipay [Redirect](/faq/api/difference-between-direct-and-redirect/) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: redirect, direct, paymentlink. |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request] (#retrieve-all-gateways) Options: ALIPAY. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 character. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                           |
| customer                       | object |                                       |

Read more about [Alipay](/payment-methods/alipay/) on our documentation page.

### Direct

Creates a Alipay [Direct](/faq/api/difference-between-direct-and-redirect/) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: redirect, direct, paymentlink. |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request] (#retrieve-all-gateways) Options: ALIPAY. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 character. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                           |
| customer                       | object |                                       |

Read more about [Alipay](/payment-methods/alipay/) on our documentation page.


{{< /description >}}