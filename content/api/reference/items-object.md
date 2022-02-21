---
weight: 605
meta_title: "API reference - items (object) - MultiSafepay Docs"

---

{{< code-block >}}
```json 
{
  "items":"<ol><li>Article 1: € 1,95</li><li>Article 2: € 2,95</li><li>Article 3: € 3,95</li></ol>"
}
 ```
{{< /code-block >}}
{{< description >}}

## items (object)

Lets you display the items in the customer's order in a single line on your checkout page instead of including a full [`shopping_cart` object](/api/#shopping-cart-items). 

**Note:** [Pay later methods](/payments/methods/pay-later/) require a full `shopping_cart` object.

**Parameter**

----------------
`items` | object | required

Contains the order items to display on your checkout page. 

----------------

{{% /description %}}
