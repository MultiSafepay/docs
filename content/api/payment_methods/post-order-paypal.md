---
weight: 323
meta_title: "API - Create a PayPal order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
> POST - /orders 

```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "PAYPAL",
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
    "gateway": "PAYPAL",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "state": "NH",
        "country": "NL",
        "phone": "0208500500",
        "email": "example@multisafepay.com",
        "referrer": "http://test.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [],
    "created": "2020-01-30T11:16:11",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "state": "NH",
      "country": "NL",
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": "39C",
      "last_name": "Approved",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-30T11:16:11",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": "Test-person-nl",
      "account_id": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
      "external_transaction_id": "8K013819T00365502LLL",
      "paypal_eligibility": "",
      "recurring_id": null,
      "recurring_model": null,
      "type": "PAYPAL"
    },
    "payment_methods": [
      {
        "account_holder_name": "Test-person-nl",
        "account_id": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
        "amount": 1000,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "EC-8K013819T00365502L",
        "payment_description": "PayPal",
        "status": "initialized",
        "type": "PAYPAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 329843232,
    "payment_url": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp"
  }
}
```

{{< /code-block >}}

{{< description >}}
## PayPal
### Redirect - PayPal

Creates a PayPal [Redirect](/faq/api/difference-between-direct-and-redirect) order.

{{< alert-notice >}} In PayPal, after a successful payment of a transaction, the order status will be set to _Completed_ and the financial status will remain set to _Initialized_. If the financial status remains _Initialized_, an order cannot be delivered since shipment of an order depends on the financial status. You must ensure that orders are set to _Completed_ for both the order and financial status after a payment. {{< /alert-notice >}}

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. 

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: PAYPAL.

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

__state__ | string

To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), the transaction request needs to have the correct state in the customer address details for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes)

----------------

Read more about [PayPal](/payment-methods/wallet/paypal) on our documentation page.

### Direct - PayPal
Creates a PayPal [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink. 

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: PAYPAL.

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

__state__ | string

To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), the transaction request needs to have the correct state in the customer address details for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes)

----------------


__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [PayPal](/payment-methods/wallet/paypal) on our documentation page.

{{< /description >}}
