---
weight: 610
meta_title: "API Reference - items (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#order-specification-with-items
url: '/api/#items-object/'
---

{{< code-block >}}
```json 
{
    "items": "<ol><li>Article 1: € 1,95</li><li>Article 2: € 2,95</li><li>Article 3: € 3,95</li></ol>",
}
 ```
{{< /code-block >}}
{{< description >}}

## items (object)

If you want to specify the items in the order without including a full [`shopping_cart` object]((/api/#shopping-cart-items), you can add a single `items` line. 

**Note:** [Post-payment methods](/payments/methods/billing-suite/) require the full `shopping_cart` object.

**Parameter**

__items__ | object

A specification of the order items to display on your checkout page.               

{{% /description %}}