---
weight: 302
meta_title: "API Reference - Create an Alipay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "locale": "cn_CN"
    }
}
```

> JSON Response 

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
> POST - /orders

```json
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "manual": false,
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "cn_CN",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "simonsmit@example.com",
        "referrer": "https://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON Response

```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
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
            "first_name": "Simon",
            "last_name": "Smit",
            "address1": "Kraanspoor",
            "house_number": "39C",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": "The Netherlands",
            "zip_code": "1033SC"
            "email": "simonsmit@example.com",
            "locale": "cn_CN",
            "phone1": "0208500500",
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
            "amount":,
            "description": "",
            "transaction_id": 123456789
            "type": "SYSTEM"
        }
        ],
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
### Redirect - Alipay
Creates an Alipay [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct, paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: ALIPAY. 

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/developer/api/notification-url) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.

----------------
__close_window__ | bool (optional)

Options: `True`, `False`. To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`. 

----------------

Read more about [Alipay](/payments/methods/wallet/alipay) on our documentation page.

### Direct - Alipay

Creates an Alipay [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct, paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: ALIPAY. 

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/developer/api/notification-url) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.


__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [Alipay](/payments/methods/wallet/alipay) on our documentation page.


{{< /description >}}
