---
weight: 1351
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
> JSON Response


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
### Partial Capture


**Parameter**

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__new_order_id__ | integer / string

The unique identifier from your system for the order (max. 50 chars).    

----------------
__new_order_status__ | string

The current status of the order. 

----------------
__invoice_id__ | integer / string

Update an existing order with a reference to your internal invoice id. The invoice id will be added to financial reports and exports generated within your MultiSafepay account (max. 50 chars).  

----------------
__carrier__ | string

The name of the shipping company delivering the customer’s order.

----------------
__reason__ | string

Add a short text memo based on the capture reason of the order.       

----------------
__memo__ | string

Add a short action text memo mentioning the shipping status of the order.     

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string. Required. Max 50 char.

----------------

Read more about [Manual Capture](/payments/features/manual-capture) on our documentation page.
{{% /description %}}