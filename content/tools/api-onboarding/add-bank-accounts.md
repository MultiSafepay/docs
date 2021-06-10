---
title : Add bank accounts
layout : single
tags : hidden
---

Use seven requests to perform actions on bank account details of merchant accounts affiliated to your partner account:

1. [Add bank account](#add-bank-account): add a bank account to a merchant account
2. [List bank accounts](#list-bank-accounts): retrieve a list of all bank accounts
3. [Get bank account](#get-bank-account): retrieve a single bank account
5. [Create payment link](#create-payment-link): create a payment link to verify a bank account
6. [Add bank statement](#add-bank-statement): add a bank statement to verify a bank account
7. [List bank statements](#list-bank-statements): retrieve a list of all bank statements
8. [Get bank statement](#get-bank-statement): retrieve a single bank statement


### The process

The requests above can be split into two steps:

1. **Add bank accounts**: Use the first three requests to add and retrieve bank accounts linked to a merchant account. 
2. **Verify bank accounts**: Use the last four requests to verify bank accounts. You can choose to verify through a payment link or by supplying a bank statement.

## Authentication
All seven bank account requests require a partner account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the corresponding API key.

## Add bank account 

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/bank-accounts`

Add a new bank account to a merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

### Query parameters
|Key|Description|
|-----|------|
|iban{{< br >}}`string`|The [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) of the bank account.{{< br >}}**Format**: alphanumeric string of up to 34 characters. Required |
|holder_name{{< br >}}`string`|Full name of the bank account holder. This can be a natural person, company or other legal entity. {{< br >}}**Format**: max 40 characters. Required.|
|currency{{< br >}}`string`|The currency of the bank account.{{< br >}}**Format**: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `EUR`). Required.|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/accounts/12345678/bank-accounts" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-account-API-key>" \
-d " \
{
  "currency" :"EUR",
  "holder_name" :"Fun B.V.",
  "iban" :"NL02ABNA0123456789"
}"
```
_Escape characters in the JSON body are omitted to improve readability._
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "currency" :"EUR",
    "holder_name" :"Fun B.V.",
    "iban" :"NL02ABNA0123456789"
  },
  "success": true
}
```
{{< /collapse >}}

---

## List bank accounts

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{account_id}/bank-accounts`

Retrieve a list of all bank accounts linked to an affiliated merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Merchant ID of the affiliated merchant account.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/12345678/bank-accounts" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "currency": "EUR",
      "holder_name": "Fun B.V.",
      "iban": "NL02ABNA0123456789"
    },
    {
      "currency": "USD",
      "holder_name": "Fun B.V.",
      "iban": "NL02ABNA0123456789"
    }
  ],
  "success": true
}
```
{{< /collapse >}}

---

## Get bank account

`GET` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}`

Retrieve a single bank account by its identifier.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The identifier of the bankaccount. {{< br >}}**Format**: ??? (e.g., `???`). Required. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-accounts/12345678" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "currency": "EUR",
    "holder_name": "Fun B.V.",
    "iban": "NL02ABNA0123456789"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Create payment link

`POST` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/payment-links`

Create a payment link for a refundable 1 EUR payment. This payment is used to verify the ownership of the associated bank account. Alternatively, supply a copy of a bank statement through the `bank-statements` request.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The identifier of the bankaccount. {{< br >}}**Format**: ??? (e.g., `???`). Required. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/bank-accounts/12345678/payment-links" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "bankaccount_id": 12345678,
    "payment_link": "https://paymentlink.com/link"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Add bank statement

`POST` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements`

Upload a bank statement to verify the ownership of the associated bank . Alternatively, create a payment link through the `payment-links` request.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The identifier of the bankaccount. {{< br >}}**Format**: ??? (e.g., `???`). Required. |

### Request body
|Key|Value|
|-----|------|
|encoded_content|Base64 encoded content. Required.|
|filename{{< br >}}`string`|Name of the bank statement file. {{< br >}}**Format**: max 250 characters. Required. |
|mime_type{{< br >}} `string`|Media type of the bank statement file .{{< br >}}**Options**: `application/pdf` `image/jpeg`|

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/bank-accounts/12345678/bank-statements" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-account-API-key>" \
-d "
{
  "encoded_content": "string",
  "filename": "bank-statement.pdf",
  "mime_type": "application/pdf"
}"
```
_Escape characters in the JSON body are omitted to improve readability._
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "encoded_content": "string",
    "filename": "bank-statement.pdf",
    "mime_type": "application/pdf"
  },
  "success": "true"
}
```
{{< /collapse >}}

---

## List bank statements

`GET` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements`

Retrieve a list of all bank statements associated with a bank account.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The identifier of the bankaccount. {{< br >}}**Format**: ??? (e.g., `???`). Required. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-accounts/12345678/bank-statements" \
-H  "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "encoded_content": "string",
      "filename": "bank-statement.pdf",
      "mime_type": "application/pdf"
    }
  ],
  "success": true
}
```
{{< /collapse >}}

---

## Get bank statement

`GET` `https://testapi.multisafepay.com/v1/json/bank-statements/{bankstatement_id}`

Retrieve a single bank statement by its identifier.

### Path parameters
|Parameter|Description|
|-----|------|
|bankstatement_id|The identifier of the bank statement {{< br >}}**Format**: ??? (e.g., `???`). Required. |

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-statements/12345678" \
-H "accept: application/json" \
-H "Authentication: Bearer <your-account-API-key>"
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "encoded_content": "string",
    "filename": "bank-statement.pdf",
    "mime_type": "application/pdf"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Next steps
You have added one or multiple bank accounts to a merchant account. Next, you can add UBOs and websites using the unique merchant account `id` .

{{< two-buttons

href-1="/tools/api-onboarding/create-account" header-1="Previous" text-1="Create a merchant account" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-ubos" header-2="Next" text-2="Add UBO details" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

