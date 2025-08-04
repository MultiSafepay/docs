---
title: FastCheckout JavaScript integration
category:
  uri: Checkout
slug: fastcheckout-integration
position: 0
privacy:
  view: public
parent:
  uri: fastcheckout
---

This technical manual is for embedding FastCheckout into your website using JavaScript.

# 1. Add the HTML elements

1. Add FastCheckout's CSS to the `<head>` of your checkout page:
   ```html
   <link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/fco/v1/fco.css">
   ```

2. Add the FastCheckout script to the bottom of the `<body>` of your checkout page:
   ```html
   <script src="https://testpay.multisafepay.com/sdk/fco/v1/fco.js"></script>
   ```

3. Add the DOM element for the FastCheckout UI in the `<body>` of your checkout page:
   ```html
   <div id="FastCheckout"></div>
   ```

# 2) Create an order

1. [Create an order](/reference/createorder/) from your server:

   ```javascript
   const createOrderResponse = createOrder()
   ```

2. Pass the response to the client side.

# 3) Construct a FastCheckout object

```javascript
const fastCheckout = new FastCheckout ({
    sessionId: createOrderResponse.data.session_id,
    locale: params.locale,
    brand: "fco"
});
```

<details id="construct-properties">
  <summary>Properties key</summary>

  <br />

  | Key         | Required | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | ----------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `brand`     | No       | Applies the default FastCheckout styling <br /> Set to `fco`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | `locale`    | No       | Sets the language and country of the FastCheckout page <br /> Format: <br /> - <a href="https://en.wikipedia.org/wiki/ISO_639" target="_blank">ISO-639 language code </a> <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} /> <br /> - <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1 alpha-2 country code</a> <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} /> <br /> Supported locales: `de_DE`, `en_US`, `es_ES`, `fr_FR`, `it_IT`, `nl_NL` |
  | `sessionId` | Yes      | The identifier of the MultiSafepay session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

  <br />
</details>

# 4. Initialize FastCheckout

1. Define the FastCheckout settings:

   ```javascript
   const settings = {
       "fco": {   
           "redirect_mode": "modal",
           "coupons": {
               "disabled": false
           },
           "cart": {
               "disabled": false
           },
           "shipping": {
              "address": {
                "required": true
               }
           },
           "checkout": {
               "customer": {
                   "enabled": true
               }
           },
           "issuers_display_mode": "radioList",
           "group_cards": true
       }
   }
   ```

<details id="initialize-properties">
  <summary>Properties key</summary>

  <br />

  All properties are **optional**.

  | Key                         | Value                                                                                                                                                                                                                                                          |
  | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `cart.disabled`             | Whether to display the shopping cart summary on the FastCheckout page: <br /> -      `true`: Hides the shopping cart <br /> - `false` (default): Displays the shopping cart                                                                                    |
  | `checkout.customer.enabled` | Whether to display the billing element on the FastCheckout page: <br /> - `true`: Displays billing element <br /> - `false` (default): Hides billing element                                                                                                   |
  | `coupons.disabled`          | Whether to display available gift cards in the payment element: <br /> - `true`: Hides gift cards <br /> - `false` (default): Displays gift cards                                                                                                              |
  | `group_cards`               | Whether to bundle available card payments into a single gateway: <br /> - `true`   (recommended): Displays a single card payment gateway <br /> - `false` (default): Displays all available card payments as separate options                                  |
  | `issuers_display_mode`      | How to display available <Glossary>issuers</Glossary>: <br /> - `list`: Displays issuers in a list with logos <br /> - `select`: Displays issuers in a dropdown list, without logos <br /> - `select-button` (default): Displays issuers as buttons with logos |
  | `redirect_mode`             | How to redirect the customer to the issuer: <br /> - `modal`: Displays the issuer page as a modal window over the FastCheckout page <br /> - `redirect` (default): Redirects to the issuer page in the current browser tab                                     |
  | `shipping.address.required` | Whether to display the shipping element on the FastCheckout page: <br /> - `true`: Displays the shipping element <br /> - `false` (default): Hides the shipping element                                                                                        |

  <br />
</details>

2. Initialize FastCheckout:

   ```javascript
   fastCheckout .init('FastCheckout', {
       settings: settings,
       onError: function (state) {
           console.log('onError', state);
       },
       onLoad: function (state) {
           console.log('onLoad', state);
       },
       onSubmit: function (state) {
           console.log('onSubmit', state);
       }
   });
   ```

3. In the method call, create event handlers for the following events:

   | Event      | Event handler                                          |
   | ---------- | ------------------------------------------------------ |
   | `onError`  | Occurs when there is an error in the FastCheckout page |
   | `onLoad`   | Occurs when the FastCheckout page is rendered          |
   | `onSubmit` | Occurs when the order is successfully submitted        |

4. `fastCheckout` has one method:

   | Method    | Description                                                            |
   | --------- | ---------------------------------------------------------------------- |
   | `clear()` | Removes all elements in the library leaving the parent container empty |

# 5) Test

To test the payment methods, see Testing payment methods - \[(/docs/testing#test-payment-details).

# 6. Go live

When you're ready to process real payments, make the following changes:

1. In [Step 1: Add the HTML elements](#1-add-the-html-elements), replace the:

   * Test JavaScript library with the **live** JavaScript library:

   ```html
   <script src="https://pay.multisafepay.com/sdk/fco/v1/fco.js"></script>
   ```

   * Test CSS file with the **live** CSS file:

   ```html
   <link rel="stylesheet" href="https://pay.multisafepay.com/sdk/fco/v1/fco.css">
   ```

2. In [Step 2: Create an order](#2-create-an-order), change the test endpoint to the **live** endpoint:
   ```
   https://api.multisafepay.com/v1/json/orders
   ```

<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
