---
weight: 40
meta_title: "API Reference - Authentication - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> Test API

``` shell
curl -X POST "https://testapi.multisafepay.com/v1/json/" \
--header "api_key: <your-test-API-key>"
```

> Live API

``` shell
curl -X POST "https://api.multisafepay.com/v1/json/" \
--header "api_key: <your-API-key>"
```

{{< /code-block >}}

{{< description >}}
## Authentication

All requests to the MultiSafepay API require authentication. 

Include your [website API key](/set-up-your-account/site-id-api-key-secure-code) as an HTTP header in your request: `api_key`

**Note**: Always keep your API keys secure. Publicly exposing your credentials can compromise your account.

{{% /description %}}