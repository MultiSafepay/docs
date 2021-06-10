---
weight: 322
meta_title: "API - Create a Mastercard transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
> POST - /orders 

```shell 

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "MASTERCARD",
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
    "ip_address": "127.0.0.1"
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

{{< /code-block >}}

{{< description >}}

## Mastercard

Creates a Mastercard [Redirect](/faq/api/difference-between-direct-and-redirect) order.

{{< alert-notice >}} Besides the individual credit card gateways, MultiSafepay offers you a generic gateway called [CREDITCARD](https://docs.multisafepay.com/api/#credit-cards). This can save space on your mobile checkout. The disadvantage is that the consumer can not immediately see which credit cards can be used. The correct credit card logo will appear automatically when the card holder provides the first digits of the credit card number. {{< /alert-notice >}}

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect.  

----------------
__gateway__ | string

Fixed value: [MASTERCARD](/payment-methods/credit-and-debit-cards/mastercard)

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

__close_window__ | bool

Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process. 

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [Mastercard](/payment-methods/credit-and-debit-cards/mastercard) on our documentation page.

