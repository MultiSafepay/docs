---
weight: 110
meta_title: "API Reference - Retrieve all gateways - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> GET - /gateways

> JSON response

```json
{
    "success": true,
    "data": [
        {
            "id": null,
            "description": null
        }
    ]
}
```
{{< /code-block >}}

{{< description >}}

## Retrieve all gateways

**Parameters**

----------------
__include__ | string | optional

Additional payment methods you want to specify.  
Format: Comma delimited.

----------------
__Options:__ coupons

----------------

To include **all** gift cards your website supports in the response, add the __include=coupons__ value to your GET request. Otherwise, only one gift card is returned in the response.


{{% /description %}}