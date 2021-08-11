---
weight: 215
meta_title: "API Reference - Discount with unit price - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#unit-price-discounts
---
{{< description >}}
### Discount with unit price 
For [post-payment methods](/payments/methods/billing-suite/), add discounts as a unit price. The example request is for a 20% discount on all unit prices.

No negative order rule is created, which avoids the refund conflict that can arise if you add discounts as separate discount rules or order rules.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Options: `VISA`, `MASTERCARD`, `AMEX`, `MAESTRO`, `CREDITCARD`.

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | required

The amount (in cents) for the customer to pay.

----------------
`shopping_cart.items` | required

See [shopping_cart.items object](/api/#shopping_cartitems-object).

----------------
`checkout_options` | object | required

The definitions for the VAT class.  

----------------

{{% /description %}}

{{< code-block >}}
> POST /orders  
```json 
{
  "type":"redirect",
  "gateway":"PAYAFTER",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":20800,
  ...
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":72,
        "quantity":2,
        "merchant_item_id":"111111",
        "tax_table_selector":"BTW21",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"20% discount on all items",
        "description":"Discount",
        "unit_price":13930,
        "quantity":1,
        "merchant_item_id":"discount",
        "tax_table_selector":"none"
      }
    ]
  },
  "checkout_options":{
    "tax_tables":{
      "default":{
        "shipping_taxed":true,
        "rate":0.21
      },
      "alternate":[
        {
          "name":"BTW21",
          "rules":[
            {
              "rate":0.21
            }
          ]
        },
        {
          "name":"none",
          "rules":[
            {
              "rate":0.00
            }
          ]
        }
      ]
    }
  }
}
```
{{< /code-block >}}