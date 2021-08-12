---
weight: 373
meta_title: "API - Payouts - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> POST /accounts/{affiliated_id}/payouts

```json 
{
  "amount":10000,
  "currency":"EUR",
  "order_id":"Payout_id_1234",
  "description":"Monthly payout",
  "var1":null,
  "var2":null,
  "var3":null
}
```

> Response

```json
{
  "data":{
    "amount":10000,
    "costs":[
      {
        "amount":50,
        "currency":"EUR"
      }
    ],
    "created":"2021-06-29T12:46:23",
    "currency":"EUR",
    "debit_credit":"D",
    "description":"Monthly payout",
    "financial_status":"reserved",
    "order_id":"Payout_id_1234",
    "payment_method":"BANKTRANS",
    "site_id":null,
    "status":"reserved",
    "transaction_id":"1234567",
    "type":"withdrawal",
    "var1":null,
    "var2":null,
    "var3":null
  },
  "includes":{
    "bankaccount":{
      "currency":"EUR",
      "holder_name":"test",
      "iban":"NL02ABNA0123456789",
      "id":"mk7uq33sl6hep"
    }
  },
  "success":true
}
```

{{< /code-block >}}
{{< description >}}
## Payouts
See also [Making payouts](/account/payouts/).

As a partner or primary account holder, use this endpoint to pay out funds from an affiliated account's balance to a connected bank account. 

By default, payouts for affiliated accounts are disabled. To enable payouts for your affiliated accounts, email your account manager at <sales@multisafepay.com>

For authentication, use your [account API key](/set-up-your-account/site-id-api-key-secure-code/). 

**Parameters**

----------------
`affiliated_id` | query parameter  | required

The account ID of the affiliated account you want to pay out funds from. 

----------------
`amount` | integer | required

The amount to pay out in cents. 

----------------
`currency` | string | required

The currency of the payout.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`order_id` | string | required

Your unique identifier for the payout. 

----------------
`description` | string | optional

A description of the transaction, which is displayed in the affiliated account.

----------------
`var1` / `var2` / `var3` | string | optional

Variables for storing additional data.   

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`order_id` | string 

Your unique identifier for the charge.

----------------
`payment_method` | string

The payment method.

----------------
`site_id` | string

The website identifier.  
See [Site ID, API key, and secure code](/account/site-id-api-key-secure-code/).

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/) of the order.

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`type` | string 

The payment flow for the checkout process.  
Options: `direct`.

----------------
`bankaccount` | object

Contains:  

`currency` | string | required

The currency of the payout.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

`holder_name` | string

The card holder's name.

`iban` | string

The customer's international bank account number (IBAN).

`id` | string

The balance ID. 

----------------

{{< /description >}}
