---
weight: 236
meta_title: "API reference - Split payments - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders  
Split by percentage only
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
        "percentage":11.2,
        "description":"Percentage fee"
      }
    ]
  }
}
```
> POST - /orders  
Split by fixed amount only 
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
      }
    ]
  }
}
```
> POST - /orders  
Split by percentage and fixed amount
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
## Split payments orders
Split the amount of a transaction between partner or affiliate accounts by a percentage, a fixed amount, or both.

{{< alert-notice >}}**Important:** If splitting by both, never give a 0 value for the percentage or the fixed amount.  {{< /alert-notice >}}

See [Split payments](/features/split-payments/).

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink` (makes the transaction appear in your MultiSafepay account under **Tools** > **Payment link generator**).  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
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

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`split_payments` | object | required

Contains:  

`split_payments.merchant` | integer

The account ID of the [affiliated MultiSafepay account](/account/partner-account-control/).   

`split_payments.percentage` | float

Specify a percentage of the amount to split.  
**Important:** Never give a 0 value. 

`split_payments.fixed` | integer

Specify the amount to split in cents.  
**Important:** Never give a 0 value. 

`split_payments.description` | string

The description of the split payment.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
{{% /description %}}
