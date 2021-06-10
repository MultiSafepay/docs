---
weight: 410
meta_title: "API - Cancel pre-transaction (sessionid) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> PATCH - /orders 

```shell

{
    "status": "cancelled",
    "exclude_order": 1
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {}
}
```
{{< /code-block >}}
{{< description >}}
## Cancel pre-transaction (sessionid)

Cancellation of a transaction based on a sessionid

**Parameters**

----------------
__status__ | string

The status of the order. Options: cancelled

----------------
__exclude_order__ | integer

Indicates the outcome of the cancellation. When exclude_order is set to 1, the pre-transaction (sessionid) will be cancelled. When exclude_order is set to 0, the pre-transaction will be cancelled as well as the transaction itself. __Please note: this only works if transactions are marked as 'Initialized'. A 'Reserved' status cannot be cancelled.__
{{% /description %}}