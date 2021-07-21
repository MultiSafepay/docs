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

All requests to the MultiSafepay [API](/faq/general/multisafepay-glossary/#api) require authentication. Authentication is provided by including your [website API key](/set-up-your-account/site-id-api-key-secure-code) as an HTTP header in your request.

The HTTP header name for the API key is: **api_key**

**Note**: When you use API keys in your integrations, keep them secure. Publicly exposing your credentials can result in your account being compromised.

{{% /description %}}