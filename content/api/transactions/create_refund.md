---
weight: 410
meta_title: "API - Create a refund - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
> POST - /orders/{order_id}/refunds 

```shell

{
    "currency": "EUR",
    "amount": "8",
    "description": "Your refund description"
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 3326965,
    "refund_id": 3326969
  }
}
```
{{% /code %}}
{{% description %}}
## Create a refund
Total or partial refund of an order

| Parameter                  | Type      | Description                                                                                 |
|----------------------------|-----------|---------------------------------------------------------------------------------------------|
| id                         | string    | The unique identifier of the order.                                                         |
| currency                   | string    | The currency to process the refund in. This must be the same as the original transaction.   |
| amount                     | integer   | The amount (in cents) to be refunded. **Please be aware that** an amount of 0 (zero) will trigger a full refund! This can be used the current balance of an transaction is unknown. |
| description                | string    |  A description to be displayed with the transaction in MultiSafepay Control. If supported by the customers bank this description will be displayed on the customers bank statement. |
{{% /description %}}