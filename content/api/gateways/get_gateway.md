---
weight: 120
meta_title: "API Reference - Retrieve a gateway - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> GET - /gateways/{id}

> JSON Response

```json
{
    "success": true,
    "data": {
      "id": null,
      "description": null
    }
}
```
{{< /code-block >}}

{{< description >}}
## Retrieve a gateway

**Parameters**

---

__id__ | string

The unique identifier of the gateway to be returned.

__country__ | string

Customer’s country code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format e.g. `NL`. Optional.

__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. Optional.

__amount__ | integer

The amount (in cents) that the customer needs to pay. Optional.


{{% /description %}}