---
title : "Transactions endpoint"
weight: 30
meta_title: "Transactions API endpoint - MultiSafepay Docs"
layout : "single"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: 'Request your transactions through our API for programmatic integrations.'
logo: '/svgs/API.svg'
aliases: 
    - /tools/transactions-api-endpoint
    - /tools/accounting/transactions-api-endpoint/
---

The transactions API endpoint returns details about transactions in your account. You can use it to automate business operations and gain insights into your transactions.

## Endpoints

The endpoint URLs are:

- **Test:** `https://testapi.multisafepay.com/v1/json/transactions`

- **Live:** `https://api.multisafepay.com/v1/json/transactions`

## API key

You will need a [valid API key](/tools/multisafepay-control/get-your-api-key/). Set your key to the `Authorization` header value, like this:

```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" --header "Content-Type: application/json" --header "api_key: <your-account-api-key>"
```

**Note:** Use your test API key when making requests to the test API URL.

## Parameters 

Requests retrieve an array of all transactions under your account. Use the following optional parameters to filter the returned transactions:

**Note:** For timestamps:  

- All timestamps are in CET/CEST timezone.  
- Multiple formats are supported and automatically detected:  
  - [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601), e.g. `2021-01-01T12:00:00` or `2021-01-01`  
  - [Unix time](https://en.wikipedia.org/wiki/Unix_time), e.g. `1609502400`

------------------
`site_id` | integer (single value or array of values)

Returns transactions for a specific website in your account.  
Default: Returns transactions for all sites under your account.  
Format: `12345`

------------------
`created_from` | string

Timestamp. Returns transactions created on or after the specified date.     

------------------
`created_until` | string 

Timestamp. Returns transactions created before but not on the specified date.  

------------------
`completed_from` | string 

Timestamp. Returns transactions completed on or before the specified date.  

------------------
`completed_until` | string 

Timestamp. Returns transactions completed before but not on the specified date.  

------------------
`financial_status` | string (single value or array of values)

Returns transactions with the specified [transaction status](/payments/multisafepay-statuses/).  
Options: `completed`, `created`, `declined`, `error`, `expired`, `initialized`, `manual`, `new`, `refunded`, `reserved`, `uncleared`, `void`.               

------------------
`status` | string (single value or array of values)

Returns transactions with the specified [order status](/payments/multisafepay-statuses/).  
Options: `completed`, `initialized`, `uncleared`, `declined`, `cancelled`, `void`, `expired`, `refunded`, `partial_refunded`, `reserved`, `chargeback`, `shipped`.   

------------------
`payment_method` | string (single value or array of values)

Returns transactions with the specified payment method.  
Format: See [Retrieve all gateways](/api/#retrieve-all-gateways), e.g. `VISA`. 

------------------
`type` | string (single value or array of values)

Returns transactions of the specified type.  
Options: `admin_fee`, `affiliate_payout`, `automatic_payout`, `chargeback`, `coupon`, `currency_conversion`, `deposit`, `fastcheckout`, `monthly_fee`, `payment`, `refund`, `reserve_chargeback`, `singup_fee`.

------------------
`limit` | integer

Specifies the maximum number of results to return per [page](#pagination).  
Default: `100`.

------------------
`after` | string

Use the `after` cursor to request the next page of [paginated](#pagination) results.  
Format: cursor, e.g. `ZD1ftlaZLHQ90EQCeQ`.

------------------
`before` | string

Use the `before` cursor to request the previous page of [paginated](#pagination) results.  
Format: cursor, e.g. `ZD1gIU-ZLPQ9AEX73Q`.

------------------

## Pagination
Requests to the transactions endpoint can return a lot of results. To make responses easier to handle, we paginate the results. You can specity how many results to return per request using the `limit` parameter. 

To access the next page of the response, use the `after` cursor from the `pager` object in the response. When you make subsequent requests, use the most recently returned `after` cursor to refresh all pages. The last page containing data returns an `after` cursor to an empty page. Further requests to this page are succesfull, but won't return any data or new cursors. 

To access the previous page of the response, use the `before` cursor from the `pager` object.

Results are sorted from newest to oldest. The `after` cursor points to older transactions.

## Example JSON response

```
{
  "amount":0,
  "completed":"string",
  "costs":[
    null
  ],
  "created":"string",
  "currency":"string",
  "debit_credit":"D_C",
  "description":"string",
  "financial_status":"string",
  "invoice_id":"string",
  "order_id":"string",
  "payment_method":"string",
  "site_id":0,
  "status":"string",
  "transaction_id":0,
  "type":"string",
  "var1":"string",
  "var2":"string",
  "var3":"string"
}
```

## Common uses

{{< details title="Overview of all transactions" >}}
**Use case:** I want a complete overview of all transactions in my MultiSafepay account.

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

## Support

For support, email the Integration Team at <integration@multisafepay.com>
