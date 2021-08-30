---
weight: 540
meta_title: "API Reference - Retrieve website categories - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#retrieve-website-categories
---
{{< code-block >}}
> GET - /categories


> JSON response

```json
{
  "success":true,
  "data":[
    {
      "code":106,
      "description":"Child and toys"
    }
  ]
}
```
{{< /code-block >}}

{{< description >}}
## Retrieve website categories
Retrieves a list of website categories.

**Response**

----------------
`code` | string 

The unique identifier of the payment gateway.

----------------
`description` | string 

A description of the transaction, which is displayed in both your account and the affiliated account.

----------------

{{% /description %}}