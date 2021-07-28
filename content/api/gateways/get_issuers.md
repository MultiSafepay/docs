---
weight: 130
meta_title: "API Reference - Retrieve gateway issuers - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> GET - /issuers{gateway}

> JSON Response


```json
{
  "success": true,
  "data": [
    {
      "code": "0031",
      "description": "ABN AMRO"
    },
    {
      "code": "0751",
      "description": "SNS Bank"
    },
    {
      "code": "0721",
      "description": "ING"
    },
    {
      "code": "0021",
      "description": "Rabobank"
    },
    {
      "code": "0761",
      "description": "ASN Bank"
    },
    {
      "code": "0771",
      "description": "Regio Bank"
    },
    {
      "code": "0511",
      "description": "Triodos Bank"
    },
    {
      "code": "0161",
      "description": "Van Lanschot Bankiers"
    },
    {
      "code": "0801",
      "description": "Knab"
    },
    {
      "code": "1099",
      "description": "Revolut"
    },
    {
      "code": "4371",
      "description": "Bunq"
    },
    {
      "code": "1235",
      "description": "Handelsbanken"
    }
  ]
}

```
{{< /code-block >}}

{{< description >}}
## Retrieve gateway issuers

**Parameters**

----------------

__code__ | string

The unique identifier of the payment gateway you want to retrieve a list of issuers for.  
Supported identifiers: [iDEAL](#ideal-issuers) 

----------------

Possible issuers for `direct` iDEAL transactions:

| IssuerID | Bank                  |
|----------|-----------------------|
| 0031     | ABN AMRO              |
| 0761     | ASN Bank              |
| 4371     | bunq                  |
| 1235     | Handelsbanken         |
| 0721     | ING                   |
| 0801     | Knab                  |
| 0021     | Rabobank              |
| 0771     | Regio Bank            |
| 1099     | Revolut               |
| 0751     | SNS Bank              |
| 0511     | Triodos Bank          |
| 0161     | Van Lanschot Bankiers |

{{% /description %}}

