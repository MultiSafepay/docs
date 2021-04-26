---
title : Add UBOs
layout : single
tags : hidden
---

## Introduction

Use the following requests to add, retrieve or update [Ultimate Beneficial Owner](/faq/getting-started/guidance-notes-ultimate-beneficial-owner-form/) (UBO) details linked to a merchant account affiliated with your partner account:

1. [Create a UBO](#create-a-ubo): Add a UBO to a merchant account.
2. [List UBOs](#list-ubos): Retrieve all UBOs for a merchant account.
3. [Get UBO](#get-a-ubo): Retrieve a single UBO by its identifier.
4. [Update UBO](#update-a-ubo): Update a UBO.
5. [Add identity document](#add-identity-document): Add an identity document to an existing UBO.
6. [List identity documents](#list-identity-documents): Retrieve all identity documents for a UBO.
7. [Get identity document](#get-identity-document): Retrieve a single identity document for a UBO.

### The process
The requests above can be divided into the following steps:

1. **Add UBOs**: Use the first four requests to add, retrieve and update UBOs linked to a merchant account.
2. **Add identity documents**: Use the last three requests to add and retrieve identity documents of UBOs linked to a merchant account. These documents are used to perform our UBO verification.

### About parameters
For every parameter, we specify whether it's _required_ or _optional_. However, this label refers only to the technical requirements for valid API requests. To perform our UBO verification, we may need _optional_ parameters to be supplied.

## Authentication
All seven UBO requests require a partner account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain in the URL from `testapi` to `api` and use the corresponding API key.

---

## Create a UBO

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/` 

Add a new UBO to a merchant account.

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|---|---|
|name {{< br >}}`string`|UBO's full name.{{< br >}}**Format**: max 200 characters. Required.|
|title {{< br >}}`string`|UBO's title.{{< br >}}**Options**: `mr` or `mrs`. Required.|
|address {{< br >}}`string`|UBO's address. {{< br >}}**Format**: max 100 characters. Optional.|
|address_apartment {{< br >}}`string`|UBO's apartment number. {{< br >}}**Format**: max 15 characters. Optional.|
|city {{< br >}}`string`|UBO's city of residence.{{< br >}}**Format**: max 100 characters. Optional.|
|state {{< br >}}`string`|UBO's province or state of residence. {{< br >}}**Format**: max 100 characters. Optional.|
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
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-account-API-key>" \
-d " \
{
  "name": "Firstname Lastname",
  "title": "mrs",
  "address": "Mainstreet 123",
  "address_apartment": "",
  "city": "Funtown",
  "state": "Noord-Holland",
  "country": "NL",
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
    "account_id": 12345678,
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "email@address.com",
    "fax": "0123456789",
    "id": "glmqo15bces6n",
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
`id` → the unique identifier of the UBO
{{< /collapse >}}

---

## List UBOs

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/ubos`

Retrieve an array of all UBOs linked to a merchant account.

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/12345678/ubos" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "account_id": 12345678,
      "address": "Mainstreet 123",
      "address_apartment": "",
      "birthday": "1980-01-31",
      "city": "Funtown",
      "country": "NL",
      "country_of_birth": "NL",
      "email": "email@address.com",
      "fax": "0123456789",
      "id": "glmqo15bces6n",
      "job_title": "CEO",
      "mobile_phone": "0123456789",
      "name": "Firstname Lastname",
      "office_phone": "0123456789",
      "percentage": 100,
      "state": "Noord-Holland",
      "title": "mrs",
      "type": "control_rights",
      "zipcode": "1234 ZP"
    }
  ],
  "page": {
    "total": 1
  },
  "success": true
}
```
`id` → the unique identifier of the UBO
{{< /collapse >}}

---

## Get a UBO

`GET` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}`

Retrieve a single UBO by its identifier.

### Path parameters
|Key|Description|
|---|---|
|ubo_id{{< br >}} `string` | The unique identifier of a UBO. {{< br >}} **Tip**: The ubo_id is returned as `id` in the [create a UBO](#create-a-ubo), [list UBOs](#list-ubos), and [get a UBO](#get-a-ubo) request. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/ubos/glmqo15bces6m" \
-H "accept: application/json" \
-H "Authorization: Bearer <your-api-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": 12345678,
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "email@address.com",
    "fax": "0123456789",
    "id": "glmqo15bces6n",
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
`id` → the unique identifier of the UBO
{{< /collapse >}}

---

## Update a UBO

`PATCH` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}`

Update information about an existing UBO.

### Path parameters
|Key|Description|
|---|---|
|ubo_id{{< br >}} `string` | The unique identifier of a UBO. {{< br >}} **Tip**: The ubo_id is returned as `id` in the [create a UBO](#create-a-ubo), [list UBOs](#list-ubos), and [get a UBO](#get-a-ubo) request. |

### Query parameters
|Key|Description|
|---|---|
|name {{< br >}}`string`|UBO's full name.{{< br >}}**Format**: max 200 characters. Optional.|
|title {{< br >}}`string`|UBO's title.{{< br >}}**Options**: `mr` or `mrs`. Optional.|
|address {{< br >}}`string`|UBO's address. {{< br >}}**Format**: max 100 characters. Optional.|
|address_apartment {{< br >}}`string`|UBO's apartment number. {{< br >}}**Format**: max 15 characters. Optional.|
|city {{< br >}}`string`|UBO's city of residence.{{< br >}}**Format**: max 100 characters. Optional.|
|state {{< br >}}`string`|UBO's province or state of residence. {{< br >}}**Format**: max 100 characters. Optional.|
|country {{< br >}}`string`|UBO's country of residence.{{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Optional.|
|zipcode {{< br >}}`string`|UBO's zip code.{{< br >}}**Format**: max 20 characters. Optional.|
|birthday {{< br >}}`string`|UBO's date of birth. {{< br >}}**Format**: yyyy-mm-dd (e.g., `1980-01-31`). Optional.|
|country_of_birth {{< br >}}`string`|UBO's country of birth.{{< br >}}**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Optional.|
|email {{< br >}}`string`|UBO's email address.{{< br >}}**Format**: max 100 characters. Optional.|
|mobile_phone {{< br >}}`string`|UBO's mobile phone number.{{< br >}}**Format**: max 25 characters. Optional.|
|office_phone {{< br >}}`string`|UBO's office phone number.{{< br >}}**Format**: max 25 characters. Optional.|
|fax {{< br >}}`string`|UBO's fax number.{{< br >}}**Format**: max 15 characters. Optional.|
|job_title {{< br >}}`string`|UBO's job title.{{< br >}}**Format**: max 100 characters. Optional.|
|percentage {{< br >}}`integer`|UBO's percentage of equity.{{< br >}}**Format**: non-fractional number from `25` to `100`. Optional.|
|type {{< br >}}`string`|UBO's type of equity.{{< br >}}**Options**: `control_rights`, `shareholder`, `voting_rights` or `other`. Optional.|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/ubos/glmqo15bces6n" \
-H "accept: application/json" \
-H "Authorization: Bearer <your-api-key>" \
-H "Content-Type: application/json" \
-d " \
{
  "email": "newemail@address.com" 
}
"
```
_Escape characters in the JSON body are omitted to improve readability._
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": 12345678,
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "newemail@address.com",
    "fax": "0123456789",
    "id": "glmqo15bces6n",
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

## Add identity document

`POST` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs`

Upload an identity document used to verify the UBO.

### Path parameters
|Key|Description|
|---|---|
|ubo_id{{< br >}} `string` | The unique identifier of a UBO. {{< br >}} **Tip**: The ubo_id is returned as `id` in the [create a UBO](#create-a-ubo), [list UBOs](#list-ubos), and [get a UBO](#get-a-ubo) request. |

### Query parameters
|Key|Description|
|---|---|
|document_type{{< br >}}`string`|The type of identity document. {{< br >}}**Options**: `id`, `passport`, `driverslicense`, `proof_of_address`|
|encoded_content{{< br >}}`string`|Base64 encoded content. Required.|
|filename{{< br >}}`string`|Name of the identity document file. {{< br >}}**Format**: max 250 characters. Required. |
|mime_type{{< br >}} `string`|Media type of the identity document file.{{< br >}}**Options**: `application/pdf`,`image/jpeg`|

{{< collapse title="Sample request" size="h3" >}}
```

curl -X POST "https://testapi.multisafepay.com/v1/json/ubos/glmqo15bces6n/identitydocs" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your-api-key>" \
-d "
{
  "document_type":"id",
  "encoded_content":"string",
  "filename":"identity-of-ubo.pdf",
  "mime_type":"application/pdf"
}
"
```
_Escape characters in the JSON body are omitted to improve readability._
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "document_type": "id",
    "filename": "identity-of-ubo.pdf",
    "id": "agi6ehoreex6a",
    "merchant_id": 12345678,
    "mime_type": "application/pdf",
    "ubo_id": "glmqo15bces6n"
  },
  "success": true
}
```
`id` → the unique identifier of the identity document
{{< /collapse >}}

---

## List identity documents

`GET` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs`

Retrieve an array of all identity documents linked to a UBO.

### Path parameters
|Key|Description|
|---|---|
|ubo_id{{< br >}} `string` | The unique identifier of a UBO. {{< br >}} **Tip**: The ubo_id is returned as `id` in the [create a UBO](#create-a-ubo), [list UBOs](#list-ubos), and [get a UBO](#get-a-ubo) request. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/ubos/glmqo15bces6n/identitydocs" \
-H "accept: application/json" \
-H "Authorization: Bearer <your-api-key>"
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "document_type": "identity",
      "filename": "identity-of-ubo.pdf",
      "id": "agi6ehoreex6a",
      "merchant_id": 12345678,
      "mime_type": "application/pdf",
      "ubo_id": "glmqo15bces6n"
    }
  ],
  "page": {
    "total": 1
  },
  "success": true
}
```
`id` → the unique identifier of the identity document
{{< /collapse >}}

---

## Get identity document

`GET` `https://testapi.multisafepay.com/v1/json/identitydocs/{identitydoc_id}`

Description.

### Path parameters
|Key|Description|
|---|---|
|identitydoc_id{{< br >}}`string`|The unique identifier of the identity document.{{< br >}}**Tip**: The identitydoc_id is returned as `id` in the [add identity document](#add-identity-document) and [list identity documents](#list-identity-documents) request. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET https://testapi.multisafepay.com/v1/json/identitydocs/agi6ehoreex6a
-H  "accept: application/json" \
-H  "Authorization: Bearer <your-api-key>
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "document_type": "identity",
    "filename": "identity-of-ubo.pdf",
    "id": "agi6ehoreex6a",
    "merchant_id": 11979097,
    "mime_type": "application/pdf",
    "ubo_id": "glmqo15bces6n"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Next steps
Now that you have created a Merchant account and added one or multiple bank account and UBOs, complete the onboarding by adding one or multiple websites using the unique Merchant account `id` .

{{< two-buttons

href-1="/tools/api-onboarding/add-bank-accounts" header-1="Previous" text-1="Add bank accounts" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 
href-2="/tools/api-onboarding/add-websites" header-2="Next" text-2="Add websites" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
