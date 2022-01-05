---
title : Add bank accounts
layout : single
url: '/api-onboarding/add-bank-accounts/'
aliases: 
    - /tools/api-onboarding/add-bank-accounts
---

Use seven requests to perform actions on bank account details of merchant accounts affiliated to your partner account:

1. [Add bank account](#add-bank-account): add a bank account to a merchant account
2. [List bank accounts](#list-bank-accounts): retrieve a list of all bank accounts
3. [Get bank account](#get-bank-account): retrieve a single bank account
4. [Create payment link](#create-payment-link): create a payment link to verify a bank account
5. [Add bank statement](#add-bank-statement): add a bank statement to verify a bank account
6. [List bank statements](#list-bank-statements): retrieve a list of all bank statements
7. [Get bank statement](#get-bank-statement): retrieve a single bank statement


### The process
The requests above can be split into two steps:

1. **Add bank accounts**: Use the first three requests to add and retrieve bank accounts linked to a merchant account. 
2. **Verify bank accounts**: Use the last four requests to verify bank accounts. You can choose to verify through a payment link or by supplying a bank statement.

## Authentication
All seven bank account requests require a partner account API key. This is not the same as a [website API key](/set-up-your-account/site-id-api-key-secure-code). For more information, email your Partner Manager.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the corresponding API key.

## 1. Add bank account 

`POST` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/bank-accounts?api_key={your-account-api-key}`

Add a new bank account to a merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Affiliate Merchant ID.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|currency <br /> `string`|The currency of the bank account. <br /> **Format**: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `EUR`). Required.|
|holder_name <br /> `string`|Full name of the bank account holder. This can be a natural person, company or other legal entity.  <br /> **Format**: max 40 characters. Required.|
|iban <br /> `string`|The [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) of the bank account. <br /> **Format**: alphanumeric string of up to 34 characters. Required |
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
In addition to the request body parameters.

|Parameter|Description|
|-----|------|
| id  `string` | The unique identifier of the bank account. Referred to as `bankaccount_id`. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/bank-accounts?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "currency" :"EUR",
  "holder_name" :"{affiliate-company-name}",
  "iban" :"NL02ABNA0123456789"
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "currency" :"EUR",
    "holder_name" :"{affiliate-company-name}",
    "iban" :"NL02ABNA0123456789",
    "id" :"t4xwvomi45heq"
  },
  "success": true
}
```
{{< /collapse >}}

---

## 2. List bank accounts

`GET` `https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/bank-accounts?api_key={your-account-api-key}`

Retrieve a list of all bank accounts linked to an affiliated merchant account.

### Path parameters
|Parameter|Description|
|-----|------|
|account_id{{< br >}}`string`|Merchant ID of the affiliated merchant account.{{< br >}}**Format**: 8 character string (e.g., `12345678`). Required.

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|currency <br /> `string`|The currency of the bank account. <br /> **Format**: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `EUR`).|
|holder_name <br /> `string`|Full name of the bank account holder. This can be a natural person, company or other legal entity.  <br /> **Format**: max 40 characters.|
|iban <br /> `string`|The [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) of the bank account. <br /> **Format**: alphanumeric string of up to 34 characters. |
| id <br />  `string` | The unique identifier of the bank account. Referred to as `bankaccount_id`.|
| status <br />  `string` | The screening status of the bank account. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/accounts/{affiliate_account_id}/bank-accounts?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": [
    {
      "currency": "EUR",
      "holder_name": "{affiliate-company-name}",
      "iban": "NL02ABNA0123456789",
      "id" :"t4xwvomi45heq",
      "status": "pending"
    },
    {
      "currency": "USD",
      "holder_name": "{affiliate-company-name}",
      "iban": "NL02ABNA0123456789",
      "id": "ytipdsfs746os",
      "status": "pending"
    }
  ],
  "success": true
}
```
{{< /collapse >}}

---

## 3. Get bank account

`GET` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}?api_key={your-account-api-key}`

Retrieve a single bank account by its identifier.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The unique identifier of the bank account. {{< br >}}**Format**: string (e.g., `upp6ogjqret36`). Required. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
|currency <br /> `string`|The currency of the bank account. <br /> **Format**: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) (e.g., `EUR`).|
|holder_name <br /> `string`|Full name of the bank account holder. This can be a natural person, company or other legal entity.  <br /> **Format**: max 40 characters.|
|iban <br /> `string`|The [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) of the bank account. <br /> **Format**: alphanumeric string of up to 34 characters. |
| id <br />  `string` | The unique identifier of the bank account. Referred to as `bankaccount_id`.|
| status <br />  `string` | The screening status of the bank account. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "currency": "EUR",
    "holder_name": "{affiliate-company-name}",
    "iban": "NL02ABNA0123456789",
    "id": "{bankaccount_id}",
    "status": "pending"
  },
  "success": true
}
```
{{< /collapse >}}

---

## 4. Create payment link

`POST` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/payment-links?api_key={your-account-api-key}`

Create a payment link for a refundable 1 EUR payment. This payment is used to verify the ownership of the associated bank account. Alternatively, supply a copy of a bank statement through the `bank-statements` request.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The unique identifier of the bankaccount. {{< br >}}**Format**: string (e.g., `upp6ogwgfit36`). Required. |

{{< collapse title="Request body parameters" size="h3" >}}
There are no parameters sent in this request.
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Description|
|-----|------|
| bankaccount_id <br />  `string` | The unique identifier of the bank account. |
| payment_link <br />  `string` | A URL where you can complete the refundable 1 EUR payment. |
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/payment-links?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "bankaccount_id": "{bankaccount_id}",
    "payment_link": "https://paymentlink.com/link"
  },
  "success": true
}
```
{{< /collapse >}}

---

## 5. Add bank statement

`POST` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements?api_key={your-account-api-key}`

