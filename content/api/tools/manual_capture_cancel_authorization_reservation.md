---
weight: 1355
---
{{< code-block >}}

> PATCH - /capture/{order_id}

```json
{
 "status": "cancelled",
 "reason": "cancel reservation note text"
}
```
> JSON Response


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
### Cancel Authorization / Reservation

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