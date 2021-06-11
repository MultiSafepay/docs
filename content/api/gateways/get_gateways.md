---
weight: 110
meta_title: "API - Retrieve all gateways - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
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