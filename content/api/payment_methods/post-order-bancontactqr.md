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
    "description": "Test order description",
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

> JSON response

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

- See also Payment methods – [Bancontact](/payments/methods/banks/bancontact).  
- Redirect only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`, `paymentlink`.

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Options: `MISTERCASH`.

----------------
`currency` | string | required

The currency for the order.  
Fixed value: `EUR`.

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`gateway_info` | object

`qr_enabled` = 1 invokes the `qr_url`.  
This parameter contains a deeplink to Bancontact/MisterCash, which can be encoded into a QR image.  
If the request is successful, you receive 2 links: a payment link and a `qr_url`. 

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------

{{< /description >}}