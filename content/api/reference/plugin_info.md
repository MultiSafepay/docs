---
weight: 630
meta_title: "API Reference - Plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< description >}}
## Plugin information

This [plugin](/faq/general/multisafepay-glossary/#plugin) information is required for a Community Integration. For more information about these requirments, please See also [a community integration](/payments/integrations/community).

**Parameters**

__shop__ | string

 The ecommerce platform in use.

----------------
__plugin_version__ | string

The version of the plugin.

----------------
__shop_version__ | string

The version of the ecommerce webshop. 

----------------
__partner__ | string

The third party developing the ecommerce webshop. 

----------------
__shop_root_url__ | string

The primary URL of the ecommerce webshop.

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
