---
title : Add websites 
layout : single
url: '/api-onboarding/add-websites/'
aliases: 
    - /tools/api-onboarding/add-websites
---

Use the following requests to add, retrieve or update websites linked to a merchant account affiliated with your partner account:

1. [Add a website](#1-add-a-website): Add a website to a merchant account.
2. [List websites](#2-list-websites): Retrieve all websites for a merchant account.
3. [Get website](#3-get-website): Retrieve a single website by its identifier.
4. [Update website](#4-update-website): Update a website.

## Authentication
All four website requests require a partner account API key. For more information, email your partner manager.

All URLs on this page are directed to our test API. To use the live API, change the subdomain in the URL from `testapi` to `api` and use the corresponding API key.

---

## 1. Add a website

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites`

Add a website to an affiliated merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`| Affiliate Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.|

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name <br /> `string`|Name of the website.  <br /> **Format**: max 120 characters. Required. |
|notification_url <br /> `string`|[Notification URL](/developer/api/notification-url/) of the website.  <br /> **Format**: URL (max 150 characters). Optional. |
|price_from <br /> `integer`| Expected minimum order value for credit card transactions.  <br /> **Format**: unsigned integer. Optional. |
|price_till <br /> `integer`| Expected maximum order value for credit card transactions.  <br /> **Format**: unsigned integer. Optional. |
|support_email <br /> `string`| Email address used to support the website's customers.  <br /> **Format**: email address (max 100 characters). Optional. |
|support_phone <br /> `string`| Phone number used to support the website's customers.  <br /> **Format**: phone number (max 100 characters). Optional. |
|URL <br /> `string`| URL of the website.  <br /> **Format**: URL (max 150 characters). Required. |
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
In addition to the request body parameters.

|Parameter|Description|
|---|---|
| account_id <br /> `string`| Affiliate Merchant ID. <br /> **Format**: 8 character string (e.g. `12345678`).|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string (e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`).|
| id  <br /> `integer`| The unique site ID for the website. **Format**: 5-digit integer (e.g. `12345`).|
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

## 2. List websites

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/sites?api_key={your-account-api-key}`

Retrieve an array of all websites linked to a merchant account.

### Path parameters
|Parameter|Description|
|---|---|
|affiliate_account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| Affiliate Merchant ID. <br /> **Format**: 8 character string (e.g. `12345678`).|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string (e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`).|
| id  <br /> `integer`| The unique site ID for the website. <br /> **Format**: 5-digit integer (e.g. `12345`).|
|name <br /> `string`|Name of the website.  <br /> **Format**: max 120 characters. |
|notification_url <br /> `string`|[Notification URL](/developer/api/notification-url/) of the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| Expected minimum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|price_till <br /> `integer`| Expected maximum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|support_email <br /> `string`| Email address used to support the website's customers.  <br /> **Format**: email address (max 100 characters). |
|support_phone <br /> `string`| Phone number used to support the website's customers.  <br /> **Format**: phone number (max 100 characters). |
|URL <br /> `string`| URL of the website.  <br /> **Format**: URL (max 150 characters).|
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

## 3. Get website

`GET` `https://testapi.multisafepay.com/v1/json/sites/{site_id}?api_key={your-account-api-key}`

Retrieve a single website by its identifier.

### Path parameters
|Parameter|Description|
|---|---|
|site_id{{< br >}}`string`|Site ID.{{< br >}}**Format**: 5 character string (e.g., `12345`). Required.{{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The site_id is returned as `id` in the [add a website](#1-add-a-website) and [list websites](#2-list-websites) request.|

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| Affiliate Merchant ID. <br /> **Format**: 8 character string (e.g. `12345678`).|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string (e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`).|
| id  <br /> `integer`| The unique site ID for the website. **Format**: 5-digit integer (e.g. `12345`).|
|name <br /> `string`|Name of the website.  <br /> **Format**: max 120 characters. |
|notification_url <br /> `string`|[Notification URL](/developer/api/notification-url/) of the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| Expected minimum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|price_till <br /> `integer`| Expected maximum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|support_email <br /> `string`| Email address used to support the website's customers.  <br /> **Format**: email address (max 100 characters). |
|support_phone <br /> `string`| Phone number used to support the website's customers.  <br /> **Format**: phone number (max 100 characters). |
|URL <br /> `string`| URL of the website.  <br /> **Format**: URL (max 150 characters).|
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

## 4. Update website

`PATCH` `https://testapi.multisafepay.com/v1/json/sites/{site_id}?api_key={your-account-api-key}`

Update information about an existing website.

### Path parameters
|Parameter|Description|
|---|---|
|site_id{{< br >}}`string`|Site ID.{{< br >}}**Format**: 5 character string (e.g., `12345`). Required.{{< br >}}{{< br >}} <img src='/svgs/Note.svg' width="4%" height="auto" /> The site_id is returned as `id` in the [add a website](#1-add-a-website) and [list websites](#2-list-websites) request.|

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
|name <br /> `string`|Name of the website.  <br /> **Format**: max 120 characters. Optional. |
|notification_url <br /> `string`|[Notification URL](/developer/api/notification-url/) of the website.  <br /> **Format**: URL (max 150 characters). Optional. |
|price_from <br /> `integer`| Expected minimum order value for credit card transactions.  <br /> **Format**: unsigned integer. Optional. |
|price_till <br /> `integer`| Expected maximum order value for credit card transactions.  <br /> **Format**: unsigned integer. Optional. |
|support_email <br /> `string`| Email address used to support the website's customers.  <br /> **Format**: email address (max 100 characters). Optional. |
|support_phone <br /> `string`| Phone number used to support the website's customers.  <br /> **Format**: phone number (max 100 characters). Optional. |
|URL <br /> `string`| URL of the website.  <br /> **Format**: URL (max 150 characters). Optional. |
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|---|---|
| account_id <br /> `string`| Affiliate Merchant ID. <br /> **Format**: 8 character string (e.g. `12345678`).|
| api_key <br /> `string`| The API key for the website. <br /> **Format**: 40 character string (e.g. `4192937dffd72a34bcaef4e4f589beb74188d0fa`).|
| id  <br /> `integer`| The unique site ID for the website. **Format**: 5-digit integer (e.g. `12345`).|
|name <br /> `string`|Name of the website.  <br /> **Format**: max 120 characters. |
|notification_url <br /> `string`|[Notification URL](/developer/api/notification-url/) of the website.  <br /> **Format**: URL (max 150 characters). |
|price_from <br /> `integer`| Expected minimum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|price_till <br /> `integer`| Expected maximum order value for credit card transactions.  <br /> **Format**: unsigned integer. |
|support_email <br /> `string`| Email address used to support the website's customers.  <br /> **Format**: email address (max 100 characters). |
|support_phone <br /> `string`| Phone number used to support the website's customers.  <br /> **Format**: phone number (max 100 characters). |
|URL <br /> `string`| URL of the website.  <br /> **Format**: URL (max 150 characters).|
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
