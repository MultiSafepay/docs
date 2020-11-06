---
weight: 120
meta_title: "API - Retrieve a gateway - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> GET - /gateways/{id}
> JSON Response

```shell

{
  "success": true,
  "data": {
    "id": "{id}",
    "description": "{description of payment method}"
  }
}

```
{{< /code-block >}}

{{< description >}}
## Retrieve a gateway

**Parameter**

----------------

__id__ | string

The unique identifier of the gateway to be returned.

{{% /description %}}