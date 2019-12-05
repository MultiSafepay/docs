---
weight: 120
meta_title: "API - Retrieve a gateway - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
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
{{% /code %}}

{{% description %}}
## Retrieve a gateway
| Parameter           | Type   | Description                                                                                             |
|---------------------|--------|---------------------------------------------------------------------------------------------------------|
| id                  | string | The unique identifier of the gateway to be returned.                                                    |

{{% /description %}}