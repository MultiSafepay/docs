---
weight: 325
meta_title: "API - Create a SOFORT order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DIRECTBANK",
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
        "locale": "de_DE"
    }
}
```
> JSON Response

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=de_DE"
    }
}
```

> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "DIRECTBANK",
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
        "locale": "de_DE",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
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
    "amount": 9743,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 348956887,
        "type": "SYSTEM"
      },
      {
        "amount":,
        "description": "",
        "transaction_id": 348956888,
        "type": "SYSTEM"
      }
    ],
    "created": "2020-01-30T10:43:39",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": null,
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": "39C",
      "last_name": "Approved",
      "locale": "de_DE",
      "phone1": "0208500500",
      "zip_code": "1033 SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-30T10:43:39",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": null,
      "account_id": 10071970,
      "external_transaction_id": null,
      "recurring_id": null,
      "recurring_model": null,
      "type": "DIRECTBANK"
    },
    "payment_methods": [
      {
        "account_id": 10071970,
        "amount": 9743,
        "currency": "EUR",
        "description": "Test Order Description",
        "payment_description": "SOFORT Banking",
        "status": "initialized",
        "type": "DIRECTBANK"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 329835554,
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=de_DE",
    "cancel_url": "http://www.example.com/client/notification?type=cancel"
  }
}
```

{{< /code-block >}}

{{< description >}}


## SOFORT
### Redirect - SOFORT
Creates a SOFORT [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect. |

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: DIRECTBANK.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. Check out the availble currencies in this [page](https://docs.multisafepay.com/payment-methods/banks/sofort-banking/#supported-currencies)

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.     

----------------

Read more about [SOFORT Banking](/payment-methods/banks/sofort-banking/) on our documentation page.


### Direct - SOFORT
Creates a SOFORT [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct. |

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: DIRECTBANK.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. Check out the availble currencies in this [page](https://docs.multisafepay.com/payment-methods/banks/sofort-banking/#supported-currencies)

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.     

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [SOFORT Banking](/payment-methods/banks/sofort-banking) on our documentation page.


{{< /description >}}