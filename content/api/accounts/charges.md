---
weight: 372
meta_title: "API - Charges - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> POST /accounts/{affiliated_id}/charges

```json 
{
   "amount" : 10000,
   "currency" : "EUR",
   "order_id" : "Charge_id_1234",
   "description" : "Monthly fees",
   "var1" : null,
   "var2" : null,
   "var3" : null
}
```

> Response

```json
{
    "data": {
        "amount": 10000,
        "costs": [],
        "created": "2021-06-29T11:00:48",
        "currency": "EUR",
        "debit_credit": "D",
        "description": "Monthly fees",
        "financial_status": "completed",
        "order_id": "Charge_id_1234",
        "payment_method": null,
        "site_id": null,
        "status": "completed",
        "transaction_id": "1234567",
        "type": "merchant_settlement",
        "var1": null,
        "var2": null,
        "var3": null 
    },
    "success": true
}
```

{{< /code-block >}}
{{< description >}}
## Charges

As a partner or primary account holder, use this endpoint to move funds from an affiliated account's balance to your own. 

By default, charges are disabled. To enable charges for your account, email your account manager at <sales@multisafepay.com>

For authentication, use your [account API key](/set-up-your-account/site-id-api-key-secure-code/). 

**Parameters**

----------------
**affiliated_id** | query parameter | required

The account ID of the affiliated account you want to charge. 

----------------
**amount** | integer | required

The amount to charge in cents. 

----------------
**currency** | string | required

The currency you want to charge the affiliated account in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
**order_id** | string | required

Your unique identifier for the charge.  

----------------
**description** | string | optional

A description of the transaction, which is displayed in both your account and the affiliated account. 

----------------
`var1` / `var2` / `var3` | string | optional

Variables for storing additional data. 

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------

{{< /description >}}
