---
weight: 213
meta_title: "API reference - Pay later refund - MultiSafepay Docs"

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
### Pay later refund
To refund a [pay later](/payments/methods/pay-later/) order, include a [`shopping_cart` object](/api/#shopping-cart-items-object) in the refund request.

1. To retrieve the items in the shopping cart of the order you want to refund, make a [get order](https://api-docs.multisafepay.com/reference/getorder) request.

2. Make a [refund order](https://api-docs.multisafepay.com/reference/refundorder) request, and add a duplicate object for each item you need to refund with a **negative** `quantity`.

**Notes:**  
- Make sure you provide the exact same `merchant_item_id`, `tax_table_selector`, and `unit_price`.  
If you enter a **negative** `unit_price`, the order is cancelled.

- To successfully process partial refunds for variations of the same item (e.g. different size, color) via the shopping cart, each `merchant-item-id` must be unique.  
For example, for different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

**Parameter**

----------------
`checkout_data` | object | required

Contains the original `shopping_cart.items` object **and** duplicate objects for items to be refunded.  
See [shopping_cart.items object](/api/#shopping-cart-items-object).

----------------
{{% /description %}}