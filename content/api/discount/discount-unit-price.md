---
weight: 52
meta_title: "API - Discount added as unit price - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< description >}}
## Discount added as unit price 
A discount added as seperate discount rule may conflict in refunding with postpaid payment methods. Therefore, it is advised to add the discount as unit price. As a result, no negative order rule is created, which means that refunding from a postpaid payment method will not cause a conflict.
{{% /description %}}

{{< code-block >}}
> Example with 20% discount calculated in all unit prices:

```shell 
{
    "type": "redirect",
    "gateway": "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 20800,
    ...
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 72,
                "quantity": 2,
                "merchant_item_id": "111111",
                "tax_table_selector": "BTW21",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
            {
                "name": "20% discount on all items",
                "description": "Discount",
                "unit_price": 13930,
                "quantity": 1,
                "merchant_item_id": "discount",
                "tax_table_selector": "none"
            }
        ]
    },
    "checkout_options": {
        "tax_tables": {
            "default": {
                "shipping_taxed": "true",
                "rate": 0.21
            },
            "alternate": [
                {
                    "name": "BTW21",
                    "rules": [
                        {
                            "rate": 0.21
                        }
                    ]
                },
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0.00
                        }
                    ]
                }
            ]
        }
    }
}
```
{{< /code-block >}}