---
weight: 225
meta_title: "API reference - Generating API tokens - MultiSafepay Docs"

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

API tokens are used to encrypt sensitive payment details from a customer's device for Payment Component orders:

- [Single payment method](/payment-components/single)
- [Multiple payment methods](/payment-components/multiple/)

Generate a new token for every order, **except** `POST /orders` requests initiated from your server.

**Note**: Tokens are active for 600 seconds.

{{% /description %}}
