---
weight: 230
meta_title: "API Reference - Challenge chargebacks - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /api/#chargebacks
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

> JSON response

```json
{
    "success": true,
    "data": {
    }
}
```
{{< /code-block >}}

{{< description >}}
## Challenge chargebacks

MultiSafepay can challenge [chargebacks](/payments/chargebacks/) on your behalf. To do so, we need documented proof of the order.

You can upload the files or documents via a POST `/order/{order_id}/files` request.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `chargeback`.

----------------
__base64__ | string | required

Binary Base 64 encoded.  
Format: PDF, JPEG, PNG. 

----------------
__description__ | integer | required

Description of or comments on the submitted file. 

----------------
__name__ | string | required

Name of the submitted file.

----------------

{{% /description %}}

