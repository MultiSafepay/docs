---
weight: 305
meta_title: "API - Create Bancontact order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MISTERCASH",
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

## Bancontact
Creates a Bancontact [Redirect](/faq/api/difference-between-direct-and-redirect/) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
| type                         | string   | Specifies the payment flow for the checkout process. Options: redirect and paymentlink.
| gateway                      | string   | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: MISTERCASH. |
| order_id                     | string   | The unique identifier from your system for the order.                                      |
| currency                     | string   | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html))  you want the customer to pay with. |
| amount                       | integer  | The amount (in cents)  that the customer needs to pay.                                     |
| description                  | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options              | object |                            |
| customer                     | object |  |

Read more about [Bancontact](/payment-methods/banks/bancontact/) on our documentation page.
{{< /description >}}
