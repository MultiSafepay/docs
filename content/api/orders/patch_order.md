---
weight: 250
meta_title: "API - Update an order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> PATCH - /orders/{order_id}

```shell
{
    "id": "MSP12345",
    "status": "shipped",
    "tracktrace_code": "3SMSP0123456789",
    "tracktrace_url": "http://tracktrace-url.com/",
    "carrier": "MSP Logistics",
    "ship_date": "01-01-1911",
    "reason": "Fulfilled by warehouse",
    "invoice_id": "AB12345",
    "invoice_url": "http://mspinvoice-AB12345.com"
    "po_number": ""
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
## Update an order
Update the order details.

**Parameters**

----------------

__id__ | string

The unique identifier of the order which should be updated.

----------------
__status__ | string

The new order status. Options: cancelled, shipped.

----------------
__tracktrace_code__ | string

The track and trace code provided by the shipping company.

----------------
__carrier__ | string

The name of the shipping company delivering the customer's order.

----------------
__ship_date__ | string

The date that the order was shipped.

----------------
__reason__ | string

Add a short free text memo to the order when setting the shipping status.

----------------
__invoice_id__ | string

Update an existing order with a reference to your internal invoice id. The invoice id will be added to financial reports and exports generated within MultiSafepay Control.

----------------
__invoice_url__ | string

The invoice url linking to the invoice_id.

----------------
__po_number__ | string

The Purchase Order number of the shipping company.


{{< /description >}}