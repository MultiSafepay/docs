---
weight: 233
meta_title: "API Reference - Split Payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "description":"Split Payment Order",
  "affiliate":{
    "split_payments":[
      {
        "merchant":1001001,
        "fixed":112,
        "description":"Fixed fee"
      },
      {
        "merchant":1001001,
        "percentage":11.2,
        "description":"Percentage fee"
      }
    ]
  }
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Split Payments
Split the amount of a transaction between multiple MultiSafepay accounts, based on a percentage, a fixed amount, or a combination of the two.

See [Split Payments](/payments/features/split-payments/).

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
`order_id` | string | required

Your unique identifier for the order.  
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
`split_payments` | object | required

Contains:  

`split_payments.merchant` | integer

The account ID of the [affiliated MultiSafepay account](/account/partner-account-control/).   

`split_payments.percentage` | float

Specify a percentage of the amount to split.

`split_payments.fixed` | integer

Specify the amount to split in cents.

`split_payments.description` | string

The description of the split payment.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
{{% /description %}}
