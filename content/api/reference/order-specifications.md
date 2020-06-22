---
weight: 610
meta_title: "API - Order specification with 'items' - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
```shell 

    "items": "<ol><li>Article 1: € 1,95</li><li>Article 2: € 2,95</li><li>Article 3: € 3,95</li></ol>",

 ```
{{< /code-block >}}
{{< description >}}

## Order specification with "items"

The line "items" can be added to the JSON request. Post payment methods require the full shopping_cart.

| Parameter                         | Type     | Description     |
|-----------------------------------|----------|-----------------|
| items                   | object   | Specification of products (items) which can be set in order to be displayed on the checkout page.                |

{{% /description %}}