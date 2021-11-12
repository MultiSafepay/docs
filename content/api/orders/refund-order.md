---
weight: 212
meta_title: "API reference - Process a refund - MultiSafepay Docs"
---
{{< code-block >}}
> POST - /orders/{order_id}/refunds 

```json
{
  "currency": "EUR",
  "amount": "500",
  "description": "",
  "refund_order_id": "refund-order-id-1234",
  "var1": "test-string1",
  "var2": "test-string2",
  "var3": "test-string3"
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "refund_id":3326969
  }
}
```
{{< /code-block >}}

{{< description >}}
### Refund an order
Process a full or partial [refund](/payments/refunds/) for an order.

To refund pay later orders, see [Refund with shopping cart](/api/#refund-with-shopping-cart).

**Parameters**

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

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`refund_order_id` | string | optional

Your unique identifier for the refund.  If this is not set, the `order_id` is used.  
Format: Maximum 50 characters.

----------------
`var1` / `var2` / `var3` | string | optional

Variables for storing additional data with the refund.

**Response** 

----------------
`transaction_id` | integer

MultiSafepay's identifier for the original transaction for payment (also known as the PSP ID for the original order).

----------------
`refund_id` | integer

MultiSafepay's identifier for the transaction for refund (also known as the PSP ID for the refund).

----------------
{{% /description %}}
