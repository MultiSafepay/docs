---
weight: 317
meta_title: "API Reference - Create an ING Home'Pay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "INGHOME",
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
    "transaction_id": 123456789
    "order_id": "my-order-id-1",
    "created": "2019-03-11T14:35:13",
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
    "modified": "2019-03-11T14:35:13",
    "customer": {
      "locale": "nl_BE",
      "first_name": "Simon",
      "last_name": "Smit",
      "address1": "Kraanspoor",
      "house_number": "39C",
      "zip_code": "1033SC",
      "city": "Amsterdam",
      "country": "NL",
      "phone1": "0208500500",
      "email": "simonsmit@example.com",
    },
    "payment_details": {
      "recurring_id": null,
      "type": "INGHOME",
      "account_id": "https://pay.multisafepay.com/direct/complete/",
      "account_holder_name": null,
      "external_transaction_id": 663302604477,
      "account_iban": "*** 1234"
    },
    "costs": [
      {
        "transaction_id": 123456789
        "description": "",
        "type": "SYSTEM",
        "amount": 
      }
    ],
    "payment_url": "https://homepay.ing.be/EN/index.jsp?RETURN_URL=https%3A%2F%2Fpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D260468043&CURRENCY=EUR&AMOUNT=000000100000&RETURN_METHOD=GET&MESSAGE=663302604477&VERSION=2&VENDOR_ID=18204457201&HASH=66d2f141b864621139096d38ce80bc4eff4bb439"
  }
}
```
> POST -/orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "INGHOME",
    "description": "product description",
    "custom_info": {},
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    }
}
```

> JSON Response

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/12RxGzQe6fsi23ml9WkS9lUfwJxo8yYVWgn/?lang=en_US"
  }
}
```


{{< /code-block >}}

{{< description >}}
## ING Home'Pay
### Direct - ING Home'Pay

Creates an ING Home'Pay [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All of the following parameters are required fields.

  
**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: INGHOME.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------    
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`. 

----------------  

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

Read more about [ING Home'Pay](/payments/methods/banks/ing-home-pay) on our documentation page.

### Redirect - ING Home'Pay
Creates an ING Home'Pay [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: INGHOME.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------    


Read more about [ING Home'Pay](/payments/methods/banks/ing-home-pay) on our documentation page.
{{< /description >}}
