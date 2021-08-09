---
weight: 609
meta_title: "API Reference - Plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< description >}}
## plugin (object)

This object is required for [community-developed integrations](/payments/integrations/community/). 

Contains:  

**Parameters**

----------------
`shop` | string | required

 The ecommerce platform that you use.

----------------
`plugin_version` | string | required

The version of the plugin.

----------------
`shop_version` | string | required

The version of the ecommerce webshop you use. 

----------------
`partner` | string | required

The name of the third party that developed the ecommerce webshop. 

----------------
`shop_root_url` | string | required

The primary URL of the ecommerce webshop.

----------------

{{% /description %}}

{{< code-block >}}
Plugin and/or integration related information

```json 
{
    "plugin": {
        "shop": "ApiTestTool",
        "plugin_version": "1.0.0",
        "shop_version": "1",
        "partner": "partner",
        "shop_root_url": "https://multisafepay.com"
    }
}
 ```
{{< /code-block >}}
