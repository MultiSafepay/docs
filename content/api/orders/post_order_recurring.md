---
weight: 230
meta_title: "API - Recurring payments - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
>  POST - /orders

```shell
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "gatewaycode",
    "recurring_id": "{recurring_id}",
    "currency": "EUR",
    "amount": "1000",
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
    "transaction_id": 0000003,
    "order_id": "my-order-id-1",
    "created": "2019-03-04T14:11:37",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": "2 x : GEOMETRIC CANDLE HOLDERS",
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-04T14:11:37",
    "customer": {
      "locale": "en",
      "first_name": null,
      "last_name": "Test Last name",
      "address1": "address 1",
      "address2": "address 2",
      "house_number": 22,
      "zip_code": 29000,
      "city": "Amsterdam ",
      "state": null,
      "country": "NL",
      "country_name": null,
      "phone1": 0208500500,
      "phone2": "",
      "email": "test@test.com"
    },
    "payment_details": {
      "recurring_id": "{recurring_id}",
      "type": "gatewaycode",
      "account_id": 1,
      "account_holder_name": "Testperson-nl",
      "external_transaction_id": "00000003",
      "account_iban": "IBAN Number ",
      "account_bic": "BIC code"
    },
    "costs": [],
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US",
    "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=apitool_"
  }
}
```

{{< /code-block >}}

{{< description >}}
## Recurring Payment

Recurring Payments can be done using Credit Cards (VISA, Mastercard) and SEPA Direct Debit.    

iDEAL and SOFORT Banking can be used for an initial payment as well, and followed up by a recurring payment with SEPA Direct Debit. A standard transaction must first be created with recurring payments enabled. The recurring ID can then be requested by [retreiving an order](https://docs.multisafepay.com/api/#retrieve-an-order) and payments can be initiated repeatedly by using [recurring payments](/tools/recurring-payments)

For more information please visit our documentation page to read more about [recurring payments](/tools/recurring-payments)

**Parameters**

----------------

__type__ | string

Specifies the payment flow for the checkout process. Options: direct.

----------------
__gateway__ | string

Specifies the payment method used for the checkout process. Options: AMEX, DIRDEB, MASTERCARD, VISA. DIRDEB is to be used after initial payment with IDEAL, DIRECTBANK (Sofort) and DIRDEB. 

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__recurring_id__ | integer

The unique recurring id used for recurring payments.

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
__notification_method__ | string

Sends push notification (POST,GET) default: GET.

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.  

----------------

{{< /description >}}
