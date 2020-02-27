---
weight: 304
meta_title: "API - Create Bank transfer order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BANKTRANS",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": " http://www.example.com/client/notification?type=notification",
        "redirect_url": " http://www.example.com/client/notification?type=redirect ",
        "cancel_url": " http://www.example.com/client/notification?type=cancel ",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110"
        "email": "example@multisafepay.com"
    }
}
```

> JSON Response 

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13UeQHxVIs83238WIJdlSYsB4owgNSqZudS/?lang=nl_NL"
    }
}
```

> POST - /orders

```shell 

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BANKTRANS",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110",
    }
}

```
> JSON Response 

```shell
{
    "success": true,
    "data": {
        "transaction_id": 343755759,
        "order_id": "my-order-id-1",
        "created": "2019-03-01T16:12:47",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test Order Description",
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
        "modified": "2020-01-06T10:47:18",
        "customer": {
            "address1": null,
            "address2": null,
            "city": null,
            "country": "NL",
            "country_name": null,
            "email": "example@multisafepay.com",
            "first_name": null,
            "house_number": null,
            "last_name": null,
            "locale": "nl_NL",
            "phone1": null,
            "phone2": "",
            "state": null,
            "zip_code": null
        },
        "payment_details": {
            "type": "BANKTRANS"
            "account_holder_name": "",
            "account_id": null,
            "external_transaction_id": "9201727123406700",
            "issuer_id": "vib",
            "recurring_id": null,
            "recurring_model": null,
        },
        "costs": [
            {
                "transaction_id": 343755759,
                "amount": 0,
                "description": "",
                "type": "SYSTEM"
            },
        "payment_methods": {
                "account_holder_name": " ",
                "amount": 1000,
                "currency": "EUR",
                "description": "Test Order Description",
                "external_transaction_id": "234374824",
                "payment_description": "Bank Transfer",
                "status": "initialized",
                "type": "BANKTRANS"
            }
        }
        "gateway_info": {
            "NL07DEUT7351106754": "NL07DEUT7351106754",
            "reference": "234374824",
            "issuer_name": "DB",
            "destination_holder_name": "MultiSafepay",
            "destination_holder_city": "Amsterdam",
            "destination_holder_country": "NL",
            "destination_holder_iban": "NL07DEUT7351106754",
            "destination_holder_swift": "DEUTNL2NXXX",
            "account_holder_country": "NL"
        },
        "payment_url": "http://www.example.com/client/notification?type=redirect&transactionid=apitool_13890779",
        "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=apitool_13890779"
    }
}
```

__Please note: The parameter 'email' must be present, otherwise MultiSafepay will be unable to send the payment details to the customer.__

{{< /code-block >}}

{{< description >}}
## Bank transfer
### Redirect - Bank transfer

The bank transfer payment method can either be a direct or redirect order. In this case, the API calls for a __redirect order__ are illustrated; therefore the customer will be redirected to the MultiSafepay payment page. Read more about creating a [redirect order](/api/#orders)

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS. |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                       |
| notification_url                | string   | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url | string	| Customer will be redirected to this page after a successful payment. |
| cancel_url |	string |	Customer will be redirected to this page after a failed payment. |
| customer                       | object |                          |
| locale                          | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. |
| ip_address                      | string   | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                               |
| email                              | string | The email address where the system can send payment instructions to the customer. |


Read more about [bank transfers](/payment-methods/bank-transfer/) on our documentation page.


### Direct - Bank transfer
* All parameters shown are required field(s)

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS. |
| order_id                       | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                       |
| notification_url                | string   | Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                |
| redirect_url | string	| Customer will be redirected to this page after a successful payment. |
| cancel_url |	string |	Customer will be redirected to this page after a failed payment. |
| customer                       | object |                          |
| locale                          | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. |

In the JSON response for a direct transaction, it is important to send payment instructions to the customer by yourself. Please be aware that all of the parameters can be different for every single transaction. Do not store this information other than for a specific transaction.

| Parameter                  | Type     | Description                                                                                  |
|----------------------------|----------|----------------------------------------------------------------------------------------------|
| gateway_info               | object | Contains the information for the customer in order to pay for the transaction.               |
| reference                  | string | A unique number the customer must mention within the bank transfer in order to have the payment recognized by MultiSafepay. |
| issuer_name                | string | The name of our bank to send the money to.                                                   |
| destination_holder_name    | string | The account holder name registered to our bank account.                                      |
| destination_holder_city    | string | The city which our bank account is registered in.                                            |
| destination_holder_country | string | The country which our bank account is registered in.                                         |
| destination_holder_iban    | string | The International Bank Account Number to send the money to.                                  |
| destination_holder_swift   | string | The Bank Identification Code to send the money to.                                           |
| account_holder_name        | string | The customer's name here if provided in transaction request.                                 |
| account_holder_city        | string | The customer's city here if provided in transaction request.                                 |
| account_holder_country     | string | The customer's country here if provided in transaction request.                              |

{{% /description %}}