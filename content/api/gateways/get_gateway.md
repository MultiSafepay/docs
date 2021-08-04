---
weight: 120
meta_title: "API Reference - Retrieve a specific gateway - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> GET - /gateways/{id}

> JSON response

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
## Retrieve a specific gateway

**Parameters**

----------------
`id` | string | required

The unique identifier of the requested gateway.

----------------
`country` | string | optional

The customer’s country code.  
Format: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. 

----------------
`currency` | string | optional

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | optional

The amount (in cents) for the customer to pay. 

----------------

{{% /description %}}