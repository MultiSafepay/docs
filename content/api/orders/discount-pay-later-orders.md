---
weight: 215
meta_title: "API reference - Discount pay later orders - MultiSafepay Docs"
---
{{< description >}}
### Discount pay later orders
To discount a [pay later](/payments/methods/pay-later/) order:

1. Reduce the total order `amount`.
2. Reduce the `unit_price` of the items in the shopping cart you want to discount.

**Note:** Do **not** add a separate `discount` item in the `shopping cart` because it is non-refundable.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.  

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Options: `VISA`, `MASTERCARD`, `AMEX`, `MAESTRO`, `CREDITCARD`.

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | required

The payment amount in the currency's smallest unit:  

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10 

**Note**: This amount includes the discount.

----------------
`shopping_cart.items` | required

See [shopping_cart.items object](/api/#shopping-cart-items-object).

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
  "amount":3000,
  ...
  "shopping_cart":{
    "items":[
      {
        "name":"Candle Holders – 50% discount",
        "description":"",
        "unit_price":15.00,
        "quantity":2,
        "merchant_item_id":"000001",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        }
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