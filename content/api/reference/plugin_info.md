---
weight: 630
meta_title: "API - Plugin - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< description >}}
## Plugin information

This [plugin](/faq/general/multisafepay-glossary/#plugin) information is required for a Community Integration. For more information about these requirments, please read more about [a community integration](/integrations/community) on our documentation page.

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

```shell 

"plugin": {
    "shop": "ApiTestTool",
    "plugin_version": "1.0.0",
    "shop_version": "1",
    "partner": "partner",
    "shop_root_url": "https://multisafepay.com"
}
 ```
{{< /code-block >}}
