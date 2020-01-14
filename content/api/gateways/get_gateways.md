---
weight: 110
meta_title: "API - Retrieve all gateways - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
> GET - /gateways?country={country}&currency={currency}&amount={amount}&include={include}

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
      "id": "FASHIONGFT",
      "description": "fashiongiftcard",
      "type": "coupon"
    }, 
  ]
}
```
{{% /code %}}

{{% description %}}
_October 2019: There have been reports of faulty functionality of this feature. If you encounter any issues or need assistance on this matter, do not hesitate to contact our Integration Team at <integration@multisafepay.com>_

| Parameter           | Type   | Description |
|---------------------|--------|-------------|
| country             | string | Specify an [ISO-3166-1](https://www.iso.org/iso-3166-country-codes.html) country code to filter out payment gateways that are not applicable for the specified country. This can be used to simplify the list of payment options presented to the customer by removing payment methods specific to other countries e.g. Giropay or iDEAL. |
| currency            | string | Specify an [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) currency code to filter out payment gateways that are not applicable for the specified currency. This can be used to simplify the list of payment options presented to the customer by only displaying payment methods supported by the transaction currency. e.g. Credit Cards. |
| amount              | string | Specify the transaction amount (in cents) to filter out payment gateways that are not applicable for that amount. This is commonly used to exclude Pay After Delivery as a payment option for very small, or large, amounts but can also be configured to exclude other payment methods. |
| include             | string | Specify comma delimited additional payment method types. Options: coupons. |

{{% note %}}
Note that if you support multiple giftcards for your webshop, you should refer to _**[Retrieve gateways - Multiple available giftcards](#retrieve-gateways-multiple-available-giftcards)**_ for more information on how to correctly retrieve ALL of them. Otherwise, only the first available giftcard will be shown.
{{% /note %}}
{{% /description %}}