---
weight: 420
meta_title: "API Reference - Refund with shopping cart - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---


{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```json


{
    "checkout_data": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 90,
                "quantity": 3,
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
                ...
            {
                "name": "Flat Rat - Fixed",
                "description": "Shipping",
                "unit_price": 10,
                "quantity": 1,
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 0
                }
            }
        ]
    }
}
```
{{< /code-block >}}
{{< description >}}
## Refund with shopping cart
Use this endpoint for refunding [post-payment](/payments/methods/billing-suite/) orders that include a shopping cart object.

1. Make a GET `/orders/{id}` request to retrieve the items in the shopping cart.

2. Add or remove items in the POST `/orders/{id}/refunds` request, depending on the type of post-payment method:    
    - For Klarna, add a "copy" of the item to refund with a negative `unit_price`.  
    - For all other post-payment methods, set a negative `quantity`.
&nbsp;      
3. Make sure that all data in the items matches the original transaction (except for the `quantity` or `unit_price`).

In the example, two out of three geometric candle holders were refunded. The exact same `merchant_item_id`, `tax_table_selector` and `unit_price` were provided.

----------------
**Parameter**

----------------
__checkout_data__ | object

Contains the original shopping cart **and** copied items to be refunded. 


{{% /description %}}