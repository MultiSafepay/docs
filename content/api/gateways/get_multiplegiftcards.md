---
weight: 125
meta_title: "API - Gateway - Multiple gift cards - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> GET - /gateways?include=coupons


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


**Parameter**

----------------

__include=coupons__ | string

Specify comma delimited additional payment method types.

----------------



Adding the __coupons__ value to your GET request will **include** all your webshop's available gift cards in the response. See the response example on the side.

If the parameter __include=coupons__ is not added in the retrieve gateway request, only one coupon will be displayed in the response.
{{% /description %}}