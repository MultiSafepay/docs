---
title : "Integrating a single Payment Component"
breadcrumb_title : "Integrating single Payment Component"
meta_title: "Payment components - Integrating Payment Component - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: 'single'
read_more: '.'
--- 

To integrate a Payment Component into your checkout for a single payment gateway, follow these steps:

## Step 1: Prepare

### Generate an API token
Payment Components require a MultiSafepay API token. See API Reference&nbsp;-&nbsp;[Generate an API token](/api/#generate-an-api-token).

**Note:** To keep your API key private, make the request from your own server. 

### Add elements to your checkout page
**1.** Add our Payment Component CSS to the `<head>` of your checkout page:  
```
link rel="stylesheet" href="https://pay.multisafepay.com/sdk/compnents/v1/components.css">
```

**2.** Add the following script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://pay.multisafepay.com/sdk/components/v1/components.js"></script>
```
**Note:** If you choose to host the Payment Component library on your own server, MultiSafepay is no longer responsible for [PCI DSS compliance](/faq/general/glossary/#payment-card-industry-data-security-standard-pci-dss).

**3.** Create a DOM element for the Payment Component UI in the `<body>` of your checkout page:
```
<div id="MSPPayment"></div>
```

## Step 2: Initialize

### Construct the Payment Component object

**1.** Initialize an `orderData` object containing information about the customer's order collected during the checkout process:

```
const orderData = {
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

{{< details title="View properties" >}}

| Key | Value |
| ---- | ---- |
| currency| Currency of the order. **Format:** [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. Required. |
| amount| Value of the order. **Format:** Number without decimal points, e.g. 100 euro is formatted as `10000`. Required. |
| customer.country|Country code of the customer, used to validate the availability of the payment method. **Format:** [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Required. |
|customer.locale | Language of the customer, used to set the Payment Component UI's language. **Format:** [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Optional. |
| template.settings.embed_mode| Embed mode is a template designed to blend in seamlessly with your ecommerce. **Format:** Boolean. Optional. |

{{< /details >}}


We use the `orderData` object to ensure the payment method is enabled, e.g. for the currency, country, and transaction value. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: orderData
});
```


### Initialize the Payment Component

Call the `PaymentComponent.init()` method with the following arguments:

```
PaymentComponent.init('payment', {
    container: '#MSPPayment',
    gateway: '<GATEWAY>',
    onLoad: state => {
        console.log('onLoad', state);
    },
    onError: state => {
        console.log('onError', state);
    }
});
```
Replace the `<GATEWAY>` placeholder with the relevant gateway code.
{{< details title="View gateway codes" >}}

|Payment method|Gateway code|
|---|---|
|Credit card|`CREDITCARD`|
|iDEAL|`IDEAL`|
|iDEAL QR|`IDEALQR`|
|Paysafecard|`???`|
|Request to Pay|`DBRTP`|
|Trustly|`TRUSTLY`|
|PayPal|`PAYPAL`|
|Afterpay|`AFTERPAY`|
|E-invoicing|`EINVOICE`|
|in3|`IN3`|
|Pay After Delivery|`PAYAFTER`|

{{< /details >}}

Create event handlers for the following events:

{{< details title="View events" >}}

| Event | Event handler |
| ---- | ---- |
|`onError`| Called when an error occurs in the Payment Component|
|`onLoad`| Called when the Payment Component UI is rendered |

{{< /details >}}

The `PaymentComponent` has the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error details, like error messages or codes.|
|`hasErrors`| Returns a boolean value depending on whether errors have been registered. |
|`getPaymentData`| Creates a `payload` object with the customer's payment details, used to create orders|

{{< /details >}}

## Step 3: Redirect to pay

### Collect payment data
**1.** To collect the customer's payment details from the Payment Component UI, call the `PaymentComponent.getPaymentData()` method:

```
PaymentComponent.getPaymentData()
```

**2.** Pass the `payment_data` to your server.

### Create an order

Make a POST `/connect/payments/create` request from your server.

In the request, append the `payment_data` collected from the Payment Component UI to the order data collected during the checkout process:

```
curl -X POST "https://testapi.multisafepay.com/v1/connect/payments/create" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-website-API-key>" \
-d " \
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "<GATEWAY>",
    "currency": "EUR",
    "amount": "100",
    "description": "Test Order Description",
...
    "payment_data": {
       "payload": "{secure_payload}"
    },
}"
```
Replace the `<GATEWAY>` placeholder with the relevant gateway code, see Step 2: [Initialize the Payment Component](#initialize-the-payment-component).

The request follows the same structure as `POST /orders` requests. 

For more information, see API Reference&nbsp;-&nbsp;[Orders](/api/#orders).

### Redirect the customer

**1.** From your server, pass the `response` to the POST `/connect/payments/create` request to the customer's device. 


**2.** Check that `response.success` is `true`.

**3.** Call the `PaymentComponent.init()` method using the following arguments:
```
PaymentComponent.init('redirection', {
    container: '#MSPPayment',
    order: response.data
});
```
If additional actions are required from the customer, the customer will be redirected to e.g. the `payment_url` or 3D Secure. If successful, the customer is then redirected to the `redirect_url`.

If no actions are required, the customer is redirected to the `redirect_url`.


## Step 4: Go live

When you're ready to process real payments, make the following changes:

**1.** In Step 2: [Construct the Payment Component object](#construct-the-payment-component-object), change the environment from `test` to `live`:
```
PaymentComponent = new MultiSafepay({
    env: 'live',
    apiToken: apiToken,
    order: orderData
});
```


**2.** In Step 3: [Make an order request](#make-an-order-request), change the test endpoint to the live endpoint:  

`https://api.multisafepay.com/v1/connect/payments/create`
