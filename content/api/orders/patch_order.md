---
weight: 250
meta_title: "API - Update an order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## Update an order

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

Update the order details.

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| id                          | string  | The unique identifier of the order which should be updated.                                |
| status                      | string  | The new order status. Options: cancelled, completed, shipped.                                   |
| tracktrace_code             | string  | The track and trace code provided by the shipping company.                                 |
| tracktrace_url              | string  | The track and trace URL provided by the shipping company.                                  |
| carrier                     | string  | The name of the shipping company delivering the customer's order.                          |
| ship_date                   | string  | The date that the order was shipped.                                                       |
| reason                      | string  | Add a short free text memo to the order when setting the shipping status.                  |
| invoice_id                  | string  | Update an existing order with a reference to your internal invoice id. The invoice id will be added to financial reports and exports generated within MultiSafepay Control. |
