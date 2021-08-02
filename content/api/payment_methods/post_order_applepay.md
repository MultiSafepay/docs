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
    "description": "Test order description",
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

- See also Payment methods – [Apple Pay](/payments/methods/wallet/applepay).  
- Redirect only.

### Detecting Apple Pay on the customer's device

To avoid an error if the customer's device doesn't support Apple Pay, we recommend running this piece of JavaScript to detect Apple Pay on the device.

**Note:** The code still displays Apple Pay as a payment method on a non-supported device. We recommend extending the script as required to hide Apple Pay.  

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.    
Fixed value: `APPLEPAY`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`.  
Format: Maximum 35 characters.

----------------
__currency__ | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__manual__ | string | required

Fixed value: `false`.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------

{{< /description >}}
