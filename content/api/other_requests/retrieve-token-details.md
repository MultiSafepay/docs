---
weight: 511
meta_title: "API Reference - Get token details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#get-info-of-a-token
---

{{< code-block >}}

> GET - /recurring/{your_customer_reference}  
/token/{your_token}

> JSON response

```json
{
  "success":true,
  "data":{
    "token":"azbkvsE0up4",
    "code":"MASTERCARD",
    "display":"Card xxxx xxxx xxxx 4444",
    "bin":555555,
    "name_holder":"Testperson-nl",
    "expiry_date":3611,
    "expired":0,
    "last4":4444,
    "model":"cardOnFile"
  }
}
```

{{< /code-block >}}

{{< description >}}

### Get token details

Retreive information about a specific [token](/payments/features/tokenization).

**Parameter**

----------------
`token` | string | required

The unique token linked to the customer reference.  

**Response**

----------------
`code` | string 

The unique identifier of the payment gateway you want to retrieve a list of issuers for.  
Supported identifiers: [iDEAL](#ideal-issuers).

----------------
`display` | string 

How the customer's credit card number is displayed.  

----------------
`name_holder` | string 

The card holder's name.  

----------------
`expiry_date` | integer 

The credit card expiry date.  
Format: `monthnumberdatenumber`.  
Example: December 2025 is formatted as `1225`.

----------------
`expired` | boolean 

Whether the card has expired.

----------------
`last4` | string 

The last 4 digits of the credit card number. 

----------------
`model` | string 

The [recurring model](/payments/features/tokenization/#recurring-models).  
Options: `cardonfile`, `subscription`, `unscheduled`.  

----------------


{{< /description >}}