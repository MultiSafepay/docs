---
weight: 214
meta_title: "API reference - Discount an order - MultiSafepay Docs"
---

{{< code-block >}}

> POST - /orders  
```json 
{
  "type":"redirect",
  "gateway":"PAYAFTER",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":8000,
  ...
  "shopping_cart":{
    "items":[
      {
        "name":"Candle Holders",
        "description":"",
        "unit_price":30.00,
        "quantity":2,
        "merchant_item_id":"000001",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":1
        }
      },
      {
        "name":"Chair",
        "description":"",
        "unit_price":40.00,
        "quantity":1,
        "merchant_item_id":"000002",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":3
        }
      },
      {
        "name":"20% discount on all items",
        "description":"Discount",
        "unit_price":-20.00,
        "quantity":1,
        "merchant_item_id":"discount",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":0
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
{{< description >}}

### Discount an order

To discount an order (except for [pay later](/api/#discount-pay-later-orders) orders):

- Reduce the total order `amount` (this determines how much the customer pays).
- Optionally, to discount:
  - All items in the order, add a separate "discount" item in the `shopping_cart`.
  - Specific items in the order, reduce the `unit_price` of those items in the `shopping_cart`.

See also [Discount pay later orders](/api/#discount-pay-later-orders).

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

{{< /description >}}