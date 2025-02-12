---
title: "Apple Pay direct integration"
category: 6298bd782d1cf4006032e765
order: 5
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'apple-pay-direct'
---

With direct integration, the ** Pay** button appears in your checkout page. Customers complete payment without being redirected to a [payment page](/docs/payment-pages/).

> ℹ️ Note
>
> If using:
>
> - Your own integration, follow all steps in this manual. 
>
> - A [ready-made integration](/docs/our-integrations) which builds the Apple Pay button, start from [Step 1](#1-validate-your-domain), [Step 2](#2-request-to-register), and [Step 6](#6-test-your-integration).

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/applePayHero.png" align ="center"/>

## Prerequisites

### Apple server requirements

- All pages that include Apple Pay must be served over HTTPS.
- Your domain must have a valid SSL certificate.
- Your server must support the TLS protocol version 1.2 or later.

For more information, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server" target="_blank">Setting up your server</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

### Customer device compatibility

To see which Apple products are compatible with Apple Pay, see Apple Developer – <a href="https://support.apple.com/en-us/HT208531" target="_blank">Devices compatible with Apple Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## 1. Validate your domain

1. <a href="https://github.com/MultiSafepay/docs/raw/master/static/domain-validation-apple-pay/domain-validation-apple-pay.zip" target="_blank">Download the compressed Apple Pay domain validation files</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Unzip the folder and select the relevant file.
3. Place the domain validation file at:
    
    ```
    https://{your-domain}/.well-known/apple-developer-merchantid-domain-association
    ```

**⚠️ Note:** For testing, download the domain validation in the **test** folder.

## 2. Request to register 

To request registration for Apple Pay direct, email the relevant website ID to <support@multisafepay.com>

## 3. Check for Apple Pay support

1. From the customer's device, check if Apple Pay is supported:
    ```javascript
    if (window.ApplePaySession && ApplePaySession.canMakePayments())
    ```
    For more information, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/checking_for_apple_pay_availability" target="_blank">Checking for Apple Pay availability</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

2. If Apple Pay is supported, display the ** Pay** button in your checkout page.

    To style the button, see Apple Developer:

    - <a href="https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/#apple-pay-mark" target="_blank">Buttons and marks</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css" target="_blank">Displaying Apple Pay buttons using CSS</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

## 4. Create an Apple Pay session

### Client-side integration

When the customer clicks or taps the ** Pay** button:

1. Create a `paymentRequest` object containing details about the order.
    ```javascript
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

    You can use `requiredBillingContactFields` to collect the customer's billing and/or shipping details from Apple Pay. If the customer hasn't previously provided their billing address to Apple Pay, they are prompted to do so.

    **⚠️ Note:** The billing and shipping details are not required to create Apple Pay direct orders with MultiSafepay. However, since the collected details are available to you in unencrypted form, you can use them to reduce checkout friction and manage orders.
    
    ---

    </details>

    **⚠️ Note:** The `total.amount` is in euros, whereas the `amount` in MultiSafepay order requests is in eurocents. 

    For more information about the `ApplePayRequest` object, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepayrequest" target="_blank">ApplePayRequest</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

2. Create an Apple Pay session.

    ```javascript
    var session = new ApplePaySession(10, ApplePayRequest);
    ```

    - As the first argument, specify the Apple Pay version your website supports. 
    - As the second argument, pass the `ApplePayRequest` object.

    For more information about Apple Pay versions, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history" target="_blank">Apple Pay on the web version history</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

    **⚠️ Note:** You can only create a session within a user gesture handler. For example, you can create the session when the user taps the ** Pay** button.

    For more information, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/creating_an_apple_pay_session" target="_blank">Creating an Apple Pay session</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

3. Create an `onvalidatemerchant` event handler, which is called once the Apple Pay payment form is displayed to the customer.
    ```javascript
    session.onvalidatemerchant = function (event) {
        var validationUrl = event.validationURL;
        var originDomain = window.location.hostname;

    // Request an Apple Pay merchant session from your server
    // The server-side request requires the validationUrl and originDomain values

    // If you succesfully create a session from your server
        session.completeMerchantValidation(<apple-pay-payment-session-data>);
    };
    ```
    For more information, see Apple Developer:
    - <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation" target="_blank">Providing merchant validation</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778021-onvalidatemerchant" target="_blank">onvalidatemerchant</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

4. To begin the merchant validation process, call the `session.begin()` method. 
    ```javascript
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
    "validation_url": "validationUrl"
    }'
    ```

    **⚠️ Note:** The actual code depends on your server-side framework.

    A successful response contains an Apple Pay merchant `session`, which expires after five minutes.

2. Pass the `session` to the client's device to use as an argument in the `session.completeMerchantValidation()` call.

## 5. Create an order

### Client-side integration

Create an `onpaymentauthorized` event handler, which is called once the customer authorizes the payment with Touch ID, Face ID, or passcode.

```javascript
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

For more information about the `payment` object, see Apple Developer:
- <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentauthorizedevent/1777999-payment" target="_blank">payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment" target="_blank">ApplePayPayment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

### Server-side integration

1. From your server, [create an order](/reference/createorder/) > Wallet order. <br> See also Examples > Apple pay direct, using the `payment.token` property. <br> To use the `payment.token` property in the order request, convert it to an escaped JSON string.

**⚠️ Note:** The billing and shipping details are **not** required for Apple Pay direct orders. 

2. To access the shipping and/or billing details from the `payment` object, use the `payment.billingContact` and `payment.shippingContact` properties.

3. To add the details to the order request, format them in accordance with [create order](/reference/createorder/) requests.

**⚠️ Note:** Billing and shipping data are **not** encrypted.

For more information about the `payment` object and its properties, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment" target="_blank">ApplePayPayment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## 6. Test your integration

To test your Apple Pay direct integration, you must:

- Meet the [testing prerequisites](#prerequisites).
- Have an <a href="https://developer.apple.com/apple-pay/sandbox-testing" target="_blank">Apple Developer account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, configured for Apple Pay, with at least one Apple Pay test card in your wallet.

To test, follow these steps:

1. In your integration, click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
2. Sign in to your Apple Developer account and select your test card.
3. Authorize the payment.

✅ &nbsp; **Success!** The transaction is completed.

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
