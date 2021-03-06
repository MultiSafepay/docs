---
weight: 316
meta_title: "API Reference - Create an iDEAL order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "IDEAL",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL"
    }
}
```
> JSON Response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
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
    "gateway": "iDEAL",
    "description": "Test Order Description",
    "custom_info": {},
    "gateway_info": {
        "issuer_id": "0031"
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

```json 
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 123456789
        "type": "SYSTEM"
      }
    ],
    "created": "2020-01-14T12:08:43",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
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
      "locale": "en_US",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "state": "NH",
      "zip_code": "1033SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-14T12:08:43",
    "order_id": "my-order-id-1",
    "payment_details": {
	  "account_bic": "string",
      "account_holder_name": null,
      "account_iban": "*** 1234",
      "account_id": null,
      "external_transaction_id": "1150001181473373",
      "issuer_id": "0031",
      "recurring_id": null,
      "recurring_model": null,
      "type": "IDEAL"
    },
    "payment_methods": [
      {
        "amount": 1000,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "1150001181473373",
        "payment_description": "iDEAL",
        "status": "initialized",
        "type": "IDEAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789
    "payment_url": "https://www.abnamro.nl/en/ideal-betalen/index.html?randomizedstring=8641247395&trxid=1150001181473373"
  }
}
```
{{< /code-block >}}
{{< description >}}
## iDEAL
### Redirect - iDEAL

Creates a iDEAL [Redirect](/developer/api/difference-between-direct-and-redirect) order.

In the case of a _Redirect_ transaction, the customer will be sent to the MultiSafepay payment page where it will then be possible to select iDEAL as a payment method.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: IDEAL.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

Has to be EUR.

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/developer/api/notification-url)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: nl_NL | 

----------------    

### Direct - iDEAL
Creates a iDEAL [Direct](/developer/api/difference-between-direct-and-redirect) order.

In the case of a _Direct_ transaction, the customer has to choose iDEAL and the issuing bank on the checkout page. Once selected, they will be directed to the payment page of the issuing bank, thus skipping the MultiSafepay payment page.

* Direct transaction requires all fields completed properly


* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct.  

----------------
__gateway_info__ | object

----------------
__issuer_id__ | integer

The unique identifier of the [issuer](#gateway-issuers)   

----------------

Read more about [iDEAL](/payments/methods/banks/ideal) on our documentation page.

{{< /description >}}

