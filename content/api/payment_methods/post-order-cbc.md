---
weight: 309
meta_title: "API Reference - Create a CBC order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "CBC",
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
        "locale": "nl_BE"
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
    "gateway": "CBC",
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
        "locale": "nl_BE",
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

> JSON Repsonse
```json
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 123456789
        "type": "SYSTEM"
      },
      {
        "amount":,
        "description": "",
        "transaction_id": 123456789
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
      "country_name": "The Netherlands",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "phone1": "0208500500",
      "locale": "nl_BE",
      "phone1": "0208500500",
      "zip_code": "1033SC"
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
      "type": "CBC"
    },
    "payment_methods": [
      {
        "amount": 1000,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": 325062361,
        "payment_description": "CBC",
        "status": "initialized",
        "type": "CBC"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789
    "payment_url": "https://www.cbc.be/olpayment?langWebSite=N&olpId=S132&olpCtx=%2FH8s4RM8GN%2FSKLOcUoTBBPus%2BWBbXCz9ChR12y5ozVDe8Rc70DjFQNQy2TaiSnTOEQkziFEQmgQy%2BHDxrqqzB%2F8I1yk5zE0%"
  }
}
```

{{< /code-block >}}

{{< description >}}
## CBC
### Redirect - CBC

Creates a CBC [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: CBC.

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

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

Read more about [CBC](/payment-methods/banks/cbc) on our documentation page.

### Direct - CBC

Creates a CBC [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: CBC.

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

Read more about [CBC](/payment-methods/banks/cbc) on our documentation page.
{{< /description >}}