---
title: "Google Pay direct integration"
breadcrumb_title: 'Direct integration'
weight: 10
meta_title: "Google Pay direct - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Apple Pay direct"
layout: 'single'
url: '/payment-methods/google-pay/direct'
noindex: '.'
aliases:
    - /payments/methods/wallet/googlepay/direct-integration
---
With a direct integration, the **Google Pay** button appears in your checkout page. Customers complete payment without being redirected to a [MultiSafepay payment page](/payment-pages/).

{{< screen src="/img/google-pay-screen.png" align="center" class="small-img desktop-radius" >}}

{{< blue-notice >}}
By accessing or using the Google Pay API, you agree to the [Google APIs Terms of Service](https://payments.developers.google.com/terms/sellertos).
{{< /blue-notice >}}

## Prerequisites

- To activate Google Pay for your MultiSafepay account, see [Activating Google Pay](/payment-methods/google-pay/activation/).
- To process Google Pay direct payments, you need a [Google Pay business account](https://pay.google.com/business/console/).
- Serve an HTTPS webpage with a TLS domain-validated certificate.

### Supported browsers

Customers can use one of the following supported web browsers: 

- Google Chrome
- Mozilla Firefox
- Apple Safari
- Microsoft Edge
- Opera
- UCWeb UC Browser

## Initialize

### Include the Google Pay library

Add the Google Pay JavaScript library to the bottom of the `<body>` of your checkout page:

```
<script
  async
  src="https://pay.google.com/gp/p/js/pay.js"
  onload="onGooglePayLoaded()">
</script>
```
**Note**: The `onload` event handler is used to display the **Google Pay** button. For more information, see [Display Google Pay button](/payments/methods/wallet/googlepay/direct-integration/#display-google-pay-button).

### Place the Google Pay button

Create an element in the `<body>` of your checkout page where you want to display the **Google Pay** button:

```
<div id="button-container" style="width: 160px; height: 40px;"></div>
```

**Note**: This element is populated in a later step. For more information, see [Display Google Pay button](/payment-methods/google-pay/direct/#display-google-pay-button).

### Configure Google Pay

**1.** Define your Google Pay API version.

On the client-side, create an object with the major and minor versions of the Google Pay API that your integration supports:

```
const baseRequest = {
  apiVersion: 2,
  apiVersionMinor: 0
};
```

**2.** Request a Google Pay payment token.

Google Pay creates a payment token to encrypt the customer's payment details for secure processing. Create a `tokenizationSpecification` object: 

```
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

**3.** Define supported payment card networks.

Create an array, with card networks accepted by your website:

```
const allowedCardNetworks = ["MASTERCARD", "VISA", "MAESTRO"];
```

**Options**: `MASTERCARD`, `VISA`, `MAESTRO`

For more information about supported payment card networks, see Google Pay – [Request objects](https://developers.google.com/pay/api/web/reference/request-objects#CardParameters).

**4.** Define supported authentication methods.

Create an array `allowedCardAuthMethods`, with authentication methods accepted by your website:

```
const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];
```

**Options**: `PAN_ONLY`, `CRYPTOGRAM_3DS`

For more information about authentication methods, see Google Pay – [Request objects](https://developers.google.com/pay/api/web/reference/request-objects#CardParameters).

**5.** Describe your allowed payment methods.

Combine the supported payment card networks and authentication methods to describe your site's support for the `CARD` payment method:

```
const baseCardPaymentMethod = {
  type: 'CARD',
  parameters: {
    allowedAuthMethods: allowedCardAuthMethods,
    allowedCardNetworks: allowedCardNetworks
  }
};
```

**6.** Extend the `baseCardPaymentMethod` object to include the `tokenizationSpecification`:

```
const cardPaymentMethod = Object.assign(
  {tokenizationSpecification: tokenizationSpecification},
  baseCardPaymentMethod
);
```

### Initialize Google Pay

Create a Google Pay `paymentsClient` object and specify the relevant environment:

```
const paymentsClient =
    new google.payments.api.PaymentsClient({environment: 'TEST'});
```

When you're done testing, change the environment to `PRODUCTION`.

## Display pay button

### Check for Google Pay support

**1.** Add your allowed payment methods to your `baseRequest` object:

```
const isReadyToPayRequest = Object.assign({}, baseRequest);
isReadyToPayRequest.allowedPaymentMethods = [baseCardPaymentMethod];
```

**2.** Create an event handler for when the Google Pay JavaScript library is loaded.

With the `isReadyToPay()` method, determine whether the Google Pay API is supported by the customer's device and browser:

```
function onGooglePayLoaded() {
    paymentsClient.isReadyToPay(IsReadyToPayRequest)
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

### Display Google Pay button

Populate the `button-container` element to create a **Google Pay** button:

```
function addGooglePayButton() {
    const buttonContainer = document.getElementById('button-container');
    const button = paymentsClient.createButton({
        buttonType: 'plain',
        onClick: onGooglePaymentButtonClicked
    });
    buttonContainer.appendChild(button);
}
```

For infomation about styling your **Google Pay** button, see Google Pay:
- [Customize your button](https://developers.google.com/pay/api/web/guides/resources/customize)
- [User experience best practices](https://developers.google.com/pay/api/web/guides/ux-best-practices)

## Create payment request

**1.** Create a `PaymentDataRequest` object and describe your integration's support for the Google Pay API:

```
const paymentDataRequest = Object.assign({}, baseRequest);
```

**2.** Add your supported payment methods:

```
paymentDataRequest.allowedPaymentMethods = [cardPaymentMethod];
```

**3.** Add the amount and currency for the customer to authorize:

```
paymentDataRequest.transactionInfo = {
  totalPriceStatus: 'FINAL',
  totalPrice: '123.45',
  currencyCode: 'EUR',
  countryCode: 'NL'
};
```

For more information about the `transactionInfo` object, see Google Pay – [Request object](https://developers.google.com/pay/api/web/reference/request-objects#TransactionInfo).

**4.** Add your merchant name and Google Pay merchant ID for display:

```
paymentDataRequest.merchantInfo = {
  merchantName: 'Example Merchant'
  merchantId: '12345678901234567890'
};
```

When using the `TEST` environment, specify:

- `Example Merchant` for `merchantName`
- `12345678901234567890` for `merchantId`

When using the `PRODUCTION` environment, specify:

- Your merchant name for `merchantName`
- Your Google Pay merchant ID for `merchantId`

To see your Google Pay merchant ID, sign into your [Google Business Console](https://pay.google.com/business/console/home).

For more information about the `merchantInfo` object, see Google Pay – [Request object](https://developers.google.com/pay/api/web/reference/request-objects#MerchantInfo).

## Handle the interaction

**1.** Create an event handler for the **Google Pay** button:

- When the customer clicks the **Google Pay** button, call the `loadPaymentData()` method.
- After the customer authorizes the payment, handle the response from the Google Pay API.

```
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

**2.** Pass the `paymentData` from the response to your server:

```
function processPayment(paymentData) {
    // send paymentData to your server
}
```

For more information about the `paymentData` object, see Google Pay – [Response objects](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData).

## Create an order

From your server, [create a Google Pay direct order](/api/#google-pay---direct).

Use:
`PaymentData.PaymentMethodData.PaymentMethodTokenizationData.token` as `gateway_info.payment_token`.
