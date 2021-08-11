---
weight: 219
meta_title: "API Reference - Full capture - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#full-capture
---
{{< code-block >}}

>POST - /orders/{order_id}/capture

```json
{
  "amount":10000,
  "new_order_id":"my-order-id-01",
  "new_order_status":"completed",
  "invoice_id":"001",
  "carrier":"",
  "reason":"",
  "memo":""
}
```
> JSON response


```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "order_id":"my-order-id-01"
  }
}
```
{{< /code-block >}}
{{< description >}}
### Full capture

**Parameters**

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`new_order_id` | integer / string

Your unique identifier for the order.  
Format: Maximum 50 characters.    

----------------
`new_order_status` | string

The updated status of the order. 

----------------
`invoice_id` | integer / string

Update an existing order with a reference to your invoice ID.  
The invoice ID is added to [reports](/business/accounting/reports/) generated from your MultiSafepay account.  Format: Maximum 50 characters.  

----------------
`carrier` | string

The name of the shipping company delivering the customer’s order.

----------------
`reason` | string

The capture reason for the order.       

----------------
`memo` | string

The shipping status of the order.     

**Response**

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------

{{% /description %}}