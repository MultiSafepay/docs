---
title : Add UBOs
layout : single
tags : hidden
---

## Introduction

Use the following requests to add, retrieve or update [Ultimate Beneficial Owner](/faq/getting-started/guidance-notes-ultimate-beneficial-owner-form/) (UBO) details to a Merchant Accounts affiliated to your Partner Account:
1. **[Create UBO](#create-ubo)**: create a new UBO
2. **[List UBOs](#list-ubos)**: retrieve a list of all UBOs
3. **[Get UBO](#get-a-ubo)**: retrieve a single UBO
4. **[Update UBO](#update-a-ubo)**: update a UBO
5. **[Add identity document](#add-identity-document)**: add identity document to an existing UBO
6. **[Get identity document](#add-identity-document)**: retrieve a single identity document of a UBO
7. **[List identity documents](#list-identity-documents)**: retrieve a list of all identity documents of a UBO

### The process
The requests above can be split into two steps:
1. **Add UBOs**: Use the first four requests to add, retrieve and update UBOs associated to a Merchant Account.
1. **Add identity documents**: Use the last three requests to add and retrieve identity documents of UBOs associated to a Merchant Account.

### About required parameters
For every parameter, we specify whether it's required or optional. However, these statements refer only to the technical requirements to make a valed API request. In order to verify the UBO, we might require optional parameters to be supplied.

## Authentication
All seven UBO requests require a Partner Account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the according API key.

---

## Create a UBO

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/` 

Add a new UBO to a Merchant Account

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|---|---|
|name {{< br >}}`string`|UBO's full name.{{< br >}}**Format**: max 200 characters. Required.|
|title {{< br >}}`string`|UBOs title.{{< br >}}**Options**: `mr` or `mrs`. Required.|
|address {{< br >}}`string`|UBO's address. {{< br >}}**Format**: max 100 characters. Optional.|
|address_apartment {{< br >}}`string`|UBO's apartment number. {{< br >}}**Format**: max 15 characters. Optional.|
|city {{< br >}}`string`|UBO's city of residence.{{< br >}}**Format**: max 100 characters. Optional.|
|state {{< br >}}`string`|???{{< br >}}**Format**: max 25 characters. Optional.|
|country {{< br >}}`string`|UBO's country of residence.{{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Required.|
|zipcode {{< br >}}`string`|UBO's zip code.{{< br >}}**Format**: max 20 characters. Optional.|
|birthday {{< br >}}`string`|UBO's date of birth. {{< br >}}**Format**: yyyy-mm-dd (e.g., `1980-01-31`). Required.|
|country_of_birth {{< br >}}`string`|UBO's country of birth.{{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Required.|
|email {{< br >}}`string`|UBO's email address.{{< br >}}**Format**: max 100 characters. Required.|
|mobile_phone {{< br >}}`string`|UBO's mobile phone number.{{< br >}}**Format**: max 25 characters. Optional.|
|office_phone {{< br >}}`string`|UBO's office phone number.{{< br >}}**Format**: max 25 characters. Optional.|
|fax {{< br >}}`string`|UBO's fax number.{{< br >}}**Format**: max 15 characters. Optional.|
|job_title {{< br >}}`string`|UBO's job title.{{< br >}}**Format**: max 100 characters. Required.|
|percentage {{< br >}}`integer`|UBO's percentage of equity.{{< br >}}**Format**: non-fractional number from `25` to `100`. Required.|
|type {{< br >}}`string`|UBO's type of equity.{{< br >}}**Options**: `control_rights`, `shareholder`, `voting_rights` or `other`. Required.|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/accounts/12345678/ubos" \
-H  "accept: application/json" \
-H  "Content-Type: application/json" \
-d " \
{
  "name": "Firstname Lastname",
  "title": "mrs",
  "address": "Mainstreet 123",
  "address_apartment": "",
  "city": "Funtown",
  "state": "Noord-Holland",
  "country": "the Netherlands",
  "zipcode": "1234 ZP"
  "birthday": "1980-01-31",
  "country_of_birth": "the Netherlands",
  "email": "email@address.com",
  "mobile_phone": "0123456789",
  "office_phone": "0123456789",
  "fax": "0123456789",
  "job_title": "CEO",
  "percentage": 100,
  "type": "control_rights",
}
"
```
_Escape characters in the JSON body are omitted to improve readability._
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "the Netherlands",
    "country_of_birth": "the Netherlands",
    "email": "email@address.com",
    "fax": "0123456789",
    "job_title": "CEO",
    "mobile_phone": "0123456789",
    "name": "Firstname Lastname",
    "office_phone": "0123456789",
    "percentage": 100,
    "state": "Noord-Holland",
    "title": "mrs",
    "type": "control_rights",
    "zipcode": "1234 ZP"
  },
  "success": true
}
```
{{< /collapse >}}

---

## List UBOs

`METHOD` `URL`

Short description.

### Path parameters
|Key|Description|
|---|---|
|||

### Query parameters
|Key|Description|
|---|---|
|||

{{< collapse title="Sample request" size="h3" >}}
```
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
```
{{< /collapse >}}

---

## Get a UBO

`METHOD` `URL`

Short description.

### Path parameters
|Key|Description|
|---|---|
|||

### Query parameters
|Key|Description|
|---|---|
|||

{{< collapse title="Sample request" size="h3" >}}
```
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
```
{{< /collapse >}}

---

## Update a UBO

`METHOD` `URL`

Short description.

### Path parameters
|Key|Description|
|---|---|
|||

### Query parameters
|Key|Description|
|---|---|
|||

{{< collapse title="Sample request" size="h3" >}}
```
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
```
{{< /collapse >}}

---

## Next steps
Now that you have created a Merchant Account and added one or multiple bank account and UBOs, complete the onboarding by adding one or multiple websites, using the unique Merchant Account `id` .

{{< two-buttons

href-1="/tools/api-onboarding/add-bank-account" header-1="Previous" text-1="Add bank accounts" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-website" header-2="Next" text-2="Add websites" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
