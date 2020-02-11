---
weight: 110
meta_title: "API - Retrieve all gateways - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> GET - /gateways

> JSON Response

```shell
{
  "success": true,
  "data": [
    {
      "id": "MASTERCARD",
      "description": "Mastercard"
    },
    {
      "id": "VISA",
      "description": "Visa"
    },
    {
      "id": "AMEX",
      "description": "AMEX",
    }, 
  ]
}
```
{{< /code-block >}}

{{< description >}}

{{% /description %}}