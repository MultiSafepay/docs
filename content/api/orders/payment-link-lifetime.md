---
weight: 207
meta_title: "API Reference - Adjust payment link lifetime - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /api/#days_active--seconds_active
---
{{< code-block >}}

```json 
{
	"days_active": 30,
	"seconds_active": 60,
	"description": "Test order description",
}
```
{{< /code-block >}}

{{< description >}}
### Adjust payment link lifetimes

To set the [lifetime of payment links](/developer/api/adjusting-payment-link-lifetimes), use the `days_active` and `seconds_active` parameters.

- If `seconds_active` is set and larger than 0, then the `seconds_active` value determines the link lifetime.
- If `days_active` is set, then the `days_active` value is used.
- If neither parameter is set, the default is 30 days.
- If both parameters are set, then the `seconds_active` value is used if larger than 0.

**Parameters**

----------------

`days_active` | string

The number of days to make the payment link active for.  
Default: 30 days.

----------------
`seconds_active` | string

The number of seconds to make the payment link active for.  
Default: 30 days.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

{{< /description >}}
