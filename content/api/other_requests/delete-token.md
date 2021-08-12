---
weight: 514
meta_title: "API Reference - Delete a token - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /api/#delete-a-token
---

{{< code-block >}}

> DELETE - /recurring/{your_customer_reference}  
/remove/{your_token}

> JSON response
```json
{
  "success":true,
  "data":{
    "removed":true
  }
}
```

{{< /code-block >}}

{{< description >}}

### Delete a token

Delete a token related to a single customer reference.

Make a DELETE request with the required placeholders in the URL:

- `your_customer_reference`: Your unique reference number for the customer.
- `your_token`: The unique token identifier associated with the customer.

**Parameter**

----------------
`token` | string | required

The unique token identifier linked to the customer reference.  

**Response**

----------------
`removed` | boolean

Whether the token was successfully deleted.

----------------

{{< /description >}}