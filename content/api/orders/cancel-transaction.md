---
weight: 225
meta_title: "API Reference - Cancel a transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#cancel-pre-transaction-sessionid
---
{{< code-block >}}
> PATCH - /orders 

```json

{
    "status": "cancelled",
    "exclude_order": 1
}
```

> JSON response

```json
{
  "success": true,
  "data": {}
}
```
{{< /code-block >}}
{{< description >}}
## Cancel a transaction 

Cancel a pretransaction and/or a transaction based on the `sessionid`.

**Parameters**

----------------
__status__ | string | required

The status of the order.  
Fixed value: `cancelled`.

----------------
__exclude_order__ | integer | required

Sets the outcome of the cancellation.  
To cancel the pretransaction, set to `1`.  
To cancel both the pretransaction and the transaction, set to `0`.  
**Note:** Setting to `0` only works if the transaction status is **Initialized**. Transactions with **Reserved** status cannot be cancelled.

----------------
{{% /description %}}