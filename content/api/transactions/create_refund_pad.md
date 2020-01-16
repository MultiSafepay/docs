---
weight: 420
meta_title: "API - Refund with shopping cart - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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
                }
            },
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": "90",
                "quantity": "-2",
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "12"
                }
            },
            {
                "name": "Nice apple",
                "description": "",
                "unit_price": "35",
                "quantity": "1",
                "merchant_item_id": "666666",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "20"
                }
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

{{% note %}}Klarna needs negative unit prices, whereas Pay After Delivery orders need negative quantities!!{{% /note %}}

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
| checkout_data                  | object | Contains the original shopping cart + copied items to be refunded. |
{{% /description %}}