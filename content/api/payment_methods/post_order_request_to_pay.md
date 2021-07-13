---
weight: 311
meta_title: "API Reference - Create a Request to Pay transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: [/api/#direct-bank-transfer]
---
{{< code-block >}}

> POST - /orders 

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DBRTP",
    "currency": "EUR",
    "amount": 9743,
    "description": "Test Order Description",
    "manual": false,
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },

```

> JSON Response 

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/12SV72okI6zR23ofq5gdEnaFYZ4qLZ3aFLj/?lang=nl_NL"
  }
}
```

> POST - /orders

```json

{
  "type": "direct",
  "order_id": "my-order-id-1",
  "gateway": "DBRTP",
  "currency": "EUR",
  "amount": 9743,
  "description": "Test Order Description",
  "manual": false,
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
    "amount": 9743,
    "amount_refunded": 0,
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 123456789
        "type": "SYSTEM"
      }
    ],
    "created": "2020-03-25T12:07:00",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "country": "NL",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-03-25T12:07:00",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": null,
      "account_id": null,
      "external_transaction_id": "P-26660200325-0935",
      "recurring_id": null,
      "recurring_model": null,
      "type": "DBRTP"
    },
    "payment_methods": [
      {
        "amount": 9743,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "P-26660200325-0935",
        "payment_description": "Request to Pay",
        "status": "initialized",
        "type": "DBRTP"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789
    "payment_url": "https://pushpayments.db.com/flow/eyJwYXlsb2FkIjp7ImlwaSI6IjE2QjIwREREMjE1NjE0QTc2Rjg0OTMwMDV="
  }
}
```

{{< /code-block >}}

{{< description >}}

## Request to Pay

### Redirect - Request to Pay


Creates a Request to Pay [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: Redirect.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__gateway__ | string

The payment gateway does not need to be specified.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

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

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process. 

----------------





### Direct - Request to Pay

Creates a Request to Pay [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

__type__ | string

Specifies the payment flow for the checkout process. Options: Direct.

----------------
__payment_options__ | object

----------------


Read more about [Request to Pay](/payments/methods/banks/request-to-pay) on our documentation page.

{{< /description >}}