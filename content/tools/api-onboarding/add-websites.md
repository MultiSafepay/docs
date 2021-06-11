---
title : Add websites 
layout : single
tags : hidden
---

Use the following requests to add, retrieve or update websites linked to a merchant account affiliated with your partner account:

1. [Add a website](#add-a-website): Add a website to a merchant account.
2. [List websites](#list-websites): Retrieve all websites for a merchant account.
3. [Get website](#get-a-website): Retrieve a single website by its identifier.
4. [Update website](#update-a-website): Update a website.

### About parameters
For every parameter, we specify whether it's _required_ or _optional_. However, this label refers only to the technical requirements for valid API requests. To process credit card transactions with the website API key, expected minimum and maximum order values need to be supplied. Furthermore, the [notification URL](/faq/api/how-does-the-notification-url-work/) is required to receive transaction status updates. However, this information may also be provided at a later time. 

## Authentication
All four website requests require a partner account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain in the URL from `testapi` to `api` and use the corresponding API key.

---

## Add a website

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/sites`

Add a website to an affiliated merchant account.

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|account ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|---|---|
|name{{< br >}}`string`|Name of the website. {{< br >}}**Format**: max 120 characters. Required. |
|URL{{< br >}}`string`| URL of the website. {{< br >}}**Format**: URL (max 150 characters). Required.. |
|notification_url{{< br >}}`string`|[Notification URL](/faq/api/how-does-the-notification-url-work/) of the website. {{< br >}}**Format**: URL (max 150 characters). Optional. |
|price_from{{< br >}}`integer`| Expected minimum order value for credit card transactions. {{< br >}}**Format**: unsigned integer. Optional. |
|price_till{{< br >}}`integer`| Expected maximum order value for credit card transactions. {{< br >}}**Format**: unsigned integer. Optional. |
|support_email{{< br >}}`string`| Email address used to support the website's customers. {{< br >}}**Format**: email address (max 100 characters). Optional. |
|support_phone{{< br >}}`string`| Phone number used to support the website's customers. {{< br >}}**Format**: phone number (max 100 characters). Optional. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/account/12345678/sites" \
-H "accept: application/json" 
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your-api-key>" \
-d "
{
  "name":"Funcompany",
  "notification_url":"https://funcompany.com/transactionhook",
  "price_from":50,
  "price_till":500,
  "support_email":"support@funcompany.nl",
  "support_phone":"0123456789",
  "url":"https://funcompany.com"
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
`account_id` → the account ID of the associated merchant account  
`api_key` → the website-level API key of the linked website  
`id` → the site ID of the linked website
{{< /collapse >}}

---

## List websites

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/sites`

Retrieve an array of all websites linked to a merchant account.

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/account/12345678/sites" \
-H "accept: application/json" \
-H "Authorization: Bearer <your-api-key>" 
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "account_id": 12345678,
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
`account_id` → the account ID of the associated merchant account  
`api_key` → the website-level API key of the linked website  
`id` → the site ID of the linked website
{{< /collapse >}}

---

## Get website

`GET` `https://testapi.multisafepay.com/v1/json/sites/{site_id}`

Retrieve a single website by its identifier.

### Path parameters
|Key|Description|
|---|---|
|site_id{{< br >}}`string`|Site ID.{{< br >}}**Format**: 5 character string (e.g., `12345`). Required.

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/account/sites/12345" \
-H "accept: application/json" \
-H "Authorization: Bearer <your-api-key>" 
```
{{< /collapse >}}


{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": 12345678,
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
`account_id` → the account ID of the associated merchant account  
`api_key` → the website-level API key of the linked website  
`id` → the site ID of the linked website
{{< /collapse >}}

---

## Update website

`PATCH` `https://testapi.multisafepay.com/v1/json/sites/{site_id}`

Update information about an existing website.

### Path parameters
|Key|Description|
|---|---|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|---|---|
|name{{< br >}}`string`|Name of the website. {{< br >}}**Format**: max 120 characters. Optional. |
|URL{{< br >}}`string`| URL of the website. {{< br >}}**Format**: URL (max 150 characters). Optional. |
|notification_url{{< br >}}`string`|[Notification URL](/faq/api/how-does-the-notification-url-work/) of the website. {{< br >}}**Format**: URL (max 150 characters). Optional. |
|price_from{{< br >}}`integer`| Expected minimum order value for credit card transactions. {{< br >}}**Format**: unsigned integer. Optional. |
|price_till{{< br >}}`integer`| Expected maximum order value for credit card transactions. {{< br >}}**Format**: unsigned integer. Optional. |
|support_email{{< br >}}`string`| Email address used to support the website's customers. {{< br >}}**Format**: email address (max 100 characters). Optional. |
|support_phone{{< br >}}`string`| Phone number used to support the website's customers. {{< br >}}**Format**: phone number (max 100 characters). Optional. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X PATCH "https://testapi.multisafepay.com/v1/json/sites/12345" \
-H "accept: application/json" \
-H "Authorization: Bearer 12345678" \
-H "Content-Type: application/json" \
-d "
{
  "notification_url": "https://funcompany.com/newhook"
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
    "api_key": "4192937dffd72a34bcaef4e4f589beb74188d0fa",
    "id": 12345,
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
`account_id` → the account ID of the associated merchant account  
`api_key` → the website-level API key of the linked website  
`id` → the site ID of the linked website
{{< /collapse >}}

---

## That's it
You've successfully created an affiliated merchant account and added the associated bank accounts, UBOs, and websites. Next, we will perform checks on the provided information.
Once those checks have been passed successfully, the newly created account is ready to process payments.  

{{< two-buttons href-1="/tools/api-onboarding/add-ubos" header-1="Previous" text-1="Add UBOs" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}
{{< two-buttons href-1="/tools/api-onboarding" header-1="Overview" text-1="Onboarding using our API" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}
