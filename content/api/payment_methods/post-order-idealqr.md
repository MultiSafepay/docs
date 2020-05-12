---
weight: 315
meta_title: "API - Create iDEAL QR order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "iDEALQR",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "gateway_info": {
        "qr_size": 250,
        "allow_multiple": false,
        "allow_change_amount": true,
        "max_amount": 2000
        "min_amount": 500
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
        "order_id": "ideal-test",
        "payment_url": "https://testpayv2.multisafepay.com/connect/896rZ0IGzhJoP2XQdqzMtHYnIG32W68yAGX/?lang=nl_NL",
        "qr_url": "https://qrcode.ideal.nl/qrcode/15b6021c-0102-4ed2-84b3-4a99272179f7.png"
    }
}
```
{{< /code-block >}}

{{< description >}}
## iDEAL QR

Creates a iDEAL QR [Redirect](/faq/api/difference-between-direct-and-redirect/) order.

_Please note: If you would like to test iDEAL QR, please note that this will only work in a Live environment. The Testing environment is currently not available._

{{< alert-notice >}} Please keep in mind that in case min_amount is not set, the value of amount will be used as the min_amount and vice versa.
If max_amount is not set, the value of amount will be used as the max_amount for this transaction. In case both min_amount and max_amount are used, the value of amount will be disregarded. {{< /alert-notice >}}

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s):

| Parameter                      | Type      | Description                                                                             |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string  | Specifies the payment flow for the checkout process. Options: redirect, direct.         |
| gateway                        | string  | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: iDEALQR. |
| order_id                       | integer / string  | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                       | string  | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                   |
| description                    | string  | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is not supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
| payment_options                | object  | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)                             |
| customer                       | object  | Contains personal information about the customer.                                       |
| gateway_info                   | object  |
| qr_size:                       | integer | QR image size in pixels, default: 250 - Sizes are between 100 and 2000, if the value does not meet this rule, default is applied. |
| allow_multiple                 | boolean | With the allow multiple parameter you can specify if a single QR code should be able to be used more than just once. |
| allow_change_amount            | boolean | With the allow_change_amount_parameter you can specify if a customer should be able to change the amount to pay. Requires parameter max_amount or min_amount or both. Often used for donations.|
|  min_amount                  | string  | With the min_amount you can specify what the minimum amount can be in case the allow_change_amount option is activated. The min_amount should not be bigger than the 'amount'. If only min_amount is used, the 'amount' should be more than the min_amount, therefore the 'amount' = max_amount. |
| max_amount                     | string  | With the max_amount you can specify what the maximum amount can be in case the allow_change_amount option is activated. If only max_amount is used, the 'amount' should be less than the max_amount. |


Read more about [iDEAL QR](/payment-methods/banks/idealqr/) on our documentation page.

{{< /description >}}
