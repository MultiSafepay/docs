---
weight: 330
meta_title: "API Reference - Create a Visa transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders 

```json 

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "VISA",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test order description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123"
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

## Visa

- See also Payment methods – [Visa](/payments/methods/credit-and-debit-cards/visa).  
- Redirect only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Fixed value: `redirect`.  

----------------
`gateway` | string | required

The gateway identifier.  
Fixed value: `VISA`.

**Note:** We also offer a generic [CREDITCARD](https://docs.multisafepay.com/api/#credit-cards) gateway. This can save space in mobile checkouts, but customers can't immediately see which credit cards are supported. When the customer enters the first digits of their card number, the relevant credit card logo appears automatically.

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
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------

{{< /description >}}
