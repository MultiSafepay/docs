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
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"APPLEPAY",
  "currency":"EUR",
  "amount":9743,
  "description":"Test Order Description",
  "manual":false,
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  }
}
```

> JSON Response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13ztRF4ic5Kz23n2Lf5F3UzcVqMRxwjlfQw/?lang=nl_NL"
  }
}
```

> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"APPLEPAY",
  "currency":"EUR",
  "amount":1495,
  "description":"Order Description",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification"
  },
  "gateway_info":{
    "payment_token":"{\"paymentData\":{\"data\":\"string\"},\"transactionIdentifier\":\"string\",\"paymentMethod\":{\"network\":\"string\",\"displayName\":\"string\"}}"
  }
}
```

> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13ztRF4ic5Kz23n2Lf5F3UzcVqMRxwjlfQw/?lang=nl_NL"
  }
}
```

{{< /code-block >}}

{{< description >}}

## Apple Pay

See also Payment methods – [Apple Pay](/payments/methods/wallet/applepay).  

### Detecting Apple Pay on the customer's device

To avoid an error if the customer's device doesn't support Apple Pay, we recommend running this piece of JavaScript to detect Apple Pay on the device.

**Note:** The code still displays Apple Pay as a payment method on a non-supported device. We recommend extending the script as required to hide Apple Pay.  

### Apple Pay - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`.  
Format: Maximum 35 characters.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.    
Fixed value: `APPLEPAY`.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string | required

Fixed value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

### Apple Pay - direct 

Creates an Apple Pay direct order. 

With direct integration, the ** Pay** button appears in your checkout page. Customers complete payment without being redirected to a payment page. Integrating Apple Pay direct payments requires a client-side integration with the Apple Pay JS API.

For a detailed integration manual, see [Apple Pay direct integration](/payments/methods/wallet/applepay/direct-integration/)

**Parameters**

----------------
`type` | string | required

Specifies the payment flow for the checkout process. For the Apple Pay direct integration, use `direct`.  

----------------
`order_id` | integer / string | required

Your unique identifier for the order. Maximum number of characters: 35.

----------------
`gateway` | string | required

For Apple Pay payments, use `APPLEPAY`.

----------------
`currency` | string | required

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
`amount` | integer | required

The amount (in cents) that the customer needs to pay.

----------------
`description` | string | required

A text which will be shown with the order in your MultiSafepay account. Max 200 characters.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`gateway_info` | object

Contains:  

`payment_token` | string

The JSON-encoded `payment.token` with the customer's encrypted payment details, generated by the Apple Pay JS API.

For more information, see Apple Pay direct integration – [Create an order](/payments/methods/wallet/applepay/direct-integration/#client-side-integration-1) and Apple Developer – [ApplePayPaymentToken](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymenttoken).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------


{{< /description >}}

