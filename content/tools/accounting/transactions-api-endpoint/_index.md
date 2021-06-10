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
---

The transactions API endpoint returns the data of transactions under your account. Using this endpoint, you can automate business operations and gain insights into your transactions.

To learn more about its applications, we examine four common use cases:

* [General overview](#create-a-general-overview): Create an overview of all transactions
* [Reconciliation](#perform-reconciliation): Automate your bookkeeping by matching mutations
* [Refunds overview](#create-a-refund-overview): Create an overview of your refunds 

## Usage

To access the transactions API endpoint, use the following URLs:

**Test**  
`https://testapi.multisafepay.com/v1/json/transactions`

**Live**  
`https://api.multisafepay.com/v1/json/transactions`


Requests to this endpoint require a [valid API key](/tools/multisafepay-control/get-your-api-key/). Set your key to the `Authorization` header value, like this:

```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" -H "Content-Type: application/json" -H "Authorization: Bearer <your-api-key>"
```

**Note:** Use your test API key when making a request to our test API.

### Parameters 

This API endpoint has no required parameters. Calls to the transactions endpoint retrieve an array of all transactions under your account.

You can use the following parameters to filter the returned transactions:

| Parameter | Description                  |
|------------------|-----------------------|
| site_id{{< br >}}`integer`| Only transactions for specified `site_id` are returned. Find your site IDs in MultiSafepay Control. By default, requests return the transactions of all sites under your account. {{< br >}} **Format:** Site ID (e.g. `12345`) |
| created_from{{< br >}}`string` | Transactions created from `created_from` are returned. This filter is inclusive, meaning that a transaction created on the specified timestamp is returned. {{< br >}} **Format:** Multiple formats are possible and automatically detected by our API: {{< br >}} → [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-01T12:00:00` or `2021-01-01`) {{< br >}} → [Unix time](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609502400`) {{< br >}} **Note:** All timestamps are in CET/CEST timezone.  |
| created_until{{< br >}}`string` | Transactions created before `created_until` are returned. This filter is exclusive, meaning that a transaction created on the specified timestamp isn't returned. {{< br >}} **Format:** Multiple formats are possible and automatically detected by our API: {{< br >}} → [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-02T12:00:00` or `2021-01-02`) {{< br >}} → [Unix time](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609588800`) {{< br >}} **Note:** All timestamps are in CET/CEST timezone. |
| completed_from{{< br >}}`string` | Transactions completed from `completed_from` are returned. This filter is inclusive, meaning that a transaction completed on the specified timestamp is returned. {{< br >}} **Format:** Multiple formats are possible and automatically detected by our API: {{< br >}} → [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-01T12:00:00` or `2021-01-01`) {{< br >}} → [Unix time](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609502400`) {{< br >}} **Note:** All timestamps are in CET/CEST timezone. |
| completed_until{{< br >}}`string` | Transactions completed before `completed_until` are returned. This filter is exclusive, meaning that a transaction completed on the specified timestamp isn't returned. {{< br >}} **Format:** Multiple formats are possible and automatically detected by our API: {{< br >}} → [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g. `2021-01-02T12:00:00` or `2021-01-02`) {{< br >}} → [Unix time](https://en.wikipedia.org/wiki/Unix_time) (e.g. `1609588800`) {{< br >}} **Note:** All timestamps are in CET/CEST timezone. |
| financial_status{{< br >}}`string`  |  Transactions with matching [financial status](/api/#financial-statuses) are returned. {{< br >}} **Options:** `completed`, `created`, `declined`, `error`, `expired`, `initialized`, `manual`, `new`, `refunded`, `reserved`, `uncleared`, `void`                |
| status{{< br >}}`string` |  Transactions with matching [transaction status](/api/#transaction-statuses) are returned. {{< br >}} **Options:** `completed`, `initialized`, `uncleared`, `declined`, `cancelled`, `void`, `expired`, `refunded`, `partial_refunded`, `reserved`, `chargeback`, `shipped`                |
| payment_method{{< br >}}`string` | Transactions with matching payment method are returned. {{< br >}} **Format:** Follows [gateway](/api/#retrieve-a-gateway) conventions (e.g. `VISA`) |
| type{{< br >}}`string` | Transactions with matching transaction type are returned. {{< br >}} **Options:** `admin_fee`, `affiliate_payout`, `automatic_payout`, `chargeback`, `coupon`, `currency_conversion`, `deposit`, `fastcheckout`, `monthly_fee`, `payment`, `refund`, `reserve_chargeback`, `singup_fee` |
| limit{{< br >}}`integer`  | Set `limit` to specify the maximum number of returned results per [page](#pagination). When `limit` is undefined it defaults to `100` to limit the response size. |
| after{{< br >}}`string` | Use the `after` cursor to request the next page when results are [paginated](#pagination). {{< br >}} **Format:** cursor (e.g. `ZD1ftlaZLHQ90EQCeQ`)
| before{{< br >}}`string` | Use the `before` cursor to request the previous page when results are [paginated](#pagination). {{< br >}} **Format:** cursor (e.g. `ZD1gIU-ZLPQ9AEX73Q`)

**Please note:** values `site_id`, `financial_status`, `status`, `payment_method`, and `type` can be specified either as single values or as arrays containing multiple values.

### Pagination
A request to the transactions endpoint can return a lot of results. To make responses easier to handle, we paginate the results. The amount of transactions returned per call can be specified using the `limit` parameter. If the `limit` parameter is undefined, the value defaults to `100`.

To access the next page of a response, use the `after` cursor from the `pager` object of the response. Upon subsequent calls, use the most recently returned `after` cursor to iterate over all pages. The last page with data will return an `after` pager to an empty page. A request to this page will be succesfull, but won't return any data or new cursors. 

To access the previous page, use the `before` cursor in the `pager` object.

_Please note that results are sorted from new to old. This means that the `after` cursor points to older transactions._

### Response

The returned transactions are `JSON` encoded, in the following structure:

```
{
  "amount": 0,
  "completed": "string",
  "costs": [
    null
  ],
  "created": "string",
  "currency": "string",
  "debit_credit": "D_C",
  "description": "string",
  "financial_status": "string",
  "invoice_id": "string",
  "order_id": "string",
  "payment_method": "string",
  "site_id": 0,
  "status": "string",
  "transaction_id": 0,
  "type": "string",
  "var1": "string",
  "var2": "string",
  "var3": "string"
}
```

## Use cases

### Create a general overview

_I want to have a complete overview of all transactions associated with my MultiSafepay account_

To create a general overview of your transactions, no parameters are required. Optionally, you may use the parameters to filter the transactions to your needs. Keep in mind that the response will be paginated by default.

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

### Perform reconciliation

_I want to match mutations to justify the balance in my accounting or bookkeeping records_

* Reconciliation may be required by law
* Automating the reconciliation process can save time and reduce errors

| Parameter  | Required value |
|------------------|-----------------------|
| type | Retrieve all transaction types by not specifying a value. Alternatively, retrieve only specified transaction types like `payment` or `refund`. |
| completed_from  | Specify the beginning of the period you want to perform reconcilliation over. For example, if you want to perform reconcilliation over January 2021, use the value `2021-01-01` |
| completed_until  | Specify the end of the period you want to perform reconcilliation over. Keep in mind that this value is exclusive. For example, if you want to perform reconcilliation over Janurary 2021, use the value `2021-02-01` |

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?completed_from=2021-01-01&completed_until=2021-02-01" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

### Create a refund overview

_I want to see the refunds associated with customer returns_

* View the orders that are to be paid back as a merchant
* Use the overview to pay back outstanding amounts for returned orders

| Parameter | Required value |
|------------------|-----------------------|
| type (transaction type) | `refund` |

Use parameters `created_from` and `created_until` to specify a date range of creation dates.

#### Sample request
```
curl -X GET "https://testapi.multisafepay.com/v1/json/transactions?type=refund" -H  "accept: application/json" -H  "Authorization: Bearer <your-api-key>"
```

## Support

If you have any issues or questions, [contact our Integration Team](mailto:integration@multisafepay.com)
