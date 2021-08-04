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
    "success": true,
    "data": {
        "token": "azbkvsE0up4",
        "code": "MASTERCARD",
        "display": "Card xxxx xxxx xxxx 4444",
        "bin": 555555,
        "name_holder": "Testperson-nl",
        "expiry_date": 3611,
        "expired": 0,
        "last4": 4444,
        "model": "cardOnFile"
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

----------------


{{< /description >}}