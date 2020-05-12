---
weight: 250
meta_title: "API - Update an order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> PATCH - /orders/{order_id}

```shell
{
    "status": "shipped",
    "tracktrace_code": "3SMSP0123456789",
    "carrier": "MSP Logistics",
    "ship_date": "01-01-1911",
    "reason": "Fulfilled by warehouse",
    "invoice_id": "AB12345"
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

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| id                          | string  | The unique identifier of the order which should be updated.                                |
| status                      | string  | The new order status. Options: cancelled, shipped.                                   |
| tracktrace_code             | string  | The track and trace code provided by the shipping company.                                 |
| tracktrace_url              | string  | The track and trace URL provided by the shipping company.                                  |
| carrier                     | string  | The name of the shipping company delivering the customer's order.                          |
| ship_date                   | string  | The date that the order was shipped.                                                       |
| reason                      | string  | Add a short free text memo to the order when setting the shipping status.                  |
| invoice_id                  | string  | Update an existing order with a reference to your internal invoice id. The invoice id will be added to financial reports and exports generated within MultiSafepay Control. |
{{< /description >}}