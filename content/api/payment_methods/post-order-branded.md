---
weight: 311
meta_title: "API reference - Create a co-branded credit card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
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

- See also Payment methods:  
  - [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires)
  - [Dankort](/payments/methods/credit-and-debit-cards/dankort) 
  - [Postepay](/payments/methods/credit-and-debit-cards/postepay)  
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

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `CREDITCARD`, `VISA`, `MASTERCARD`.

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
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Note:** The co-branded card logo only displays if the `locale` is correctly supplied.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

---------------- 

{{< /description >}}
