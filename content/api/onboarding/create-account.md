---
weight: 40
meta_title: "API - Add an account - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> /signup-account

```shell

curl -X POST "https://testapi.multisafepay.com/v1/json/signup-account"
-H  "accept: application/json"
-H  "Content-Type: application/json"
-H "Authentication: Bearer <your-account-API-key>"
-d "{
        "account": {
                "address1" :"Flowerstreet 123",
                "address2" :"",
                "address3" :"",
                "apartment" :"5A",
                "city" :"Amsterdam",
                "coc_number" :"123456",
                "company_name" :"Fun B.V.",
                "country" :"NL",
                "email" :"info@funcompany.com",
                "fax" :"00311234567890",
                "phone" :"00311234567890",
                "vat_number" :"NL999999999B99",
                "zipcode" :"1234 ZP"
                },
        "contact_person" :{
                "name" :"string",
                "password" :"string",
                "title" :"mr"
                },
        "currencies" : [
                "EUR"
        ]
}"
```

{{< /code-block >}}

{{< description >}}

`POST` `https://testapi.multisafepay.com/v1/json/signup-account`

Create a new affiliated Merchant Account.


**Parameters**
|Key|Description|
|-----|------|
|**account** {{< br >}} `object`|This object holds company information|
|account.address1{{< br >}}`string`|First line of company address {{< br >}}**Format**: max 64 characters. Optional.|
|account.address2{{< br >}}`string`|Second line of company address{{< br >}}**Format**: max 64 characters. Optional.|
|account.address3{{< br >}}`string`|Third line of company address {{< br >}}**Format**: max 64 characters. Optional.|
|account.apartment{{< br >}}`string`|Apartment number of company address{{< br >}}**Format**: max 9 characters. Optional.|
|account.city{{< br >}}`string`|City of company address{{< br >}}**Format**: max 50 characters Optional.|
|account.coc_number{{< br >}}`string`|Chamber of commerce number {{< br >}}**Format**: max 50 characters. Optional.|
|account.company_name{{< br >}}`string`|Name of company {{< br >}}**Format**: max 200 characters. Required.|
|account.country{{< br >}}`string`|Country code of company {{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Required.|
|account.email{{< br >}}`string`|Company email address {{< br >}}**Format**: max 100 characters. Required.|
|account.fax{{< br >}}`string`|Company fax number{{< br >}}**Format**: max 15 characters. Optional.|
|account.phone{{< br >}}`string`|Company phone number{{< br >}}**Format**: max 15 characters. Optional.|
|account.vat_number{{< br >}}`string`|Company VAT number{{< br >}}**Format**: max 50 characters. Optional.|
|account.zipcode{{< br >}}`string`|Company ZIP Code{{< br >}}**Format**: max 30 characters. Optional.|
|**contact_person**{{< br >}}`object`|This object holds contact person information|
|contact_person.name{{< br >}}`string`|Name of company contact person{{< br >}}**Format**: ??? . Required.|
|contact_person.password{{< br >}}`string`|Password of company contact person{{< br >}} **Format**: ??? . Required.|
|contact_person.email{{< br >}}`string`|Email address of company contact person. This email address can be used to sign into MultiSafepay Control. However, more Users can be [added to the Merchant Account at a later time](/tools/multisafepay-control/users/){{< br >}}**Format**: ??? . Required.|
|currencies{{< br >}}`array`|List of currencies (company wishes to accept? company currently has bank accounts in?){{< br >}}**Format**: array of strings in [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `[EUR,USD]`). Required.|

{{< /description >}}
