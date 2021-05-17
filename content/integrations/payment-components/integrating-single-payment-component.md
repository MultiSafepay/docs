---
title : "Integrating a single Payment Component"
breadcrumb_title : "Integrating single Payment Component"
meta_title: "Payment components - Integrating Payment Component - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: 'single'
read_more: '.'
--- 

To integrate the Payment Component for a single payment gateway into your checkout, follow these steps:

## Step 1: Prepare

### Generate an API token
Payment Components require a MultiSafepay API token. Request the token from your own server to keep your API key private. 

For more information, see API&nbsp;-&nbsp;[Generate an API token](/api/#generate-an-api-token).


### Add elements to your checkout page
**1.** Add the external CSS to the `<head>` of your checkout page:  
```
link rel="stylesheet" href="https://pay.multisafepay.com/sdk/compnents/v1/components.css">
```


**2.** Add the script to the bottom of the `<body>` of your checkout page:  
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

### Required properties
| Key | Value |
| ---- | ---- |
| currency| Currency of the order. **Format:** [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) (e.g. `EUR`).|
| amount| Value of the order. **Format:** Number without decimal points (e.g. 100 euro is formatted as `10000`). |
| customer.country|Country code of the customer, used to validate the availability of the payment method. **Format:** [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g. `NL`). |

### Optional properties
| Key | Value |
| ---- | ---- |
|customer.locale | Language of the customer, used to set the Payment Component UI's language. **Format:** [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g. `NL`). |
| template.settings.embed_mode| Embed mode is a template designed to blend in seamlessly with your ecommerce. **Format:** Boolean. |

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

Call the `PaymentComponent.init()` method using the following arguments:

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
{{< details title="View gateways" >}}

Replace the `<GATEWAY>` placeholder with one of the following gateway codes:
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

## Step 3: Request and redirect

### Collect payment data
**1.** To collect the customer payment details from the Payment Component UI, call the `PaymentComponent.getPaymentData()` method:

```
PaymentComponent.getPaymentData()
```

**2.** Pass the `payment_data` to your server.

### Make an order request

Make an order request from your server to the test endpoint.

In the request, append the `payment_data` collected in the Payment Component UI to the order data collected during the checkout process:

```
curl -X POST "https://testapi.multisafepay.com/v1/connect/payments/create" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authentication: Bearer <your-website-API-key>" \
-d " \
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "CREDITCARD",
    "currency": "EUR",
    "amount": "100",
    "description": "Test Order Description",
...
    "payment_data": {
       "payload": "{secure_payload}"
    },
}"
```
The request follows the same structure as `POST /order` requests. 

For more information, see API&nbsp;-&nbsp;[POST orders](/api/#orders).

### Redirect the customer

**1.** From your server, pass the response to the order request to the customer's device. 


**2.** Check that the request is successful.

**3.** Call the `PaymentComponent.init()` method using the following arguments:
```
PaymentComponent.init('redirection', {
    container: '#MSPPayment',
    order: response.data
});
```
If 3D Secure verification is required, the customer is first directed to 3D Secure. If successful, the customer is then redirected to the `redirect_url`. 

If 3D Secure is not required, the customer is redirected to the `redirect_url`.



## Go live

When you're ready to process real credit card payments, make the following changes:

**1.** When constructing the `PaymentComponent` object (see [step 3](#step-3-construct-the-credit-card-component-object)), change the environment from `test` to `live`:
```
PaymentComponent = new MultiSafepay({
    env: 'live',
    apiToken: apiToken,
    order: orderData
});
```


**2.** When making order requests (see [step 6](#step-6-make-an-order-request)), change the test endpoint to the live endpoint:  

`https://api.multisafepay.com/v1/connect/payments/create`
