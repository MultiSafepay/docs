---
weight: 611
meta_title: "API Reference - Shopping cart - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
```json 
{
  "shopping_cart":{
    "name":"",
    "description":"",
    "unit_price":100,
    "quantity":2,
    "merchant_item_id":"",
    "tax_table_selector":"",
    "weight":{
      
    },
    "options":[
      
    ],
    "value":200,
    "unit":""
  }
}
```

{{< /code-block >}}

{{< description >}}
## shopping_cart.items (object)

All items in the shopping cart, including the tax class.    
If you have a custom integration, include the complete specification of the `shopping_cart`.  

Contains:  

**Parameters**

----------------
`name` | string | required

The customer's name.

----------------
`description` | string | required

A description of the item that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`unit_price` | float | required

The unit price (in decimals) of the item, excluding VAT.  
Format: Maximum 10 decimal places.

----------------
`quantity` | integer | required

The number of units of the item. 

----------------
`merchant_item_id` | string | required

Fixed value: `msp-shipping`.

----------------
`tax_table_selector` | string | required

The tax ruling.  

**Note:** A 0 value throws an error: _'1029: Invalid tax rate specified for item'_.  
Format: The `tax_table_selector` and `tax_table` names are both `strings`.

----------------
`weight` | string | required

The weight of the item.  

----------------
`options` | string | required

An array of objects including `id`, `set_id`, `value`, `price`, `type`, and `price_type`. 

----------------
`value` | integer | required

The weight of the item corresponding to the [unit](/api/#unit).  
Example: unit= KG, value= 12. The weight of the item is 12 kilograms. 

----------------
`unit` | string | required

The unit of weight, e.g. `KG`.

----------------
{{% /description %}}