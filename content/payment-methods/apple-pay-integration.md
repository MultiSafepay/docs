---
title: "Apple Pay integration"
category: 6298bd782d1cf4006032e765
order: 504
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'apple-pay-integration'
---

# Direct integration

With direct integration, the ** Pay** button appears in your checkout page. Customers complete payment without being redirected to a [payment page](/docs/payment-pages/).

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/applePayHero.png" align ="center"/>

## Prerequisites

### Apple server requirements

- All pages that include Apple Pay must be served over HTTPS.
- Your domain must have a valid SSL certificate.
- Your server must support the TLS protocol version 1.2 or later.

> ℹ More information
> See Apple Developer – [Setting up your server](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

### Customer device compatibility

To see which Apple products are compatible with Apple Pay, see Apple Developer – [Devices compatible with Apple Pay](https://support.apple.com/en-us/HT208531).

## 1. Validate your domain

1. [Download the compressed Apple Pay domain validation files](https://github.com/MultiSafepay/docs/raw/master/static/domain-validation-apple-pay/domain-validation-apple-pay.zip).
2. Unzip the folder and select the relevant file.
3. Place the domain validation file at:
    ```
    https://{your-domain}/.well-known/apple-developer-merchantid-domain-association
    ```

## 2. Request to register 

To request registration for Apple Pay direct, email the relevant site ID to <sales@multisafepay.com>

## 3. Check for Apple Pay support

1. From the customer's device, check if Apple Pay is supported:
    ```
    if (window.ApplePaySession && ApplePaySession.canMakePayments())
    ```

    > ℹ More information
    > See Apple Developer – [Checking for Apple Pay availability](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/checking_for_apple_pay_availability).

2. If Apple Pay is supported, display the ** Pay** button in your checkout page.

    To style the button, see Apple Developer:

    - [Buttons&nbsp;and&nbsp;marks](https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/#apple-pay-mark)
    - [Displaying Apple Pay Buttons Using CSS](https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css)

## 4. Create an Apple Pay session

### Client-side integration

When the customer clicks or taps the ** Pay** button:

1. Create a paymentRequest object containing details about the order.
    ```
    var ApplePayRequest = {
        "countryCode": "NL",
        "currencyCode": "EUR",
        "merchantCapabilities": [
            "supports3DS"
        ], 
        "supportedNetworks": [
        "amex",
        "maestro",
        "masterCard",
        "visa",
        "vPay"
        ],
        "requiredBillingContactFields":[
            "postalAddress",
            "billingAddress"
        ],
        "total":{
            "label": "Your Merchant Name",
            "type": "final",
            "amount": 15.95
        }
    };
    ```
    
    <details id="how-to-request-shipping-and-billing-details">
    <summary>How to request shipping and billing details</summary>
    <br>

    You can use the `requiredBillingContactFields` to collect the customer's billing and/or shipping details through Apple Pay. If the customer hasn't previously provided their billing address to Apple Pay, they are prompted to do so.

    > **Note:** The billing and shipping details aren't required for creating Apple Pay direct orders with MultiSafepay. However, since the collected details are available to you in unencrypted form, you can use them to reduce checkout friction and manage orders.

    </details>
    <br>

    > **Note:** The `total.amount` is in euro's, whereas the amount set in our order requests is in cents. 

    > ℹ More information
    > To learn more about the `ApplePayRequest` object, see Apple Developer – [ApplePayRequest](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayrequest).

2. Create an Apple Pay session.

    ```
    var session = new ApplePaySession(10, ApplePayRequest);
    ```

    - As the first argument, specify the Apple Pay version your site supports. 
    - As the second argument, pass the `ApplePayRequest` object.
    <br>

    > ℹ More information
    > To learn more about Apple Pay versions, see Apple Developer – [Apple Pay on the web version history](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history).

    > **Note:** You can only create a session within a user gesture handler. For example, you can create the session when the user taps the ** Pay** button.

    > ℹ More information
    > See Apple Developer – [Creating an Apple Pay session](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/creating_an_apple_pay_session).

3. Create an `onvalidatemerchant` event handler that is called once the Apple Pay payment form is displayed to the customer.
    ```
    session.onvalidatemerchant = function (event) {
        var validationUrl = event.validationURL;
        var originDomain = window.location.hostname;

    // Request an Apple Pay merchant session from your server
    // The server-side request requires the validationUrl and originDomain values

    // If you succesfully create a session from your server
        session.completeMerchantValidation(<apple-pay-payment-session-data>);
    };
    ```
    > ℹ More information
    > See Apple Developer:
    > - [Providing merchant validation](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation)
    > - [onvalidatemerchant](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778021-onvalidatemerchant)

4. To begin the merchant validation process, call the `session.begin()` method. 
    ```
    session.begin();
    ```

    This displays the Apple Pay payment sheet to the customer and triggers the `onvalidatemerchant` event handler.

### Server-side integration

1. With the `validationUrl` and `originDomain` from the client's device, request an Apple Pay merchant session from MultiSafepay.

    ```
    curl -X POST "https://api.multisafepay.com/v1/json/wallets/sessions/applepay" \
    -H "Authorization: Bearer <website-api-key>" \
    -d '{
    "origin_domain": "originDomain",
    "validation_url": "validationUrl",
    }'
    ```

    > **Note:** The code depends on your server-side framework.

    A successful response contains an Apple Pay merchant `session`, which expires after five minutes.

2. Pass the `session` to the client's device to use as an argument in the `session.completeMerchantValidation()` call.

## 5. Create an order

### Client-side integration

1. Create an `onpaymentauthorized` event handler that is called once the customer authorizes the payment with Touch ID, Face ID, or passcode.
    ```
    session.onpaymentauthorized = function (event) {

        // Create a payment object
        var payment = event.payment;

        // With the payment object:
        // - Create an Apple Pay direct order from your server
        // - Return the success attribute of the response 

        if (success == true) {
            session.completePayment(ApplePaySession.STATUS_SUCCESS);
        // Redirect the customer to your success page
        };
        if (success == false) {
            session.completePayment(ApplePaySession.STATUS_FAILURE);
        };
    };
    ```

    The `payment` object contains the customer's encrypted payment details (`payment.token`) and, if requested, the `billingContact` and `shippingContact`.

    > ℹ More information
    > To learn more about the `payment` object, see Apple Developer:
    > - [payment](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentauthorizedevent/1777999-payment)
    > - [ApplePayPayment](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment)

### Server-side integration

1. From your server, [create an order](/reference/createorder/) > Wallet order. See also Examples > Apple pay direct, using the `payment.token` property. To use the `payment.token` property in the order request, convert it to an escaped JSON string.

2. The billing and shipping details are not required for Apple Pay direct orders. 

    - To access the shipping and/or billing details from the `payment` object, use the `payment.billingContact` and `payment.shippingContact` properties.
    - To add the details to the order request, format them in accordance with [create order](/reference/createorder/) requests.

> **Note:** Billing and shipping data are not encrypted.

> ℹ More information
> To learn more about the `payment` object and its properties, see Apple Developer – [ApplePayPayment](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment).

## 6. Test your integration

To test your Apple Pay direct integration, you need to:

- Meet the [testing prerequisites](/docs/apple-pay-integration#prerequisites)
- Have an [Apple Developer account](https://developer.apple.com/apple-pay/sandbox-testing), configured for Apple Pay, with at least one Apple Pay test card in your wallet

To test, follow these steps:

1. In your integration, click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
2. Sign in to your Apple Developer account and select your test card.
3. Authorize the payment.
  The transaction is completed.
<br>

---

# Redirect integration

With redirect integration, customers are redirected to a [payment page](/docs/payment-pages/) to complete payment.

## API

See:

- [Create order](/reference/createorder/) > Wallet order
- Examples > Apple Pay redirect

## Detecting Apple Pay on the customer's device

If a customer uses an unsupported device to navigate to an Apple Pay payment page, they won't be able to complete the payment. To prevent this, check whether Apple Pay is supported on the customer's device before creating the payment page.

``` 
try {
    if (window.ApplePaySession && ApplePaySession.canMakePayments()) {
    console.log('Apple Pay available');
    // Create an Apple Pay payment page from your server
    }
    } catch (error) {
    console.debug('An error occurred while verifying if Apple Pay is available:', error);
    }
```
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
