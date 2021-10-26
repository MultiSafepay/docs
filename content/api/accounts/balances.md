---
weight: 371
meta_title: "API - Balances - MultiSafepay Docs"

---

{{< code-block >}}

> GET /accounts/{affiliated_id}/balances

> Response

```json
{
  "data":[
    {
      "account_id":12345678,
      "amount_available":0,
      "amount_reserved":0,
      "currency":"EUR",
      "id":"qzk7mjd92idka",
      "modified":"2021-01-01 12:34:13"
    }
  ],
  "page":{
    "total":1
  },
  "success":true
}
```

{{< /code-block >}}
{{< description >}}
## Balances

As a partner or primary account holder, use this endpoint to retrieve the balance of an affiliated account. 

For authentication, use your [account API key](/set-up-your-account/site-id-api-key-secure-code/). 

**Parameters**

----------------

`affiliated_id` | query parameter  | required

The account ID of the affiliated account. 

**Responses**

----------------
`account_id` | string

The international bank account number (IBAN) to be charged for the transaction.

----------------
`amount_available` | integer

The available balance in cents.  
This is the total balance minus the reserved balance. 

----------------
`amount_reserved` | integer

The reserved balance in cents. 

----------------
`currency` | string

The currency of the balance.  
Includes every available currency in the affiliate's account.
**Format**: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`id` | string

The balance ID. 

----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

----------------
{{< /description >}}
