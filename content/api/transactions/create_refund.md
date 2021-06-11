---
weight: 410
meta_title: "API - Create a refund - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```shell

{
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "8",
    "description": "Your refund description"
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 3326965,
    "refund_id": 3326969
  }
}
```
{{< /code-block >}}
{{< description >}}
## Create a refund
Total or partial refund of an order

**Parameters**

----------------
__order_id__ | integer / string

The order_id of the order you want to refund.


----------------
__currency__ | string

The currency to process the refund in. This must be the same as the original transaction.  

----------------
__amount__ | integer

The amount (in cents) to be refunded. **Please be aware that** an amount of 0 (zero) will trigger a full refund! This can be used when the current balance of a transaction is unknown.

----------------
__description__ | string

A description to be displayed with the transaction in MultiSafepay Control. If supported by the customers bank this description will be displayed on the customers bank statement.


{{% /description %}}
