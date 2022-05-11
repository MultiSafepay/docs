---
title : Add websites 
layout : single
url: '/api-onboarding/add-websites/'
aliases: 
    - /tools/api-onboarding/add-websites
---

Use the following requests to add, retrieve, or update websites linked to an affiliated merchant account:

- [Add a website](#add-a-website): Add a website to a merchant account.
- [List websites](#list-websites): Retrieve all websites for a merchant account.
- [Get website](#get-website): Retrieve a specific website.
- [Update website](#update-website): Update a website.

## Authentication
All of the website requests require a partner account API key. For more information, email your partner manager.

All URLs on this page are directed to our test API. To use the live API, change the subdomain in the URL from `testapi` to `api` and use the corresponding API key.

---

## Add a website

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites`

Add a website to an affiliated merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`| The affiliated merchant ID.{{< br >}}**Format**: 8 character string, e.g. `12345678`. Required.|

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name <br /> `string`|Name of the website.  <br /> **Format**: Max 120 characters. Required. |
|notification_url <br /> `string`|The [webhook endpoint](/integrations/webhooks/) for the website.  <br /> **Format**: URL (max 150 characters). Optional. |
|price_from <br /> `integer`| The expected minimum order value for credit card transactions.  <br /> **Format**: Unsigned integer. Optional. |
|price_till <br /> `integer`| The expected maximum order value for credit card transactions.  <br /> **Format**: Unsigned integer. Optional. |
|support_email <br /> `string`| The website's customer support email address.  <br /> **Format**: Email address (max 100 characters). Optional. |
|support_phone <br /> `string`| The customer support phone number for the website.  <br /> **Format**: Phone number (max 100 characters). Optional. |
|URL <br /> `string`| The URL of the website.  <br /> **Format**: URL (max 150 characters). Required. |
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
The following are in addition to the request body parameters.

|Parameter|Description|
|---|---|
| account_id <br /> `string`| The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string, e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`.|
| id  <br /> `integer`| The unique identifier of the website. <br /> **Format**: 5-digit integer, e.g. `12345`.|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites?api_key={your-account-api-key}" \
--header "accept: application/json" 
--header "Content-Type: application/json" \
--data-raw '{
  "name":"Funcompany",
  "notification_url":"https://funcompany.com/transactionhook",
  "price_from":50,
  "price_till":500,
  "support_email":"support@funcompany.nl",
  "support_phone":"0123456789",
  "url":"https://funcompany.com"
}'
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "api_key": "4192937dffd72a34bcaef4e4f589beb74188d0fa",
    "id": 12345,
    "name": "Funcompany",
    "notification_url": "https://funcompany.com/transactionhook",
    "price_from": 50,
    "price_till": 500,
    "support_email": "support@funcompany.nl",
    "support_phone": "0123456789",
    "url": "https://funcompany.com"
  },
  "success": true
}
```
{{< /collapse >}}

---

## List websites

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites?api_key={your-account-api-key}`

Retrieve an array of all websites linked to a merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`|The affiliated merchant ID.{{< br >}}**Format**: 8 character string, e.g. `12345678`. Required.

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string, e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`.|
| id  <br /> `integer`| The unique identifier of the website. Referred to as `site_id`. <br /> **Format**: 5-digit integer, e.g. `12345`.|
|name <br /> `string`| The name of the website.  <br /> **Format**: Max 120 characters. |
|notification_url <br /> `string`|The [webhook endpoint](/integrations/webhooks/) for the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| The expected minimum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|price_till <br /> `integer`| The expected maximum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|support_email <br /> `string`| The website's customer support email address.  <br /> **Format**: Email address (max 100 characters). |
|support_phone <br /> `string`| The customer support phone number for the website.  <br /> **Format**: Phone number (max 100 characters). |
|URL <br /> `string`| The URL of the website.  <br /> **Format**: URL (max 150 characters).|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "account_id": {affiliate_account_id},
      "api_key": "4192937dffd72a34bcaef4e4f589beb74188d0fa",
      "id": 12345,
      "name": "Funcompany",
      "notification_url": "https://funcompany.com/transactionhook",
      "price_from": 50,
      "price_till": 500,
      "support_email": "support@funcompany.nl",
      "support_phone": "0123456789",
      "url": "https://funcompany.com"
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

## Get website

`GET` `https://testapi.multisafepay.com/v1/json/sites/{site_id}?api_key={your-account-api-key}`

Retrieve information about a specific website.

### Path parameters
|Parameter|Description|
|---|---|
|site_id{{< br >}}`integer`|The unique identifier of the website.{{< br >}}**Format**: 5-digit integer, e.g. `12345`. Required.{{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `site_id` is returned as `id` in the [add a website](#add-a-website) and [list websites](#list-websites) requests.|

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string, e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`.|
| id  <br /> `integer`| The unique identifier of the website. Referred to as `site_id`. **Format**: 5-digit integer, e.g. `12345`.|
|name <br /> `string`|Name of the website.  <br /> **Format**: Max 120 characters. |
|notification_url <br /> `string`|The [webhook endpoint](/integrations/webhooks/) for the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| The expected minimum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|price_till <br /> `integer`| The expected maximum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|support_email <br /> `string`| The website's customer support email address.  <br /> **Format**: Email address (max 100 characters). |
|support_phone <br /> `string`| The customer support phone number for the website.  <br /> **Format**: Phone number (max 100 characters). |
|URL <br /> `string`| The URL of the website.  <br /> **Format**: URL (max 150 characters).|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/sites/{site_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "api_key": "4192937dffd72a34bcaef4e4f589beb74188d0fa",
    "id": {site_id},
    "name": "Funcompany",
    "notification_url": "https://funcompany.com/transactionhook",
    "price_from": 50,
    "price_till": 500,
    "support_email": "support@funcompany.nl",
    "support_phone": "0123456789",
    "url": "https://funcompany.com"
  },
  "success": true
}
```

{{< /collapse >}}

---

## Update website

`PATCH` `https://testapi.multisafepay.com/v1/json/sites/{site_id}?api_key={your-account-api-key}`

Update information about an existing website.

### Path parameters
|Parameter|Description|
|---|---|
|site_id{{< br >}}`integer`|The unique identifier of the website.{{< br >}}**Format**: 5-digit integer, e.g. `12345`. Required.{{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The `site_id` is returned as `id` in the [add a website](#add-a-website) and [list websites](#list-websites) requests.|

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name <br /> `string`|The name of the website.  <br /> **Format**: Max 120 characters. Optional. |
|notification_url <br /> `string`|The [webhook endpoint](/integrations/webhooks/) for the website.  <br /> **Format**: URL (max 150 characters). Optional. |
|price_from <br /> `integer`| The expected minimum order value for credit card transactions.  <br /> **Format**: Unsigned integer. Optional. |
|price_till <br /> `integer`| The expected maximum order value for credit card transactions.  <br /> **Format**: Unsigned integer. Optional. |
|support_email <br /> `string`| The website's customer support email address.  <br /> **Format**: Email address (max 100 characters). Optional. |
|support_phone <br /> `string`| The customer support phone number for the website.  <br /> **Format**: Phone number (max 100 characters). Optional. |
|URL <br /> `string`| The URL of the website.  <br /> **Format**: URL (max 150 characters). Optional. |
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| The affiliated merchant ID. <br /> **Format**: 8 character string, e.g. `12345678`.|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string, e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`.|
| id  <br /> `integer`| The unique identifier of the website. Referred to as `site_id`. **Format**: 5-digit integer, e.g. `12345`.|
|name <br /> `string`|The name of the website.  <br /> **Format**: max 120 characters. |
|notification_url <br /> `string`|The [webhook endpoint](/integrations/webhooks/) for the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| The expected minimum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|price_till <br /> `integer`| The expected maximum order value for credit card transactions.  <br /> **Format**: Unsigned integer. |
|support_email <br /> `string`| The website's customer support email address.  <br /> **Format**: Email address (max 100 characters). |
|support_phone <br /> `string`| The customer support phone number for the website.  <br /> **Format**: Phone number (max 100 characters). |
|URL <br /> `string`| The URL of the website.  <br /> **Format**: URL (max 150 characters).|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/sites/{site_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "notification_url": "https://funcompany.com/newhook"
}'
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": {affiliate_account_id},
    "api_key": "4192937dffd72a34bcaef4e4f589beb74188d0fa",
    "id": {site_id},
    "name": "Funcompany",
    "notification_url": "https://funcompany.com/newhook",
    "price_from": 50,
    "price_till": 500,
    "support_email": "support@funcompany.nl",
    "support_phone": "0123456789",
    "url": "https://funcompany.com"
  },
  "success": true
}
```
{{< /collapse >}}

---

## That's it!
You've successfully created an affiliated merchant account and added the associated bank accounts, UBOs, and websites. Next, we will perform checks on the provided information.
Once those checks have passed successfully, the newly created account is ready to process payments.  

{{< two-buttons href-1="/tools/api-onboarding/add-ubos" header-1="Previous" text-1="Add UBOs" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}
{{< two-buttons href-1="/tools/api-onboarding" header-1="Overview" text-1="Onboarding using our API" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}
