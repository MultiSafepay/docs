---
title : "Credit Card Component"
layout : "single"
tags : "hidden"
---

## Introduction

The Credit Card Component by MultiSafepay allows the possibility of offering your customers a seamless checkout experience as our Javascript based component is easy to implement in your environment.

## Preparation

### Setting up your Test environment

The Credit Card Component includes two files, each for both the Test and Live environment. After testing, the files can be changed to those listed in [Step 4](/tools/credit-card-component/#4-push-to-live)


The Credit Card Component library contains the credit card fields:  

```
<script src="https://testpay.multisafepay.com/sdk/components/v1/components.js"></script>
```
**Source:** [components.js](https://pay.multisafepay.com/sdk/components/v1/components.js)

The Credit Card Component stylesheet contains the styling template of the Credit Card Component:


```
<link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v1/components.css">
```
**Source:** [components.css](https://pay.multisafepay.com/sdk/components/v1/components.css)

{{< br >}}

### Get API token

Get the `api_token`, which is used for encrypting the credit card input. This call uses authentication, so **do not expose your own** `api_key`. Make sure your server sends this request and not the client or browser. For example, you can load this when the customer is loading the checkout of your website.

#### Request

```
GET https://api.multisafepay.com/v1/connect/auth/api_token?api_key=xxx
```

{{< br >}}

#### Response

```
{
    "success": true,
    "data":
    { "api_token": "pub.v2.xxxxxxxx" }
}
```

{{< br >}}

## Implementation

### 1. Initialize Credit Card Component library

You must initialize the Credit Card Component library and link it to the container element (selector).

The constructor takes three values:

`env`: test/live, decides the API mode {{< br >}} 
`apiToken`: response from GET API token {{< br >}} 
`order`: contains values of the quote

### Request

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
{{< br >}}

### 2. Pass preOrder data to the Credit Card Component

The Credit Card Component requires some initial information about your customer's shopping cart. This information is used to perform validation checks, such as:

- Is the selected payment method compatible with the currency?
- Is the selected payment method compatible with the order value?

```
const preOrder = {
    currency: 'EUR',
    amount: 10000,
    customer: {
        locale: 'EN',
        country: 'NL',
        reference: 'Customer123'
    },
    template : {
        settings: {
            embed_mode: true
        }
    }
};
```
{{< br >}}

#### Required variables
| Key | Value |
| ---- | ---- |
| currency | Currency of the order. {{< br >}} **Format:** [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) |
| amount | Value of the order. {{< br >}} **Format:** Number without decimal points (e.g., 100EU > `10000`) |

#### Optional variables
| Key | Value |
| --- | --- |
| locale | Your customer's browser language, which is used to set the Credit Card Component's language. {{< br >}} **Format:** [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) |
| country | Your customer's country code, which is used to validate the availability of the payment method. {{< br >}} **Format:** [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) |]
| reference | A unique reference to your customer, used in tokenization. {{< br >}} **Format:** string |
| embed_mode | Embed mode is a template designed to blend in seamlessly with your ecommerce. {{< br >}} **Format:** boolean |


### 3. Place a Test order

After the customer has entered their credit card details, the encrypted data can be sent to the MultiSafepay API to finish the transaction. The endpoint: __testapi.multisafepay.com/v1/connect/payments/create__ can be used to submit the test order.<br>

On the frontend you can retrieve the encrypted credit card data through the following code:

```
PaymentComponent.getPaymentData().payment_data.payload
```
{{< br >}}

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
{{< br >}}

After sending the transaction request, you will get a `payment_url` back.
This `payment_url` will be a link to the issuer, where the customer will be required to enter his 3D Secure details.

After completion, the customer will be returned to the `redirect_url` from the transaction request.

### 4. Push to Live
When you are ready to switch to the live environment, you can use the following endpoint:

__api.multisafepay.com/v1/connect/payments/create__

The [test files](/credit-card-component/#setting-up-your-test-environment) must also be replaced with the live files listed below:

**components.js**
```
<script src="https://pay.multisafepay.com/sdk/components/v1/components.js"></script>
```

**components.css**

```
<link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v1/components.css">
```

The Credit Card Component library which decides the API mode must also be changed from __test__ to __live__:

```
request

PaymentComponent = new MultiSafepay({
    env: 'live',
    apiToken: apiToken,
    order: configOrder
});
```
{{< br >}}

## CSS styling

Our CSS is designed to give you full styling control over the component. Below is an example of the main classes of our component:

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

{{< br >}}
### Checking for errors

Apart from having the onError handler, you can also actively request the instantiated library for any errors using the following:

### Requests

```
PaymentComponent.getErrors()
```
### Contact

If you have any questions regarding the process or face any issues, feel free to contact our Integration Team at <integration@multisafepay.com>
