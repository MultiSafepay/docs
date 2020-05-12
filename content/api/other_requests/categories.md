---
weight: 510
meta_title: "API - Categories - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> GET - /categories


> JSON Response

```shell
{
    "success": true,
    "data": [
        {
            "code": 999,
            "description": "Adult"
        },
        {
            "code": 106,
            "description": "Child and toys"
        }
    ]
}
```
{{< /code-block >}}

{{< description >}}
## Categories
Returns a list of website categories.
{{% /description %}}