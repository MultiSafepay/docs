---
weight: 212
meta_title: "API Reference - Process a refund - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#create-a-refund
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

> JSON response

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
### Refund an order
Process a full or partial [refund](/payments/refunds/) for an order.

**Parameters**

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency to process the refund in.  
This must be the same as the original transaction.  

----------------
`amount` | integer | required

The amount (in cents) to be refunded.  

**Note:** A 0 amount triggers a full refund. Use when the current balance of the transaction is unknown.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
{{% /description %}}
