---
weight: 520
meta_title: "API - Chargeback - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders/{order_id}/files

```shell
{
    "type": "",
    "base64": "",
    "description": "",
    "name": ""
}
```

> JSON Response

```shell
{
    "success": true,
    "data": {
    }
}
```
{{< /code-block >}}

{{< description >}}
## Chargeback

MultiSafepay can challenge the chargeback on your behalf, but to do so, we need documented proof of the order.

You can upload the files or documents via an API request, or email the Support Team at <support@multisafepay.com>

Read more about [chargebacks](/faq/chargebacks) on our documentation page.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: chargeback.

----------------
__base64__ | string

Binary Base 64 encoded. Upload images "pdf, jpeg and png". 

----------------
__description__ | integer

Description or comments of the submitted file. 

----------------
__name__ | string

Name of the file.

{{% /description %}}

