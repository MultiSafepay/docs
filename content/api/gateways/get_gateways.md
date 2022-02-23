---
weight: 110
meta_title: "API Reference - Retrieve activated gateways - MultiSafepay Docs"

---
{{< code-block >}}

> GET - /gateways

> JSON response

```json
{
  "success": true,
  "data":[
    {
      "id": "VISA",
      "description": "Visa"
    },
    {
      "id": "IDEAL",
      "description": "iDEAL"
    }
  ]
}
```
{{< /code-block >}}

{{< description >}}

## Retrieve activated gateways

Retrieve all activated gateways.

**Parameters**

----------------
`include` | string | query parameter | optional

By default, only one activated [gift cards](/api/#gift-cards) is included in the response.

To include all activated gift cards in the response, specify `coupons`.

**Value:** `coupons`

----------------

{{% /description %}}