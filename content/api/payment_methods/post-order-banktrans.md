---
weight: 307
meta_title: "API - Create Bank transfer order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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
        "country": "NL",
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
        "country": "NL",
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
                "payment_description": "Bank transfer",
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

Creates a Bank transfer [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)

----------------
__email__ | string

The email address where the system can send payment instructions to the customer. 

----------------
__country__ | string

Customer’s provided country code in [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) format e.g. 'NL'. This will provide a local bank account to the customer to pay to, where available.  

----------------


__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [bank transfers](/payment-methods/bank-transfer) on our documentation page.


### Direct - Bank transfer 

Creates a Bank transfer [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BANKTRANS.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)

----------------
__email__ | string

The email address where the system can send payment instructions to the customer. 

----------------
__country__ | string

Customer’s provided country code in [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) format e.g. 'NL'. This will provide a local bank account to the customer to pay to, where available.  

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

In the JSON response for a direct transaction, it is important to send payment instructions to the customer by yourself. Please be aware that all of the parameters can be different for every single transaction. Do not store this information other than for a specific transaction.

**Parameters**

----------------
__gateway_info__ | object

Contains the information for the customer in order to pay for the transaction.

----------------
__reference__ | string

A unique number the customer must mention within the bank transfer in order to have the payment recognized by MultiSafepay.

----------------
__issuer_name__ | string

The name of our bank to send the money to.    

----------------
__destination_holder_name__ | string

The account holder name registered to our bank account.

----------------
__destination_holder_city__ | string

The city which our bank account is registered in.  

----------------
__destination_holder_country__ | string

The country which our bank account is registered in.

----------------
__destination_holder_iban__ | string

The International Bank Account Number to send the money to.

----------------
__destination_holder_swift__ | string

The Bank Identification Code to send the money to. 

----------------
__account_holder_name__ | string

The customer's name here if provided in transaction request. 

----------------
__account_holder_city__ | string

The customer's city here if provided in transaction request.  

----------------
__account_holder_country__ | string

The customer's country here if provided in transaction request.  


{{% /description %}}