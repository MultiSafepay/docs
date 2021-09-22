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

Cancel a pretransaction and/or a transaction based on the `order_id`.

**Parameters**

----------------
`status` | string | required

The [order status](/payments/multisafepay-statuses/).  
Value: `cancelled`.

----------------
`exclude_order` | integer | required

Sets the outcome of the cancellation.  
To cancel the pretransaction, set to `1`.  
To cancel both the pretransaction and the transaction, set to `0`.  

**Note:** Setting to `0` does not work for iDEAL payments. For other payment methods, it only works if the transaction status is **Initialized**. Transactions with **Reserved** status cannot be cancelled.

----------------
{{% /description %}}