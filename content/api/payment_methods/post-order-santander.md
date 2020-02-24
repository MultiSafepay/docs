---
weight: 324
meta_title: "API - Create Santander Betaalplan order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "SANTANDER",
    "currency": "EUR",
    "amount": 50000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "locale": "en_US",
        "ip_address": "31.148.195.10",
        "forwarded_ip": "",
        "first_name": "John",
        "last_name": "Doe",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "state": "",
        "country": "NL",
        "email": "test@example.com",
        "referrer": "http://example.com",
        "user_agent": "Mozilla//5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "male",
        "phone": "0612345678",
        "email": "youremail@email.com"
    }
}
```
> JSON Response

```shell
{
    "success": true,
    "data": {
        "transaction_id": 2333720,
        "order_id": "my-order-id-1",
        "created": "2017-08-07T10:07:07",
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
        "modified": "2017-08-07T10:07:07",
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
            "type": "SANTANDER",
            "account_id": null,
            "account_holder_name": null,
            "external_transaction_id": null
        },
        "costs": [
            {
                "transaction_id": 406933,
                "description": "Cost Description",
                "type": "SYSTEM",
                "amount": 0.49
            }
        ],
        "payment_url": "https://retailersowtest.santander.nl/EDurables/Home.aspx?guid=XXXXX"
    }
}
```
{{< /code-block >}}

{{< description >}}
## Santander Betaalplan
* All parameters shown are required field(s)

| Parameter                     | Type     | Description                                                                               |
|-------------------------------|----------|-------------------------------------------------------------------------------------------|
type                            | string | Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink. |
gateway                         | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: SANTANDER. |
order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                     |
currency                        | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
amount                          | integer | The amount (in cents) that the customer needs to pay. In this case minimum 30000.         
description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping cart' objects for this. |
payment_options                 | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/).                               |
customer                        | object | Contains the personal information of the customer. <i>Values for first_name and last_name require minimum two characters.</i>    |
gateway_info                    | object | Contains the information of the customer needed for the credit check.                     |
ip_address                      | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/).                                                                            |
forwarded_ip                    | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/).                                                                                                                           |    
Please note that <i>first_name</i> and <i>last_name</i> in the _customer_ object requires minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Make sure you check out our dedicated documentation for [Betaalplan](/payment-methods/betaalplan/).
{{< /description >}}
