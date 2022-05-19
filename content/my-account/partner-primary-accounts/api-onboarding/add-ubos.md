---
title : Add UBOs
layout : single
url: '/api-onboarding/add-ubos/'
aliases: 
    - /tools/api-onboarding/add-ubos
---

Use the following requests to add, retrieve or update [ultimate beneficial owner](/account/ubo/) (UBO) details for an affiliated merchant account:

Add, retrieve, and update UBOs:

- [Create a UBO](#create-a-ubo): Add a UBO to a merchant account.
- [List UBOs](#list-ubos): Retrieve all UBOs for a merchant account.
- [Get UBO](#get-a-ubo): Retrieve a specific UBO by its identifier.
- [Update UBO](#update-a-ubo): Update a UBO.

Add and retrieve UBO identification documents:

- [Add identity document](#add-identity-document): Add an identity document to an existing UBO.
- [List identity documents](#list-identity-documents): Retrieve all identity documents for a UBO.
- [Get identity document](#get-identity-document): Retrieve a specific identity document for a UBO.

## Authentication
All the UBO requests require a partner account API key. This is not the same as a [site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code). For more information, email your partner manager.

All URLs on this page are directed to our test API. To use the live API, change the subdomain in the URL from `testapi` to `api` and use the corresponding API key.

---

## Create a UBO

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/ubos?api_key={your-account-api-key}` 

Add a new UBO to a merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`| The affiliated merchant ID.{{< br >}}**Format**: 8 character string, e.g. `12345678`. Required.

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name  <br /> `string`|The UBO's full name. <br /> **Format**: Max 200 characters. Required.|
|title  <br /> `string`|The UBO's title. <br /> **Options**: `mr` or `mrs`. Required.|
|address  <br /> `string`|The UBO's address.  <br /> **Format**: Max 100 characters. Optional.|
|address_apartment  <br /> `string`|The UBO's apartment number.  <br /> **Format**: Max 15 characters. Optional.|
|city  <br /> `string`|The UBO's city of residence. <br /> **Format**: Max 100 characters. Optional.|
|state  <br /> `string`|The UBO's province or state of residence.  <br /> **Format**: Max 100 characters. Optional.|
|country  <br /> `string`|The UBO's country of residence. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Required.|
|zipcode  <br /> `string`|The UBO's ZIP code. <br /> **Format**: max 20 characters. Optional.|
|birthday  <br /> `string`|The UBO's date of birth.  <br /> **Format**: yyyy-mm-dd, e.g. `1980-01-31`. Required.|
|country_of_birth  <br /> `string`|The UBO's country of birth. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Required.|
|email  <br /> `string`|The UBO's email address. <br /> **Format**: Max 100 characters. Required.|
|mobile_phone  <br /> `string`|The UBO's mobile phone number. <br /> **Format**: Max 25 characters. Optional.|
|office_phone  <br /> `string`|The UBO's office phone number. <br /> **Format**: Max 25 characters. Optional.|
|job_title  <br /> `string`|The UBO's job title. <br /> **Format**: Max 100 characters. Required.|
|percentage  <br /> `integer`|The UBO's percentage of equity. <br /> **Format**: Non-fractional number from `25` to `100`. Required.|
|type  <br /> `string`|The UBO's type of equity. <br /> **Options**: `control_rights`, `shareholder`, `voting_rights` or `other`. Required.|
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
The following are in addition to the request body parameters.

|Parameter|Description|
|-----|------|
| account_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
| id <br /> `string` | The unique identifier of the UBO. Referred to as `ubo_id`. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/ubos?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "name": "Firstname Lastname",
  "title": "mrs",
  "address": "Mainstreet 123",
  "address_apartment": "",
  "city": "Funtown",
  "state": "Noord-Holland",
  "country": "NL",
  "zipcode": "1234 ZP",
  "birthday": "1980-01-31",
  "country_of_birth": "NL",
  "email": "email@address.com",
  "mobile_phone": "0123456789",
  "office_phone": "0123456789",
  "job_title": "CEO",
  "percentage": 100,
  "type": "control_rights"
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "email@address.com",
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

## List UBOs

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/ubos`

Retrieve an array of all UBOs linked to a merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`|The affiliated merchant ID.{{< br >}}**Format**: 8 character string, e.g. `12345678`. Required.|

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
|address  <br /> `string`|The UBO's address.  <br /> **Format**: Max 100 characters.|
|address_apartment  <br /> `string`|The UBO's apartment number.  <br /> **Format**: Max 15 characters.|
|birthday  <br /> `string`|The UBO's date of birth.  <br /> **Format**: yyyy-mm-dd (e.g., `1980-01-31`).|
|city  <br /> `string`|The UBO's city of residence. <br /> **Format**: Max 100 characters.|
|country  <br /> `string`|The UBO's country of residence. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`.|
|country_of_birth  <br /> `string`|The UBO's country of birth. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`.|
|email  <br /> `string`|The UBO's email address. <br /> **Format**: Max 100 characters.|
| id <br /> `string` | The unique identifier of the UBO. Referred to as `ubo_id`. |
|job_title  <br /> `string`|The UBO's job title. <br /> **Format**: Max 100 characters.|
|mobile_phone  <br /> `string`|The UBO's mobile phone number. <br /> **Format**: Max 25 characters.|
|name  <br /> `string`|The UBO's full name. <br /> **Format**: Max 200 characters.|
|office_phone  <br /> `string`|The UBO's office phone number. <br /> **Format**: Max 25 characters.|
|percentage  <br /> `integer`|The UBO's percentage of equity. <br /> **Format**: Non-fractional number from `25` to `100`.|
|state  <br /> `string`|The UBO's province or state of residence.  <br /> **Format**: Max 100 characters.|
|title  <br /> `string`|The UBO's title. <br /> **Options**: `mr` or `mrs`.|
|type  <br /> `string`|The UBO's type of equity. <br /> **Options**: `control_rights`, `shareholder`, `voting_rights` or `other`.|
|zipcode  <br /> `string`|The UBO's ZIP code. <br /> **Format**: Max 20 characters.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/ubos?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "account_id": {affiliate_account_id},
      "address": "Mainstreet 123",
      "address_apartment": "",
      "birthday": "1980-01-31",
      "city": "Funtown",
      "country": "NL",
      "country_of_birth": "NL",
      "email": "email@address.com",
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
{{< /collapse >}}

---

## Get a UBO

`GET` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}?api_key={your-account-api-key}`

Retrieve a specific UBO.

### Path parameters
|Parameter|Description|
|---|---|
|ubo_id  `string` | The unique identifier of the UBO you want to retrieve. {{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `ubo_id` is returned as `id` in the [create a UBO](#create-a-ubo) and [list UBOs](#list-ubos) requests. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
|address  <br /> `string`|The UBO's address.  <br /> **Format**: Max 100 characters.|
|address_apartment  <br /> `string`|The UBO's apartment number.  <br /> **Format**: Max 15 characters.|
|birthday  <br /> `string`|The UBO's date of birth.  <br /> **Format**: yyyy-mm-dd, e.g. `1980-01-31`.|
|city  <br /> `string`|The UBO's city of residence. <br /> **Format**: Max 100 characters.|
|country  <br /> `string`|The UBO's country of residence. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`.|
|country_of_birth  <br /> `string`|The UBO's country of birth. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`.|
|email  <br /> `string`|The UBO's email address. <br /> **Format**: Max 100 characters.|
| id <br /> `string` | The unique identifier of the UBO. Referred to as `ubo_id`. |
|job_title  <br /> `string`|The UBO's job title. <br /> **Format**: Max 100 characters.|
|mobile_phone  <br /> `string`|The UBO's mobile phone number. <br /> **Format**: Max 25 characters.|
|name  <br /> `string`|The UBO's full name. <br /> **Format**: Max 200 characters.|
|office_phone  <br /> `string`|The UBO's office phone number. <br /> **Format**: Max 25 characters.|
|percentage  <br /> `integer`|The UBO's percentage of equity. <br /> **Format**: Non-fractional number from `25` to `100`.|
|state  <br /> `string`|The UBO's province or state of residence.  <br /> **Format**: Max 100 characters.|
|title  <br /> `string`|The UBO's title. <br /> **Options**: `mr` or `mrs`.|
|type  <br /> `string`|The UBO's type of equity. <br /> **Options**: `control_rights`, `shareholder`, `voting_rights` or `other`.|
|zipcode  <br /> `string`|The UBO's ZIP code. <br /> **Format**: Max 20 characters.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "email@address.com",
    "id": "{ubo_id}",
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

## Update a UBO

`PATCH` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}?api_key={your-account-api-key}`

Update information about an existing UBO.

### Path parameters
|Parameter|Description|
|---|---|
|ubo_id  `string` | The unique identifier of the UBO you want to update. {{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `ubo_id` is returned as `id` in the [create a UBO](#create-a-ubo) and [list UBOs](#list-ubos) requests. |

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name  <br /> `string`|The UBO's full name. <br /> **Format**: Max 200 characters. Optional.|
|title  <br /> `string`|The UBO's title. <br /> **Options**: `mr` or `mrs`. Optional.|
|address  <br /> `string`|The UBO's address.  <br /> **Format**: Max 100 characters. Optional.|
|address_apartment  <br /> `string`|The UBO's apartment number.  <br /> **Format**: Max 15 characters. Optional.|
|city  <br /> `string`|The UBO's city of residence. <br /> **Format**: Max 100 characters. Optional.|
|state  <br /> `string`|The UBO's province or state of residence.  <br /> **Format**: Max 100 characters. Optional.|
|country  <br /> `string`|The UBO's country of residence. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Optional.|
|zipcode  <br /> `string`|The UBO's ZIP code. <br /> **Format**: Max 20 characters. Optional.|
|birthday  <br /> `string`|The UBO's date of birth.  <br /> **Format**: yyyy-mm-dd, e.g. `1980-01-31`. Optional.|
|country_of_birth  <br /> `string`|The UBO's country of birth. <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Optional.|
|email  <br /> `string`|The UBO's email address. <br /> **Format**: Max 100 characters. Optional.|
|mobile_phone  <br /> `string`|The UBO's mobile phone number. <br /> **Format**: Max 25 characters. Optional.|
|office_phone  <br /> `string`|The UBO's office phone number. <br /> **Format**: Max 25 characters. Optional.|
|job_title  <br /> `string`|The UBO's job title. <br /> **Format**: Max 100 characters. Optional.|
|percentage  <br /> `integer`|The UBO's percentage of equity. <br /> **Format**: Non-fractional number from `25` to `100`. Optional.|
|type  <br /> `string`|The UBO's type of equity. <br /> **Options**: `control_rights`, `shareholder`, `voting_rights` or `other`. Optional.|
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
The following are in addition to the request body parameters.

|Parameter|Description|
|-----|------|
| account_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string, e.g., `12345678`.|
| id <br /> `string` | The unique identifier of the UBO. Referred to as `ubo_id`. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/ubos/glmqo15bces6n?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "email": "newemail@address.com" 
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "address": "Mainstreet 123",
    "address_apartment": "",
    "birthday": "1980-01-31",
    "city": "Funtown",
    "country": "NL",
    "country_of_birth": "NL",
    "email": "newemail@address.com",
    "id": "{ubo_id}",
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

`POST` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs?api_key={your-account-api-key}`

Upload an identity document to verify a UBO.

### Path parameters
|Parameter|Description|
|---|---|
|ubo_id  `string` | The unique identifier of the UBO you want to verify. {{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `ubo_id` is returned as `id` in the [create a UBO](#create-a-ubo) and [list UBOs](#list-ubos) requests. |

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|document_type <br /> `string`|The type of identity document.  <br /> **Options**: `id`, `passport`, `driverslicense`, `proof_of_address`|
|encoded_content <br /> `string`|Base64 encoded content. Required.|
|filename <br /> `string`|The identity document filename.  <br /> **Format**: Max 250 characters. Required. |
|mime_type <br />  `string`|The media type of the identity document file. <br /> **Options**: `application/pdf`,`image/jpeg`|
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
The following are in addition to the request body parameters.

|Parameter|Description|
|-----|------|
| id <br /> `string` | The unique identifier of the identity document. Referred to as `identitydoc_id`. |
| ubo_id  `string`| The unique identifier of a UBO.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```

curl -X POST "https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "document_type":"id",
  "encoded_content":"string",
  "filename":"identity-of-ubo.pdf",
  "mime_type":"application/pdf"
}'
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "document_type": "id",
    "filename": "identity-of-ubo.pdf",
    "id": "agi6ehoreex6a",
    "merchant_id": {affiliate_account_id},
    "mime_type": "application/pdf",
    "ubo_id": "{ubo_id}"
  },
  "success": true
}
```
{{< /collapse >}}

---

## List identity documents

`GET` `https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs?api_key={your-account-api-key}`

Retrieve an array of all identity documents for a UBO.

### Path parameters
|Parameter|Description|
|---|---|
|ubo_id  `string` | The unique identifier of the UBO you want to retrieve identity documents for. {{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `ubo_id` is returned as `id` in the [create a UBO](#create-a-ubo) and [list UBOs](#list-ubos) requests. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
| document_type <br /> `string`|The type of identity document.  <br /> **Options**: `id`, `passport`, `driverslicense`, `proof_of_address`|
| filename <br /> `string`|The identity document filename.  <br /> **Format**: Max 250 characters.|
| id <br /> `string` | The unique identifier of the identity document. Referred to as `identitydoc_id`. |
| merchant_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.
|mime_type <br />  `string`|The media type of the identity document file. <br /> **Options**: `application/pdf`,`image/jpeg`|
| ubo_id <br /> `string`| The unique identifier of a UBO.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/ubos/{ubo_id}/identitydocs?api_key={your-account-api-key}" \
--header "accept: application/json" \
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
      "merchant_id": {affiliate_account_id},
      "mime_type": "application/pdf",
      "ubo_id": "{ubo_id}"
    }
  ],
  "page": {
    "total": 1
  },
  "success": true
}
```
{{< /collapse >}}

---

## Get identity document

`GET` `https://testapi.multisafepay.com/v1/json/identitydocs/{identitydoc_id}?api_key={your-account-api-key}`

Retrieve a specific identity document.

### Path parameters
|Parameter|Description|
|---|---|
|identitydoc_id{{< br >}}`string`|The unique identifier of the identity document you want to retrieve.{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `identitydoc_id` is returned as `id` in the [add identity document](#add-identity-document) and [list identity documents](#list-identity-documents) requests. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
| document_type <br /> `string`|The type of identity document.  <br /> **Options**: `id`, `passport`, `driverslicense`, `proof_of_address`|
| filename <br /> `string`|The identity document filename.  <br /> **Format**: Max 250 characters.|
| id <br /> `string` | The unique identifier of the identity document. Referred to as `identitydoc_id`. |
| merchant_id <br /> `string` | The affiliated merchant ID. <br /> **Format**: 8 character string (e.g., `12345678`).
|mime_type <br />  `string`|The media type of the identity document file. <br /> **Options**: `application/pdf`,`image/jpeg`|
| ubo_id <br /> `string`| The unique identifier of the UBO the identity document is for.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET https://testapi.multisafepay.com/v1/json/identitydocs/{identitydoc_id}?api_key={your-account-api-key}
--header "accept: application/json" \
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "document_type": "identity",
    "filename": "identity-of-ubo.pdf",
    "id": "{identitydoc_id}",
    "merchant_id": {affiliate_merchant_id},
    "mime_type": "application/pdf",
    "ubo_id": "{ubo_id}"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Next steps
Now that you have created an affiliated merchant account and added one or multiple bank account and UBOs, complete the onboarding by adding one or multiple websites using the unique affiliated merchant `id` .

{{< two-buttons

href-1="/tools/api-onboarding/add-bank-accounts" header-1="Previous" text-1="Add bank accounts" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 
href-2="/tools/api-onboarding/add-websites" header-2="Next" text-2="Add websites" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
