---
weight: 600
meta_title: "API reference - Checkout options - MultiSafepay Docs"

---

{{< code-block >}}
```json 
"checkout_options": {
  "tax_tables": {
    "default": {
      "shipping_taxed": "true",
      "rate": "0.21"
    },
    "alternate": [
      {
        "name": "BTW21",
        "standalone": true,
        "rules": [
          {
            "rate": "0.21"
          }
        ]
      },
      {
        "name": "BTW6",
        "standalone": true,
        "rules": [
          {
            "rate": "0.06"
          }
        ]
      },
      {
        "name": "BTW0",
        "standalone": true,
        "rules": [
          {
            "rate": "0.00"
          }
        ]
      },
      {
        "name": "0.0000",
        "standalone": false,
        "rules": [
          {
            "rate": "0"
          }
        ]
      },
      {
        "name": "FEE",
        "standalone": false,
        "rules": [
          {
            "rate": "0.00"
          }
        ]
      },
      {
        "name": "2",
        "standalone": true,
        "rules": [
          {
            "rate": "0.0825",
            "country": "US"
          },
          {
            "rate": "0.08375",
            "country": "US"
          }
        ]
      }
    ]
  }
}
```

{{< /code-block >}}

{{< description >}}
## checkout options (object)

The settings for payment processing.

Contains:  

**Parameters**

----------------
`tax_tables` | object | required

Set default VAT settings and create VAT classes in the `alternate` array that you can apply to individual [shopping cart](/api/#shopping-cart-items-object) items.

Contains:

----------------
`tax_tables.default` | object

The default VAT setting. Used when no value is set for [`shopping_cart.items.tax_table_selector`](/api/#shopping-cart-items-object).

Contains:

----------------
`default.shipping_taxed` | float

Whether or not the shipping costs are taxed.

----------------
`default.rate` | float

The tax rate percentage expressed as a fraction.

**Example:** 15% is expressed as `0.15`.

----------------
`tax_tables.alternate` | array

An array of client-defined VAT classes that you can apply to items in the [shopping cart](/api/#shopping-cart-items-object).

Contains:

----------------
`alternate.name` | string

The client-defined ID. Used to apply tax settings to items in the [shopping cart](/api/#shopping-cart-items-object) through the `tax_table_selector` attribute.

----------------
`alternate.standalone` | boolean

Whether or not the shipping costs are taxed.

----------------
`alternate.rules` | array

----------------
`alternate.rules.rate` | float

The tax rate percentage expressed as a fraction.

----------------
`alternate.rules.country` | string

The country where the tax rate applies.

{{% /description %}}