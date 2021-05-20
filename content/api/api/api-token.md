---
weight: 45
meta_title: "API - API generate an API token - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> GET - /connect/auth/api_token/

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