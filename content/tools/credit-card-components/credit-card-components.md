---
title : "Credit card components"
---

## Introduction

The _Payment component_ by MultiSafepay allows you the possibility to offer your customers a seamless checkout experience as our Javascript based component is easy to implement in your environment.


## Environments

MultiSafepay provides a TEST environment and a LIVE environment. The TEST environment is useful for developing and testing the Credit card component integration with our API. Once the integration has been developed, processing real transactions is as simple as changing the API endpoint and using a different API key.<br>

For more information about our API, please visit our [API reference](https://docs.multisafepay.com/api/)


## API Authentication

All requests to the MultiSafepay API endpoint require authentication. This is provided by including an API key as an HTTP header in your request. Each website has its own API key so if you are operating multiple websites, be sure to use the correct API key for each site. The API key can be found under the website settings in your [MultiSafepay Control](https://merchant.multisafepay.com/)<br> 

The HTTP header name for the API Key is `api_key`

## Implementation

### Step 1: Setting up your TEST environment

The payment component includes [three files](https://pay.multisafepay.com/sdk/components/v1), each for both the TEST and LIVE environment. After testing, the files can be changed to those listed in [Step 6](/tools/credit-card-components/credit-card-components/#step-6-switching-from-test-to-live)

* The MultiSafepay encryption library minified, which can be autoloaded by connect.js. The cardholder details are encrypted in a secure manner and sent to MultiSafepay<br>
[msp-crypt.min.js](https://pay.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js)

{{< alert-notice >}} `<script src="https://testpay.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js" type="text/javascript" id="msp-crypt-msp-module"></script>` {{< /alert-notice >}}


* The payment component library contains the credit card fields:<br>
[components.js](https://pay.multisafepay.com/sdk/components/v1/components.js)

{{< alert-notice >}} `<script src="https://testpay.multisafepay.com/sdk/components/v1/components.js"></script>` {{< /alert-notice >}}

* The payment component stylesheet contains the styling template of the credit card component:<br>
[components.css](https://pay.multisafepay.com/sdk/components/v1/components.css)

{{< alert-notice >}} `<link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v1/components.css">` {{< /alert-notice >}}

### Step 2: Get API token

Get the `api_token`, which is used for encrypting the credit card input. This call uses authentication, so **do not expose your own** `api_key`. Make sure your server sends this request and not the client or browser. For example, you can load this when the customer is loading the checkout of your website.

`GET /v1/connect/auth/api_token`

Example: https://api.multisafepay.com/v1/connect/auth/api_token?api_key=xxx

`response`

```
{
  "api_token": "pub.v2.xxxxxx.xxxxxx"
}
```

### Step 3: Initialize Payment Components library

You must initialize the payment components library and link it to the container element (selector).

The constructor takes three values:

`env` -> test/live, decides the API mode<br> 
`apiToken` -> api_token from step 1<br>
`order` -> contains values of the quote

`request`

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: configOrder
});
 
PaymentComponent.init('payment', {
    container: '#MSPPayment',
    gateway: 'CREDITCARD',
    onError: state => {
        console.log('onError', state);
   }
});
```

### Step 4: Styling template

The credit card component comes with two styling templates. For a more seamless integration, we recommend to enable our embedded template, the following parameter needs to be added:

```
const configOrder = {
    currency: 'EUR',
    amount: 100,
    template : {
        settings: {
            embed_mode: true
        }
};
```


### Step 5: Place an order

After the customer has entered their credit card details, the encrypted data can be sent to the MultiSafepay API to finish the transaction.<br>

On the frontend you can retrieve the encrypted credit card data through the following code:

```
PaymentComponent.getPaymentData().payment_data.payload
```

This payload can be sent with a [direct CREDITCARD transaction request](https://docs.multisafepay.com/api/#create-a-direct-order)

```
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "CREDITCARD",
    "currency": "EUR",
    "amount": "100",
    "description": "Test Order Description",
...
    "payment_data": {
       "payload": $payload
    },
}
```

After sending the transaction request, you will get a `payment_url` back.
This `payment_url` will be a link to the issuer, where the customer will be required to enter his 3D Secure details.

After completion, the customer will be returned to the `redirect_url` from the transaction request.

### Step 6: Switching from TEST to LIVE

#### LIVE environment files

After testing, you can change the TEST files to the LIVE files listed below:

* msp-crypt.min.js<br>

{{< alert-notice >}} `<script src="https://pay-10.dev.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js" type="text/javascript" id="msp-crypt-msp-module"></script>` {{< /alert-notice >}}

* components.js<br>

 {{< alert-notice >}} `<script src="https://pay-10.dev.multisafepay.com/sdk/components/v1/components.js"></script>` {{< /alert-notice >}}

* components.css<br>

 {{< alert-notice >}} `<link rel="stylesheet" href="https://pay-10.dev.multisafepay.com/sdk/components/v1/components.css">` {{< /alert-notice >}}

### TEST to LIVE environment

 You must also change the environment from: 

```
env: 'test',

to 

env: 'live',
```

## Optional features

### CSS styling

Our CSS is designed to give you full styling control over the component. Below is an example of the main classes of our component:

{{< br >}}
{{< responsive_svg src="/diagrams/svg/CCC_CSS" alt="TEST" align="center" >}}
{{< br >}}
{{< br >}}

These classes can be customized to match the exact look and feel of your webshop environment. Below is an example of some basic styling done on the main classes from the component:

```
.msp-container-ui .msp-ui-payment-form {
padding: 15px;
border: 1px solid #ff002c;
margin: 0;
}
 
.msp-container-ui .msp-ui-form-label {
font-weight: 500;
display: block;
}
 
.msp-container-ui .msp-ui-form-control {
background-color: #fff;
border: 1px solid #ccc;
color: #666;
font-weight: 400;
font-size: 14px;
padding: 6px 12px;
display: block;
width: 100%;
}
 
.msp-container-ui .msp-ui-form-control .msp-ui-credit-card-input {
background-repeat: no-repeat;
background-attachment: scroll;
background-position: 98% 3px;
padding-right: 40px;
}
```

### Checking for errors

Apart from having the onError handler, you can also actively request the instantiated library for any errors using the following:

`Requests`

```
PaymentComponent.getErrors()
```

