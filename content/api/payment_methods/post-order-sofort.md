---
weight: 325
meta_title: "API Reference - Create a SOFORT order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DIRECTBANK",
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
        "locale": "de_DE"
    }
}
```
> JSON Response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=de_DE"
    }
}
```

> POST - /orders

```json
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "DIRECTBANK",
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
        "locale": "de_DE",
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
    "amount": 9743,
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
      "country_name": "The Netherlands",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "de_DE",
      "phone1": "0208500500",
      "zip_code": "1033SC"
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
    "transaction_id": 123456789
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=de_DE",
    "cancel_url": "http://www.example.com/client/notification?type=cancel"
  }
}
```

{{< /code-block >}}

{{< description >}}


## SOFORT
### Redirect - SOFORT
Creates a SOFORT [redirect](/developer/api/difference-between-direct-and-redirect) order.

- All fields must be completed correctly.

- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`. |

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: DIRECTBANK.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  Check out the availble currencies in this [page](https://docs.multisafepay.com/payment-methods/banks/sofort-banking/#supported-currencies)

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.     
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

See also [SOFORT Banking](/payments/methods/banks/sofort-banking).

### Direct - SOFORT
Creates a SOFORT [direct](/developer/api/difference-between-direct-and-redirect) order.

- All fields must be completed correctly.

- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  Options: `direct`. |

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: DIRECTBANK.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  Check out the availble currencies in this [page](https://docs.multisafepay.com/payment-methods/banks/sofort-banking/#supported-currencies)

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.   

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

See also [SOFORT Banking](/payments/methods/banks/sofort-banking).


{{< /description >}}