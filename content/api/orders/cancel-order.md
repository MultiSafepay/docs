---
weight: 206
meta_title: "API reference - Cancel an order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
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

Cancel a pretransaction based on the `order_id`.

**Parameters**

----------------
`status` | string | required

The [order status](/payments/multisafepay-statuses/).  
Value: `cancelled`.

----------------
`exclude_order` | integer | optional

Sets the outcome of the cancellation.  
To cancel the pretransaction, set to `1`.  

----------------
{{% /description %}}