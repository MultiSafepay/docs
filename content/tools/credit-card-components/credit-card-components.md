---
title : "Credit card components"
---

The _Payment component_ by MultiSafepay gives you the possibility to offer your customers a seamless payment experience. Our Javascript based component is easy to implement to your environment and can be modified to blend in with the customer checkout experience. One simple line will allow you to change and modify the component to also accept other payment method types.

## Environments

MultiSafepay provides a TEST environment and a LIVE environment. The TEST environment is useful for developing and testing the Credit card component integration with our API. Once the integration has been developed, processing real transactions is as simple as changing the API endpoint and using a different API Key. Further technical details can be found on our [API section](http://docs.multisafepay.com/api)

### API Authentication

All requests to the MultiSafepay API endpoint require authentication.Authentication is provided by including an API key as an HTTP header in your request. Each website has its own API key so if you are operating multiple websites, be sure to use the correct API key for each site. The API key can be found under the website settings in MultiSafepay Control. The HTTP header name for the API Key is: `api_key`

### Files

The Payment component includes [3 files](https://pay.multisafepay.com/sdk/components/v1):

The MultiSafepay encryption library minified, which will be autoloaded by connect.js:<br>
[msp-crypt.min.js](https://pay.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js)

The Payment component library:<br>
[components.js](https://pay.multisafepay.com/sdk/components/v1/components.js)

The Payment component stylesheet:<br>
[components.css](https://pay.multisafepay.com/sdk/components/v1/components.css)

## Implementation

### Step 1: Get API token

Get the `api_token`, which is used for encrypting the credit card input. This call uses authentication, so **do not expose your own** `api_key`. Make sure your server sends this request and not the client or browser. For example, you can load this when the customer is loading the checkout of your website.

`GET /v1/connect/auth/api_token`

Example: https://api.multisafepay.com/v1/connect/auth/api_token?api_key=xxx

`response`

```
{
  "api_token": "pub.v2.xxxxxx.xxxxxx"
}
```

### Step 2: Initialize Payment Components library

You must initialize the Payment components library and link it to the container element (selector).

The constructor takes three values:

`env` -> test/live, decides the api mode<br>
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


### Step 3: Mounting files

The following three files need to be mounted in the TEST environment:

1. `<script src="https://testpay.multisafepay.com/sdk/components/v1/components.js"></script>`

2. `<script src="https://testpay.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js" type="text/javascript" id="msp-crypt-msp-module"></script>`

3. `<link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v1/components.css">`

Alternativley, the following files need to be mounted in the PRODUCTION environment:


1. `<script src="https://pay-10.dev.multisafepay.com/sdk/components/v1/components.js"></script>`

2. `<script src="https://pay-10.dev.multisafepay.com/sdk/components/v1/assets/msp-crypt.min.js" type="text/javascript" id="msp-crypt-msp-module"></script>`

3. `<link rel="stylesheet" href="https://pay-10.dev.multisafepay.com/sdk/components/v1/components.css">`

### Step 4: Place order

After the customer has entered their credit card details, the encrypted data can be sent to the MultiSafepay API to finish the transaction.
On the frontend you can retrieve the encrypted credit card data through the following code:

```
PaymentComponent.getPaymentData().payment_data.payload
```

This payload can be sent with a [direct CREDITCARD transaction request]((https://docs.multisafepay.com/api/#create-a-direct-order))

```
{
    "type": "direct",
    "order_id": "apitool_7931462",
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

### Optional: Checking for errors within the Payment Component

Apart from having the onError handler, you can also actively request the instantiated library for any errors using the following:

`Requests`

```
PaymentComponent.getErrors()
```

### Optional: Styling template

The credit card component comes with two styling templates. In order to enable the second template, the following parameter needs to be added:

```
const orderData = {
    currency: 'X',
    amount: X,
    template : {
        settings: {
            embed_mode: true
        }
};
```
 