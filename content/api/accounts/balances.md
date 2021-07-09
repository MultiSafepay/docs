---
weight: 371
meta_title: "API - Balances - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> GET /accounts/{affiliated_id}/balances

> Response

```json
{
    "data": [
        {
            "account_id": 12345678,
            "amount_available": 0,
            "amount_reserved": 0,
            "currency": "EUR",
            "id": "qzk7mjd92idka",
            "modified": "2021-01-01 12:34:13"
        }
    ],
    "page": {
        "total": 1
    },
    "success": true
}
```

{{< /code-block >}}
{{< description >}}
## Balances

As a partner or primary account holder, request the balance of an affiliated account. 

By default, balance requests are disabled. To enable balance requests for your account, email your account manager at <sales@multisafepay.com>

### Request parameters

**affiliated_id** | query parameter  

The account ID of the affiliated account. **Required**.

### Response

The response is an array of objects that represent the balance of every available currency.

**account_id**  | integer

The account ID of the affiliated MultiSafepay account.

**amount_available** | integer

The available balance in cents. This is the total balance minus the reserved balance. 

**amount_reserved** | integer

The reserved balance in cents. 

**currency** | string

The currency of the balance.  
**Format**: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)

**id** | string

The balance ID. 

**modified** | string

The timestamp of the last modification of the balance. Modifications may result from incoming payments, refunds, charges, and payouts. **Format**: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)


{{< /description >}}
