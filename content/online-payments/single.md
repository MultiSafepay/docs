---
title : "Single payment method"
category: 6278c92bf4ad4a00361431b0
order: 301
hidden: false
slug: 'payment-component-single'
parentDoc: 62a848399bb3eb004023f291 
excerpt: 'Technical manual for integrating a payment component using a single payment method.'
--- 

# Step 1: Add the elements

Add the following elements to your checkout page:

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

# Step 2: Initialize the component

## Generate an API token

  Payment Components require a MultiSafepay API token. See API reference – [Generate an API token](https://docs-api.multisafepay.com/reference/generateapitoken).

  > **Tip!** To keep your API key private, request the token from your own server.  

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
    | customer.country| The customer's country code. Checks the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Optional**. |
    |customer.locale | The customer's language. Sets the language of the payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
    | customer.reference| Your unique customer reference. **Required for recurring payments**. |
    | recurring.model| The [tokenization model](/recurring-payments/). **Required for recurring payments**. |
    | template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |

    </details>

    <details id="how-to-process-recurring-payments">
    <summary>How to process recurring payments</summary>
    <br>

    [Recurring payments](/recurring-payments/) lets you store a customer’s payment details as a secure, encrypted token.

    For subsequent payments, customers can select their stored payment details and pay with a single click.

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

    | Payment method| Gateway ID|
    |---|---|
    | Bank Transfer | `BANKTRANS` |
    | Bancontact | `MISTERCASH` |
    | Credit cards |`CREDITCARD`|
    | iDEAL|`IDEAL`|
    | PayPal | `PAYPAL` |
    | SEPA Direct Debit | `DIRDEB` |
    | Sofort | `DIRECTBANK`|

    </details>

3. Create event handlers for the following events:

    <details id="events">
    <summary>Events</summary>
    <br>

    | Event | Event handler |
    | ---- | ---- |
    |`onError`| Called when an error occurs in the payment component|
    |`onLoad`| Called when the payment component UI is rendered |
    |`onSelect`| Occurs when the customer selects an issuer with iDEAL. |
    |`onSubmit`| Occurs when the customer clicks the payment button (when using the button generated by the component). |
    |`onValidation`| Occurs when form validation changes. Can be used to disable the payment button until all fields are validated. |

    </details>

    **Note:** The `PaymentComponent` uses the following methods:

    <details id="methods">
    <summary>Methods</summary>
    <br>

    | Method | Description |
    | ---- | ---- |
    |`getErrors`| Returns error details, e.g. error messages or codes|
    |`hasErrors`| Returns a boolean value depending on whether errors have been registered |
    |`getPaymentData`| Returns a `payment_data` object with a `payload` containing the customer's payment details, used to [create orders](/payment-components/single/step-3/), and the `gateway`.|
    |`getOrderData`| Returns an object containing a `payment_data` object and the full order configuration. |

    </details>

# Step 3: Create an order

## Collect payment data

1. To collect the customer's payment details from the payment component UI, call the `PaymentComponent.getPaymentData()` method:

    ```
    PaymentComponent.getPaymentData()
    ```

2. Pass the `payment_data` to your server.

## Create an order

Create an order from your server, appending the `payment_data` collected from the payment component UI to the order data.

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Payment component.

## Redirect the customer

1. From your server, pass the response to the [create order](https://docs-api.multisafepay.com/reference/createorder) request to the customer's device. 

2. Check that `response.success` is `true`.

3. Handle the response:

    <details id="bank-transfer-payments">
    <summary>Bank Transfer payments</summary>
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

    <details id="other-payment-methods">
    <summary>Other payment methods</summary>
    <br>

    Call the `PaymentComponent.init()` method using the following arguments:
    ```
    PaymentComponent.init('redirection', {
        order: response.data
    });
    ```

    If 3D Secure verification is:

    - Required, the customer is first directed to 3D Secure. If successful, the customer is then redirected to the `redirect_url`. 
    - Not required, the customer is redirected to the `redirect_url`.

    </details>

# Step 4: Go live

To test the payment method, use our [Test payment details](/testing/test-payment-details/).

When you're ready to process real payments, make the following changes:

1. In [Step 1: Add the elements](#step-1-add-the-elements), replace test JavaScript library with the live JavaScript library:
    ```
    <script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
    ```

    Next, replace the test CSS file with the live CSS file:
    ```
    <link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
    ```

2. In [Step 2: Construct the component object](#step-2-initialize-the-component), change the environment from `test` to `live`:
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

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)