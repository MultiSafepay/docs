---
weight: 305
meta_title: "API - Create Bank transfer order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders 

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BANKTRANS",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": " http://www.example.com/client/notification?type=notification",
        "redirect_url": " http://www.example.com/client/notification?type=redirect ",
        "cancel_url": " http://www.example.com/client/notification?type=cancel ",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110"
        "email": "example@multisafepay.com"
    }
}
```
> JSON Response 

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13UeQHxVIs83238WIJdlSYsB4owgNSqZudS/?lang=nl_NL"
    }
}
```

{{< /code-block >}}
{{< description >}}
### Redirect request

The bank transfer payment method can either be a direct or redirect order. In this case, the API calls for a __redirect order__ are illustrated; therefore the consumer will be redirected to the MultiSafepay payment page. Please refer to the dedicated documentation regarding creating a [redirect order](/api/#orders).



| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS. |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                       |
| notification_url                | string   | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url | string	| Customer will be redirected to this page after a successful payment. |
| cancel_url |	string |	Customer will be redirected to this page after a failed payment. |
| customer                       | object |                          |
| locale                          | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. |
| ip_address                      | string   | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                               |
| email                              | string | The email address where the system can send payment instructions to the customer. |


Please make sure you check out our dedicated documentation for [bank transfers](/payment-methods/bank-transfer/).
{{< /description >}}