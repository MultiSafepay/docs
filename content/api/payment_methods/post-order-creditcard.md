---
weight: 310
meta_title: "API - Create Credit Card order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders 

```shell 

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "CREDITCARD",
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
## Credit Cards

Creates a Credit Card [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: Redirect.                   |
| gateway                         | string | The unique gateway id to immediately direct the customer to the payment method. Options: [CREDITCARD](/payment-methods/credit-and-debit-cards) |
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer has to pay.                                     |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                 | object |   |
| notification_url                | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)|
| redirect_url                    | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.|
| cancel_url                      | string    | Customer will be redirected to this page after a failed payment.  | 



Read more about [credit cards](/payment-methods/credit-and-debit-cards) on our documentation page.

{{< /description >}}