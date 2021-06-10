---
weight: 320
meta_title: "API - Create a KBC order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "KBC",
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
        "locale": "nl_BE"
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
    "gateway": "KBC",
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
        "locale": "nl_BE",
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

> JSON Repsonse
```shell
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 344230330,
        "type": "SYSTEM"
      },
      {
        "amount":,
        "description": "",
        "transaction_id": 344230331,
        "type": "SYSTEM"
      }
    ],
    "created": "2019-03-08T10:15:37",
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
      "house_number": 39C,
      "last_name": "Approved",
      "phone1": "0208500500",
      "locale": "nl_BE",
      "phone1": "020 8500 500",
      "zip_code": "1033 SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2019-03-08T10:15:37",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": null,
      "account_id": null,
      "external_transaction_id": 325062361,
      "recurring_id": null,
      "recurring_model": null,
      "type": "KBC"
    },
    "payment_methods": [
      {
        "amount": 1000,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": 325062361,
        "payment_description": "KBC",
        "status": "initialized",
        "type": "KBC"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 325062361,
    "payment_url": "https://www.kbc.be/olpayment?langWebSite=N&olpId=S132&olpCtx=%2FH8s4RM8GN%2FSKLOcUoTBBPus%2BWBbXCz9ChR12y5ozVDe8Rc70DjFQNQy2TaiSnTOEQkziFEQmgQy%2BHDxrqqzB%2F8I1yk5zE0%"
  }
}
```

{{< /code-block >}}

{{< description >}}
## KBC
### Redirect - KBC

Creates a KBC [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: KBC.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

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

Contains personal information about the customer. 

---------------- 

__close_window__ | bool

Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

Read more about [KBC](/payment-methods/banks/kbc) on our documentation page.

### Direct - KBC

Creates a KBC [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: KBC.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

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

Contains personal information about the customer. 

---------------- 

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [KBC](/payment-methods/banks/kbc) on our documentation page.
{{< /description >}}