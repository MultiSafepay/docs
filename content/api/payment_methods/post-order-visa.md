---
weight: 313
meta_title: "API reference - Create a Visa transaction - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders 

```json 
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"VISA",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123"
  }
}
```

> JSON response 

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```

{{< /code-block >}}

{{< description >}}

### Visa

- See also Payment methods – [Visa](/payment-methods/visa).  
- Redirect only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The gateway identifier.  
Value: `VISA`.

**Note:** We also offer a generic [CREDITCARD](https://docs.multisafepay.com/api/#credit-cards) gateway. This can save space in mobile checkouts, but customers can't immediately see which credit cards are supported. When the customer enters the first digits of their card number, the relevant credit card logo appears automatically.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------

{{< /description >}}
