---
weight: 1330
---
{{< code-block >}}
> POST - /orders 

```shell 

{
   "type": "direct",
   "gateway": "VISA",
   "order_id": "my-test-order-01",
   "currency": "EUR",
   "amount": 100,
   "description": "test product description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
   "customer": {
       "locale": "nl_NL",
       "ip_address": "10.1.5.1",
       "first_name": "Testperson-nl",
       "last_name": "Approved",
       "address1": "Kraanspoor",
       "house_number": "39C",
       "zip_code": "1033SC",
       "city": "Amsterdam",
       "country": "NL",
       "phone": "0208500500",
       "email": "test@example.com",
       "referrer": "http://example.com",
       "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
   },
   "gateway_info": {
       "flexible_3d": false,
       "card_number": "4111111111111111",
       "card_holder_name": "MultiSafepay",
       "card_expiry_date": "2412",
      "term_url": "http://example.com/?type=term&api_key=<api_key>",
        "card_cvc": "321"
   }
}

```
> JSON Response

```shell 
{
    "success": true,
    "data": {
        "transaction_id": 001,
        "order_id": "my-test-order-01",
        "created": "2019-05-16T10:51:54",
        "currency": "EUR",
        "amount": 100,
        "description": "test product description",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "completed",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2019-05-16T10:51:54",
        "customer": {
            "locale": "nl_NL",
            "first_name": "Testperson-nl",
            "last_name": "Approved",
            "address1": "Kraanspoor",
            "address2": null,
            "house_number": "39C",
            "zip_code": "1033SC",
            "city": "Amsterdam",
            "state": null,
            "country": "NL",
            "country_name": null,
            "phone1": "0208500500",
            "phone2": "",
            "email": "test@example.com"
        },
        "custom_info": {
            "custom_1": null,
            "custom_2": null,
            "custom_3": null
        },
        "payment_details": {
            "type": "VISA",
            "account_id": null,
            "account_holder_name": "MultiSafepay",
            "external_transaction_id": 0010,
            "last4": 1111,
            "card_expiry_date": 2412
        },
        "costs": [
            {
                "transaction_id": 001,
                "description": "0.0 % For Visa CreditCards Transactions",
                "type": "SYSTEM",
                "amount": 0.0
            }
        ],
         "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-test-order-01",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-test-order-01"
    }
}
```
{{< /code-block >}}

{{< description >}}

### Direct, Flexible 3D set on _false_

Flexible 3D is a feature that allows you to enable/disable [3D Secure](/faq/general/glossary/#3d-secure) at API level. The Flexible 3D mandates whether or not a transaction should be completed with the 3D Secure verification or not.

Credit card transactions which are processed with the 3D Secure protocol require a form of authentication of the customer during the payment process. Setting Flexible 3D to _false_ will disable the verfication process.

The parameter flexible_3d is a property of gateway_info in the POST request.

**Activating Flexible 3D Secure will override the rules of the Dynamic 3D settings, meaning that payments will not be enrolled with a 3D authentication.**

**__Please note__: MultiSafepay no longer supports [Flexible 3D](https://docs.multisafepay.com/tools/flexible_3d) with merchants based in Europe due to PSD2 regulations.**

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: VISA and MASTERCARD.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work)  

----------------
__customer__ | object

Contains personal information about the customer.

----------------
__gateway_info__ | object

Defines certain customer data (payment details).

----------------
__flexible_3d__ | boolean

True, enable the 3D Secure authentication. False, disable the 3D Secure authentication.

----------------
__term_url__ | string

URL that is used to instruct the card issuer where to redirect the authorisation query. 

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

{{< /description >}}