---
weight: 520
meta_title: "API - Chargeback - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
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
{{% /code %}}

{{% description %}}
## Chargeback

MultiSafepay can challenge the chargeback on your behalf, but to do so, we need documented proof of the order.
Upload files / documents via an API request.

_We will be changing the process for handling chargebacks through the API in Q3 2019. Please contact your account manager or contact us at <integration@multisafepay.com> for more information_.

For more information about chargebacks, please refer to our [dedicated page](/payment-methods/creditcards/what-is-a-chargeback/).

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| type                        | string  | Specifies the payment flow for the checkout process. Options: chargeback. |
| base64                      | string  | Binary Base 64 encoded. Upload images "pdf, jpeg and png". |
| description                 | string  | Description or comments of the submitted file. |
| name                        | string  | Name of the file.
{{% /description %}}


