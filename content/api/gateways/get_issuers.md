---
weight: 130
meta_title: "API - Gateway issuers - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{% code %}}

> GET - /issuers/ideal

<br>

> JSON Response

```shell
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
      "code": "4371",
      "description": "Bunq"
    },
    {
      "code": "1234",
      "description": "Moneyou"
    },
    {
      "code": "1235",
      "description": "Handelsbanken"
    }
  ]
}

```
{{% /code %}}

{{% description %}}
## Gateway Issuers
| Parameter         | Type   | Description                                                                                             |
|-------------------|--------|---------------------------------------------------------------------------------------------------------|
| id                | string | The unique identifier of the payment gateway to retrieve an issuer list for. Currently supported identifiers are: [iDEAL](#ideal-issuers) |

Direct iDEAL Transactions can have the following Issuers:

| IssuerID | Bank                  |
|----------|-----------------------|
| 0031     | ABN AMRO              |
| 0761     | ASN Bank              |
| 4371     | bunq                  |
| 1235     | Handelsbanken         |
| 0721     | ING                   |
| 0801     | Knab                  |
| 1234     | Moneyou               |
| 0021     | Rabobank              |
| 0771     | Regio Bank            |
| 0751     | SNS Bank              |
| 0511     | Triodos Bank          |
| 0161     | Van Lanschot Bankiers |
{{% /description %}}

