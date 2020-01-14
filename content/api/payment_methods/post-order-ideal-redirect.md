---
weight: 313
meta_title: "API - Create iDEAL order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
> POST - /orders 

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "IDEAL",
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
{{% /code %}}

{{% description %}}
## iDEAL /-Redirect 

* All parameters shown are required field(s)

| Parameter                      | Type      | Description                                                                             |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string  | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.
| gateway                        | string  | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: IDEAL. |
| order_id                       | integer / string  | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                    |
| currency                       | string  | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                   |
| description                    | string  | A free text description which will be shown with the order in MultiSafepay Control. If the customers bank supports it this description will also be shown on the customer`s bank statement. |
| payment_options             | object    |                             |
| notification_url            | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                | string    | Customer will be redirected to this page after a successful payment. |
| cancel_url                  | string    | Customer will be redirected to this page after a failed payment.  | 
| customer                    | object    |                                 |
| locale                      | string    | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 
{{% /description %}}