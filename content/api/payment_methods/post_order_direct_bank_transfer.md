---
weight: 396
meta_title: "API - Create Direct Bank Transfer transaction - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders 

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DBRTP",
    "currency": "EUR",
    "amount": "9743",
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },

```

> JSON Response 

```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/12SV72okI6zR23ofq5gdEnaFYZ4qLZ3aFLj/?lang=nl_NL"
  }
}
```

> POST - /orders

```shell 

{
    {
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "DBRTP",
    "currency": "EUR",
    "amount": "9743",
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
```

> JSON Response 

```shell
{
  "success": true,
  "data": {
    "amount": 9743,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 36166179527,
        "type": "SYSTEM"
      }
    ],
    "created": "2020-03-25T12:07:00",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "country": "NL",
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": "39C",
      "last_name": "Approved",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033 SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-03-25T12:07:00",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": null,
      "account_id": null,
      "external_transaction_id": "P-26660200325-0935",
      "recurring_id": null,
      "recurring_model": null,
      "type": "DBRTP"
    },
    "payment_methods": [
      {
        "amount": 9743,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "P-26660200325-0935",
        "payment_description": "Direct Bank Transfer",
        "status": "initialized",
        "type": "DBRTP"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 36166179527,
    "payment_url": "https://pushpayments.db.com/flow/eyJwYXlsb2FkIjp7ImlwaSI6IjE2QjIwREREMjE1NjE0QTc2Rjg0OTMwMDV="
  }
}
```

{{< /code-block >}}

{{< description >}}

## Direct Bank Transfer

Creates a Direct Bank Transfer [Redirect](/faq/api/difference-between-direct-and-redirect/) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: Redirect.                   |
| gateway                         | string | The payment gateway does not need to be specified.
| order_id                        | <nobr>string\|integer</nobr> | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer has to pay.                                     |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                 | object |   |
| notification_url                | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)|
| redirect_url                    | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.|
| cancel_url                      | string    | Customer will be redirected to this page after a failed payment.  | 


### Direct Bank Transfer

Creates a Direct Bank Transfer [Direct](/faq/api/difference-between-direct-and-redirect/) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: Direct.                   |
| payment_options                 | object |   |



Read more about [Direct Bank Transfer](/payment-methods/banks/direct-bank-transfer/) on our documentation page.

{{< /description >}}