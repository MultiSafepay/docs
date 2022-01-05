---
title : Create a merchant account
layout : single
url: '/api-onboarding/create-account/'
aliases: 
    - /tools/api-onboarding/create-account
---

Use the following requests to create, retrieve or update merchant accounts affiliated to your partner account:

1. [Signup account](#signup-account): create a new merchant account
2. [List accounts](#list-accounts): retrieve a list of all merchant accounts
3. [Get account](#get-account): retrieve a single merchant account
4. [Update account](#update-account): update a merchant account

## Authentication
All four account requests require a partner account API key. This is not the same as a [website API key](/set-up-your-account/site-id-api-key-secure-code). For more information, email your Partner Manager.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the corresponding API key.

---

## 1. Signup account

`POST` `https://testapi.multisafepay.com/v1/json/signup-account?api_key={your-account-api-key}`

Create a new affiliated merchant account.

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|**account**  <br /> `object`|This object holds company information|
|account.address1  `string`|First line of company address  <br /> **Format**: max 64 characters. Optional.|
|account.address2<br />`string`|Second line of company address<br />**Format**: max 64 characters. Optional.|
|account.address3<br />`string`|Third line of company address <br />**Format**: max 64 characters. Optional.|
|account.apartment<br />`string`|Apartment number of company address<br />**Format**: max 9 characters. Optional.|
|account.city<br />`string`|City of company address<br />**Format**: max 50 characters Optional.|
|account.coc_number<br />`string`|Chamber of commerce number <br />**Format**: max 50 characters. Optional.|
|account.company_name<br />`string`|Name of company. This must be unique. <br />**Format**: max 200 characters. Required.|
|account.country<br />`string`|Country code of company <br />**Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Required.|
|account.email<br />`string`|Company email address. Transaction updates are sent to this address. This must be unique. <br />**Format**: max 100 characters. Required.|
|account.fax<br />`string`|Company fax number<br />**Format**: max 15 characters. Optional.|
|account.phone<br />`string`|Company phone number<br />**Format**: max 15 characters. Optional.|
|account.vat_number<br />`string`|Company VAT number<br />**Format**: max 50 characters. Optional.|
|account.zipcode<br />`string`|Company ZIP Code<br />**Format**: max 30 characters. Optional.|
|**user**<br />`object`|This object holds user information|
|user.name<br />`string`|Full name of the primary user. The name can be modified later. Required.|
|user.email<br />`string`|Email address of the primary user. The welcome email with secure code is sent to this address. This must be unique. Required.|
|user.password<br />`string`|Password of the primary user. Required.|
|currencies<br />`array`|List of currencies the company wishes to process<br />**Format**: array of strings in [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `[EUR,USD]`). Required.|

{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
In addition to the request body parameters.

|Parameter|Description|
|-----|------|
| id<br />`string`| The unique identifier of the affiliated merchant account. Referred to as `{account_id}`. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/signup-account?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "account": {
    "address1": "Flowerstreet 123",
    "address2": "",
    "address3": "",
    "apartment": "5A",
    "city": "Amsterdam",
    "coc_number": "123456",
    "company_name": "{affiliate-company-name}",
    "country": "NL",
    "email": "{affiliate-email-address}",
    "fax": "00311234567890",
    "phone": "00311234567890",
    "vat_number": "NL999999999B99",
    "zipcode": "1234 ZP"
  },
  "user": {
    "name": "Ad Admin",
    "email": "{affiliate-email-address}",
    "password": "password"
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
      "company_name": "{affiliate-company-name},
      "country": "NL",
      "email": "{affiliate-email-address}",
      "fax": "00311234567890",
      "id": 12345678,
      "phone": "00311234567890",
      "vat_number": "NL999999999B99",
      "zipcode": "1234 ZP"
    },
    "user": {
      "name": "Ad Admin",
      "email": "{affiliate-email-address}",
      "password": "***"
    },
    "currencies": [
      "EUR"
    ]
  },
  "success": true
}
```
{{< /collapse >}}

---
 
## 2. List accounts

`GET` `https://testapi.multisafepay.com/v1/json/accounts?api_key={your-account-api-key}`

Retrieve an array of all merchant accounts affiliated to your partner account.

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|address1 <br /> `string`|First line of company address  <br /> **Format**: max 64 characters. |
|address2 <br /> `string`|Second line of company address <br /> **Format**: max 64 characters.|
|address3 <br /> `string`|Third line of company address  <br /> **Format**: max 64 characters.|
|apartment <br /> `string`|Apartment number of company address <br /> **Format**: max 9 characters.|
|city <br /> `string`|City of company address <br /> **Format**: max 50 characters.|
|coc_number <br /> `string`|Chamber of commerce number  <br /> **Format**: max 50 characters.|
|company_name <br /> `string`|Name of company.  <br /> **Format**: max 200 characters.|
|country <br /> `string`|Country code of company  <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`).|
|email <br /> `string`|Company email address. Transaction updates are sent to this address.  <br /> **Format**: max 100 characters.|
|fax <br /> `string`|Company fax number <br /> **Format**: max 15 characters. |
|id <br /> `string`| The unique identifier of the affiliated merchant account. Referred to as `{account_id}`. |
|phone <br /> `string`|Company phone number <br /> **Format**: max 15 characters. |
|vat_number <br /> `string`|Company VAT number <br /> **Format**: max 50 characters. |
|zipcode <br /> `string`|Company ZIP Code <br /> **Format**: max 30 characters. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts?api_key={your-account-api-key}" \
--header "accept: application/json" \
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
      "company_name": "{affiliate-company-name}",
      "country": "NL",
      "email": "{affiliate-email-address}",
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
{{< /collapse >}}

---

## 3. Get account

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}?api_key={your-account-api-key}`

Retrieve the account details of a specific affiliated merchant account.

#### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Affiliate merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|address1 <br /> `string`|First line of company address  <br /> **Format**: max 64 characters. |
|address2 <br /> `string`|Second line of company address <br /> **Format**: max 64 characters.|
|address3 <br /> `string`|Third line of company address  <br /> **Format**: max 64 characters.|
|apartment <br /> `string`|Apartment number of company address <br /> **Format**: max 9 characters.|
|city <br /> `string`|City of company address <br /> **Format**: max 50 characters.|
|coc_number <br /> `string`|Chamber of commerce number  <br /> **Format**: max 50 characters.|
|company_name <br /> `string`|Name of company.  <br /> **Format**: max 200 characters.|
|country <br /> `string`|Country code of company  <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`).|
|email <br /> `string`|Company email address. Transaction updates are sent to this address.  <br /> **Format**: max 100 characters.|
|fax <br /> `string`|Company fax number <br /> **Format**: max 15 characters. |
|id <br /> `string`| The unique identifier of the affiliated merchant account. Referred to as `{account_id}`. |
|phone <br /> `string`|Company phone number <br /> **Format**: max 15 characters. |
|vat_number <br /> `string`|Company VAT number <br /> **Format**: max 50 characters. |
|zipcode <br /> `string`|Company ZIP Code <br /> **Format**: max 30 characters. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
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
    "company_name": "{affiliate-company-name}",
    "country": "NL",
    "email": "{affiliate-email-address}",
    "fax": "00311234567890",
    "id": "12345678",
    "phone": "00311234567890",
    "vat_number": "NL999999999B99",
    "zipcode": "1234 ZP"
  },
  "success": true
}
```
{{< /collapse >}}

---

## 4. Update account

`PATCH` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}?api_key={your-account-api-key}`

Update the account details of an affiliated merchant account.

#### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Affiliate merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|address1 <br /> `string`|First line of company address  <br /> **Format**: max 64 characters. Optional.|
|address2 <br /> `string`|Second line of company address <br /> **Format**: max 64 characters. Optional.|
|address3 <br /> `string`|Third line of company address  <br /> **Format**: max 64 characters. Optional.|
|apartment <br /> `string`|Apartment number of company address <br /> **Format**: max 9 characters. Optional.|
|city <br /> `string`|City of company address <br /> **Format**: max 50 characters Optional.|
|coc_number <br /> `string`|Chamber of commerce number  <br /> **Format**: max 50 characters. Optional.|
|company_name <br /> `string`|Name of company  <br /> **Format**: max 200 characters. Optional.|
|country <br /> `string`|Country code of company  <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Optional.|
|email <br /> `string`|Company email address  <br /> **Format**: max 100 characters. Optional.|
|fax <br /> `string`|Company fax number <br /> **Format**: max 15 characters. Optional.|
|phone <br /> `string`|Company phone number <br /> **Format**: max 15 characters. Optional.|
|vat_number <br /> `string`|Company VAT number <br /> **Format**: max 50 characters. Optional.|
|zipcode <br /> `string`|Company ZIP Code <br /> **Format**: max 30 characters. Optional.|
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|address1 <br /> `string`|First line of company address  <br /> **Format**: max 64 characters. Optional.|
|address2 <br /> `string`|Second line of company address <br /> **Format**: max 64 characters. Optional.|
|address3 <br /> `string`|Third line of company address  <br /> **Format**: max 64 characters. Optional.|
|apartment <br /> `string`|Apartment number of company address <br /> **Format**: max 9 characters. Optional.|
|city <br /> `string`|City of company address <br /> **Format**: max 50 characters Optional.|
|coc_number <br /> `string`|Chamber of commerce number  <br /> **Format**: max 50 characters. Optional.|
|company_name <br /> `string`|Name of company  <br /> **Format**: max 200 characters. Optional.|
|country <br /> `string`|Country code of company  <br /> **Format**: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `NL`). Optional.|
|email <br /> `string`|Company email address  <br /> **Format**: max 100 characters. Optional.|
|fax <br /> `string`|Company fax number <br /> **Format**: max 15 characters. Optional.|
|phone <br /> `string`|Company phone number <br /> **Format**: max 15 characters. Optional.|
|vat_number <br /> `string`|Company VAT number <br /> **Format**: max 50 characters. Optional.|
|zipcode <br /> `string`|Company ZIP Code <br /> **Format**: max 30 characters. Optional.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
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
    "company_name": "{affiliate-company-name}",
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
{{< /collapse >}}

---

## Next steps
You have successfully created a merchant account. Now, you can add bank accounts, UBOs, and websites, using the affiliate merchant account ID.

{{< two-buttons

href-1="/tools/api-onboarding" header-1="Overview" text-1="Read introduction" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-bank-accounts" header-2="Next" text-2="Add bank accounts " img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
