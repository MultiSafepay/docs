---
weight: 341 
meta_title: "API - Create Direct Debit order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DIRDEB",
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
        "locale": "nl_NL"
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

> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "DIRDEB",
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
        "locale": "nl_NL",
        "ip_address": "31.148.195.10",
        "forwarded_ip": ""
    },
    "gateway_info": {
        "account_id": "NL87ABNA0000000001",
        "account_holder_name": "J Janse",
        "account_holder_city": "Amsterdam",
        "account_holder_country": "NL",
        "account_holder_iban": "NL87ABNA0000000001",
        "account_holder_bic": "NL",
        "emandate": "madateID"
    }
}
```
> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 259898679,
    "order_id": "y-order-id-1",
    "created": "2019-03-08T09:23:46",
    "currency": "EUR",
    "amount": 9743,
    "description": "Test order description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": "",
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-08T09:23:46",
    "customer": {
      "locale": "nl_NL",
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
      "recurring_id": "",
      "type": "DIRDEB",
      "account_id": "NL87ABNA0000000001",
      "account_holder_name": "J Janse",
      "external_transaction_id": "6190662598986790",
      "account_iban": "NL87ABNA0000000001",
      "account_bic": "ABNANL01"
    },
    "costs": [
      {
        "transaction_id": 279354751,
        "description": "0.3 For Direct Debit Transactions",
        "type": "SYSTEM",
        "amount": 0.3
      }
    ],
    "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-order-id-1",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-order-id-1"
  }
}
```

{{< /code-block >}}
{{< description >}}
## Direct Debit
### Redirect - Direct Debit
When submitting a Direct Debit, the transaction data is checked.    

* If approved, we return the status `initialized`.
* After midnight, the transaction will be forwarded to our bank and the status changes to `uncleared`.
* Once the funds are received on our bank account, the status changes to `completed`.

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


### Direct - Direct Debit

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
type                             | string | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
gateway                           | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: DIRDEB. |
order_id                          | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
currency                          | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
amount                            | integer | The amount (in cents) that the customer needs to pay.                                   |
description                       | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this.  |
payment_options                   | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)                             |
customer                          | object | Contains the personal information of the customer.                                      |
gateway_info                      | object |
account_id                        | string | IBAN to be charged for the transaction.                                                 |
account_holder_name               | string | Name of the owner of the bank account to be charged for the transaction.                |
account_holder_city               | string | Place where the owner of the bank account to be charged for the transaction lives.      |
account_holder_country            | string | Country where the owner of the bank account to be charged for the transaction lives.    |
account_holder_iban               | string | IBAN to be charged for the transaction.                                                 |
account_holder_swift              | string | SWIFT of the bank account to be charged for the transaction.                            |
account_holder_bic                | string | BIC of the bank account to be charged for the transaction.                              |
emandate                          | string | For your own adminstration, put the e-mandate here.                                     |
ip_address                        | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                               |
forwarded_ip                      | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                                                                           |


Please make sure you check out our dedicated documentation for [Direct Debit](/payment-methods/direct-debit/).

{{< /description >}}