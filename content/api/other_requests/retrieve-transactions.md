---
weight: 530
meta_title: "API reference - Retrieve transactions - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
> GET - /transactions


> JSON response

```json
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
{{< /code-block >}}

{{< description >}}
## Retrieve transactions

Get details about transactions in your account. 

For use cases and sample requests, see [Transactions endpoint](/business/accounting/transactions-api-endpoint/).

Requests retrieve an array of all transactions under your account. See also [Pagination](/developer/api/pagination/).

**API key**

Set your [API key](/tools/multisafepay-control/get-your-api-key/) to the `Authorization` header value:

`curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" --header "Content-Type: application/json" --header "api_key: <your-account-api-key>"`


**Note:** Use your test API key when making requests to the test API URL.

**Parameters**

Use the following optional parameters to filter the returned transactions:

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
Options: `admin_fee`, `affiliate_payout`, `automatic_payout`, `chargeback`, `coupon`, `currency_conversion`, `deposit`, `fastcheckout`, `monthly_fee`, `payment`, `refund`, `reserve_chargeback`, `signup_fee`.

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

{{% /description %}}