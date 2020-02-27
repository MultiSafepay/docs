---
weight: 303
meta_title: "API - Create Bancontact QR order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MISTERCASH",
    "currency": "EUR",
    "amount": "1009",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "gateway_info": {
        "qr_enabled": 1
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
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL",
        "qr_url": "https://payv2.multisafepay.com/simulator/qr?mtp_method=mistercash&token=xxxx"
    }
}
```
{{< /code-block >}}
{{< description >}}
## Bancontact QR
* All parameters shown are required field(s)

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
| type                         | string   | Specifies the payment flow for the checkout process. Options: redirect and paymentlink.
| gateway                      | string   | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: MISTERCASH. |
| order_id                     | integer / string   | The unique identifier from your system for the order.                                      |
| currency                     | string   | Has to be EUR. |
| amount                       | integer  | The amount (in cents)  that the customer has to pay.                                     |
| description                  | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options              | object |                            |
| gateway_info                 | object | The qr_enabled = 1 invokes the qr_url. This parameter contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point. This QR image generation can be done at a bpost systems or within the postman application at bpost (if possible). 
| customer                     | object |  |

<aside class="warning">After placing the order, you will receive 2 links as response on a successfull Bancontact QR request: a payment link and a qr_url. This qr_url contains a deeplink to Bancontact/MisterCash which can be encoded into a QR image at any later point. QR image generation can be done at a bpost system or within the postman application at bpost.</aside>

Read more about [Bancontact](/payment-methods/banks/bancontact/) on our documentation page.
{{< /description >}}