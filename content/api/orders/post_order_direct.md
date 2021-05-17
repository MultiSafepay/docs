---
weight: 220
meta_title: "API - Create a Direct Order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
> POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "IDEAL",
    "description": "product description",
    "gateway_info": {
        "issuer_id": "0021"
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

```shell
{
  "success": true,
  "data": {
    "transaction_id": 00002,
    "order_id": "my-order-id-1",
    "created": "2019-03-04T13:52:07",
    "currency": "EUR",
    "amount": 1000,
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
    "modified": "2019-03-04T13:52:07",
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
      "type": "IDEAL",
      "account_id": null,
      "account_holder_name": null,
      "external_transaction_id": "0050003729272772",
      "account_iban": "*** 1234",
      "isser_id": "0021"
    },
    "costs": [
      {
        "transaction_id": 00002,
        "description": "iDEAL Transactions",
        "type": "SYSTEM",
        "amount": 
      }
    ],
    "payment_url": "https://betalen.rabobank.nl/ideal-betaling/landingpage?random=44b2dcf080f29f6f52d05802fd76e31285ac564dc974319f0109e1d978234770&trxid=0050003729272772"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Create a Direct Order

Depending on the payment method, additional information should be provided. See each payment method reference for additional information.  

Supported payment methods are:   
IDEAL, CREDITCARD, PAYAFTER, EINVOICE, KLARNA, DIRDEB, DIRECTBANK, BANKTRANS, PAYPAL, BELFIUS, ING, KBC, CBC, ALIPAY

**Parameters**

----------------

__type__ | string

Specifies the payment flow for the checkout process. Options: direct.

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
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__gateway_info__ | object

----------------
__issuer_id__ | string

Contains the [issuer_id](/api/#gateway-issuers)  

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__notification_method__ | string

Sends push notification (POST,GET) default: GET.

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

If the payment fails, the customer is redirected to this page.


{{< /description >}}
