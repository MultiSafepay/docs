---
weight: 120
meta_title: "API - Retrieve a gateway - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> GET - /gateways/{id}
> JSON Response

```shell

{
  "success": true,
  "data": {
    "id": "{id}",
    "description": "{description of payment method}"
  }
}

```
{{< /code-block >}}

{{< description >}}
## Retrieve a gateway

**Parameter**

----------------

__id__ | string

The unique identifier of the gateway to be returned.

{{% /description %}}