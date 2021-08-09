---
weight: 218
meta_title: "API Reference - Cancel an authorized or reserved transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#manual-capture-authorization
---

{{< code-block >}}
> POST - /orders 

```json
{
    "type": "redirect",
    "order_id": "order_id_0000001",
    "gateway": "",
    "currency": "EUR",
    "amount": 10000,
    "description": "Manual Capture Test",
    "capture": "manual",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "referrer": "https://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON response

```json
{
    "success": true,
    "data": {
        "order_id": "order_id_0000001",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
{{< /code-block >}}
{{< description >}}
## Manual capture orders

See [Manual capture](/payments/features/manual-capture). 

This only applies to specific credit card payment methods, including MasterCard, VISA and Maestro.

### Create a manual capture order

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.    
Options: `redirect`, `direct`, `checkout`, `paymentlink`.

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`capture` | string

A manual capture has been generated. 

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------

{{% /description %}}