---
weight: 310
meta_title: "API Reference - Create Credit Card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json 

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "CREDITCARD",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123"
  }
}
```

> JSON Response 

```json
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

Creates a Credit Card [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: Redirect.                   |
| gateway                         | string | The unique gateway id to immediately direct the customer to the payment method. Options: [CREDITCARD](/payments/methods/credit-and-debit-cards) |
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer has to pay.                                     |
| description                     | string | A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                 | object |   |
| notification_url                | string    | Endpoint where we will send the notifications to [notification_url](/developer/api/notification-url)|
| redirect_url                    | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.|
| cancel_url                      | string    | Customer will be redirected to this page after a failed payment.  | 



Read more about [credit cards](/payments/methods/credit-and-debit-cards) on our documentation page.

{{< /description >}}