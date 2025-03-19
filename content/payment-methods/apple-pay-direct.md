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

# Step-by-step guide

Check the steps below on how to integrate Apple Pay direct for your platform:

<style>
  /* Overall Styles - Reduced font size for all elements within steps-container */
  .steps-container {
    font-size: 0.9em; /* Reduced overall font size */
  }

  b {
    color: #384248 !important;
  }

  .steps {
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .step-item {
    display: flex;
    margin-bottom: 8px; /* Reduced margin */
    align-items: center;
  }

  .step-item img {
    pointer-events: none;
  }

  .step-item h4 {
    pointer-events: none;
  }

  .card-container-setup {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    padding: 12px; /* Reduced padding */
    text-align: center;
    border-radius: 5px;
    margin: 6px; /* Reduced margin */
    width: 200px; /* Reduced width */
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card-container-setup:hover {
    box-shadow: 0 8px 16px 0 rgb(0 0 0 / 20%);
    transform: translateY(-0.2rem);
    transition: all 0.2s;
    cursor: pointer;
  }

  .field-description blockquote,
  .field-description dl,
  .field-description ol,
  .field-description p,
  .field-description pre,
  .field-description table,
  .field-description ul,
  .markdown-body blockquote,
  .markdown-body dl,
  .markdown-body ol,
  .markdown-body p,
  .markdown-body pre,
  .markdown-body table,
  .markdown-body ul {
    margin-bottom: 10px !important; /* Reduced margin */
    margin-top: 10px !important; /* Reduced margin */
  }

  .step-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .step-number {
    background-color: #007bff;
    color: white;
    border-radius: 50%;
    width: 35px; /* Increased width */
    height: 35px; /* Increased height */
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-left: 8px; /* Reduced margin */
    font-size: 1em; /* Increased font size */
  }

  .step-description, .step-description-3 {
    flex: 1;
    margin-left: 8px; /* Reduced margin */
    display: flex;
    align-items: center;
    height: 100%;
    font-size: 0.9rem; /* Smaller font size */
    margin-top: 0px;
    margin-bottom: 0px;
    width: 700px; /* Increased width */
  }
  .step-description-3 .space {
  margin-left: 5px; /* Adjust the value as needed */
  margin-right: 5px;
	}
  
  .step-description a{
    text-decoration: none !important;
    margin-right: 5px;
  }
  
  .step-description-3 a{
    text-decoration: none !important;
    
  }

  .step-description p {
    margin-bottom: 8px; /* Reduced margin */
  }

  .configure-text {
    font-size: 18px; /* Smaller font size */
    font-weight: lighter;
  }

  /* Mobile Styles (applied when screen width is 768px or less) */
  @media (max-width: 768px) {
    .step-item {
      flex-direction: column;
      align-items: stretch;
    }

    .step-info {
      order: -1;
      width: 100%;
      margin-bottom: 8px; /* Reduced margin */
    }

    .card-container-setup {
      width: 100%;
      margin: 6px 0; /* Reduced margin */
    }

    .step-number {
      margin-left: 0;
      margin-right: 8px; /* Reduced margin */
    }
    
    .configure-text {
      font-size: 16px; /* Smaller font size on mobile */
    }
  }

  /* Larger Screen (Desktop) Styles */
  @media (min-width: 769px) {
    .step-item {
      flex-direction: row;
      align-items: center;
    }

    .step-info {
      order: 0;
      width: auto;
      margin-bottom: 0;
    }

    .card-container-setup {
      width: 200px; /* Reduced width */
      margin: 6px; /* Reduced margin */
    }

    .step-number {
      margin-left: 8px; /* Reduced margin */
      margin-right: 0;
    }

    .step-description {
      margin-left: 8px; /* Reduced margin */
    }
  }
  
  .card-container-setup{
    display: none;
  }
</style>

<div class="steps-container">
  <div class="steps">
    <div class="step-item">
      <div class="card-container-setup">
        <a href="/docs/hardware-setup" style="text-decoration: none;">
          <div>
            <img
              src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Settings.svg"
              style="margin: 5px; max-height: 100px; max-width: 100px;">
          </div>
        </a>
      </div>
      <div class="step-info">
        <div class="step-number">1</div>
        <p class="step-description configure-text"><a href="https://docs.multisafepay.com/docs/apple-pay-direct-integration-test-jesse#1-validate-your-domain">Validate your domain</a> to ensure compatibility with your platform</p>
      </div>
    </div>
    <div class="step-item">
      <div class="card-container-setup">
        <a href="/docs/smartpos-activation" style="text-decoration: none;">
          <div>
            <img
              src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Activation.svg"
              style="margin: 5px; max-height: 100px; max-width: 100px;">
          </div>
        </a>
      </div>
      <div class="step-info">
        <div class="step-number">2</div>
        <p class="step-description configure-text">Request registration for Apple Pay direct for your MultiSafepay account</p>
      </div>
    </div>
    <div class="step-item">
  <div class="card-container-setup">
    <a href="/docs/event-notifications" style="text-decoration: none;">
      <div>
        <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Notifications.svg"
          style="margin: 5px; max-height: 100px; max-width: 100px;">
      </div>
    </a>
  </div>
  <div class="step-info">
    <div class="step-number">3</div>
    <p class="step-description-3 configure-text">Check if the customer's <span class="space"><a href="https://docs.multisafepay.com/docs/apple-pay-direct-integration-test-jesse#3-check-for-apple-pay-support">device supports</a></span> Apple Pay</p>
  </div>
</div>
<div class="steps-container">
  <div class="steps">
    <div class="step-item">
      <div class="card-container-setup">
        <a href="/docs/hardware-setup" style="text-decoration: none;">
          <div>
            <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Settings.svg"
              style="margin: 5px; max-height: 100px; max-width: 100px;">
          </div>
        </a>
      </div>
      <div class="step-info">
        <div class="step-number">4</div>
        <p class="step-description configure-text"><a href="https://docs.multisafepay.com/docs/apple-pay-direct-integration-test-jesse#4-create-an-apple-pay-session">Create and configure</a> the Apple Pay session</p>
      </div>
    </div>
    <div class="step-item">
      <div class="card-container-setup">
        <a href="/docs/smartpos-activation" style="text-decoration: none;">
          <div>
            <img
              src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Activation.svg"
              style="margin: 5px; max-height: 100px; max-width: 100px;">
          </div>
        </a>
      </div>
      <div class="step-info">
        <div class="step-number">5</div>
        <p class="step-description configure-text"><a href="https://docs.multisafepay.com/docs/apple-pay-direct-integration-test-jesse#5-create-an-order">Develop your endpoint</a> to handle Apple Pay Direct order creation</p>
      </div>
    </div>
  </div>
</div>

***

# Prerequisites

## Apple server requirements

- All pages that include Apple Pay must be served over HTTPS.
- Your domain must have a valid SSL certificate.
- Your server must support the TLS protocol version 1.2 or later.

For more information, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server" target="_blank">Setting up your server</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Customer device compatibility

To see which Apple products are compatible with Apple Pay, see Apple Developer – <a href="https://support.apple.com/en-us/HT208531" target="_blank">Devices compatible with Apple Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 1. Validate your domain

1. <a href="https://github.com/MultiSafepay/docs/raw/master/static/domain-validation-apple-pay/domain-validation-apple-pay-live.zip" target="_blank">Download the compressed Apple Pay domain validation files</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Unzip the folder and select the relevant file.
3. Place the domain validation file at:

   ```
   https://{your-domain}/.well-known/apple-developer-merchantid-domain-association
   ```

# 2. Request to register

To request registration for Apple Pay direct, email the relevant website ID to [support@multisafepay.com](mailto:[support@multisafepay.com](mailto:support@multisafepay.com))

# 3. Check for Apple Pay support

1. From the customer's device, check if Apple Pay is supported:
   ```javascript
   if (window.ApplePaySession && ApplePaySession.canMakePayments())
   ```
   For more information, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/checking_for_apple_pay_availability" target="_blank">Checking for Apple Pay availability</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

2. If Apple Pay is supported, display the ** Pay** button in your checkout page.

   To style the button, see Apple Developer:

   - <a href="https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/#apple-pay-mark" target="_blank">Buttons and marks</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
   - <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css" target="_blank">Displaying Apple Pay buttons using CSS</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# 4. Create an Apple Pay session

## Client-side integration

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

   ***

   </details>

   **⚠️ Note:** The `total.amount` is in euros, whereas the `amount` in MultiSafepay order requests is in euro cents.

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

## Server-side integration

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

# 5. Create an order

## Client-side integration

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

## Server-side integration

1. From your server, [create an order](/reference/createorder/) > Wallet order. <br> See also Examples > Apple pay direct, using the `payment.token` property. <br> To use the `payment.token` property in the order request, convert it to an escaped JSON string.
2. To access the shipping and/or billing details from the `payment` object, use the `payment.billingContact` and `payment.shippingContact` properties.
3. To add the details to the order request, format them in accordance with [create order](/reference/createorder/) requests.

**⚠️ Note:** Billing and shipping data are **not** encrypted.

For more information about the `payment` object and its properties, see Apple Developer – <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment" target="_blank">ApplePayPayment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Test your integration

If you want to test your Apple Pay direct integration, you must:

- Have an <a href="https://developer.apple.com/apple-pay/sandbox-testing" target="_blank">Apple Developer account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> configured for Apple Pay.
- Create a <a href="https://developer.apple.com/apple-pay/sandbox-testing/#:~:text=supports%20TLS%C2%A01.2.-,Create%20a%20Sandbox%20Tester%20Account,-To%20create%20a"> Sandbox Tester account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and add a <a href="https://developer.apple.com/apple-pay/sandbox-testing/#:~:text=Adding%20a%20Test%20Card%20Number"> Test Card Number</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

If you meet these requirements, email [integration@multisafepay.com](mailto:integration@multisafepay.com) for further instructions.

<br />

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)