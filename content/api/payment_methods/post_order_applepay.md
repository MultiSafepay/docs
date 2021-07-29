---
weight: 304
meta_title: "API Reference - Create an Apple Pay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> Detect Apple Pay on the customer's device

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
See also [Apple Pay](/payments/methods/wallet/applepay).

### Detecting Apple Pay on the customer's device

To avoid an error if the customer's device doesn't support Apple Pay, we recommend running this piece of JavaScript to detect Apple Pay on the device.

**Note:** The code still displays Apple Pay as a payment method on a non-supported device. We recommend extending the script as required to hide Apple Pay.  

### Redirect
- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are **required** fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`.  

----------------
__gateway__ | string

The payment gateway doesn't need to be specified.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`.  
Format: Maximum 35 characters.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
See also [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------

__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

{{< /description >}}
