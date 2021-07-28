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

### Authentication
Use your [account API key](/set-up-your-account/site-id-api-key-secure-code/). 

To retrieve your account API key, email your account manager at <sales@multisafepay.com>

### Parameters

**affiliated_id** | query parameter

The account ID of the affiliated account you want to charge. **Required**.

**amount** | integer 

The amount to charge in cents. **Required**.

**currency** | string

The currency you want to charge the affiliated account in. **Required**.  
**Format**: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)

**order_id** | string 

Your unique identifier for the charge. **Required**. 

**description** | string

A description of the transaction, which is displayed in both your account and the affiliated account. **Optional**. 

**var1** | string

A variable for storing additional data. **Optional**.

**var2** | string

A second variable for storing additional data. **Optional**.

**var3** | string

A third variable for storing additional data. **Optional**.

{{< /description >}}
