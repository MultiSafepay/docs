---
title: "Reconciliation via API"
category: 62962dee7af1c800355771a1
order: 1
hidden: false
slug: 'api-reconciliation'
---
The transactions API endpoint returns details about your transactions. You can use it to automate reconciliation and gain insight into your transactions.

See API reference for individual transactions – [Get transaction](/reference/gettransaction/).

See API reference to list transactions - [List transactions](/reference/listtransactions/).

# Use cases

## Overview of all transactions

Use the optional parameters to filter transactions.  

**Sample request:**

```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" /
--header "accept: application/json" /
--header "api_key: <your-account-api-key>" /
```

## Accounting reconciliation

Reconciliation may be required by law, and automating the process saves time and reduces errors.  

**Sample request:**

```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?completed_from=2021-01-01&completed_until=2021-02-01" /
--header "accept: application/json" /
--header "api_key: <your-account-api-key>" /
```

## Overview of paid/unpaid refunds

**Sample request:**
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" /
--header "accept: application/json" /
--header "api_key: <your-account-api-key>" /
```
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)