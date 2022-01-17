---
weight: 218
meta_title: "API reference - Manual Capture - MultiSafepay Docs"

---

{{< code-block >}}
> POST - /orders 

```json
{
  "type":"redirect",
  "order_id":"order_id_0000001",
  "gateway":"",
  "currency":"EUR",
  "amount":10000,
  "description":"Manual Capture Test",
  "capture":"manual",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "referrer":"https://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  }
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"order_id_0000001",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```
{{< /code-block >}}
{{< description >}}
## Manual Capture orders

See [Manual Capture](/payments/features/manual-capture). 

This only applies to specific credit card payment methods, including MasterCard, VISA and Maestro.

### Create a Manual Capture order

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.    
Options: `redirect`, `direct`, `paymentlink` (makes the transaction appear in your MultiSafepay dashboard under **Tools** > **Payment link generator**).

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

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

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
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
