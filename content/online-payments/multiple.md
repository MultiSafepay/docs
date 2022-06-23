---
title: "Multiple payment methods"
category: 6278c92bf4ad4a00361431b0
order: 302
hidden: false
slug: 'payment-component-multiple'
parentDoc: 62a848399bb3eb004023f291 
excerpt: 'Technical manual for integrating a payment component using multiple payment methods.'
--- 

# Step 1: Add the elements

1. Add the component's CSS to the `<head>` of your checkout page:  
    ```
    <link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v2/components.css">
    ```

2. Add the component's script to the bottom of the `<body>` of your checkout page:  
    ```
    <script src="https://testpay.multisafepay.com/sdk/components/v2/components.js"></script>
    ```

3. Add the DOM element for the component's UI in the `<body>` of your checkout page:
    ```
    <div id="MultiSafepayPayment"></div>
    ```

## Choose your payment button

Decide if you want to:

- Generate a button with the component (see [Step 2](#step-2-initialize-the-component) below). **Recommended.**
- Use an existing button, e.g. if your checkout already includes one.
- Create your own button:

    ```
    <button id="payment-button"></button>
    ```

# Step 2: Initialize the component

## Generate an API token
Payment Components require a MultiSafepay API token. See API reference – [Generate an API token](https://docs-api.multisafepay.com/reference/generateapitoken).

> **Tip!** To keep your API key private, request the token from your own server. 

## Construct the component object

1. Initialize an `orderData` object containing information about the customer's order collected during the checkout process:
    ```
    const orderData = {
        currency: 'EUR',
        amount: 10000,
        customer: {
            locale: 'en',
            country: 'NL',
            reference: 'Customer123'
        },    
        payment_options: {
            settings: {
                connect: {
                    group_cards: true
                }
            }
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
    <br>

    | Key | Value |
    | ---- | ---- |
    | currency| The currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
    | amount| The value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
    | customer.country|The customer's country code. Used to validate the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Optional**. |
    |customer.locale | The customer's language. Sets the language of the payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
    | customer.reference| Your unique customer reference. **Required for recurring payments**. |
    | recurring.model| The [recurring model](/recurring-payments/). **Required for recurring payments**. |
    | template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |
    |payment_options.settings.connect.group_cards| Groups all credit card payment methods as a single option in the list of payment methods. Format:&nbsp;Boolean. **Optional**. Default: `false`.|

    </details>

    <details id="how-to-process-recurring-payments">
    <summary>How to process recurring payments</summary>
    <br>

    [Recurring payments](/recurring-payments/) is a feature that lets you store a customer’s payment details as a secure, encrypted token.

    Upon subsequent payments, customers can select their stored payment details and pay with a single click.

    To process recurring payments in your payment component:

    - Add the `cardOnFile` recurring model
    - Provide the relevant `customer.reference`

    ```
    const orderData = {
        currency: 'EUR',
        amount: 10000,
        customer: {
            locale: 'en',
            country: 'NL',
            reference: 'Customer123'
        },
        recurring: {
            model: 'cardOnFile'
        }
    };
    ```

    Recurring payments are supported for all credit card payments.

    **Note**: For test credit card details, see Test payment details – [Credit and debit cards](/testing/#credit-and-debit-cards).

    To use recurring payments in your payment component, you need to enable recurring payments for your account. If you haven't already, email <sales@multisafepay.com>

    </details>

    **Note:** We use the `orderData` object to ensure the payment methods are enabled, e.g. for the currency, country, and transaction value. 

2. Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

    ```
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

```
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
    },
    onSubmit : state => {
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
                });
            }
        });
    }
});
```

</details>

<details id="own-or-existing-button">
<summary>Own or existing button</summary>
<br>

```    
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

| Event | Event handler |
| ---- | ---- |
|`onLoad`| Occurs when the payment component UI is rendered. |
|`onError`| Occurs when an error occurs in the payment component. |
|`onSelect`| Occurs when the customer selects an <<glossary:issuer>> with iDEAL. |
|`onSubmit`| Occurs when the customer clicks the payment button (when using the button generated by the component). |
|`onValidation`| Occurs when form validation changes. Can be used to disable the payment button until all fields are validated. |

</details>

The `PaymentComponent` has the following methods:

<details id="methods">
<summary>Methods</summary>
<br>

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error messages or codes|
|`hasErrors`| Returns a boolean value about whether errors were registered |
|`getPaymentData`| Returns a `payment_data` object with a `payload` containing the customer's payment details, used to [create orders](/payment-component-single/), and the `gateway`.|
|`getOrderData`| Returns an object containing a `payment_data` object and the full order configuration. |

</details>

# Step 3: Create an order

## Handle the interaction

> **Tip!** This step only applies if using your own or an existing payment button.

1. Assign the button element to a variable:

    ```
    const paymentButton = document.querySelector('#payment-button');
    ```

2. Create an event handler for the payment button:

    - When the customer clicks the payment button, call the `getPaymentData()` method.
    - Send the response to your server and [create an order](#create-an-order).
    - Return the reponse from your server to the client-side to redirect the customer.
    <br>

    ```
    paymentButton.addEventListener('click', e => {
        paymentButton.addAttribute('disabled');
        if (PaymentComponent.hasErrors()) {
            let errors = PaymentComponent.getErrors();
            console.log(errors);
            return false;
        }
        createOrder(PaymentComponent.getPaymentData()).then(response => {
            if(!response || !response.success) {
                paymentButton.removeAttribute('disabled');
                console.log(response);
            } else {
                PaymentComponent.init('redirection', {
                    order: response.data
                });
            }
        });
    });
    ```
  
## Avoid duplicate orders

When using your own payment button, if the customer clicks it again during the latency before redirection, this creates duplicate orders. 

To avoid duplicate orders, disable the button until you have attempted to create an order.  
Then, check `response.success`:

- If `true`, don't re-enable the button and proceed to the redirect.
- If `false`, re-enable the button for the customer to try again. 

    <details id="redirect-to-3d-authentication">
    <summary>Redirect to 3D authentication</summary>
    <br>

    The `init('redirection')` method redirects customers paying by credit card to the relevant page.

    If 3D Secure authentication is:

    - Required, the customer is first directed to 3D Secure. If successful, they are then redirected to the `redirect_url`. 

    - Not required, the customer is redirected to the `redirect_url`.

    </details>

    <details id="redirect-bank-transfer-payments">
    <summary>Redirect Bank Transfer payments</summary>
    <br>

    In the `gateway_info` object, you receive the bank account details for the customer to wire the funds to.

    Render the account details in the interface for the customer with clear instructions. (MultiSafepay also emails these details to the customer.)

    **Example gateway_info object**
    ```
    {
    "gateway_info":{
        "mtpinfo":"NL25DEUT7351811717",
        "reference":"9202124254788300",
        "issuer_name":"Sofortbank",
        "destination_account_id":"003001380000",
        "destination_holder_name":"MultiSafepay",
        "destination_holder_city":"Zurich",
        "destination_holder_country":"CH",
        "destination_holder_iban":"NL25DEUT7351811717",
        "destination_holder_swift":"DEUTCHZZ",
        "account_holder_name":"testperson-nl approved",
        "account_holder_city":"gravenhage",
        "account_holder_coutry":"NL"
    }
    }
    ```
    </details>

## Create an order

Create an order from your server, appending the `payment_data` collected from the payment component UI to the order data.

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Payment component.

# Step 4: Go live

To test the payment methods, use our [Testing](/testing/test-payment-details/).

When you're ready to process real payments, make the following changes:

1. In [Step 1: Add the elements](/#step-1-add-the-elements), replace test JavaScript library with the live JavaScript library:
    ```
    <script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
    ```

    Next, replace the test CSS file with the live CSS file:
    ```
    <link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
    ```

2. In [Step 2: Construct the component object](#step-2-construct-the-component-object), change the environment from `test` to `live`:
    ```
    PaymentComponent = new MultiSafepay({
        env: 'live',
        apiToken: apiToken,
        order: orderData
    });
    ```

3. In [Step 3: Create an order](#step-3-create-an-order), change the test endpoint to the live endpoint:  

    `https://api.multisafepay.com/v1/json/orders`
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
