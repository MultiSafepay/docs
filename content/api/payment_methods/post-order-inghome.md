---
weight: 315
meta_title: "API - Create ING Home'Pay order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "INGHOME",
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
    "transaction_id": 260468043,
    "order_id": "apitool_3401000",
    "created": "2019-03-11T14:35:13",
    "currency": "EUR",
    "amount": 100000,
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
    "modified": "2019-03-11T14:35:13",
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
      "type": "INGHOME",
      "account_id": "https://pay.multisafepay.com/direct/complete/",
      "account_holder_name": null,
      "external_transaction_id": 663302604477,
      "account_iban": "66d2f141b864621139096d38ce80bc4eff4bb439"
    },
    "costs": [
      {
        "transaction_id": 279925866,
        "description": "1 For ING HomePay Transactions",
        "type": "SYSTEM",
        "amount": 1
      }
    ],
    "payment_url": "https://homepay.ing.be/EN/index.jsp?RETURN_URL=https%3A%2F%2Fpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D260468043&CURRENCY=EUR&AMOUNT=000000100000&RETURN_METHOD=GET&MESSAGE=663302604477&VERSION=2&VENDOR_ID=18204457201&HASH=66d2f141b864621139096d38ce80bc4eff4bb439"
  }
}
```
{{% /code %}}

{{% description %}}
## ING Home'Pay
* All parameters shown are required field(s)

| Parameter                    | Type     | Description                                                                                |
|------------------------------|----------|--------------------------------------------------------------------------------------------|
type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink. |
gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways). Options: INGHOME. |
order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                      |
currency                       | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
amount                         | integer | The amount (in cents) that the customer needs to pay.                                      |
description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
payment_options                | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
customer                       | object | Contains personal information about the customer.                                          |


Please make sure you check out our dedicated documentation for [ING Home'Pay](/payment-methods/ing-home-pay/).
{{% /description %}}
