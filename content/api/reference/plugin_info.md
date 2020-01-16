---
weight: 630
meta_title: "API - plugin - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< description >}}
## Plugin information

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
    "shop_root_url": "http://multisafepay.com"
}
 ```
{{< /code-block >}}
