---
weight: 520
meta_title: "API - Chargeback - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders/{order_id}/files

```shell
{
    "type": "",
    "base64": "",
    "description": "",
    "name": ""
}
```

> JSON Response

```shell
{
    "success": true,
    "data": {
    }
}
```
{{< /code-block >}}

{{< description >}}
## Chargeback

MultiSafepay can challenge the chargeback on your behalf, but to do so, we need documented proof of the order.
Upload files / documents via an API request.

_We will be changing the process for handling chargebacks through the API in Q3 2019. Please contact your account manager or contact us at <integration@multisafepay.com> for more information_.

Read more about [chargebacks](/faq/chargebacks/) on our documentation page.

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| type                        | string  | Specifies the payment flow for the checkout process. Options: chargeback. |
| base64                      | string  | Binary Base 64 encoded. Upload images "pdf, jpeg and png". |
| description                 | string  | Description or comments of the submitted file. |
| name                        | string  | Name of the file.
{{% /description %}}


