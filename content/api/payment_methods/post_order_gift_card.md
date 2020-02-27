---
weight: 314
meta_title: "API - Create gift card order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - / order 


```shell 

{
    "type": "redirect",
    "order_id": "my-order-id",
    "gateway": "VVVGIFTCRD",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/json-live/notification?type=notification",
        "redirect_url": "http://www.example.comclient/json-live/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/json-live/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "80.123.456.789",
        "country": "NL",
        "email": "test@example.com"
    }
}
```

> JSON Response
```shell 

{
  "success": true,
  "data": {
    "order_id": "my-order-id",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```  
{{< /code-block >}}

{{< description >}}
## Gift card
* All parameters shown are required field(s)

| Parameter                      | Type      | Description                                                                             |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string  | Specifies the payment flow for the checkout process. Options: redirect.
| gateway                        | string  | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. All gateway name options of our standard gift cards are shown below. Note: we will only preselect the gift card supplied in the gateway.  |
| order_id                       | integer / string  | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                       | string  | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                   |
| description                    | string  | A free text description which will be shown with the order in MultiSafepay Control. If the customers bank supports it this description will also be shown on the customer`s bank statement. |
| payment_options                | object    |                             |
| notification_url               | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                   | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                     | string    | Customer will be redirected to this page after a failed payment.  |
| customer                    | object    |                                 |
| locale                      | string    | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 
| ip_address                  | string    | The IP address of the customer. “Required” with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field.  [More info](/faq/api/ip_address/) | 
| country                     | string    | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) |
| email                       | string    | Customer’s provided email address. Used to send Second Chance emails and in fraud checks.   |





The gateway names of the standard gift cards MultiSafepay offers

| Gift card name                 | Gateway name, gift card     |                         |
|--------------------------------|-----------------------------|-------------------------| 
| Beautyandwellness              | BEAUTYWELL                  |   |
| Bloemencadeaukaart             | BLOEMENCAD                  |   |
| Boekenbon                      | BOEKENBON                   |   |
| Degrotespeelgoedwinkel         | DEGROTESPL                  |   | 
| Fashioncheque                  | FASHIONCHQ                  |   |
| Fashiongiftcard                | FASHIONGFT                  |   |
| Fietsenbon                     | FIETSENBON                  |   |
| Gezondheidsbon                 | GEZONDHEID                  |   |
| Givacard                       | Branded gift cards will provide a gateway name upon release of the personilized gift card by our development team.                 |   |          
| Goodcard                       | GOODCARD                    |   |
| Nationale bioscoopbon          | NATNLBIOSC                  |   | 
| Nationaletuinbon               | NATNLETUIN                  |   |
| Parfumcadeaukaart              | PARFUMCADE                  |   | 
| Sportenfit                     | SPORTENFIT                  |   | 
| Vuur & rook gift card           | VRGIFTCARD                  |   | 
| VVV Cadeaukaart                | VVVGIFTCRD                  |   |
| Webshopgiftcard                | WEBSHOPGFT                  |   |
| Wijncadeau                     | WIJNCADEAU                  |   | 
| Yourgift                       | YOURGIFT                    |   |           

Read more about the [gift cards](/payment-methods/prepaid-cards/gift-cards/) we offer on our documentation page.
{{< /description >}}