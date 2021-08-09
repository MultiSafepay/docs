---
weight: 220
meta_title: "API Reference - Partial capture - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#partial-capture
---
{{< code-block >}}

> POST - /orders/{order_id}/capture

```json
{
 "amount": 2000,
 "new_order_id": "my-order-id-01",
 "new_order_status": "completed",
 "invoice_id": "",
 "carrier": "",
 "reason": "",
 "memo": ""
}
```
> JSON response


```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
        "order_id": "my-order-id-01"
    }
}
```
{{< /code-block >}}
{{< description >}}
### Partial capture

**Parameter**

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`new_order_id` | integer / string

Your unique identifier for the order.  
Format: Maximum 50 characters.    

----------------
`new_order_status` | string

The current status of the order. 

----------------
`invoice_id` | integer / string

Update an existing order with a reference to your internal invoice ID.  
The invoice ID is added to [reports](/business/accounting/reports/) generated from your MultiSafepay account.  
Format: Maximum 50 characters.  

----------------
`carrier` | string

The name of the shipping company delivering the customer’s order.

----------------
`reason` | string

The capture reason for the order.       

----------------
`memo` | string

The shipping status of the order.     

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------

{{% /description %}}