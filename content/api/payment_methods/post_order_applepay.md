---
weight: 304
meta_title: "API Reference - Create an Apple Pay transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> Detect Apple Pay on customer's device

```javascript
try {
    if (window.ApplePaySession && ApplePaySession.canMakePayments()) {
    console.log('ApplePay available');
    }
    } catch (error) {
    console.debug('An error occurred while verifying if Apple Pay is available:', error);
    }
```

> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "APPLEPAY",
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
```

> JSON Response

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13ztRF4ic5Kz23n2Lf5F3UzcVqMRxwjlfQw/?lang=nl_NL"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Apple Pay
Creates an Apple Pay [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly.

### How to detect Apple Pay on a device

This JavaScript code will _detect_ if Apple Pay is supported on a device. We recommend you to use this code to avoid an error being displayed if the device does not support Apple Pay. 

Please note that the code will still _display_ Apple Pay as a payment method on a non-supported device. We recommend extending the script to your own needs in order to hide Apple Pay.  

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect.  

----------------
__gateway__ | string

The payment gateway does not need to be specified.

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


Read more about [Apple Pay](/payment-methods/wallet/applepay) on our documentation page.
{{< /description >}}
