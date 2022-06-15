---
title : "Reconciliation via API"
category: 62962dee7af1c800355771a1
order: 300
hidden: false
---
The transactions API endpoint returns details about your transactions. You can use it to automate reconciliation and gain insight into your transactions.

See API reference – [Get transaction](https://docs-api.multisafepay.com/reference/gettransaction).

# Use cases

## Overview of all transactions

Use the optional parameters to filter transactions.  

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```  

## Accounting reconciliation

Reconciliation may be required by law, and automating the process saves time and reduces errors.  

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?completed_from=2021-01-01&completed_until=2021-02-01" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```

## Overview of paid/unpaid refunds

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" --header "accept: application/json" --header "api_key: <your-account-api-key>"
```

> 📘 **Support**
> Email <support@multisafepay.com>
