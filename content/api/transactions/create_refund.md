---
weight: 410
meta_title: "API Reference - Create a refund - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```json

{
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 8,
    "description": "Your refund description"
}
```

> JSON Response

```json
{
  "success": true,
  "data": {
    "transaction_id": 123456789
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
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__currency__ | string | required

The currency to process the refund in. This must be the same as the original transaction.  

----------------
__amount__ | integer | required

The amount (in cents) to be refunded. **Please be aware that** an amount of 0 (zero) will trigger a full refund! This can be used when the current balance of a transaction is unknown.

----------------
__description__ | string | required

A description to be displayed with the transaction in your MultiSafepay account. If supported by the customers bank this description will be displayed on the customers bank statement.


{{% /description %}}
