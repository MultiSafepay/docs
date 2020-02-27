---
weight: 220
meta_title: "API - Create Direct Order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}
> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "My-order-id-2",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "IDEAL",
    "description": "product description",
    "gateway_info": {
        "issuer_id": "0021"
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 00002,
    "order_id": "My-order-id-2",
    "created": "2019-03-04T13:52:07",
    "currency": "EUR",
    "amount": 1000,
    "description": "product description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": null,
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-04T13:52:07",
    "customer": {
      "locale": "en_US",
      "first_name": null,
      "last_name": null,
      "address1": null,
      "address2": null,
      "house_number": null,
      "zip_code": null,
      "city": null,
      "state": null,
      "country": null,
      "country_name": null,
      "phone1": null,
      "phone2": "",
      "email": ""
    },
    "payment_details": {
      "recurring_id": null,
      "type": "IDEAL",
      "account_id": null,
      "account_holder_name": null,
      "external_transaction_id": "0050003729272772",
      "account_iban": "https://betalen.rabobank.nl/ideal-betaling/landingpage?random=44b2dcf080f29f6f52d05802fd76e31285ac564dc974319f0109e1d978234770&trxid=0050003729272772",
      "isser_id": "0021"
    },
    "costs": [
      {
        "transaction_id": 00002,
        "description": "iDEAL Transactions",
        "type": "SYSTEM",
        "amount": 
      }
    ],
    "payment_url": "https://betalen.rabobank.nl/ideal-betaling/landingpage?random=44b2dcf080f29f6f52d05802fd76e31285ac564dc974319f0109e1d978234770&trxid=0050003729272772"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Creates a Direct Order
Creates a direct order.    

Depending on the payment method, additional information should be provided. See each payment method reference for additional information.  

Supported payment methods are:   
IDEAL, CREDITCARDS, PAYAFTER, EINVOICE, KLARNA, KLARNA_ACC, DIRDEB, DIRECTBANK, BANKTRANS, PAYPAL, BELFIUS, ING, KBC, ALIPAY

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string    | Specifies the payment flow for the checkout process. Options: direct.                    |
| order_id                       | integer / string    | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                   |
| currency                       | string    | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer   | The amount (in cents) that the customer needs to pay.                                   |
| gateway                        | string    | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. |
| description                    | string  | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| gateway_info                   | object    |                                                             |
| issuer_id                      | string    | Contains the [issuer_id](/api/#gateway-issuers)    |
| payment_options                | object    |                             |
| notification_url               | string    | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| notification_method            | string    | Sends push notification (POST,GET) default: GET. | 
| redirect_url                   | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                     | string    | Customer will be redirected to this page after a failed payment.  |                                                  
{{< /description >}}