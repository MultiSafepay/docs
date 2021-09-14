---
weight: 221
meta_title: "API reference - Cancel an authorized or reserved transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#cancel-authorization--reservation
---
{{< code-block >}}

> PATCH - /capture/{order_id}

```json
{
  "status":"cancelled",
  "reason":"cancel reservation note text"
}
```
> JSON response


```json
{
  "success":true,
  "data":{
    
  }
}
```
{{< /code-block >}}
{{< description >}}
### Cancel an authorized or reserved transaction

**Parameters**

----------------
`status` | string | required

The [order status](/payments/multisafepay-statuses/).

To cancel an authorized or reserved transaction, specify `cancelled`.

----------------
`reason` | string | required

The reason for cancelling the order.

----------------
`description` | string | optional

Use to provide additional information.

----------------


{{% /description %}}