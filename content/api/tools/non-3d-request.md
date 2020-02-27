---
weight: 1320
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

> POST - /orders

```shell

{
  "type": "direct",
  "gateway": "CREDITCARD",
  "order_id": "order-1",
  "currency": "EUR",
  "amount": 1000,
  "description": "product description",
  "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "127.0.0.1"
  },
  "gateway_info": {
    "card_number": "4111111111111111",
    "card_holder_name": "Holder Name",
    "card_expiry_date": "1612",
    "cvc": "123"
  }
}
```
> JSON Response    
> When no 3D verification is required, the transaction status response will be processed directly and no form will be sent.

```shell 
{
    "success": true,
    "data": {
        ...
    }
}
```
{{< /code-block >}}

{{< description >}}
### 3D disabled or NON 3D transaction

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string    | Specifies the payment flow for the checkout process. Options: direct.       |
| gateway                        | string    | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: CREDITCARD. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                   |
| currency                       | string    | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer   | The amount (in cents) that the customer needs to pay.        |
| description                    | string    | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object    |                             |
| notification_url               | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                   | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                     | string    | Customer will be redirected to this page after a failed payment.  | 
| customer                       | object    |    |
| locale                         | string    | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 
| ip_address                     | string    | The IP address of the customer. “Required” with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field.  [More info](/faq/api/ip_address/) | 
| gateway_info                   | object    |    |
| card_number                    | string    | Full credit card number. |
| card_holder_name               | string    | Name on the credit card. |
| card_expiry_date               | string    | Card expire date. |
| card_cvc                       | string    | Card CVC number. This might vary depending of the card type. Some cards like MAESTRO may not be required. |

Read more about [Server to Server](/tools/server2server/) on our documentation page.
{{% /description %}}