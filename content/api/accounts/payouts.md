---
weight: 373
meta_title: "API - Payouts - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> POST /accounts/{affiliated_id}/payouts

```json 
{
   "amount" : 10000,
   "currency" : "EUR",
   "order_id" : "Payout_id_1234",
   "description" : "Monthly payout",
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
        "costs": [
            {
                "amount": 50,
                "currency": "EUR"
            }
        ],
        "created": "2021-06-29T12:46:23",
        "currency": "EUR",
        "debit_credit": "D",
        "description": "Monthly payout",
        "financial_status": "reserved",
        "order_id": "Payout_id_1234",
        "payment_method": "BANKTRANS",
        "site_id": null,
        "status": "reserved",
        "transaction_id": "1234567",
        "type": "withdrawal",
        "var1": null,
        "var2": null,
        "var3": null
    },
    "includes": {
        "bankaccount": {
            "currency": "EUR",
            "holder_name": "test",
            "iban": "NL02ABNA0123456789",
            "id": "mk7uq33sl6hep"
        }
    },
    "success": true
}
```

{{< /code-block >}}
{{< description >}}
## Payouts

As a partner or primary account holder, use this endpoint to pay out funds from an affiliated account's balance to a connected bank account. 

By default, payouts for affiliated accounts are disabled. To enable payouts for your affiliated accounts, email your account manager at <sales@multisafepay.com>

### Authentication
Use your [account API key](/set-up-your-account/site-id-api-key-secure-code/). 

To retrieve your account API key, email your account manager at <sales@multisafepay.com>

### Parameters

**affiliated_id** | query parameter  

The account ID of the affiliated account you want to pay out funds from. **Required**.

**amount** | integer 

The amount to pay out in cents. **Required**.

**currency** | string

The currency of the payout. **Required**. Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)

**order_id** | string 

Your unique identifier for the payout. **Required**. 

**description** | string

A description of the transaction, which is displayed in the affiliated account. **Optional**. 

**var1** | string

A variable for storing additional data. **Optional**.

**var2** | string

A second variable for storing additional data. **Optional**.

**var3** | string

A third variable for storing additional data. **Optional**.

{{< /description >}}
