---
weight: 547
meta_title: "API Reference - Update card expiry date - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /api/#update-credit-card-expiry-date-of-a-token
---

{{< code-block >}}

> PATCH - recurring/{your_customer_reference}  
/update/{your_token}

```json
{
    "expiry_date": "2903"
}
```
> JSON response

```json
{
    "success": true,
    "data": {
        "updated": true
    }
}
```

{{< /code-block >}}

{{< description >}}

### Update card expiry date

Update the credit card expiry date for a token when it expires.

Make a PATCH request with the required placeholders in the URL:

- `your_customer_reference`: Your unique reference number for the customer.
- `your_token`: The unique token identifier associated with the customer.

**Parameter**

----------------
__expiry_date__ | integer | required

The updated expiry date.  
Format: `monthnumberdatenumber`.  
Example: December 2025 is formatted as `1225`.

----------------
{{< /description >}}
