---
weight: 606
meta_title: "API reference - payment_details (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
```json 
{
  "payment_details":{
    "account_holder_name":null,
    "account_id":"NL87ABNA0000000001",
    "external_transaction_id":null,
    "recurring_id":null,
    "recurring_model":null,
    "type":"DIRECTBANK"
  }
}
```


{{< /code-block >}}

{{< description >}}
## payment details (object)

May contain:  

**Parameters**

----------------
`account_holder_name` | string

The name of the account holder to be charged for the transaction.             

----------------
`account_id`  | string

The international bank account number (IBAN) to be charged for the transaction.

----------------
`recurring_id`  | string

The unique identifier for the recurring payment.

----------------
`recurring_model` | string 

The [recurring model](/features/recurring-payments/#recurring-models).  
Options: `unscheduled`, `subscription`, `cardonfile`.  

----------------
`type` | string

The payment gateway.

----------------
`account_bic` | string

The bank identification code (BIC) of the customer's bank.

----------------
`issuer_id` | integer

The unique identifier of the gateway issuer.  
See [Retrieve gateway issuers](/api/#gateway-issuers).

----------------
`external_transaction_id` | string

The order reference number from a third party, e.g. the payment method.

----------------

{{% /description %}}