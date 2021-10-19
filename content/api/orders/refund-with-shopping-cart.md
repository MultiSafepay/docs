---
weight: 213
meta_title: "API reference - Refund with shopping cart - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---


{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```json
{
  "checkout_data":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":90,
        "quantity":3,
        "merchant_item_id":"111111",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        },
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":-90,
        "quantity":2,
        "merchant_item_id":"111111",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      ...
      {
        "name":"Flat Rate - Fixed",
        "description":"Shipping",
        "unit_price":10,
        "quantity":1,
        "merchant_item_id":"msp-shipping",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":0
        }
      }
    ]
  }
}
```
{{< /code-block >}}
{{< description >}}
### Refund with shopping cart
Refund [pay later](/payments/methods/pay-later/) orders that include a [`shopping_cart` object](/api/#shopping-cart-items-object).

1. Make a `GET /orders/{id}` request to retrieve the items in the shopping cart.

2. Make a `POST /orders/{id}/refunds` request:    
    - For Klarna, add a duplicate object for each item you need to refund with a **negative** `unit_price`.  
    - For all other pay later methods, set a negative `quantity`.

**Note:** Make sure you provide the exact same `merchant_item_id`, `tax_table_selector`, and `unit_price`.

The example refunds two out of three geometric candle holders. 

**Parameter**

----------------
`checkout_data` | object | required

Contains the original `shopping_cart.items` object **and** duplicate objects for items to be refunded.  
See [shopping_cart.items object](/api/#shopping-cart-items-object).

----------------
{{% /description %}}