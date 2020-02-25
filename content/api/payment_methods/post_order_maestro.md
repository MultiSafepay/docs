---
weight: 379
meta_title: "API - Create Maestro order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell 
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MAESTRO",
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
    "locale": "nl_NL",
    "ip_address": "127.0.0.1"
  }
}
```

> JSON Response 
```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}

## Maestro

* All parameters shown are required field(s) for a [Maestro](https://docs.multisafepay.com/payment-methods/banks/maestro/) Redirect transaction.

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: redirect.                   |
| gateway                         | string | Fixed value: [MAESTRO](https://docs.multisafepay.com/payment-methods/banks/maestro/)|
| order_id                        | string\|integer | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer has to pay.                                     |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                 | object |   |
| notification_url                | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)|
| redirect_url                    | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.|
| cancel_url                      | string    | Customer will be redirected to this page after a failed payment. | 


Please make sure you check out our dedicated documentation for [Maestro](https://docs.multisafepay.com/payment-methods/banks/maestro/)