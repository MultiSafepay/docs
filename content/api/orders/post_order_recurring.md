---
weight: 230
meta_title: "API - Recurring payments - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}
>  POST - /orders

```shell
{
    "type": "direct",
    "order_id": "My-order-id-3",
    "gateway": "gatewaycode",
    "recurring_id": "{recurring_id}",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 0000003,
    "order_id": "My-order-id-3",
    "created": "2019-03-04T14:11:37",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": "2 x : GEOMETRIC CANDLE HOLDERS",
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-04T14:11:37",
    "customer": {
      "locale": "en",
      "first_name": null,
      "last_name": "Test Last name",
      "address1": "address 1",
      "address2": "address 2",
      "house_number": 22,
      "zip_code": 29000,
      "city": "Amsterdam ",
      "state": null,
      "country": "NL",
      "country_name": null,
      "phone1": 0208500500,
      "phone2": "",
      "email": "test@test.com"
    },
    "payment_details": {
      "recurring_id": "{recurring_id}",
      "type": "gatewaycode",
      "account_id": 1,
      "account_holder_name": "Testperson-nl",
      "external_transaction_id": "00000003",
      "account_iban": "IBAN Number ",
      "account_bic": "BIC code"
    },
    "costs": [],
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US",
    "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=apitool_"
  }
}
```

{{< /code-block >}}

{{< description >}}
## Recurring Payment

Recurring Payments can be done using Credit Cards (VISA, Mastercard) and SEPA Direct Debit.    

iDEAL and SOFORT Banking can be used for an initial payment as well, and followed up by a recurring payment with SEPA Direct Debit. A merchant account with recurring payment enabled will receive a recurring ID in the transaction response. The recurring ID can be used for future transactions.

For more information about recurring payments, please refer to our [dedicated page](/tools/recurring-payments/)

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string   | Specifies the payment flow for the checkout process. Options: direct.                     |
| gateway                        | string   | Specifies the payment method used for the checkout process. Options: AMEX, DIRDEB, MASTERCARD, VISA. DIRDEB is to be used after initial payment with IDEAL, DIRECTBANK (Sofort) and DIRDEB. |
| order_id                       | integer / string   | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                    |
| recurring_id	                 | integer	| The unique recurring id used for recurring payments.
| currency                       | string   | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer  | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string   | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items'or 'shopping_cart' objects for this. |
| payment_options                | object    |                             |
| notification_url               | string    | Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| notification_method            | string    | Sends push notification (POST,GET) default: GET. | 
| redirect_url                   | string    | Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times. |
| cancel_url                     | string    | Customer will be redirected to this page after a failed payment.  |  

{{< /description >}}
