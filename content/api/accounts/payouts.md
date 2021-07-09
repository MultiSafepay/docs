---
weight: 372
meta_title: "API - Payouts - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> /accounts/{affiliated_id}/payouts

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

As a partner or primary account holder, use payouts to move funds from an affiliated account's balance to a connected bank account. 

By default, payouts for affiliated accounts are disabled. Contact your account manager to enable payouts for your affiliated accounts.

### Parameters

**affiliated_id** | query parameter

The account ID of the affiliated account that is to be paid out. **Required**.

**amount** | integer 

The amount to pay out in cents. **Required**.

**currency** | string

The currency of the payout. **Required**.  
**Format**: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)

**order_id** | string 

Your unique identifier for the payout. **Required**. 

**description** | string

A description for the transaction. The description is displayed in the affiliated account. **Optional**. 

**var1** | string

A variable used to store additional data. **Optional**.

**var2** | string

A variable used to store additional data. **Optional**.

**var3** | string

A variable used to store additional data. **Optional**.

{{< /description >}}