Upload a bank statement to verify the ownership of the associated bank . Alternatively, create a payment link through the `payment-links` request.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The unique identifier of the bank account. {{< br >}}**Format**: string (e.g., `upp6ogjwpot36`). Required. |

{{< collapse title="Request body parameters" size="h3" >}}
|Parameter|Value|
|-----|------|
|encoded_content|Base64 encoded content. Required.|
|filename <br /> `string`|Name of the bank statement file.  <br /> **Format**: max 250 characters. Required. |
|mime_type <br />  `string`|Media type of the bank statement file . <br /> **Options**: `application/pdf` `image/jpeg`|
{{< /collapse >}}

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Value|
|-----|------|
|account_id <br /> `string`| Merchant ID of the affiliated merchant account. <br /> **Format**: 8 character string (e.g., `12345678`).|
|bankaccount_id <br /> `string`|The unique identifier of the bank account.  <br /> **Format**: string (e.g., `upp6ogjwpot36`).|
|document_type <br />  `string`|Document type of the file. |
|filename <br /> `string`|Name of the bank statement file.  <br /> **Format**: max 250 characters.|
| id <br />  `string`| The unique identifier of the bank statement. Referred to as `{bankstatement_id}`. |
|mime_type <br />  `string`|Media type of the bank statement file . <br /> **Options**: `application/pdf` `image/jpeg`|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X POST "https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements?api_key={your-account-api-key}" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
  "encoded_content": "string",
  "filename": "bank-statement.pdf",
  "mime_type": "application/pdf"
}'
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": "{affiliate_account_id}",
    "bankaccount_id": "{bankaccount_id}",
    "document_type": null,
    "filename": "bank-statement.pdf",
    "id": "4jrp7krwlrafq",
    "mime_type": "application/pdf"
  },
  "success": "true"
}
```
{{< /collapse >}}

---

## 6. List bank statements

`GET` `https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements?api_key={your-account-api-key}`

Retrieve a list of all bank statements associated with a bank account.

### Path parameters
|Parameter|Description|
|-----|------|
|bankaccount_id| The unique identifier of the bankaccount. {{< br >}}**Format**: string (e.g., `upp6ogjwldt36`). Required. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Value|
|-----|------|
|account_id <br /> `string`| Merchant ID of the affiliated merchant account. <br /> **Format**: 8 character string (e.g., `12345678`).|
|bankaccount_id <br /> `string`|The unique identifier of the bank account.  <br /> **Format**: string (e.g., `upp6ogjwpot36`).|
|document_type <br />  `string`|Document type of the file. |
|filename <br /> `string`|Name of the bank statement file.  <br /> **Format**: max 250 characters.|
| id <br />  `string`| The unique identifier of the bank statement. Referred to as `{bankstatement_id}`. |
|mime_type <br />  `string`|Media type of the bank statement file . <br /> **Options**: `application/pdf` `image/jpeg`|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-accounts/{bankaccount_id}/bank-statements?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": "{affiliate_account_id}",
    "bankaccount_id": "{bankaccount_id}",
    "document_type": "bankstatement",
    "filename": "bank-statement.pdf",
    "id": "4jrp7krwlrafq",
    "mime_type": "application/pdf"
  },
  "success": "true"
}
```
{{< /collapse >}}

---

## 7. Get bank statement

`GET` `https://testapi.multisafepay.com/v1/json/bank-statements/{bankstatement_id}?api_key={your-account-api-key}`

Retrieve a single bank statement by its identifier.

### Path parameters
|Parameter|Description|
|-----|------|
|bankstatement_id|The unique identifier of the bank statement {{< br >}}**Format**: string (e.g., `it613jfo4psde`). Required. |

{{< collapse title="Response body parameters" size="h3" >}}
|Parameter|Value|
|-----|------|
|account_id <br /> `string`| Merchant ID of the affiliated merchant account. <br /> **Format**: 8 character string (e.g., `12345678`).|
|bankaccount_id <br /> `string`|The unique identifier of the bank account.  <br /> **Format**: string (e.g., `upp6ogjwpot36`).|
|document_type <br />  `string`|Document type of the file. |
|filename <br /> `string`|Name of the bank statement file.  <br /> **Format**: max 250 characters.|
| id <br />  `string`| The unique identifier of the bank statement. Referred to as `{bankstatement_id}`. |
|mime_type <br />  `string`|Media type of the bank statement file . <br /> **Options**: `application/pdf` `image/jpeg`|
{{< /collapse >}}

{{< collapse title="Sample request" size="h3" >}}
```
curl -X GET "https://testapi.multisafepay.com/v1/json/bank-statements/{bankstatement_id}?api_key={your-account-api-key}" \
--header "accept: application/json" \
```
{{< /collapse >}}

{{< collapse title="Sample response" size="h3" >}}
```
{
  "data": {
    "account_id": "{affiliate_account_id}",
    "bankaccount_id": "{bankaccount_id}",
    "document_type": "bankstatement",
    "filename": "bank-statement.pdf",
    "id": "{bankstatement_id},
    "mime_type": "application/pdf"
  },
  "success": true
}
```
{{< /collapse >}}

---

## Next steps
You have added one or multiple bank accounts to a merchant account. Next, you can add UBOs and websites using the unique affiliate merchant ID.

{{< two-buttons

href-1="/tools/api-onboarding/create-account" header-1="Previous" text-1="Create a merchant account" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-ubos" header-2="Next" text-2="Add UBO details" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

