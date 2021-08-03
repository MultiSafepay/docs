---
weight: 265
meta_title: "API Reference - Update an order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> PATCH - /orders/{order_id}

```json
{
    "id": "MSP12345",
    "status": "shipped",
    "tracktrace_code": "3SMSP0123456789",
    "tracktrace_url": "http://tracktrace-url.com/",
    "carrier": "MSP Logistics",
    "ship_date": "01-01-1911",
    "reason": "Fulfilled by warehouse",
    "invoice_id": "AB12345",
    "invoice_url": "http://mspinvoice-AB12345.com",
    "po_number": ""
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
## Update an order
Update the details of an order.

**Parameters**

----------------
__id__ | string | required

The unique identifier of the order you want to update.

----------------
__status__ | string | required

The new status of the order.  
Options: `cancelled`, `shipped`.

----------------
__tracktrace_code__ | string | optional

The track and trace code provided by the shipping company.

----------------
__carrier__ | string | optional

The name of the shipping company delivering the customer's order.

----------------
__ship_date__ | string | optional

The date that the order was shipped.

----------------
__reason__ | string | optional

Add a short, free text memo for the order when setting the shipping status.

----------------
__invoice_id__ | string | optional

Add your invoice ID to an existing order.  
The ID appears on [reports](/business/accounting/reports/) generated from your MultiSafepay account.

----------------
__invoice_url__ | string | optional

The invoice URL linking to the `invoice_id`.

----------------
__po_number__ | string | optional

The shipping company's purchase order number.

----------------
{{< /description >}}