---
weight: 125
meta_title: "API - Gateway - Multiple gift cards - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
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