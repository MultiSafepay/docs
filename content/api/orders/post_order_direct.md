---
weight: 220
meta_title: "API Reference - Create a direct order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
> POST - /orders

```json
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

```json
{
  "success": true,
  "data": {
    "transaction_id": 123456789
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
      "first_name": "Simon",
      "last_name": "Smit",
      "company_name": null,
      "address1": "Kraanspoor",
      "address2": "",
      "house_number": "39C",
      "zip_code": "1033SC",
      "city": "Amsterdam",
      "state": "NH",
      "country": "NL",
      "country_name": "The Netherlands",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "email": "simonsmit@example.com"
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
        "transaction_id": 123456789
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

## Create a direct order

Supported payment methods:   
ALIPAY, BANKTRANS, BELFIUS, CBC, CREDITCARD, DIRDEB, DIRECTBANK, EINVOICE, IDEAL, ING, KBC, KLARNA, PAYAFTER, PAYPAL

For additional **required** information, see the relevant [payment method](/api/#payment-methods).


**Parameters**

----------------

__type__ | string | required

The payment flow for the checkout process. Options: `direct`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__currency__ | string | required

The currency you want the customer to pay in.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__gateway_info__ | object

----------------
__issuer_id__ | string

The unique identifier of the gateway issuer.  
To retrieve issuer IDs, see [Retrieve gateway issuers](/api/#gateway-issuers).

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.  
For more information, see [notification_url](/developer/api/notification-url).

----------------
__notification_method__ | string

Sends push notification.  
Options: `POST`, `GET`. Default: `GET`.

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.  
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.  
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------

__close_window__ | bool | optional

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.  
Options: `True`, `False`.  

----------------


{{< /description >}}
