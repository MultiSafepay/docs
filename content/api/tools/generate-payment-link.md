---
weight: 1360
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## Generating a payment link

For several scenarios, it can be useful for our merchants to generate a payment link. The payment link allows MultiSafepay Control to create a unique transaction that the payment can be matched with.

> POST - /orders

```shell

{
    "type": "paymentlink",
    "order_id": "test-123",
    "gateway": "",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "en_US"
    }
}
```

> JSON Response


```shell 
{
  "success": true,
  "data": {
    "order_id": "test-123",
    "payment_url": "https://devpayv2.multisafepay.com/connect/89QENbhQYcJoP2CO0kx6pSRrw8v2JFnTynr/?lang=nl_NL"
  }
}
```

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string    | Specifies the payment flow for the checkout process. Fill in 'paymentlink'.       |
| order_id                       | string    | The unique identifier from your system for the order. Required. Max 50 char.      |
| currency                       | string    | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer   | The amount (in cents) that the customer needs to pay.        |
| description                    | string    | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| gateway (optional)             | string    | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. |

The rest of the fields are optional.