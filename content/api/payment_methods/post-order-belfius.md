---
weight: 306
meta_title: "API - Create Belfius order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "BELFIUS",
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
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```

> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BELFIUS",
    "description": "Test Order Description",
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
        "transaction_id": "279354751",
        "order_id": "my-order-id-1",
        "created": "2019-03-07T13:41:15",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test Order Description",
        "items": null,
        "amount_refunded":"0",
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2020-01-07T13:41:15",
        "customer": {
            "locale": "be_BE",
            "first_name": "Testperson-nl",
            "address1": "Kraanspoor",
            "address2": null,
            "house_number": "39",
            "zip_code": "1033 SC"
            "city": "Amsterdam",
            "country": "NL";,
            "country_name": "Netherlands",
            "phone1": "020 8500 500",
            "email": "",
},
        "payment_details": {
            "recurring_id": null,
            "type": "BELFIUS"
"account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
            "account_holder_name": null,
            "external_transaction_id": "279354751",
},
        "costs": [
{
        "transaction_id": "279354751",
        "description": "Test Order Description",
        "type": "BELFIUS"
        "amount": "1000",
},
        "payment_methods": [
                "account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
                "currency": "EUR",
                "external_transaction_id": "279354751",
                "payment_description": "",
                "status": "initialized",
}
],
  "payment_url": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723"
    }
}
```
{{< /code-block >}}

{{< description >}}
## Belfius
### Redirect
* All parameters shown are required field(s) for a Belfius __Redirect__ transaction.

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
type                           | string | Specifies the payment flow for the checkout process. Options: direct , redirect , paymentlink. |
gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BELFIUS.
order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                       |
currency                       | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
amount                         | integer | The amount (in cents) that the customer needs to pay.                                      |
description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the customer's bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items'or 'shopping_cart' objects for this. |
payment_options                | object |                                |
customer                       | object |                                          |

### Direct

* All parameters shown are required field(s) for a Belfius __Direct__ transaction.

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
type                           | string | Specifies the payment flow for the checkout process. Options: direct , redirect , paymentlink. |
gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BELFIUS.
order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                       |
currency                       | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
amount                         | integer | The amount (in cents) that the customer needs to pay.                                      |
description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the customer's bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items'or 'shopping_cart' objects for this. |
payment_options                | object |                                |
| notification_url            | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                | string    | Customer will be redirected to this page after a successful payment. |
| cancel_url                  | string    | Customer will be redirected to this page after a failed payment.  | 

Read more about [Belfius](/payment-methods/banks/belfius/) on our documentation page.

{{< /description >}}