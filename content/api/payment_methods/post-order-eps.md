---
weight: 312
meta_title: "API - Create EPS order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "EPS",
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
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
{{< /code-block >}}

{{< description >}}
## EPS

Creates an EPS Redirect order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: redirect.                     | 
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: EPS. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the customers bank statement. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                            |
| customer                       | object |                                      |

Read more about [EPS](/payment-methods/banks/eps/) on our documentation page.
{{< /description >}}