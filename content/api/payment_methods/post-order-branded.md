---
weight: 314
meta_title: "API reference - Create a co-branded credit card order - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /order

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
    "locale":"it_IT",
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
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=it_IT"
  }
}
```

{{< /code-block >}}

{{< description >}}
### Co-branded credit cards 

- See also:  
  - [Cartes Bancaires](/payment-methods/cartes-bancaires/)
  - [Dankort](/payment-methods/dankort/) 
  - [Maestro](/payment-methods/maestro/)
  - [Postepay](/payment-methods/postepay/) 
  - [V Pay](/payment-methods/vpay/)  
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

The unique gateway identifier for the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `CREDITCARD`, `VISA`, `MASTERCARD`.

----------------
`currency` | string | required

The currency of the payment.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`amount` | integer | required

The payment amount in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Note:** The co-branded card logo only displays if the `locale` is correctly supplied.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

---------------- 

{{< /description >}}
