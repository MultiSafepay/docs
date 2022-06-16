---
title : 'Previous release'
category: 6278c92bf4ad4a00361431b0
order: 304
hidden: false
slug: 'payment-component-previous-release'
parentDoc: 62a848399bb3eb004023f291 
excerpt: 'Technical manual for integrating the previous release of the payment component.'
--- 

# Step 1: Add the elements

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

# Step 2: Initialize the component

## Generate an API token
Payment Components require a MultiSafepay API token. See API reference – [Generate an API token](https://docs-api.multisafepay.com/reference/generateapitoken).

:warning: To keep your API key private, request the token from your own server. 

## Construct the component object

1. Initialize an `orderData` object, containing information about the customer's order collected during the checkout process:

    ```
    const orderData = {
        currency: 'EUR',
        amount: 10000,
        customer: {
            locale: 'en',
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

    <details id="properties">
    <summary>Properties</summary>
    <br>

    | Key | Value |
    | ---- | ---- |
    | currency| The currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
    | amount| The value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
    | customer.country| The customer's country code. Checks the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Required**. |
    |customer.locale | The customer's language. Sets the language of the payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
    | template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |

    </details>

    **Note:** We use the `orderData` object to ensure the payment method is enabled and the currency, country, and transaction amount are supported. 

2. Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

    ```
    PaymentComponent = new MultiSafepay({
        env: 'test',
        apiToken: apiToken,
        order: orderData
    });
    ```

## Initialize the component

1. Call the `PaymentComponent.init()` method with the following arguments:

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
2. Replace the `<GATEWAY>` placeholder with the relevant payment gateway identifier.

    <details id="gateway-ids">
    <summary>Gateway IDs</summary>
    <br>

    |Payment method|Gateway IDs|
    |---|---|
    |Credit card|`CREDITCARD`|
    |iDEAL|`IDEAL`|

    </details>

3. Create event handlers for the following events:

    <details id="events">
    <summary>Events</summary>
    <br>

    | Event | Event handler |
    | ---- | ---- |
    |`onError`| Called when an error occurs in the payment component|
    |`onLoad`| Called when the payment component UI is rendered |

    </details>

    **Note:** The `PaymentComponent` uses the following methods:

    <details id="methods">
    <summary>Methods</summary>
    <br>

    | Method | Description |
    | ---- | ---- |
    |`getErrors`| Returns error details, e.g. error messages or codes.|
    |`hasErrors`| Returns a boolean value depending on whether errors have been registered. |
    |`getPaymentData`| Creates a `payload` object with the customer's payment details, used to create orders|

    </details>

# Step 3: Create an order

## Collect payment data

1. To collect the customer's payment details from the payment component UI, call the `PaymentComponent.getPaymentData()` method:

    ```
    PaymentComponent.getPaymentData()
    ```

2. Pass the `payment_data` to your server.

## Create an order

Make a [Create order](https://docs-api.multisafepay.com/reference/createorder) > Payment component request from your server:

- Append the `payment_data` collected from the payment component UI to the `orderData` collected during the checkout process.
- Replace the `<GATEWAY>` placeholder with the relevant gateway identifier, see [Step 2: Initialize the component](#step-2-initialize-the-component).

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

1. From your server, pass the response to the [create order](https://docs-api.multisafepay.com/reference/createorder) request to the customer's device. 

2. Check that `response.success` is `true`.

3. Call the `PaymentComponent.init()` method using the following arguments:
    ```
    PaymentComponent.init('redirection', {
        order: response.data
    });
    ```
    
    If the customer needs to perform additional actions, they are redirected to the relevant page, e.g. the `payment_url` or 3D Secure. Then, if successful, they are redirected to the `redirect_url`.

    If no further action is required, the customer is redirected to the `redirect_url`.

# Step 4: Go live

When you're ready to process real payments, make the following changes:

1. In [Step 2: Construct the component object](#step-2-initialize-the-component), change the environment from `test` to `live`:
    ```
    PaymentComponent = new MultiSafepay({
        env: 'live',
        apiToken: apiToken,
        order: orderData
    });
    ```

2. In [Step 3: Create an order](#step-3-create-an-order), change the test endpoint to the live endpoint:  

    `https://api.multisafepay.com/v1/json/orders`
<br>

---

> 💬  Support
> Email <support@multisafepay.com>