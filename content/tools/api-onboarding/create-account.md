---
title : Create a Merchant Account
layout : single
tags : hidden
---

## Introduction

Use the following requests to perform actions on new or existing Merchants Accounts affiliated to your Partner Account:
1. [Signup account](#signup-account): Create a new Merchant Account
2. [List accounts](#list-accounts): Retrieve a list of all Merchant Account
3. [Get account](#get-account): Retrieve a single Merchant Account
4. [Update account](#update-account): Update a Merchant Account

## Authentication
All four account requests require a Partner Account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

## Requests


### Signup account

`POST` `https://testapi.multisafepay.com/v1/json/signup-account`

Create a new affiliated Merchant Account.


**Parameters**
|Key|Description|
|-----|------|
|**account**{{< br >}}`object`|This object holds company information|
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
|contact_person.email{{< br >}}`string`|Email address of company contact person{{< br >}}**Format**: ??? . Required.|
|currencies{{< br >}}`array`|List of currencies (company wishes to accept? company currently has bank accounts in?){{< br >}}**Format**: array of strings in [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `[EUR,USD]`). Required.|

**Request**
```
curl -X POST "https://testapi.multisafepay.com/v1/json/signup-account" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-account-API-key>" \
-d " \
{
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
_Escape characters in the JSON body are omitted to improve readability._

**Response**
```
poop
```

### List accounts

`GET` `https://api.multisafepay.com/v1/json/accounts`

Retrieve an array of all Merchant Accounts affiliated to the Partner Account.

**Parameters**  
This request doesn't require any parameters.

**Request**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< br >}}
**Response**
```
{
  "data": [
    {
      "address1": "Flowerstreet 123",
      "address2": "",
      "address3": "",
      "apartment": "5A",
      "city": "Funtown",
      "coc_number": "123456",
      "company_name": "Fun B.V.",
      "country": "NL",
      "email": "info@funcompany.com",
      "fax": "00311234567890",
      "phone": "00311234567890",
      "vat_number": "NL999999999B99",
      "zipcode": "1234 ZP"
    }
  ],
  "success": true
}
```

{{< br >}}

### Get account

|Parameter|Description|
|-----|------|
|


### Update account

|Parameter|Description|
|-----|------|
|
Parameters



## Next steps
Now that you have created a Merchant Account, bank accounts, UBOs and websites can be added, using the unique Merchant Account `id` .

{{< two-buttons

href-1="/tools/api-onboarding" header-1="Overview" text-1="Read introduction" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-bank-account" header-2="Next" text-2="Add bank accounts " img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
