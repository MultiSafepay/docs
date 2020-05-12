---
weight: 125
meta_title: "API - Gateway - Multiple gift cards - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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
## Retrieve gateways - Multiple available gift cards
| Parameter           | Type   | Description |
|---------------------|--------|-------------|
| include=coupons            | string | Specify comma delimited additional payment method types. |

Adding the ```coupons``` value to your GET request will **include** all your webshop's available gift cards in the response. See the response example on the side.

If the parameter ```ìnclude=coupons``` is not added in the retrieve gateway request, only one coupon will be displayed in the response.
{{% /description %}}