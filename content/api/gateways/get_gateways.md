---
weight: 110
meta_title: "API - Retrieve all gateways - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> GET - /gateways

> JSON Response

```shell
{
  "success": true,
  "data": [
    {
      "id": "MASTERCARD",
      "description": "Mastercard"
    },
    {
      "id": "VISA",
      "description": "Visa"
    },
    {
      "id": "AMEX",
      "description": "AMEX",
    }, 
  ]
}
```
{{< /code-block >}}

{{< description >}}

{{% /description %}}