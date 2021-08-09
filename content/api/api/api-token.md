---
weight: 45
meta_title: "API Reference - Generating API tokens - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> GET - /auth/api_token/

> JSON response
```json
{
  "success": true,
  "data": {
    "api_token": "pub.v2.xxxxxxxx"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Generating API tokens

API tokens are used to encrypt sensitive payment details from a customer's device.

Generate a new token for every order, **except** `POST /orders` requests initiated from your server.

{{% /description %}}
