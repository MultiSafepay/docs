---
weight: 214
meta_title: "API Reference - Discount with order rule - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#order-rule-discounts-non-refundable
---


{{< code-block >}}

> POST - /orders  
```json 
{
    "type": "redirect",
    "gateway": "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 17424,
    ...
    "shopping_cart": {
        "items": [{
            "name": "Geometric Candle Holders",
            "description": "",
            "unit_price": 90.00,
            "quantity": 2,
            "merchant_item_id": "111111",
            "tax_table_selector": "none",
            "weight": {
                "unit": "KG",
                "value": 12
            }
        }, {
            "name": "20% discount on all items",
            "description": "Discount",
            "unit_price": -43.56,
            "quantity": 1,
            "merchant_item_id": "discount",
            "tax_table_selector": "none",
            "weight": {
                "unit": "KG",
                "value": 0
            }
        }]
    },
    "checkout_options": {
        "tax_tables": {
            "default": {
                "shipping_taxed": true,
                "rate": 0.21
            },
            "alternate": [{
                    "name": "BTW21",
                    "rules": [{
                        "rate": 0.21
                    }]
                },
                {
                    "name": "none",
                    "rules": [{
                        "rate": 0.00
                    }]
                }
            ]
        }
    }
}
```
{{< /code-block >}}
{{< description >}}
### Discount with order rule
For all payment methods except [post-payment methods](/payments/methods/billing-suite/), the main way of adding a discount **before** submitting a transaction request is to add it as an order rule (non-refundable). 

For post-payment methods, adding a discount as an order rule or a separate discount rule can create a conflict for partial refunds, especially when the discount is a percentage. You cannot undo or partially refund the negative amount. Instead, add discounts as a [unit price](#discount-with-unit-price).

**Note:** Avoid adding discounts as a separate discount rule because, for partial refunds, you can't undo the negative amount.
{{< /description >}}