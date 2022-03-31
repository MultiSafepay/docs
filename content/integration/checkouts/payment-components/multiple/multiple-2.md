---
title : "Integrating multiple payment components"
breadcrumb_title : "Step 2"
meta_title: "Payment Components - Integrating multiple payment methods step 2 - MultiSafepay Docs"

layout: 'single'
read_more: '.'
url: '/payment-components/multiple/step-2/'
--- 

## Step 2: Initialize the component

### Generate an API token
Payment Components require a MultiSafepay API token. See API reference&nbsp;–&nbsp;[Generate an API token](https://api-docs.multisafepay.com/reference/generateapitoken).

{{< alert-notice >}} **Note:** To keep your API key private, request the token from your own server. {{< /alert-notice >}} 

### Construct the component object

**1.** Initialize an `orderData` object containing information about the customer's order collected during the checkout process:

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

{{< details title="View properties" >}}

| Key | Value |
| ---- | ---- |
| currency| The currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
| amount| The value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
| customer.country|The customer's country code. Used to validate the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Optional**. |
|customer.locale | The customer's language. Sets the language of the payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
| customer.reference| Your unique customer reference. **Required for recurring payments**. |
| recurring.model| The [recurring model](/payments/features/tokenization/). **Required for recurring payments**. |
| template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |
|payment_options.settings.connect.group_cards| Groups all credit card payment methods as a single option in the list of payment methods. Format:&nbsp;Boolean. **Optional**. Default: `false`.|

{{< /details >}}


{{< details title="Processing recurring payments" >}}

[Recurring Payments](/payments/features/tokenization/) is a feature that lets you store a customer’s payment details as a secure, encrypted token.

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

Recurring Payments are supported for all credit card payments.

**Note**: For test credit card details, see Test payment details – [Credit and debit cards](/testing/test-payment-details/#credit-and-debit-cards).

To use recurring payments in your payment component, you need to enable recurring payments for your account. If you haven't already, email <sales@multisafepay.com>

{{< /details >}}

**Note:** We use the `orderData` object to ensure the payment methods are enabled, e.g. for the currency, country, and transaction value. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: orderData
});
```

### Initialize the component

Initialize the component using:

{{< details title="Payment component button" >}}
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

{{< /details >}}

{{< details title="Own or existing button" >}}

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
{{< /details >}}

In the method call, create event handlers for the following events: 
{{< details title="Events" >}}

| Event | Event handler |
| ---- | ---- |
|`onLoad`| Occurs when the payment component UI is rendered. |
|`onError`| Occurs when an error occurs in the payment component. |
|`onSelect`| Occurs when the customer selects an issuer with iDEAL. |
|`onSubmit`| Occurs when the customer clicks the payment button (when using the button generated by the component). |
|`onValidation`| Occurs when form validation changes. Can be used to disable the payment button until all fields are validated. |

{{< /details >}}

The `PaymentComponent` has the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error messages or codes|
|`hasErrors`| Returns a boolean value about whether errors were registered |
|`getPaymentData`| Returns a `payment_data` object with a `payload` containing the customer's payment details, used to [create orders](/payment-components/single/step-3/), and the `gateway`.|
|`getOrderData`| Returns an object containing a `payment_data` object and the full order configuration. |

{{< /details >}}

{{< two-buttons

href-1="/payment-components/multiple/" header-1="Back" text-1="Step 1: Add the elements" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/multiple/step-3" header-2="Next" text-2="Step 3: Create an order" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
