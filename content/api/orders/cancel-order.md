---
weight: 206
meta_title: "API reference - Cancel an order - MultiSafepay Docs"

---
{{< code-block >}}
> PATCH - /orders/{order_id}  

```json
{
  "status":"cancelled",
  "exclude_order":1
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
### Cancel an order 

Cancel an unpaid order using on the `order_id`.

**Parameters**

----------------
`status` | string | required

The [order status](/about-payments/multisafepay-statuses/).  
Value: `cancelled`.

----------------
`exclude_order` | integer | optional

Sets the outcome of the cancellation.  
To cancel the order, set to `1`.  

----------------
{{% /description %}}