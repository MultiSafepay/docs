---
weight: 630
meta_title: "API - Plugin - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< description >}}
## Plugin information

This [plugin](/faq/getting-started/glossary/#plugin) information is required for a Community Integration. For more information about these requirments, please read more about [a community integration](https://docs.multisafepay.com/integrations/community/community/) on our documentation page.

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| shop                        | string   | The ecommerce platform in use. |
| plugin_version			| string | The version of the plugin. |
| shop_version			| string | The version of the ecommerce webshop. |
| partner					| string | The third party developing the ecommerce webshop. |
| shop_root_url			| string | The primary URL of the ecommerce webshop. |
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
