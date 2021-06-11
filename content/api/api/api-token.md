---
weight: 45
meta_title: "API - API generate an API token - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> GET - /auth/api_token/

> JSON Response
``` shell
{
  "success": true,
  "data": {
    "api_token": "pub.v2.xxxxxxxx"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Generate an API token

API tokens are used to encrypt sensitive payment details.

For every order, generate a new API token.

{{% /description %}}