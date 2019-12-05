---
weight: 510
meta_title: "API - Categories - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
> GET - /categories

<br>

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
{{% /code %}}

{{% description %}}
## Categories
Returns a list of website categories.
{{% /description %}}