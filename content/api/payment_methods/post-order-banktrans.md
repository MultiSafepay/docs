---
weight: 304
meta_title: "API - Create Bank transfer order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}

> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "BANKTRANS",
    "currency": "EUR",
    "amount": "9743",
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
        "transaction_id": 2340670,
        "order_id": "my-order-id-1",
        "created": "2017-09-29T15:55:09",
        "currency": "EUR",
        "amount": 9743,
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
        "modified": "2017-09-29T15:55:09",
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
            "type": "BANKTRANS",
            "account_id": null,
            "account_holder_name": "",
            "external_transaction_id": "9201727123406700"
        },
        "costs": [
            {
                "transaction_id": 413281,
                "description": "",
                "type": "SYSTEM",
                "amount": 0
            }
        ],
        "gateway_info": {
            "reference": "5190692604051530",
            "issuer_name": "DB",
            "destination_holder_name": "MultiSafepay",
            "destination_holder_city": "Amsterdam",
            "destination_holder_country": "NL",
            "destination_holder_iban": "NL63DEUT7351103321",
            "destination_holder_swift": "DEUTNL2NXXX",
            "account_holder_name": "{customer's name here if provided in transaction request}",
            "account_holder_city": "{customer's city here if provided in transaction request}",
            "account_holder_country": "{customer's country here if provided in transaction request}"
        },
        "payment_url": "https://www.example.com/client/success?transactionid=my-order-id-1",
        "cancel_url": "https://www.example.com/client/failed?transactionid=my-order-id-1"
    }
}
```
{{% /code %}}

{{% description %}}
## Bank transfer

* All parameters shown are required field(s)

| Parameter                      | Type     | Description                                                                              |
|--------------------------------|----------|------------------------------------------------------------------------------------------|
| type                           | string | Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. |
| gateway                        | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS. |
| order_id                       | string | The unique identifier from your system for the order.                                    |
| currency                       | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                         | integer | The amount (in cents) that the customer needs to pay.                                    |
| description                    | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object |                       |
| customer                       | object |                          |

In the JSON response for a direct transaction, the following is important in order to send instructions to the customer by yourself. Please be aware that all of the parameters can be different for every single transaction. Do not store this information other than for a specific transaction.

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


Please make sure you check out our dedicated documentation for [bank transfers](/payment-methods/bank-transfer/).
{{% /description %}}