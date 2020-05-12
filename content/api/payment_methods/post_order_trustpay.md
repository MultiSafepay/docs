---
weight: 327
meta_title: "API - Create TrustPay order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders 

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "CZK",
    "amount": 1000,
    "gateway": "",
    "description": "Test Order Description",
    "custom_info": {},
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "country": "CZ",
        "email": "test@example.com"
    }
}
```

> JSON Response


```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=en_CZ"
  }
}
```
{{< /code-block >}}

{{< description >}}
## TrustPay

Creates a TrustPay [Redirect](/faq/api/difference-between-direct-and-redirect/) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string   | Specifies the payment flow for the checkout process. Options: redirect.                   |
| gateway                        | string   | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request] (#retrieve-all-gateways)  |
| order_id                       | integer / string   | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                     |
| currency                       | string   | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. The payment method only processes the currency Czech koruna (CZK). |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                  |
| description                    | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 character. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.  |
| payment_options                | object   |                                                                                        |
| notification_url               | string   | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                                                                                  |
| redirect_url                   | string   | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.   | 
| cancel_url                     | string   | Customer will be redirected to this page after a failed payment.                        | 
| customer                       | object   |                                                                                        |
| first_name                     | string   | The customer’s first name.                                                              |
| last_name                      | string   | The customer’s last name.                                                              | 
| country                        | string   | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)                                                                                                         | 
| email                          | string   | Customer’s provided email address. Used to send Second Chance emails, in fraud checks and the sending bank transfer email.                                                                                                      |
Read more about [TrustPay](/payment-methods/banks/trustly/) on our documentation page.
{{< /description >}}
