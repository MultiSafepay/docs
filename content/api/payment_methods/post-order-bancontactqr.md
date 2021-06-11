---
weight: 306
meta_title: "API - Create a Bancontact QR order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MISTERCASH",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "gateway_info": {
        "qr_enabled": 1
    },
    "customer": {
        "locale": nl_BE"
    }
}
```

> JSON Response

```shell
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

Creates a Bancontact QR [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect and payment link.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

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

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__gateway_info__ | object

The qr_enabled = 1 invokes the qr_url. This parameter contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point.

----------------
__customer__ | object

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

After placing the order, you will receive 2 links as response on a successfull Bancontact QR request: a payment link and a qr_url. This qr_url contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point.


Read more about [Bancontact](/payment-methods/banks/bancontact) on our documentation page.

{{< /description >}}