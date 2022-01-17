---
title : "Reconciliation through API"
weight: 30
meta_title: "Reconciliation through API - MultiSafepay Docs"
layout : "single"
short_description: 'Request your transactions through our API for programmatic reconciliation.'
logo: '/svgs/API.svg'
aliases: 
    - /tools/transactions-api-endpoint
    - /tools/accounting/transactions-api-endpoint/
    - /business/accounting/transactions-api-endpoint/
---

The transactions API endpoint returns details about your transactions. You can use it to automate business operations such as reconciliation and gain insights into your transactions.

See API reference – [Retrieve transactions](/api/#retrieve-transactions).

Common uses include:

{{< details title="Overview of all transactions" >}}
**Use case:** I want a complete overview of all my transactions.

**Parameters:** You can use the optional parameters above to filter the transactions returned as required.

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```  
{{< /details >}}

{{< details title="Accounting reconciliation" >}}
**Use case:** I want to match mutations to reconcile the balance in my accounting records.

- Reconciliation may be required by law.
- Automating the reconciliation process can save time and reduce errors.

**Parameters:** All required:

- `type` 
- `completed_from` 
- `completed_until` 

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?completed_from=2021-01-01&completed_until=2021-02-01" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```

{{< /details >}}

{{< details title="Overview of refunds" >}}
**Use case:** I want an overview of refunds paid and to be paid.

**Parameters:** 

- Required: `type`  
- Optional to specify a date range:
  - `created_from` 
  - `created_until` 

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```
{{< /details >}}

For support, email the Integration Team at <integration@multisafepay.com>
