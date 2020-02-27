---
weight: 1355
---
{{< code-block >}}

> PATCH - /capture/<order_id>

```shell
{
 "status": "cancelled",
 "reason": "cancel reservation note text"
}
```
> JSON Response


```shell
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

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| reason                           | string    | Add a short text memo based on the capture reason of the order.       |
| status                           | string    | The order status of the manual capture request.     |

Read more about [Manual Capture](/tools/manual-capture/) on our documentation page.
{{% /description %}}