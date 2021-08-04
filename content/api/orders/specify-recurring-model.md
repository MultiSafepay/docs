---
weight: 237
meta_title: "API Reference - Specify recurring model - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#original-tokenization-transaction
---

{{< code-block >}}

> POST - /orders

```json
{
        "type": "redirect",
        "gateway": "CREDITCARD",
        "order_id": "my-order-id-1",
        "currency": "EUR",
        "recurring_model": "unscheduled",
        "amount": 10000,
        "description": "Tokenization - ALL - Original unscheduled",
        "payment_options": {
                "notification_url": "http://www.example.com/client/notification?type=notification",
                "redirect_url": "http://www.example.com/client/notification?type=redirect",
                "cancel_url": "http://www.example.com/client/notification?type=cancel",
                "close_window": true
        },
        "customer": {
                "locale": "nl_NL",
                "ip_address": "123.123.123.123",
                "forwarded_ip": "",
                "first_name": "Simon",
                "last_name": "Smit",
                "address1": "Kraanspoor",
                "house_number": "39C",
                "zip_code": "1033SC",
                "city": "Amsterdam",
                "country": "NL",
                "birthday": "1970-07-10",
                "gender": "mr",
                "phone": "0208500500",
                "email": "simonsmit@example.com",
                "referrer": "http://example.com",
                "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "reference": "AutoQAReference"
        }
}
```
> JSON response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```

{{< /code-block >}}


{{< description >}}

### Specify recurring model

Create an original [tokenization](/payments/features/tokenization) order using a specific recurring model:

- **Card on file (COF)**: The cardholder has authorized you to store their card details.
- **Subscription**: Agreement or services that are billed at the end of your billing cycle.
- **Unscheduled**: Event triggered for application, e.g. a mobile top-up when no credit is left on the phone.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`.     

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
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
`recurring_model` | string | required

The recurring model.  
Options: `unscheduled`, `subscription`, `cardonfile`.

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
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------


{{< /description >}}
