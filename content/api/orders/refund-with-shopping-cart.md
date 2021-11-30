---
weight: 213
meta_title: "API reference - Refund with shopping cart - MultiSafepay Docs"

---


{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```json
{
  "checkout_data": {
    "items": [
      {
        "name": "Test",
        "description": "",
        "unit_price": 100,
        "quantity": 1,
        "merchant_item_id": "1111",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": "12"
        }
      },
      {
        "name": "Test",
        "description": "",
        "unit_price": 100,
        "quantity": -1,
        "merchant_item_id": "1111",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": "12"
        }
      }
    ]
  }
}
```
{{< /code-block >}}
{{< description >}}
### Refund with shopping cart
To refund a [pay later](/payments/methods/pay-later/) order, include a [`shopping_cart` object](/api/#shopping-cart-items-object) in the refund request.

1. To retrieve the items in the shopping cart of the order you want to refund, make a `GET /orders/{order_id}` request.

2. Make a `POST /orders/{order_id}/refunds` request, and add a duplicate object for each item you need to refund with a **negative** `quantity`.

{{< alert-notice >}} **Note:**  
Make sure you provide the exact same `merchant_item_id`, `tax_table_selector`, and `unit_price`.  
If you refund with a **negative** `unit_price` this will cancel the order. {{< /alert-notice >}} 

**Parameter**

----------------
`checkout_data` | object | required

Contains the original `shopping_cart.items` object **and** duplicate objects for items to be refunded.  
See [shopping_cart.items object](/api/#shopping-cart-items-object).

----------------
{{% /description %}}