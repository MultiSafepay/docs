---
title: "Multiple payment methods"
category: 62bd999547298d001abc714c
order: 2
hidden: false
slug: 'payment-component-multiple'
parentDoc: 62a848399bb3eb004023f291 
--- 

 
This technical manual is for integrating a payment component using multiple payment methods.


<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/payment-components-examples" target="_blank"><span>Component examples</span></a>
 
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/payment-component-multiple.png" width="450"/>
 
# 1\. Add the HTML elements
 
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
 
## Choose your payment button
 
Decide if you want to:
 
- Generate a button with the component (see [Step 2](#2-initialize-the-component) below). **Recommended.**
- Use an existing button, e.g. if your checkout already includes one.
- Create your own button:
 
  ```html
<button id="payment-button"></button>
  ```
 
# 2. Initialize the component
 
## Generate an API token
 
Payment components require a MultiSafepay API token. See API reference – [Generate an API token](/reference/generateapitoken/).
 
✅   **Tip!** To keep your API key private, request the token from your own server.
 
## Construct the component object
 
1. Initialize an `orderData` object containing information about the customer's <<glossary:order>> collected during the checkout process:
 
   ```javascript
   const orderData = {
       currency: 'EUR',
       amount: 10000,
       customer: {
           locale: 'en',
           country: 'NL'
       },    
       payment_options: {
           settings: {
               connect: {
                   group_cards: true
                   qr: {
                       enabled: true,
                       autoload: false
               }
           }
       },
   };
   ```
 
   <details id="properties">
<summary>Properties</summary>
<br>
 
   [block:parameters]{"data":{"h-0":"Key","h-1":"Required","h-2":"Value","0-0":"amount","0-1":"Yes","0-2":"The value of the order. <br> Format: Number without decimal points, e.g. 100 euro is formatted as `10000`","1-0":"currency","1-1":"Yes","1-2":"The currency of the order. <br> Format: <a href=\"https://en.wikipedia.org/wiki/ISO_4217\" target=\"_blank\">ISO-4217</a> <i class=\"fa fa-external-link\" style=\"font-size:12px;color:#8b929e\"></i>, e.g. `EUR`","2-0":"customer.country","2-1":"No","2-2":"The customer's country code. Used to validate the availability of the payment method. <br> Format: <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\" target=\"_blank\">ISO-3166-1 alpha-2</a> <i class=\"fa fa-external-link\" style=\"font-size:12px;color:#8b929e\"></i>, e.g. `NL`","3-0":"customer.locale","3-1":"No","3-2":"The customer's language. Sets the language of the payment component UI. <br> Format: <a href=\"https://en.wikipedia.org/wiki/ISO_639\" target=\"_blank\">ISO 639</a> <i class=\"fa fa-external-link\" style=\"font-size:12px;color:#8b929e\"></i> <br> Supported languages: `en`, `es`, `fr`, `it`, `nl`","4-0":"customer.reference","4-1":"Yes, for recurring payments","4-2":"Your unique customer reference.  \n(\\*currently not supported for QR payments.)","5-0":"payment_options.settings.connect.group_cards","5-1":"No","5-2":"Groups all card payment methods as a single option in the list of payment methods. <br> Format: Boolean <br> Default: `false`.","6-0":"payment_options.settings.connect.qr","6-1":"No","6-2":"Allows QR code to be rendered for iDEAL and Bancontact: `enabled`  \n `autoload` allows automatic display of QR code, and subsequent redirect for these methods. Default: `true`","7-0":"recurring.model","7-1":"Yes, for recurring payments","7-2":"The [recurring model](/docs/recurring-payments/).","8-0":"template.settings.embed_mode","8-1":"No","8-2":"A template designed to blend in seamlessly with your ecommerce platform. <br> Format: Boolean"},"cols":3,"rows":9,"align":["left","left","left"]}[/block]
 
   <br>
 
   </details>
 
   <details id="how-to-process-recurring-payments">
<summary>How to process recurring payments</summary>
<br>
 
   [Recurring payments](/docs/recurring-payments/) is a solution that lets you store a customer’s payment details as a secure, encrypted token.
 
   Upon subsequent payments, customers can select their stored payment details and pay with a single click.
 
   To process recurring payments in your payment component:
 
   - Add the `cardOnFile` recurring model
   - Make [List tokens](/reference/listtokens) request from your server and provide a`tokens`  
<br>
 
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
> Your payment component now automatically renders a checkbox where customers can choose whether they would like to store their payment details for future visits.
 
   Recurring payments are supported for all card payments.
 
   📘 **Note:** To test card details, see Test payment details – [Credit and debit cards](/docs/testing#credit-and-debit-cards).
 
   To use recurring payments in your payment component, you need to enable recurring payments for your account. If you haven't already, email [\[sales@multisafepay.com\](mailto:sales@multisafepay.com)](mailto:[sales@multisafepay.com](mailto:sales@multisafepay.com))
 
   </details>
 
   📘 **Note:** We use the `orderData` object to ensure the payment methods are enabled, e.g. for the currency, country, and order value.
 
2. Construct a `PaymentComponent` object in the `test` environment using the `order` object and your API token:
 
   ```javascript
   PaymentComponent = new MultiSafepay({
       env: 'test',
       apiToken: apiToken,
       order: orderData
   });
   ```
 
## Initialize the component
 
Initialize the component using:
 
<details id="payment-component-button">
<summary>Payment component button</summary>
<br>
 
```javascript
PaymentComponent.init('dropin', {
   container: '#MultiSafepayPayment',
    onGetQR: function (state) {      
        console.log('onGetQR', state);
    },
    onError: function (state) {      
        console.log('onError', state);
    },
    onEvent: function (state) {
        console.log('onEvent', state);
    },
    onSubmit: function (state) {
        if(PaymentComponent.hasErrors()) {
            let errors = PaymentComponent.getErrors();
            console.log(errors);
            return;
        }

        // Send state.paymentData to your server (createOrder)
        // Create an order from your server
        // Return the response from your server to the client-side
        // With the response, redirect the customer or log an error

        createOrder(PaymentComponent.getPaymentData()).then(response => {
            console.log(response);
            if(response.success) {
                PaymentComponent.init('redirection', {
                    order: response.data

            }
        });
    },    
    onValidation: function (state) {
     console.log('onValidation', state);
    },  
    onSelect: function (state) { 
        console.log('onSelect', state);
    },
    onLoad: function (state) {
        console.log('onLoad', state);
    }
});
```
 
</details>
 
<details id="own-or-existing-button">
<summary>Own or existing button</summary>
<br>
 
```javascript
PaymentComponent.init('dropin', {
    container : '#MultiSafepayPayment',
    onSelect : state => {
        console.log('onSelect', state);
    }, 
    onError : state => {
        console.log('onError', state);
    },
    onLoad : state => {
        console.log('onLoad', state);
    }
});
```
 
</details>
 
In the method call, create event handlers for the following events:
 
<details id="events">
<summary>Events</summary>
<br>
 
[block:parameters]
{
  "data": {
    "h-0": "Event",
    "h-1": "Event handler",
    "0-0": "`onError`",
    "0-1": "Occurs when there is an error in the payment component.",
    "1-0": "`onGetQR`",
    "1-1": "Occurs when the QR is rendered in the payment component.  \n**Example**:  \n  \n onGetQR: e => {  \n   createOrder(e.orderData).then(response => {  \n        PaymentComponent.setQR({  \n            order: response.data  \n            });  \n    });  \n},  \n\\`\\`\\`  \nAfter creating the order, you invoke getQR.",
    "2-0": "`onLoad`",
    "2-1": "Occurs when the payment component UI is rendered.",
    "3-0": "`onSelect`",
    "3-1": "Occurs when the customer selects an <<glossary:issuer>> with iDEAL.",
    "4-0": "`onSubmit`",
    "4-1": "Occurs when the customer clicks the payment button (when using the button generated by the component).",
    "5-0": "`onValidation`",
    "5-1": "Occurs when form validation changes. Can be used to disable the payment button until all fields are validated."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]
 
 
</details>
 
The `PaymentComponent` has the following methods:
 
<details id="methods">
<summary>Methods</summary>
<br>
 
[block:parameters]
{
  "data": {
    "h-0": "Method",
    "h-1": "Description",
    "0-0": "`getErrors`",
    "0-1": "Returns error messages or codes.",
    "1-0": "`hasErrors`",
    "1-1": "Returns a boolean value about whether errors were registered.",
    "2-0": "`getOrderData`",
    "2-1": "Returns an object containing a `payment_data` object and the full order configuration.",
    "3-0": "`getPaymentData`",
    "3-1": "Returns a `payment_data` object with a `payload` containing the customer's payment details, used to [create orders](/docs/payment-component-single/), and the `gateway`.",
    "4-0": "`setQR ()`",
    "4-1": "Returns a  boolean to set up the QR code. Requires argument `orderData`.  \nIf `orderData` is not sent, the payment will not be associated to the order."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]
 
 
</details>
 
# 3\. Create an order
 
## Handle the interaction
 
✅   **Tip!** This step only applies if using your own or an existing payment button.
 
1. Assign the button element to a variable:
 
   ```javascript
   const paymentButton = document.querySelector('#payment-button');
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
<br>
 
| Key        | Required | Description                                                                                                                                                                                                 |
| ---------- | :------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gateway`  | Yes      | The unique `gateway_id` to redirect the customer to the specific payment method.                                                                                                                            |
| `payload`  | Yes      | Information required to process the payment.<br> **Note:** Do not edit or modify the `payload` or otherwise the payment fails.                                                                              |
| `tokenize` | Optional | For [recurring payments](/docs/recurring-payments).<br> If a customer selects to either save their cardholder data for future visits or use an existing token, a`payment_data.tokenize` parameter is added. |
 
**Note:** When `payment_data.tokenize` is set to `true`you need to append `customer.reference` to the order data.
 
</details>
 
2. Create an event handler for the payment button:
 
   - When the customer clicks the payment button, call the component's `getPaymentData()` method.
   - Send the response to your server and [create an order](#create-an-order).
   - Return the reponse from your server to the client-side to redirect the customer.  
<br>
 
### Redirect the customer
 
You need to fetch the property payment_url, which will then - depending on the result - redirect the customer to the correct page. This may be for 3ds required cards towards the authentication step, or for frictionless / not required 3ds, towards the success page.  
The handling of the payment_url lies on your side.
 
The component's `redirection` handler redirects the customer to the relevant page:
 
- If customer actions are required to complete the payment (e.g. by completing 3D Secure or iDEAL issuer authentication), the customer is redirected to the relevant page. If successful, the customer is then redirected to the `redirect_url`, i.e. the "success page". 
- If no customer action is required to complete the payment, the customer is redirected to the `redirect_url`, i.e. the "success page".
- If the customer chooses to pay by bank transfer, the component displays the banking details needed for customers to complete payment. 
- If a QR code is available for customers to complete payment on their mobile device, the component displays the QR code.
 
### Avoid duplicate orders
 
When using your own payment button, if the customer clicks it again before they are redirected, this can create duplicate orders.
 
To avoid duplicate orders, disable the button until you have attempted to create an order.  
 
Then, check `response.success`:
 
- If `true`, don't re-enable the button, and proceed with the redirect.
- If `false`, re-enable the button for the customer to try again.
 
  ```js
  paymentButton.addEventListener('click', e => {
      paymentButton.addAttribute('disabled');
      if (PaymentComponent.hasErrors()) {
          let errors = PaymentComponent.getErrors();
          console.log(errors);
          return false;
      }
      createOrder(PaymentComponent.getPaymentData()).then(response => {
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
 
## Create an order
 
Create an <<glossary:order>> from your server, appending the `payment_data` collected from the payment component UI to the order data.
 
See API reference – [Create order](/reference/createorder/) > Payment component.
 
# 4\. Go live
 
To test the payment methods, see Testing payment methods - \[(/docs/testing#test-payment-details).
 
When you're ready to process real payments, make the following changes:
 
1. In [Step 1: Add the elements](#1-add-the-elements), replace the test JavaScript library with the live JavaScript library:
 
   ```html
<script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
   ```
 
   Next, replace the test CSS file with the live CSS file:
 
   ```html
<link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
   ```
 
2. In [Step 2: Construct the component object](#2-construct-the-component-object), change the environment from `test` to `live`:
   ```js
   PaymentComponent = new MultiSafepay({
       env: 'live',
       apiToken: apiToken,
       order: orderData
   });
   ```
 
3. In [Step 3: Create an order](#3-create-an-order), change the test endpoint to the **live** endpoint:
   ```
https://api.multisafepay.com/v1/json/orders
   ```