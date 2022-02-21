---
weight: 110
meta_title: "API Reference - Retrieve activated gateways - MultiSafepay Docs"

---
{{< code-block >}}

> GET - /gateways

> JSON response

```json
{
  "success": true,
  "data":[
    {
      "id": "VISA",
      "description": "Visa"
    },
    {
      "id": "IDEAL",
      "description": "iDEAL"
    }
  ]
}
```
{{< /code-block >}}

{{< description >}}

## Retrieve activated gateways

Retrieve all activated gateways.

**Parameters**

----------------
`include` | string | optional | query parameter

By default, only one activated gift card is included in the response.

To include all activated [gift cards](/api/#gift-cards) in the response, specify `coupons`.

**Options**: `coupons`

----------------
`country` | string | optional | query parameter

The customer’s country code.  
Format: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. 

----------------
`currency` | string | optional | query parameter

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`amount` | integer | optional | query parameter

The amount the customer needs to pay in the currency's smallest unit:  

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10 

----------------

{{% /description %}}