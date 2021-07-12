---
title : Create a merchant account
layout : single
tags : hidden
aliases: 
    - /tools/api-onboarding/create-account
---

Use the following requests to create, retrieve or update merchant accounts affiliated to your partner account:

1. [Signup account](#signup-account): create a new merchant account
2. [List accounts](#list-accounts): retrieve a list of all merchant accounts
3. [Get account](#get-account): retrieve a single merchant account
4. [Update account](#update-account): update a merchant account

### About parameters
For every parameter, we specify whether it's _required_ or _optional_. However, this label refers only to the technical requirements for valid API requests. To perform our know your customer checks, we may need _optional_ parameters to be supplied.

## Authentication
All four account requests require a partner account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the corresponding API key.

---

## Signup account

`POST` `https://testapi.multisafepay.com/v1/json/signup-account`

Create a new affiliated merchant account.

### Query parameters
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
|contact_person.name{{< br >}}`string`|Name of company contact person{{< br >}}**Format**:  . Required.|
|contact_person.password{{< br >}}`string`|Set a password for the company contact person's account. Required.|
|contact_person.title{{< br >}}`string`|Title of company contact person{{< br >}}**Options**: `mr`, `ms`, `mrs`. Required.|
|currencies{{< br >}}`array`|List of currencies the company wishes to process{{< br >}}**Format**: array of strings in [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `[EUR,USD]`). Required.|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/signup-account" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--header "api_key: <your-account-api-key>" \
--data-raw '{
  "account": {
    "address1": "Flowerstreet 123",
    "address2": "",
    "address3": "",
    "apartment": "5A",
    "city": "Amsterdam",
    "coc_number": "123456",
    "company_name": "Fun B.V.",
    "country": "NL",
    "email": "info@funcompany.com",
    "fax": "00311234567890",
    "phone": "00311234567890",
    "vat_number": "NL999999999B99",
    "zipcode": "1234 ZP"
  },
  "contact_person": {
    "name": "Contact Person",
    "password": "password",
    "title": "mr"
  },
  "currencies": [
    "EUR"
  ]
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account": {
      "address1": "Flowerstreet 123",
      "address2": "",
      "address3": "",
      "apartment": "5A",
      "city": "Amsterdam",
      "coc_number": "123456",
      "company_name": "Fun B.V.",
      "country": "NL",
      "email": "info@funcompany.com",
      "fax": "00311234567890",
      "id": 12345678,
      "phone": "00311234567890",
      "vat_number": "NL999999999B99",
      "zipcode": "1234 ZP"
    },
    "contact_person": {
      "id": 123456,
      "name": "Contact Person",
      "password": "***",
      "title": "mr"
    },
    "currencies": [
      "EUR"
    ]
  },
  "success": true
}
```
`account.id` → the account ID
`contact_person.id` → the contact person ID
{{< /collapse >}}

---
 
## List accounts

`GET` `https://testapi.multisafepay.com/v1/json/accounts`

Retrieve an array of all merchant accounts affiliated to your partner account.

### Parameters
This request doesn't require any parameters.

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts" \
--header "accept: application/json" \
--header "api_key: <your-account-api-key>"
```
{{< br >}}
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
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
	  "id": "12345678",
      "phone": "00311234567890",
      "vat_number": "NL999999999B99",
      "zipcode": "1234 ZP"
    }
  ],
  "success": true
}
```
`account.id` → the account ID
{{< /collapse >}}

---

## Get account

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}`

Retrieve the account details of a specific affiliated merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.


{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/12345678" \
--header "accept: application/json" \
--header "api_key: <your-account-api-key>"
```
{{< br >}}
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
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
	"id": "12345678",
    "phone": "00311234567890",
    "vat_number": "NL999999999B99",
    "zipcode": "1234 ZP"
  },
  "success": true
}
```
`id` → the account ID
{{< /collapse >}}

---

## Update account

`PATCH` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}`

Update the account details of an affiliated merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|-----|------|
|address1{{< br >}}`string`|First line of company address {{< br >}}**Format**: max 64 characters. Optional.|
|address2{{< br >}}`string`|Second line of company address{{< br >}}**Format**: max 64 characters. Optional.|
|address3{{< br >}}`string`|Third line of company address {{< br >}}**Format**: max 64 characters. Optional.|
|apartment{{< br >}}`string`|Apartment number of company address{{< br >}}**Format**: max 9 characters. Optional.|
|city{{< br >}}`string`|City of company address{{< br >}}**Format**: max 50 characters Optional.|
|coc_number{{< br >}}`string`|Chamber of commerce number {{< br >}}**Format**: max 50 characters. Optional.|
|company_name{{< br >}}`string`|Name of company {{< br >}}**Format**: max 200 characters. Optional.|
|country{{< br >}}`string`|Country code of company {{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Optional.|
|email{{< br >}}`string`|Company email address {{< br >}}**Format**: max 100 characters. Optional.|
|fax{{< br >}}`string`|Company fax number{{< br >}}**Format**: max 15 characters. Optional.|
|phone{{< br >}}`string`|Company phone number{{< br >}}**Format**: max 15 characters. Optional.|
|vat_number{{< br >}}`string`|Company VAT number{{< br >}}**Format**: max 50 characters. Optional.|
|zipcode{{< br >}}`string`|Company ZIP Code{{< br >}}**Format**: max 30 characters. Optional.|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/accounts/12345678" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--header "api_key: <your-account-api-key>" \
--data-raw '{
  "email" :"newemail@funcompany.com",
  "zipcode" :"5678 NW"
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "address1": "Flowerstreet 123",
    "address2": "",
    "address3": "",
    "apartment": "5A",
    "city": "Funtown",
    "coc_number": "123456",
    "company_name": "Fun B.V.",
    "country": "NL",
    "email": "newemail@funcompany.com",
    "fax": "00311234567890",
	"id": "12345678",
    "phone": "00311234567890",
    "vat_number": "NL999999999B99",
    "zipcode": "5678 NW"
  },
  "success": true
}
```
`id` → the account ID
{{< /collapse >}}

---

## Next steps
You have successfully created a merchant account. Now, you can add bank accounts, UBOs, and websites, using the unique merchant account ID.

{{< two-buttons

href-1="/tools/api-onboarding" header-1="Overview" text-1="Read introduction" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-bank-accounts" header-2="Next" text-2="Add bank accounts " img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
