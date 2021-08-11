---
weight: 206
meta_title: "API Reference - Cancel an order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#cancel-pre-transaction-sessionid
    - /api/#cancel-a-transaction
---
{{< code-block >}}
> PATCH - /orders 

```json

{
  "status":"canceled",
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

Cancel a pretransaction and/or a transaction based on the `sessionid`.

**Parameters**

----------------
`status` | string | required

The [order status](/payments/multisafepay-statuses/) of the order.  
Fixed value: `canceled`.

----------------
`exclude_order` | integer | required

Sets the outcome of the cancellation.  
To cancel the pretransaction, set to `1`.  
To cancel both the pretransaction and the transaction, set to `0`.  
**Note:** Setting to `0` only works if the transaction status is **Initialized**. Transactions with **Reserved** status cannot be canceled.

----------------
{{% /description %}}