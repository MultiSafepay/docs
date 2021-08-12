---
weight: 512
meta_title: "API Reference - Get all customer tokens - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#list-all-tokens-for-a-customer-reference
---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}

> JSON response

```json
{
  "success":true,
  "data":{
    "tokens":[
      {
        "token":"QZTCh7jdk8",
        "code":"MASTERCARD",
        "display":"1234 5678 9101 2345",
        "bin":555555,
        "name_holder":"Test-person-nl",
        "expiry_date":1234,
        "expired":0,
        "last4":1111,
        "recurring_model":"cardOnFile"
      },
      {
        "token":"GVXjq3432o4",
        "code":"VISA",
        "display":"1234 5678 9101 2345",
        "bin":411111,
        "name_holder":"WebcashierE2E",
        "expiry_date":1234,
        "expired":0,
        "last4":2222,
        "recurring_model":"unscheduled"
      }
    ]
  }
}
```

{{< /code-block >}}

{{< description >}}

### Get all customer tokens

Retrieve all [tokens](/payments/features/tokenization) related to a specific customer reference.

If there are lots of tokens, you can use the `limit` and `offset` parameters to limit the number of tokens retrieved.

Example: If `limit` is set to 15 and `offset` to 0, then 17 tokens are listed (tokens 0 to 16).

**Parameter**

----------------
`token` | string | required

The unique token identifier linked to the customer reference.  

----------------
`limit` | integer | required

The number of tokens to list.  
If empty, the default is 10.

----------------
`offset` | integer | required

The number of the token to start the list from.  
If empty, the default is 0, i.e. the first token.

**Response**

----------------
`tokens` | object

Contains:  

`code` | string 

The unique identifier of the payment gateway.

`display` | string 

How the customer's credit card number is displayed.

`name_holder` | string 

The card holder's name. 

`expiry_date` | integer 

The credit card expiry date.  
Format: `monthnumberdatenumber`.  
Example: December 2025 is formatted as `1225`.

`expired` | boolean 

Whether the card has expired.

`last4` | string 

The last 4 digits of the credit card number.

`recurring_model` | string 

The [recurring model](/payments/features/tokenization/#recurring-models).  
Options: `cardonfile`, `subscription`, `unscheduled`.  

----------------

{{< /description >}}