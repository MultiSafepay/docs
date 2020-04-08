---
weight: 317
meta_title: "API - Create ING Home'Pay order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "INGHOME",
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
        "locale": "be_BE"
    }
}
```
> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 260468043,
    "order_id": "my-order-id-1",
    "created": "2019-03-11T14:35:13",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "items": null,
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-11T14:35:13",
    "customer": {
      "locale": "be_BE",
      "first_name": "Testperson-nl",
      "last_name": "Approved",
      "address1": "Kraanspoor",
      "house_number": "39C",
      "zip_code": "1033 SC",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": "Netherlands",
      "phone1": "0208500500",
      "email": "example@multisafepay.com",
    },
    "payment_details": {
      "recurring_id": null,
      "type": "INGHOME",
      "account_id": "https://pay.multisafepay.com/direct/complete/",
      "account_holder_name": null,
      "external_transaction_id": 663302604477,
      "account_iban": ""
    },
    "costs": [
      {
        "transaction_id": 279925866,
        "description": "",
        "type": "SYSTEM",
        "amount": 
      }
    ],
    "payment_url": "https://homepay.ing.be/EN/index.jsp?RETURN_URL=https%3A%2F%2Fpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D260468043&CURRENCY=EUR&AMOUNT=000000100000&RETURN_METHOD=GET&MESSAGE=663302604477&VERSION=2&VENDOR_ID=18204457201&HASH=66d2f141b864621139096d38ce80bc4eff4bb439"
  }
}
```
> POST -/orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "INGHOME",
    "description": "product description",
    "custom_info": {},
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/12RxGzQe6fsi23ml9WkS9lUfwJxo8yYVWgn/?lang=en_US"
  }
}
```


{{< /code-block >}}

{{< description >}}
## ING Home'Pay
### Direct

Creates an ING Home'Pay Direct order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink. |
gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: INGHOME. |
order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                      |
currency                       | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
amount                         | integer | The amount (in cents) that the customer needs to pay.                                      |
description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
payment_options                | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
customer                       | object | Contains personal information about the customer.                                          |


Read more about [ING Home'Pay](/payment-methods/banks/ing-home-pay/) on our documentation page.

### Redirect
Creates an ING Home'Pay Redirect order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink. |
gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: INGHOME. |
order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                      |
currency                       | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
amount                         | integer | The amount (in cents) that the customer needs to pay.                                      |
description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
payment_options                | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)                                |


Read more about [ING Home'Pay](/payment-methods/banks/ing-home-pay/) on our documentation page.
{{< /description >}}
