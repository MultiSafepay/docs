---
weight: 307
meta_title: "API Reference - Create Bank transfer order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
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
        "ip_address": "123.123.123.123",
        "email": "simonsmit@example.com"
    }
}
```

> JSON Response 

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13UeQHxVIs83238WIJdlSYsB4owgNSqZudS/?lang=nl_NL"
    }
}
```

> POST - /orders

```json 

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
        "ip_address": "123.123.123.123",
        "disable_send_email": false,
    }
}

```
> JSON Response 

```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
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
            "address1": "Kraanspoor",
            "address2": "",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": "The Netherlands",
            "email": "simonsmit@example.com",
            "first_name": "Simon",
            "house_number": "39C",
            "last_name": "Smit",
            "locale": "nl_NL",
            "phone1": "0208500500",
            "phone2": "00310000001",
            "state": "NH",
            "zip_code": "1033SC"
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
                "transaction_id": 123456789
                "amount": 0,
                "description": "",
                "type": "SYSTEM"
            }
        ],
        "payment_methods": {
            "account_holder_name": " ",
            "amount": 1000,
            "currency": "EUR",
            "description": "Test Order Description",
            "external_transaction_id": "234374824",
            "payment_description": "Bank transfer",
            "status": "initialized",
            "type": "BANKTRANS"
        },
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

Creates a Bank transfer [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

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

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)

----------------
__email__ | string

The email address where the system can send payment instructions to the customer. 

----------------
__country__ | string

Customer’s provided country code in [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) format e.g. 'NL'. This will provide a local bank account to the customer to pay to, where available.  

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------


__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [bank transfers](/payments/methods/banks/bank-transfer) on our documentation page.


### Direct - Bank transfer 

Creates a Bank transfer [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All of the following parameters are required fields.


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

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

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)

 ----------------

  __disable_send_email (optional)__	| boolean

Set to _True_ if you will send your own bank transfer payment instructions to customers and do not want MultiSafepay to do this. This value defaults to _false_.


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
