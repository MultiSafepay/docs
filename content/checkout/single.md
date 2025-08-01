---
title: "Single payment method"
category: 62bd999547298d001abc714c
order: 1
hidden: false
slug: 'payment-component-single'
parentDoc: 62a848399bb3eb004023f291 
--- 
This technical manual is for integrating a payment component using a single payment method.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/payment-component-single.png" width="450" />

# 1. Add the HTML elements

Add the following elements to your checkout page:

1. Add the component's CSS to the `<head>` of your checkout page:
   ```html
   <link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v2/components.css">
   ```

2. Add the component's script to the bottom of the `<body>` of your checkout page:
   ```html
   <script src="https://testpay.multisafepay.com/sdk/components/v2/components.js"></script>
   ```

3. Add the DOM element for the component's UI in the `<body>` of your checkout page:
   ```html
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
           locale: 'de_De',
           country: 'de'
       }
   };
   ```

   <details id="properties">
     <summary>Properties</summary>

     <br />

     | Key                | Required                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
     | ------------------ | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `amount`           | Yes                         | The value of the order. <br /> Format: Number without decimal points, e.g. 100 euro is formatted as `10000`                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | `currency`         | Yes                         | The currency of the order. <br /> Format: <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO-4217</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, e.g. `EUR`                                                                                                                                                                                                                                                                                                              |
     | `customer.country` | No                          | The customer's country code. Checks the availability of the payment method. <br /> Format: <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, e.g. `NL`                                                                                                                                                                                                                                          |
     | `customer.locale`  | No                          | The customer's language. Sets the language of the payment component UI. <br /> Format: <a href="https://en.wikipedia.org/wiki/ISO_639" target="_blank">ISO 639 language codes</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> and <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166 country codes.</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> <br /> Supported languages: `en_EN`, `es_ES`, `fr_FR`, `it_IT`, `nl_NL` |
     | `recurring.model`  | Yes, for recurring payments | The [tokenization model](/docs/recurring-payments/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

     <br />
   </details>

   <details id="how-to-process-recurring-payments">
     <summary>How to process recurring payments</summary>

     <br />

     [Recurring payments](/docs/recurring-payments/) lets you store a customer’s payment details as a secure, encrypted token.

     For subsequent payments, customers can select their stored payment details and pay with a single click.

     To process recurring payments in your payment component:

     * Add the `cardOnFile` recurring model
     * Make [List tokens](/reference/listtokens) request from your server and provide a`tokens`\ <br />

     ```JavaScript
     const orderData = {
         currency: 'EUR',
         amount: 10000,
         customer: {
             locale: 'en',
             country: 'NL'
         },
     template : {
         settings: {
             embed_mode: true
         }
     }
     };
       
     const recurringData = {
     "model": "cardOnFile",
     "tokens": [
         {
             "token": "AvqeOjgdm8A",
             "code": "IDEAL",
             "display": "xxxxxxxxxNL81PSTB0000012345",
             "bin": null,
             "name_holder": "Schilder",
             "expiry_date": "",
             "expired": 0,
             "last4": null,
             "model": "cardOnFile"
         },
         {
             "token": "BcEWsknWsYg",
             "code": "MASTERCARD",
             "display": "Card xxxx xxxx xxxx 4444",
             "bin": 555555,
             "name_holder": "Holder",
             "expiry_date": 2412,
             "expired": 0,
             "last4": 4444,
             "model": "cardOnFile"
         }]};
     ```

     > ✅ Success
     >
     > Your payment component now automatically renders a checkbox where customers can choose whether they would like to store their cardholder data for future visits.

     Recurring payments are supported for all card payments.

     **⚠️ Note:** To test card details, see Test payment details – [Credit and debit cards](/docs/testing#credit-and-debit-cards).

     To use recurring payments in your payment component, you need to enable recurring payments for your account. If you haven't already, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

     ***
   </details>

**⚠️ Note:** We use the `orderData` object to ensure the payment method is enabled, and the currency, country, and order amount are supported.

2. Construct a `PaymentComponent` object in the `test` environment using the `order` object and your API token:

```javascript
const PaymentComponent = new MultiSafepay({
	order: orderData,
	recurring: recurringData
});
```

**⚠️ Note:** To use recurring payments in your payment components, initialize the component using the `recurring` object.

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

     | Payment method   | Gateway ID   |
     | ---------------- | ------------ |
     | Bank transfer    | `BANKTRANS`  |
     | Bancontact       | `MISTERCASH` |
     | Betaal per maand | `SANTANDER`  |
     | Card payments    | `CREDITCARD` |
     | Direct debit     | `DIRDEB`     |
     | iDEAL            | `IDEAL`      |
     | In3              | `IN3`        |
     | PayPal           | `PAYPAL`     |
     | Sofort           | `DIRECTBANK` |
   </details>

3. Create event handlers for the following events:

   <details id="events">
     <summary>Events</summary>

     <br />

     | Event          | Event handler                                                                                                  |
     | -------------- | -------------------------------------------------------------------------------------------------------------- |
     | `onError`      | Called when an error occurs in the payment component.                                                          |
     | `onLoad`       | Called when the payment component UI is rendered.                                                              |
     | `onSelect`     | Occurs when the customer selects an <Glossary>issuer</Glossary> with iDEAL.                                    |
     | `onSubmit`     | Occurs when the customer clicks the payment button (when using the button generated by the component).         |
     | `onValidation` | Occurs when form validation changes. Can be used to disable the payment button until all fields are validated. |
   </details>

   **⚠️ Note:** The `PaymentComponent` uses the following methods:

   <details id="methods">
     <summary>Methods</summary>

     <br />

     | Method           | Description                                                                                                                                                                                     |
     | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `getErrors`      | Returns error details, e.g. error messages or codes                                                                                                                                             |
     | `hasErrors`      | Returns a boolean value depending on whether errors have been registered                                                                                                                        |
     | `getPaymentData` | Returns a `payment_data` object containing the `gateway`, and a `payload` containing the customer's payment details, used to [create orders](/docs/payment-component-single#3-create-an-order). |
     | `getOrderData`   | Returns an object containing a `payment_data` object and the full order configuration.                                                                                                          |
   </details>

# 3) Create an order

## Handle the interaction

1. Assign the button element to a variable:

   ```javascript
   PaymentComponent.getPaymentData()
   ```

The `payment_data` includes the following parameters:

```JSON
  {
    "payment_data": {
    "gateway": "CREDITCARD",
    "payload": "xxxxxxxx",
    "tokenize": true
  }};
```

<details id="properties">
  <summary>Parameters</summary>

  <br />

  | Key        | Required | Description                                                                                                                                                                                                   |
  | ---------- | :------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `gateway`  | Yes      | The unique `gateway_id` to redirect the customer to the specific payment method.                                                                                                                              |
  | `payload`  | Yes      | Information required to process the payment.<br /> **Note:** Do not edit or modify the `payload` or otherwise the payment fails.                                                                              |
  | `tokenize` | Optional | For [recurring payments](/docs/recurring-payments).<br /> If a customer selects to either save their cardholder data for future visits or use an existing token, a`payment_data.tokenize` parameter is added. |

  <br />

  **⚠️ Note:** When `payment_data.tokenize` is set to `true`you need to append `customer.reference` to the order data.
</details>

2. Create an event handler for the payment button to:

* When the customer clicks the payment button, call the component's `getPaymentData()` method.
* Send the response to your server and [create an order](#create-an-order).
* Return the response from your server to the client side to redirect the customer.

### Redirect the customer

The component's `redirection` handler redirects the customer to the relevant page:

* If customer actions are required to complete payment (e.g. by completing 3D Secure or iDEAL issuer authentication), the customer is redirected to the relevant page. If successful, the customer is then redirected to the `redirect_url`, i.e. the "success page".
* If no customer action is required to complete payment, the customer is redirected to the `redirect_url`, i.e. the "success page".
* If the customer chooses to pay by bank transfer, the component displays the banking details needed for customers to complete payment.
* If a QR code is available for customers to complete payment on their mobile device, the component displays the QR code.

### Avoid duplicate orders

When using your own payment button, if the customer clicks it again before they are redirected, this can create duplicate orders.

To avoid duplicate orders, disable the button until you have attempted to create an order.

Then, check `response.success`:

* If `true`, don't re-enable the button, and proceed to the redirect.
* If `false`, re-enable the button for the customer to try again.

  ```js
  paymentButton.addEventListener('click', e => {
      paymentButton.disabled = true;
      if (PaymentComponent.hasErrors()) {
          let errors = PaymentComponent.getErrors();
          console.log(errors);
          return false;
      }
      createOrder(PaymentComponent.getOrderData()).then(response => {
          if(!response || !response.success) {
              paymentButton.disabled = false;
              console.log(response);
          } else {
              PaymentComponent.init('redirection', {
                  order: response.data
              });
          }
      });
  });
  ```

Use the `createOrder()` function to pass the `orderData` to your server.

## Create an order

Create an <Glossary>order</Glossary> from your server, appending the `payment_data` collected from the payment component UI to the order data.

#### Example

```json
    {
    "type": "direct",
    "order_id": "test_order_id",
    "currency": "EUR",   
    "amount": 100,    
    "description": "Test Order Description",    
    "payment_data": 
        {    
        "payload":"payment_component_method_response",
        "gateway": "CREDITCARD",    
        }
    }
```

See API reference – [Create order](/reference/createorder/) > Payment component.

## Redirect the customer

1. From your server, pass the response to the [create order](/reference/createorder/) request to the customer's device.

2. Check that `response.success` is `true`.

3. Handle the response

   Call the `PaymentComponent.init()` method using the following arguments:

   ```js
   PaymentComponent.init('redirection', {
       order: response.data
   });
   ```

   The component's `redirection` handler redirects the customer to the relevant page:

   * If customer action is required to complete payment (e.g. by completing 3D Secure or iDEAL issuer authentication), the customer is redirected to the relevant page. If successful, the customer is then redirected to the `redirect_url`, (i.e. the "success page").
   * If no customer action is required to complete payment, the customer is redirected to the `redirect_url`, (i.e. the "success page").
   * If the customer chooses to pay by bank transfer, the component displays the banking details needed for customers to complete payment.
   * If a QR code is available for customers to complete payment on their mobile device, the component displays the QR code.

# 4) Go live

To test the payment method, use our [Testing](/docs/testing#test-payment-details).

When you're ready to process real payments, make the following changes:

1. In [Step 1: Add the HTML elements](#1-add-the-html-elements), replace the:

   * Test JavaScript library with the **live** JavaScript library:

   ```
   <script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
   ```

   * Test CSS file with the **live** CSS file:

   ```
   <link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
   ```

2. In [Step 2: Construct the component object](#construct-the-component-object), change the environment from `test` to `live`:
   ```javascript
   PaymentComponent = new MultiSafepay({
       env: 'live',
       apiToken: apiToken,
       order: orderData
   });
   ```

3. In [Step 3: Create an order](#3-create-an-order), change the test endpoint to the live endpoint:
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