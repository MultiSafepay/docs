---
weight: 325 
meta_title: "API - Create a SEPA Direct Debit order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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
        "account_holder_name": "Example",
        "account_holder_iban": "NL87ABNA0000000001",
        "emandate": "mandateID"
    }
}
```
> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 259898679,
    "order_id": "my-order-id-1",
    "created": "2019-03-08T09:23:46",
    "currency": "EUR",
    "amount": 9743,
    "description": "Test order description",
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
 ...
    },
    "payment_details": {
      "recurring_id": "",
      "type": "DIRDEB",
      "account_id": "NL87ABNA0000000001",
      "account_holder_name": "Example",
      "external_transaction_id": "6190662598986790",
      "account_iban": "NL87ABNA0000000001",
    },
    "costs": [
      {
        "transaction_id": 279354751,
        "description": "0.0 For SEPA Direct Debit Transactions",
        "type": "SYSTEM",
        "amount": 0.0
      }
    ],
    "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-order-id-1",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-order-id-1"
  }
}
```

{{< /code-block >}}
{{< description >}}
## SEPA Direct Debit
### Redirect - SEPA Direct Debit

Creates a SEPA Direct Debit [Redirect](/faq/api/difference-between-direct-and-redirect) order.

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

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

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

 Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US.

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

### Direct - SEPA Direct Debit

Creates a SEPA Direct Debit [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: DIRDEB.

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

Contains the personal information of the customer.     

----------------
__gateway_info__ | object

----------------
__account_id__ | string

IBAN to be charged for the transaction.

----------------
__account_holder_name__ | string

Name of the owner of the bank account to be charged for the transaction. 

----------------
__account_holder_iban__ | string

IBAN to be charged for the transaction.

----------------
__emandate__ | string

For your own adminstration, put the e-mandate here.

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)

----------------
__forwarded_ip__ | string

The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [SEPA Direct Debit](/payment-methods/banks/sepa-direct-debit) on our docuemntation page.

{{< /description >}}