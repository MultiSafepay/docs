---
weight: 610
meta_title: "API - Shopping cart - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
```shell 
"name": "",
```

```shell
"description": "",
```

```shell 
"unit_price": "",
```

```shell
"quantity": "",
```

```shell
"merchant_item_id": "",
```

```shell 
"tax_table_selector": "",
```

```shell 
"weight": {},
```

```shell 
"options": [],
```

{{< /code-block >}}

{{< description >}}
## shopping_cart.items
### name
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| name                             | string   | The customer's name | 

### description
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| description                         | string  | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is not supported. Use the ‘items’ or ‘shopping_cart’ objects for this.                                                                            |

### quantity
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| quantity                       | integer   | The number of items for a specific item in the shopping cart.                                                                            |

### merchant_item_id
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| merchant_item_id                       | string   | A unique ID relating to the specified item in the shopping cart.                                                          |


### tax_table_selector
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| tax_table_selector                          | string   | The tax ruling specified.                                                           |
|                                    |          |                                                                                      | 

### weight
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| weight                          | object   | The weight of the item in the shopping cart.                                          |
|                                    |          |                                                                                      | 

### options
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| options                           | string   |  An array of objects including id, set_id, value, price, type and price_type.                                       |
|                                    |          |                                                                                      | 
                                                                                                
{{% /description %}}