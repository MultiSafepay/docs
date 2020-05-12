---
weight: 410
meta_title: "API - Create a refund - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
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
{{< /code-block >}}
{{< description >}}
## Create a refund
Total or partial refund of an order

| Parameter                  | Type      | Description                                                                                 |
|----------------------------|-----------|---------------------------------------------------------------------------------------------|
| id                         | string    | The unique identifier of the order.                                                         |
| currency                   | string    | The currency to process the refund in. This must be the same as the original transaction.   |
| amount                     | integer   | The amount (in cents) to be refunded. **Please be aware that** an amount of 0 (zero) will trigger a full refund! This can be used the current balance of an transaction is unknown. |
| description                | string    |  A description to be displayed with the transaction in MultiSafepay Control. If supported by the customers bank this description will be displayed on the customers bank statement. |
{{% /description %}}