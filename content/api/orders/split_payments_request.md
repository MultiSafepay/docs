---
weight: 240
meta_title: "API - Split payments - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

> POST - /orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-4",
    "currency": "EUR",
    "amount": "1000",
    "description": "Split Payment Order",
    "affiliate": {
        "split_payments": [
            {
                "merchant": 1001001,
                "fixed": 112,
                "description": "Fixed fee"
            },
            {
                "merchant": 1001001,
                "percentage": 11.2,
                "description": "percentage fee"
            }
        ]
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-4",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Split Payments
The split payment tool allows you to split the amount of a transaction over several MultiSafepay Control accounts. [Merchants](/faq/getting-started/glossary/#merchant) can choose to split payments based on percentage, a fixed amount or a combination of the two.

Read more about [split payments](/tools/split-payments/) on our documentation page.

| Parameter                             | Type      | Description                                                                      |
|---------------------------------------|-----------|----------------------------------------------------------------------------------|
| type                                  | string    | Specifies the payment flow for the checkout process. Options: direct, redirect and paymentlink.                             |
| gateway                               | string    | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request.     |
| order_id                              | integer / string    | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                             |
| currency                              | string    | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.                |
| amount                                | integer   | The amount (in cents) that the customer needs to pay.                             |
| description                           | string    | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this.        |
| payment_options                       | object    |                                                                                  |
| notification_url                      | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                 |
| redirect_url                          | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.              |
| cancel_url                            | string    | Customer will be redirected to this page after a failed payment.                  | 
| split_payments                        | object    |                                                                                  |
| split_payments.merchant               | integer   | Affiliate AccountID of a MultiSafepay Control.                                                          |
| split_payments.percentage             | float     | Define a percentage of the amount to split.                                       |
| split_payments.fixed                  | integer   | Define amount to split in cents.                                                  |
| split_payments.description            | string    | Description.                                                                      |

{{% /description %}}
