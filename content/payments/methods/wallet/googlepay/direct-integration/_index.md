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
With direct integration, the **Google Pay** button appears in your checkout page, where customers complete payment without being redirected to a [MultiSafepay payment page](/payment-pages/).

{{< screen src="/img/google-pay-screen.png" align="center" class="small-img desktop-radius" >}}

{{< blue-notice >}}
**Note:** By accessing or using the Google Pay API, you agree to the [Google API Terms of Service](https://payments.developers.google.com/terms/sellertos).
{{< /blue-notice >}}

{{< details title="Prerequisites">}}

- Google Pay must be [activated in your MultiSafepay account](/payment-methods/google-pay/activation/).
- You need a [Google Pay My Business account](https://pay.google.com/business/console/).
- You must serve an HTTPS webpage with a TLS domain-validated certificate.

{{< /details >}}

{{< details title="Supported browsers" >}}

Customers can use the following supported web browsers: 

- Apple Safari
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera
- UCWeb UC Browser

{{< /details >}}

## Step 1: Initialize

### Add the Google Pay library

Add the Google Pay JavaScript library to the bottom of the `<body>` of your checkout page:

```
<script
  async
  src="https://pay.google.com/gp/p/js/pay.js"
  onload="onGooglePayLoaded()">
</script>
```
**Note**: The `onload` event handler is used to display the **Google Pay** button. For more information, see [Display the Google Pay button](/payment-methods/google-pay/direct/#display-the-google-pay-button).

### Place the Google Pay button

Create an element in the `<body>` of your checkout page where you want to display the **Google Pay** button:

```
<div id="button-container" style="width: 160px; height: 40px;"></div>
```

**Note**: This element is populated in a later step. For more information, see [Display the Google Pay button](/payment-methods/google-pay/direct/#display-the-google-pay-button).

### Configure Google Pay

**1.** Define which version of the Google Pay API you are using.

On the client-side, create an object containing the major and minor versions of the Google Pay API that your integration supports:

```
const baseRequest = {
  apiVersion: 2,
  apiVersionMinor: 0
};
```

**2.** Configure the Google Pay payment token request.

**Note:** Google Pay uses payment tokens to encrypt the customer's payment details for secure processing. 

Create a `tokenizationSpecification` object: 

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

Create an `allowedCardNetworks` array containing card networks accepted by your website:

```
const allowedCardNetworks = ["MAESTRO", "MASTERCARD", "VISA"];
```

**Options**: `MAESTRO`, `MASTERCARD`, `VISA`.

For more information about supported payment card networks, see Google Pay&nbsp;–&nbsp;[Request objects](https://developers.google.com/pay/api/web/reference/request-objects#CardParameters).

**4.** Define supported authentication methods.

Create an `allowedCardAuthMethods` array containing authentication methods accepted by your website:

```
const allowedCardAuthMethods = ["CRYPTOGRAM_3DS", "PAN_ONLY"];
```

**Options**: `CRYPTOGRAM_3DS`, `PAN_ONLY`.

For more information about authentication methods, see Google Pay&nbsp;–&nbsp;[Request objects](https://developers.google.com/pay/api/web/reference/request-objects#CardParameters).

**5.** Describe your supported payment methods.

Combine the supported payment card networks and authentication methods to describe what your site supports for the `CARD` payment method:

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

When you have finished testing, change the environment to `PRODUCTION`.

## Step 2: Display the button

### Check for Google Pay support

**1.** Add your supported payment methods to your `baseRequest` object:

```
const isReadyToPayRequest = Object.assign({}, baseRequest);
isReadyToPayRequest.allowedPaymentMethods = [baseCardPaymentMethod];
```

**2.** Create an event handler for when the Google Pay JavaScript library is loaded.

With the `isReadyToPay()` method, check if the Google Pay API is supported by the customer's device and browser:

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

### Display the Google Pay button

To create a **Google Pay** button, populate the `button-container` element:

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
### Style the button

For infomation about styling your **Google Pay** button, see Google Pay:

- [Customize your button](https://developers.google.com/pay/api/web/guides/resources/customize)
- [User experience best practices](https://developers.google.com/pay/api/web/guides/ux-best-practices)
- [Brand guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines)

## Step 3: Create a payment request

Create a function that returns a `PaymentDataRequest` object:

- Describe your integration's support for the Google Pay API.
- Add your supported payment methods.
- Add the amount and currency for the customer to authorize.
- Add your merchant name and Google Pay merchant ID for display.

```
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
        merchantName: 'Example Merchant'
        merchantId: '12345678901234567890'
    };
    return paymentDataRequest;
}
```

You will call this function from the **Google Pay** button event handler in the next step. This way, attributes like the `totalPrice` can be updated up until the customer chooses to pay.

For more information about the `transactionInfo` object, see Google Pay&nbsp;–&nbsp;[TransactionInfo](https://developers.google.com/pay/api/web/reference/request-objects#TransactionInfo).

### merchantInfo values

In the `TEST` environment:

- `merchantName` = `Example Merchant`
- `merchantId` = `12345678901234567890` 

In the `PRODUCTION` environment:

- `merchantName` = Your merchant name  
- `merchantId` = Your Google Pay merchant ID  

To see your Google Pay merchant ID, sign in to your [Google Pay Business Console](https://pay.google.com/business/console/home).

For more information about the `merchantInfo` object, see Google Pay&nbsp;–&nbsp;[Request object](https://developers.google.com/pay/api/web/reference/request-objects#MerchantInfo).

## Step 4: Handle the interaction

**1.** Create an event handler for the **Google Pay** button:

- When the customer clicks the **Google Pay** button, call the `loadPaymentData()` method.
- Google prompts the customer to select their card and authorize the payment.
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

For more information about the `paymentData` object, see Google Pay&nbsp;–&nbsp;[Response objects](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData).

## Step 5: Create an order

From your server, create a [Google Pay direct order](/api/#google-pay---direct).

For the `gateway_info.payment_token`, use `PaymentData.PaymentMethodData.PaymentMethodTokenizationData.token`.

## Step 6: Redirect the customer

In response to the API request you made in the previous step, you receive a `payment_url` (see API Reference – [Google Pay direct order](/api/#google-pay---direct)).

Pass the `payment_url` from your server to the customer's device and redirect the customer to the URL:

```
document.location = payment_url
```

Depending on how the customer's card is stored in their Google Pay account, the URL references your success page, or a 3D Secure authentication page.

If the customer's credit card was stored as:

- **Token** (`CRYPTOGRAM_3DS`), the `payment_url` redirects to your success page.
- **Card on file** (`PAN_ONLY`), the `payment_url` may redirect to a 3D Secure authentication page.

If 3D Secure authentication is required, the customer is automatically redirected to your success page after authentication.

## Test and go live

After you've implemented the steps above, to test your integration:

- [MultiSafepay's Google Pay testing procedure](/payment-methods/google-pay/integration-testing/#testing)
- [Google Pay – Integration checklist](https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist)

Then, when you're ready to go live:

- When constructing the `paymentsClient` object, set the environment to `PRODUCTION`.
- Set the attributes of `merchantInfo` to your business name and Google Pay merchant ID.