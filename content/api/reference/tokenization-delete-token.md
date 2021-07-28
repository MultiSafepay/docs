---
weight: 609
meta_title: "API Reference - Tokenization - Delete token - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> DELETE - recurring/{your_customer_reference}/remove/{your_token}

> JSON Response
```json
{
    "success": true,
    "data": {
        "removed": true
    }
}
```

{{< /code-block >}}

{{< description >}}

### Delete a token

This API call allows you to delete a token related to a single customer reference.

* All of the following parameters are required fields.

**Parameter**

__token__ | string

The unique token linked to the customer reference.  

----------------

{{< /description >}}