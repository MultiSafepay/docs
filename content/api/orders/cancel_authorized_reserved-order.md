---
weight: 221
meta_title: "API Reference - Cancel an authorized or reserved transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#cancel-authorization--reservation
---
{{< code-block >}}

> PATCH - /capture/{order_id}

```json
{
 "status": "canceled",
 "reason": "cancel reservation note text"
}
```
> JSON response


```json
{
    "success": true,
    "data": {
        ...
    }
}
```
{{< /code-block >}}
{{< description >}}
### Cancel an authorized or reserved transaction

**Parameters**

----------------
`reason` | string | required

The capture reason for the order.  

----------------
`status` | string | required

The [order status](/payments/multisafepay-statuses/) of the manual capture request. 

----------------

{{% /description %}}