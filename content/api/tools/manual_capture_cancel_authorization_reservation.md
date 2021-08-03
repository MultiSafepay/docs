---
weight: 1355
meta_title: "API Reference - Cancel an authorized or reserved transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#cancel-authorization--reservation
---
{{< code-block >}}

> PATCH - /capture/{order_id}

```json
{
 "status": "cancelled",
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
__reason__ | string

Add a short text memo based on the capture reason of the order.  

----------------
__status__ | string

The order status of the manual capture request.

----------------

See also [Manual Capture](/payments/features/manual-capture).
{{% /description %}}