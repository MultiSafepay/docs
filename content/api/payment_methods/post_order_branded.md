---
weight: 340
meta_title: "API - Create A Branded Credit Card order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## Branded credit card 

> POST - /order

```shell 
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "VISA",
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
        "locale": "it_IT",
         "ip_address": "31.148.195.10"
    }
}
```
> JSON Response

```shell 

{
  "success": true,
  "data": {
    "order_id": "My-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=it_IT"
  }
}
```


* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string   | Specifies the payment flow for the checkout process. Options: redirect.                   |
| gateway                         | string   | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: CREDITCARD, VISA and MASTERCARD.  |
| order_id                        | string   | The unique identifier from your system for the order.                                    |
| currency                        | string   | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with.  |
| amount                          | integer  | The amount (in cents) that the customer needs to pay.                                      |
| description                     | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this.  |
| payment_options                 | object   |                             |
| notification_url                | string   | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url                    | string   | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                      | string   | Customer will be redirected to this page after a failed payment.  | 
| customer                        | object   |                                 |
| locale                          | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 
| ip_address                      | string   | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                               |

 The desired logo of a branded credit card will only be shown if the locale is correctly supplied in a transaction request.

Please make sure to check out our dedicated documentation on [CartaSi](/payment-methods/branded-credit-cards/cartasi-what-is-it/), [Cartes Bancaires](/payment-methods/branded-credit-cards/carte-bleue-what-is-it/), [Dankort](/payment-methods/branded-credit-cards/dankort-what-is-it/) and [Postepay](/payment-methods/branded-credit-cards/postepay/). 

```shell

CartaSi and Postepay 

    "customer": {
        "locale": "it_IT 
```

```shell 

Dankort 

    "customer": {
        "locale": "da_DK"
```

```shell 

Cartes Bancaires 

    "customer": {
        "locale": "fr_FR"
```
