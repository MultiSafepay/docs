---
title: 'Previous release'
category: 62bd999547298d001abc714c
order: 0
hidden: true
slug: 'payment-component-previous-release'
parentDoc: 62a848399bb3eb004023f291 
--- 
This technical manual is for integrating the previous release of the payment component.

# 1. Add the elements

1. Add the component's CSS to the `<head>` of your checkout page:
   ```
   <link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v1/components.css">
   ```

2. Add the component's script tothe bottom of the `<body>` of your checkout page:
   ```
   <script src="https://pay.multisafepay.com/sdk/components/v1/components.js"></script>
   ```

3. Add the DOM element for the component's UI in the `<body>` of your checkout page:
   ```
   <div id="MultiSafepayPayment"></div>
   ```

# 2) Initialize the component

## Generate an API token

Payment Components require a MultiSafepay API token. See API reference – [Generate an API token](/reference/generateapitoken/).

  **💡 Tip!** To keep your API key private, request the token from your own server.

## Construct the component object

1. Initialize an `orderData` object, containing information about the customer's <Glossary>order</Glossary> collected during the checkout process:

   ```javascript
   const orderData = {
      currency: 'EUR',
      amount: 10000,
      customer: {
          locale: 'en',
          country: 'NL',
          reference: 's9Q8ikjFJBCX'
      },
      template : {
          settings: {
              embed_mode: true
          }
      }
   };
   ```

   <details id="properties">
     <summary>Properties</summary>

     <br />

     | Key                           | Value                                                                                                                                                                                                                                                                                                                  |
     | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | currency                      | The currency of the order. Format: <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO-4217</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, e.g. `EUR`. **Required**.                                                                                                |
     | amount                        | The value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**.                                                                                                                                                                                                    |
     | customer.country              | The customer's country code. Checks the availability of the payment method. Format: <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, e.g. `NL`. **Required**.                            |
     | customer.locale               | The customer's language. Sets the language of the payment component UI. <br /> Format: <a href="https://en.wikipedia.org/wiki/ISO_639" target="_blank">ISO 639</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> <br /> Supported languages: `en`, `es`, `fr`, `it`, `nl`. **Optional**. |
     | template.settings.embed\_mode | A template designed to blend in seamlessly with your ecommerce platform. Format: Boolean. **Optional**.                                                                                                                                                                                                                |
   </details>

   **⚠️ Note:** We use the `orderData` object to ensure the payment method is enabled and the currency, country, and order amount are supported.

2. Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

   ```javascript
   PaymentComponent = new MultiSafepay({
      env: 'test',
      apiToken: apiToken,
      order: orderData
   });
   ```

## Initialize the component

1. Call the `PaymentComponent.init()` method with the following arguments:

   ```javascript
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

2. Replace the `<GATEWAY>` placeholder with the relevant payment gateway identifier.

   <details id="gateway-ids">
     <summary>Gateway IDs</summary>

     <br />

     | Payment method | Gateway IDs  |
     | -------------- | ------------ |
     | Card payments  | `CREDITCARD` |
     | iDEAL          | `IDEAL`      |
   </details>

3. Create event handlers for the following events:

   <details id="events">
     <summary>Events</summary>

     <br />

     | Event     | Event handler                                        |
     | --------- | ---------------------------------------------------- |
     | `onError` | Called when an error occurs in the payment component |
     | `onLoad`  | Called when the payment component UI is rendered     |
   </details>

   The `PaymentComponent` uses the following methods:

   <details id="methods">
     <summary>Methods</summary>

     <br />

     | Method           | Description                                                                           |
     | ---------------- | ------------------------------------------------------------------------------------- |
     | `getErrors`      | Returns error details, e.g. error messages or codes.                                  |
     | `hasErrors`      | Returns a boolean value depending on whether errors have been registered.             |
     | `getPaymentData` | Creates a `payload` object with the customer's payment details, used to create orders |
   </details>

# 3) Create an order

## Collect payment data

1. To collect the customer's payment details from the payment component UI, call the `PaymentComponent.getPaymentData()` method:

   ```javascript
   PaymentComponent.getPaymentData()
   ```

2. Pass the `payment_data` to your server.

## Create an order

Make a [Create order](/reference/createorder/) > Payment component request from your server:

* Append the `payment_data` collected from the payment component UI to the `orderData` collected during the checkout process.
* Replace the `<GATEWAY>` placeholder with the relevant gateway identifier, see [Step 2: Initialize the component](#step-2-initialize-the-component).

  ```
  curl -X POST "https://testapi.multisafepay.com/v1/json/orders" \
  --header "accept: application/json" \
  --header "Content-Type: application/json" \
  --header "api_key: <your-website-API-key>" \
  --data-raw '{
      "type": "direct",
      "order_id": "my-order-id-1",
      "gateway": "<GATEWAY>",
      "currency": "EUR",
      "amount": 100,
      "description": "Test order description",
  ...
      "payment_data": {
      "payload": "{secure_payload}"
      },
  }'
  ```

## Redirect the customer

1. From your server, pass the response to the [create order](/reference/createorder/) request to the customer's device.

2. Check that `response.success` is `true`.

3. Call the `PaymentComponent.init()` method using the following arguments:

   ```javascript
   PaymentComponent.init('redirection', {
      order: response.data
   });
   ```

   If the customer needs to perform additional actions, they are redirected to the relevant page, e.g. the `payment_url` or 3D Secure. Then, if successful, they are redirected to the `redirect_url`.

   If no further action is required, the customer is redirected to the `redirect_url`.

# 4) Go live

When you're ready to process real payments, make the following changes:

1. In [Step 2: Construct the component object](#step-2-initialize-the-component), change the environment from `test` to `live`:
   ```javascript
   PaymentComponent = new MultiSafepay({
      env: 'live',
      apiToken: apiToken,
      order: orderData
   });
   ```

2. In [Step 3: Create an order](#step-3-create-an-order), change the test endpoint to the live endpoint:
   ```
   https://api.multisafepay.com/v1/json/orders
   ```

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)