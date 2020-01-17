---
weight: 125
meta_title: "API - Gateway - Multiple giftcards - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

> GET - /json/gateways?include=coupons


> JSON Response

```shell
{
    "success": true,
    "data": [
        {
            "id": "MASTERCARD",
            "description": "MasterCard"
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
        {
            "id": "VVVBON",
            "description": "vvvbon",
            "type": "coupon"
        },
        {
            "id": "FASHIONCHQ",
            "description": "fashioncheque",
            "type": "coupon"
        }
    ]
}

``` 
{{< /code-block >}}

{{< description >}}
## Retrieve gateways - Multiple available giftcards
| Parameter           | Type   | Description |
|---------------------|--------|-------------|
| include=coupons            | string | Specify comma delimited additional payment method types. |

Adding the ```coupons``` value to your GET request will **include** all your webshop's available giftcards in the response. See the response example on the side.

If the parameter ```ìnclude=coupons``` is not added in the retrieve gateway request, only one coupon will be displayed in the response.
{{% /description %}}