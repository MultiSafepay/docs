---
title: "Google Pay direct integration"
category: 6298bd782d1cf4006032e765
order: 7
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'google-pay-direct'
---
With direct integration, the **Google Pay** button appears in your checkout page, where customers complete payment without being redirected to a [payment page](/docs/payment-pages/).

> ℹ️ Note
> 
> If using:
> 
> - Your own integration, follow all steps in this manual. 
> - A [ready-made integration](/docs/our-integrations) which builds the Google Pay button, start from [Step 8](#8-test-and-go-live).

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/google-pay-screen.png"  align ="center"/>

# Prerequisites

<details id="supported-browsers">
<summary>Supported browsers</summary>
<br>

- Apple Safari
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera
- UCWeb UC Browser

***

</details>

- Google Pay must be [activated in your MultiSafepay account](/docs/google-pay#activation).
- You must serve an HTTPS webpage with a TLS domain-validated certificate.
- After setting up your backend, you need to register your business and website in <a href="https://pay.google.com/business/console/" target="_blank">Google Pay's Business Console</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- By accessing or using the Google Pay API, you agree to the <a href="https://payments.developers.google.com/terms/sellertos" target="_blank">Google API Terms of Service</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 1. Initialize

## Add the Google Pay library

Add the Google Pay JavaScript library to the bottom of the `<body>` of your checkout page:

```javascript
<script
  async
  src="https://pay.google.com/gp/p/js/pay.js"
  onload="onGooglePayLoaded()">
</script>
```

**⚠️ Note:** The `onload` event handler is used to display the **Google Pay** button. For more information, see [Display the Google Pay button](#3-display-the-google-pay-button).

## Place the Google Pay button

Create an element in the `<body>` of your checkout page where you want to display the **Google Pay** button:

```html
<div id="button-container" style="width: 160px; height: 40px;"></div>
```

**⚠️ Note:** This element is populated in a later step. For more information, see [Display the Google Pay button](#display-the-google-pay-button).

## Configure Google Pay

1. Define which version of the Google Pay API you are using.

   On the client-side, create an object containing the major and minor versions of the Google Pay API that your integration supports:

   ```javascript
   const baseRequest = {
   apiVersion: 2,
   apiVersionMinor: 0
   };
   ```

2. Configure the Google Pay payment token request.

   **⚠️ Note:** Google Pay uses payment tokens to encrypt the customer's payment details for secure processing. 

   Create a `tokenizationSpecification` object: 

   ```javascript
   const tokenizationSpecification = {
   type: 'PAYMENT_GATEWAY',
   parameters: {
       'gateway': 'multisafepay',
       'gatewayMerchantId': 'yourMultiSafepayAccountId'
   }
   };
   ```

   - For `gateway`, specify `multisafepay`.
   - For `gatewayMerchantId`, specify your MultiSafepay account ID.

3. Define supported payment card networks.

   Create an `allowedCardNetworks` array containing card networks accepted by your website:

   ```javascript
   const allowedCardNetworks = ["MASTERCARD", "VISA"];
   ```

   **Options:** `MASTERCARD`, `VISA`.

   For more information about supported payment card networks, see Google Pay – <a href="https://developers.google.com/pay/api/web/reference/request-objects#CardParameters" target="_blank">Request objects</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

4. Define supported authentication methods.

   Create an `allowedCardAuthMethods` array containing authentication methods accepted by your website:

   ```javascript
   const allowedCardAuthMethods = ["CRYPTOGRAM_3DS", "PAN_ONLY"];
   ```

   **Options:** `CRYPTOGRAM_3DS`, `PAN_ONLY`.

   For more information about authentication methods, see Google Pay – <a href="https://developers.google.com/pay/api/web/reference/request-objects#CardParameters" target="_blank">Request objects</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

5. Describe your supported payment methods.

   Combine the supported payment card networks and authentication methods to describe what your website supports for the `CARD` payment method:

   ```javascript
   const baseCardPaymentMethod = {
   type: 'CARD',
   parameters: {
       allowedAuthMethods: allowedCardAuthMethods,
       allowedCardNetworks: allowedCardNetworks
   }
   };
   ```

6. Extend the `baseCardPaymentMethod` object to include the `tokenizationSpecification`:

   ```javascript
   const cardPaymentMethod = Object.assign(
   {tokenizationSpecification: tokenizationSpecification},
   baseCardPaymentMethod
   );
   ```

## Initialize Google Pay

Create a Google Pay `paymentsClient` object and specify the relevant environment:

```javascript
const paymentsClient =
    new google.payments.api.PaymentsClient({environment: 'TEST'});
```

When you have finished testing, change the environment to `PRODUCTION`.

# 2. Display the button

## Check for Google Pay support

1. Add your supported payment methods to your `baseRequest` object:

   ```javascript
   const isReadyToPayRequest = Object.assign({}, baseRequest);
   isReadyToPayRequest.allowedPaymentMethods = [baseCardPaymentMethod];
   ```

2. Create an event handler for when the Google Pay JavaScript library is loaded.

   With the `isReadyToPay()` method, check if the Google Pay API is supported by the customer's device and browser:

   ```javascript
   function onGooglePayLoaded() {
       paymentsClient.isReadyToPay(isReadyToPayRequest)
           .then(function(response) {
               if (response.result) {
                   addGooglePayButton();
               }
           })
           .catch(function(err) {
               // Show error in developer console for debugging
               console.error(err);
           });
   }
   ```

## Display the Google Pay button

To create a **Google Pay** button, populate the `button-container` element:


```javascript
function addGooglePayButton() {
    const buttonContainer = document.getElementById('button-container');
    const button = paymentsClient.createButton({
        buttonType: 'plain',
        onClick: onGooglePaymentButtonClicked
    });
    buttonContainer.appendChild(button);
}
```

## Style the button

For infomation about styling your **Google Pay** button, see Google Pay:

- <a href="https://developers.google.com/pay/api/web/guides/resources/customize" target="_blank">Customize your button</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://developers.google.com/pay/api/web/guides/ux-best-practices" target="_blank">User experience best practices</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://developers.google.com/pay/api/web/guides/brand-guidelines" target="_blank">Brand guidelines</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# 3. Create a payment request

Create a function that returns a `PaymentDataRequest` object:

- Describe your integration's support for the Google Pay API.
- Add your supported payment methods.
- Add the amount and currency for the customer to authorize.
- Add the country code as `NL`.
- Add your merchant name and Google Pay merchant ID for display.

```javascript
function getGooglePaymentDataRequest() {
    const paymentDataRequest = Object.assign({}, baseRequest);
    paymentDataRequest.allowedPaymentMethods = [cardPaymentMethod];
    paymentDataRequest.transactionInfo = {
        totalPriceStatus: 'FINAL',
        totalPrice: '123.45',
        currencyCode: 'EUR',
        countryCode: 'NL'
    };
    paymentDataRequest.merchantInfo = {
        merchantName: 'Example Merchant',
        merchantId: '12345678901234567890'
    };
    return paymentDataRequest;
}
```

You will call this function from the **Google Pay** button event handler in the next step. This way, attributes like the `totalPrice` can be updated up until the customer chooses to pay.

For more information about the `transactionInfo` object, see Google Pay – <a href="https://developers.google.com/pay/api/web/reference/request-objects#TransactionInfo" target="_blank">TransactionInfo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## merchantInfo values

In the `TEST` environment:

- `merchantName` = `Example Merchant`
- `merchantId` = `12345678901234567890` 

In the `PRODUCTION` environment:

- `merchantName` = Your merchant name  
- `merchantId` = Your Google Pay merchant ID  

To see your Google Pay merchant ID, sign in to your <a href="https://pay.google.com/business/console/home" target="_blank">Google Pay Business Console</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

For more information about the `merchantInfo` object, see Google Pay – <a href="https://developers.google.com/pay/api/web/reference/request-objects#MerchantInfo" target="_blank">Request object</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 4. Handle the interaction

1. Create an event handler for the **Google Pay** button:

   - When the customer clicks the **Google Pay** button, call the `loadPaymentData()` method.
   - Google prompts the customer to select their card and authorize the payment.
   - After the customer authorizes the payment, handle the response from the Google Pay API.

   ```javascript
   function onGooglePaymentButtonClicked() {
       const paymentDataRequest = getGooglePaymentDataRequest();
       paymentsClient.loadPaymentData(paymentDataRequest)
           .then(function(paymentData) {
               processPayment(paymentData);
           })
           .catch(function(err){
               console.error(err);
           });
   }
   ```

2. Pass the `paymentData` from the response to your server:

   ```javascript
   function processPayment(paymentData) {
       // send paymentData to your server
   }
   ```

   For more information about the `paymentData` object, see Google Pay – <a href="https://developers.google.com/pay/api/web/reference/response-objects#PaymentData" target="_blank">Response objects</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 5. Create an order

From your server, [create an order](/reference/createorder/) > Wallet order. See in the Request pane, Examples > Google Pay direct.

For the `gateway_info.payment_token`, use `paymentData.paymentMethodData.tokenizationData.token`.

For 3D Secure authentication, add `customer.browser` object in your request. See recipe - <a href="https://docs.multisafepay.com/recipes/create-a-customerbrowser-object" target="_blank">Customer browser</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 6. Redirect the customer

In response to the API request you made in the previous step, you receive a `payment_url`.

Pass the `payment_url` from your server to the customer's device and redirect the customer to the URL:

```
document.location = payment_url
```

Depending on how the customer's card is stored in their Google Pay account, the URL references your success page, or a 3D Secure authentication page.

If the customer's card was stored as:

- **Token** (`CRYPTOGRAM_3DS`), the `payment_url` redirects to your success page.
- **Card on file** (`PAN_ONLY`), the `payment_url` may redirect to a 3D Secure authentication page.

If 3D Secure authentication is required, the customer is automatically redirected to your success page after authentication.

# 7. Submit your details for approval

Go to <a href="https://pay.google.com/business/console/" target="_blank">Google Pay's Business Console</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and submit your business details and add the websites where you want to enable the Google Pay button.

<details id="google-validation">
<summary>How to validate your website</summary>
<br>

**Provide your business details:**

1. Under **Business Profile**, click **Get started**.
2. Complete both the **Business identity** and **Business information** sections
3. Click **Save**.

**Send your website details for approval:**

**⚠️Note:** Every website where you want to implement the Google Pay button must be approved. This includes your own test environment.

1. Under **Google Pay API**, click **Create an integration**.
2. Click **Get started**, accept the terms and conditions and click **Continue**
3. Under **Integrate with your website**, click **Add website**.
4. Add the website where you want to integrate **Google Pay direct**.
5. Set the **Google Pay API integration type** to **Gateway**.
6. Upload the requested screenshots for each section of your website.
7. Click **Save**.

</details>

Once all details have been provided and approved, go to **Google Pay API**. In the form, check every box once you have confirmed that all steps have been cleared. Click **Submit for approval**.

Once Google approves your website, you can proceed to test your integration.

**⚠️Note:** You won't be able to test Google Pay direct unless Google approves your website.

# 8. Test and go live

After you've implemented the steps above, to test your integration:

- [MultiSafepay's Google Pay testing procedure](/docs/testing#google-pay)
- <a href="https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist" target="_blank">Google Pay – Integration checklist</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

Then, when you're ready to go live:

- When constructing the `paymentsClient` object, set the environment to `PRODUCTION`.
- Set the attributes of `merchantInfo` to your business name and Google Pay merchant ID.

### Ready-made integrations

To enable Google Pay direct for your ready-made integration, go to the payment method settings in your <<glossary:backend>> and add the merchant ID and merchant name from your <a href="https://pay.google.com/business/console/" target="_blank">Google Pay Business Console</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> .

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)