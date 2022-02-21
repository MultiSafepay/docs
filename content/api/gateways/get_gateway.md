---
weight: 120
meta_title: "API reference - Retrieve a specific gateway - MultiSafepay Docs"

---
{{< code-block >}}

> GET - /gateways/{id}

> JSON response

```json
{
  "success":true,
  "data":{
    "id": null,
    "description": null
  }
}
```
{{< /code-block >}}

{{< description >}}
## Retrieve a gateway

Retrieve a gateway by its ID.

**Parameters**

----------------
`id` | string | required | query parameter

The unique identifier of the requested gateway.

{{% /description %}}