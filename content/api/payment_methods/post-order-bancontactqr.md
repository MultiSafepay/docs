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

Creates a Bancontact QR [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect and payment link.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: MISTERCASH.

----------------

__currency__ | string

Has to be EUR.

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
__gateway_info__ | object

The qr_enabled = 1 invokes the qr_url. This parameter contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

After placing the order, you will receive 2 links as response on a successfull Bancontact QR request: a payment link and a qr_url. This qr_url contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point.


Read more about [Bancontact](/payments/methods/banks/bancontact) on our documentation page.

{{< /description >}}