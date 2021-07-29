---
weight: 306
meta_title: "API Reference - Create a Bancontact QR order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MISTERCASH",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "gateway_info": {
        "qr_enabled": 1
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
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL",
        "qr_url": "https://payv2.multisafepay.com/simulator/qr?mtp_method=mistercash&token=xxxx"
    }
}
```
{{< /code-block >}}
{{< description >}}
## Bancontact QR
See also Payment methods – [Bancontact](/payments/methods/banks/bancontact).

- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__gateway__ | string

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: MISTERCASH.

----------------

__currency__ | string

The currency for the order.  
Options: `EUR`.

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
__gateway_info__ | object

`qr_enabled` = 1 invokes the `qr_url`.  
This parameter contains a deeplink to Bancontact/MisterCash, which can be encoded into a QR image.  
If the request is successful, you receive 2 links: a payment link and a `qr_url`. 

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

{{< /description >}}