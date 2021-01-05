---
weight: 420
meta_title: "API - Refund with shopping cart - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---


{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```shell


{
    "checkout_data": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": "90",
                "quantity": "3",
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "12"
                ...
            },
            {
                "name": "Flat Rat - Fixed",
                "description": "Shipping",
                "unit_price": "10",
                "quantity": "1",
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "0"
                }
            }
        ]
    }
}
```
{{< /code-block >}}
{{< description >}}
## Refund with shopping cart
This request is used for creating a refund in orders with shopping cart like Pay After Delivery, E-Invoicing, Klarna and AfterPay.

To proceed with a refund:

1. A request should be done to GET - /orders/{id} to obtain the cart items of the order and possible refunded items
2. Add/remove items in the refund. In Klarna, refunds are done adding a "copy" of the item to refund, with negative "unit_price", all others should set negative "quantity".
3. Please make sure that all data in the items match with the original transaction (except for the quantity/unit_price): In the example, two out of three 'Geometric Candle Holders' were refunded. Please note that the exact same 'merchant_item_id', 'tax_table_selector' and 'unit_price' were provided.

{{% note %}} Klarna needs negative unit prices, whereas Pay After Delivery orders need negative quantities! {{% /note %}}

----------------
**Parameter**

----------------
__checkout_data__ | object

Contains the original shopping cart + copied items to be refunded. 


{{% /description %}}