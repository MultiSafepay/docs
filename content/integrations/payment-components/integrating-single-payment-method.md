---
title : "Integrating a single payment gateway"
breadcrumb_title : "Integrating a single payment gateway"
meta_title: "Payment Components - Integrating a single payment gateway - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
--- 

To integrate a payment component into your checkout for a single payment method, follow these steps:

## Step 1: Install

### Generate an API token
Payment components require a MultiSafepay API token. See API Reference&nbsp;–&nbsp;[Generate an API token](/api/#generate-an-api-token).

**Note:** To keep your API key private, request the token from your own server. 

### Add elements to your checkout page
**1.** Add the Payment component CSS to the `<head>` of your checkout page:  
```
link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v1/components.css">
```

**2.** Add the Payment component script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://pay.multisafepay.com/sdk/components/v1/components.js"></script>
```
**Note:** If you choose to host the Payment component library on your own server, MultiSafepay is no longer responsible for [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss).

**3.** Add the DOM element for the Payment component UI in the `<body>` of your checkout page:
```
<div id="MultiSafepayPayment"></div>
```

## Step 2: Initialize

### Construct the payment component object

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
| currency| Currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
| amount| Value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
| customer.country| Customer's country code. Used to check the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Required**. |
|customer.locale | Customer's language. Used to set the language of the Payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
| template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |

{{< /details >}}

**Note:** We use the `orderData` object to ensure the payment method is enabled, e.g. for the currency, country, and transaction value. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: orderData
});
```

### Initialize the payment component

Call the `PaymentComponent.init()` method with the following arguments:

```
PaymentComponent.init('payment', {
    container: '#MultiSafepayPayment',
    gateway: '<GATEWAY>',
    onLoad: state => {
        console.log('onLoad', state);
    },
    onError: state => {
        console.log('onError', state);
    }
});
```
Replace the `<GATEWAY>` placeholder with the relevant payment gateway code.
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
|AfterPay|`AFTERPAY`|
|E-invoicing|`EINVOICE`|
|in3|`IN3`|
|Pay After Delivery|`PAYAFTER`|

{{< /details >}}

Create event handlers for the following events:

{{< details title="View events" >}}

| Event | Event handler |
| ---- | ---- |
|`onError`| Called when an error occurs in the payment component|
|`onLoad`| Called when the Payment component UI is rendered |

{{< /details >}}

The `PaymentComponent` uses the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error details, like error messages or codes.|
|`hasErrors`| Returns a boolean value depending on whether errors have been registered. |
|`getPaymentData`| Creates a `payload` object with the customer's payment details, used to create orders|

{{< /details >}}

## Step 3: Redirect to pay

### Collect payment data
**1.** To collect the customer's payment details from the Payment component UI, call the `PaymentComponent.getPaymentData()` method:

```
PaymentComponent.getPaymentData()
```

**2.** Pass the `payment_data` to your server.

### Create an order

Make a POST [`/orders`](/api/#orders) request from your server:

- Append the `payment_data` collected from the Payment component UI to the `orderData` collected during the checkout process.
- Replace the `<GATEWAY>` placeholder with the relevant gateway code, see Step 2: [Initialize the payment component](#initialize-the-payment-component).

```
curl -X POST "https://testapi.multisafepay.com/v1/json/orders" \
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

### Redirect the customer

**1.** From your server, pass the `response` to the POST `/orders` request to the customer's device. 

**2.** Check that `response.success` is `true`.

**3.** Call the `PaymentComponent.init()` method using the following arguments:
```
PaymentComponent.init('redirection', {
    order: response.data
});
```
- If the customer needs to perform additional actions, they are redirected, e.g. to the `payment_url` or 3D Secure. Then, if successful, they are redirected to the `redirect_url`.

- If no further action is required, the customer is redirected to the `redirect_url`.

## Step 4: Go live

When you're ready to process real payments, make the following changes:

**1.** In Step 2: [Construct the Payment component object](#construct-the-payment-component-object), change the environment from `test` to `live`:
```
PaymentComponent = new MultiSafepay({
    env: 'live',
    apiToken: apiToken,
    order: orderData
});
```


**2.** In Step 3: [Create an order](#create-an-order), change the test endpoint to the live endpoint:  

`https://api.multisafepay.com/v1/json/orders`

## Next steps

{{< two-buttons

href-1="/integrations/payment-components" header-1="Overview" text-1="Payment Components" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/integrations/payment-components/customizing-payment-components" header-2="Next" text-2="Customizing Payment Components" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
