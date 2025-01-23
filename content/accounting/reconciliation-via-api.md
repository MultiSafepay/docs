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

# Authentication

To authenticate your API requests, you need to provide the correct <a href="https://docs.multisafepay.com/docs/sites#site-id-api-key-and-security-code" target="_blank">API key</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. The type of key required depends on the request:

- For [Get transaction](/reference/gettransaction/) requests, use the **website API key** of the website where the transaction was made.
- For [List transactions](/reference/listtransactions/) requests, use an **account API key** to list all transaction for an acount. Use a **website API key** to list transactions for a specific website.

# Use cases

## Retrieve individual transactions

Enter the `transaction_id` to retrieve details for a single transaction.

**Example**

```curl
curl -X GET "https://testapi.multisafepay.com/v1/json/{transaction_id}" /
--header "accept: application/json" /
--header "api_key: <your-website-api-key>" /
```

## Overview of all transactions

Use the optional parameters to filter transactions.  

**Example**

```curl
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" /
--header "accept: application/json" /
--header "api_key: <your-account/website-api-key>" /
```

## Accounting reconciliation

Reconciliation may be required by law, and automating the process saves time and reduces errors.  

**Example**

```curl
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?completed_from=2021-01-01&completed_until=2021-02-01" /
--header "accept: application/json" /
--header "api_key: <your-account/website-api-key>" /
```

## Overview of paid/unpaid refunds

**Example**

```curl
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" /
--header "accept: application/json" /
--header "api_key: <your-account/website-api-key>" /
```
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)