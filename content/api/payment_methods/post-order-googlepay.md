---
weight: 321
meta_title: "API reference - Create a Google Pay order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"GOOGLEPAY",
  "currency":"EUR",
  "amount":9743,
  "description":"Test Order Description",
  "manual":false,
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  }
}
```

> JSON Response

```json
{
  "success": true,
  "data": {
    "order_id": "apitool_6735216",
    "payment_url": "https://devpayv2.multisafepay.com/connect/926YjHh8ZJUj83eQWPgTWKcy70J5F8s6vJ0/?lang=nl_NL",
    "session_id": "926YjHh8ZJUj83eQWPgTWKcy70J5F8s6vJ0"
  }
}
```

> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"GOOGLEPAY",
  "currency":"EUR",
  "amount":1495,
  "description":"Order Description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification"
  },
  "gateway_info":{
    "payment_token":"<google-pay-payment-token>"
  }
}
```

> JSON response

```json
{
  "success": true,
  "data": {
    "order_id": "apitool_6735216",
    "payment_url": "https://devpayv2.multisafepay.com/connect/926YjHh8ZJUj83eQWPgTWKcy70J5F8s6vJ0/?lang=nl_NL",
    "session_id": "926YjHh8ZJUj83eQWPgTWKcy70J5F8s6vJ0"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Google Pay

See also Payment methods – [Google Pay](/payment-methods/google-pay/).  

### Google Pay - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 35 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.    
Value: `GOOGLEPAY`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

### Google Pay - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`.  

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 35 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.    
Value: `GOOGLEPAY`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Value: `false`.

----------------
`payment_options.` | object | required

See [payment_options (object)](/api/#payment-options-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

`gateway_info.payment_token` | string | required

The payment token returned from the client-side Google Pay API call. 

Access the token at `PaymentData.PaymentMethodData.PaymentMethodTokenizationData.token`.

For more information, see [Google Pay direct integration](/payments/methods/wallet/googlepay/direct-integration/).

{{< /description >}}
