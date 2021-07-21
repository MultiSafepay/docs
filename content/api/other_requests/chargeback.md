---
weight: 520
meta_title: "API Reference - Chargeback - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders/{order_id}/files

```json
{
    "type": "",
    "base64": "",
    "description": "",
    "name": ""
}
```

> JSON Response

```json
{
    "success": true,
    "data": {
    }
}
```
{{< /code-block >}}

{{< description >}}
## Chargeback

MultiSafepay can challenge [chargebacks](/payments/chargebacks/) on your behalf. To do so, we need documented proof of the order.

You can upload the files or documents via a POST `/order/{order_id}/files` request.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: `chargeback`.

----------------
__base64__ | string

Binary Base 64 encoded. Upload images "pdf, jpeg and png". 

----------------
__description__ | integer

Description of or comments on the submitted file. 

----------------
__name__ | string

Name of the file.

{{% /description %}}

