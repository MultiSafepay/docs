---
title : "Integrating the previous release"
breadcrumb_title : "Step 2"
meta_title: "Payment Components - Integrating the previous release step 2 - MultiSafepay Docs"

layout: "single"
read_more: "."
url: "/payment-components/previous-release/step-2/"
--- 

## Step 2: Initialize the component

### Generate an API token
Payment Components require a MultiSafepay API token. See API reference&nbsp;–&nbsp;[Generate an API token](https://docs-api.multisafepay.com/reference/generateapitoken).

{{< alert-notice >}} **Note:** To keep your API key private, request the token from your own server. {{< /alert-notice >}} 

### Construct the component object

**1.** Initialize an `orderData` object, containing information about the customer's order collected during the checkout process:

```
const orderData = {
    currency: "EUR",
    amount: 10000,
    customer: {
        locale: "en",
        country: "NL",
        reference: "Customer123"
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
| customer.country| The customer's country code. Checks the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Required**. |
|customer.locale | The customer's language. Sets the language of the payment component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
| template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |

{{< /details >}}

**Note:** We use the `orderData` object to ensure the payment method is enabled and the currency, country, and transaction amount are supported. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: "test",
    apiToken: apiToken,
    order: orderData
});
```

### Initialize the component

**1.** Call the `PaymentComponent.init()` method with the following arguments:

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
**2.** Replace the `<GATEWAY>` placeholder with the relevant payment gateway identifier.
{{< details title="View gateway IDs" >}}

|Payment method|Gateway IDs|
|---|---|
|Credit card|`CREDITCARD`|
|iDEAL|`IDEAL`|

{{< /details >}}

**3.** Create event handlers for the following events:

{{< details title="View events" >}}

| Event | Event handler |
| ---- | ---- |
|`onError`| Called when an error occurs in the payment component|
|`onLoad`| Called when the payment component UI is rendered |

{{< /details >}}

**Note:** The `PaymentComponent` uses the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error details, e.g. error messages or codes.|
|`hasErrors`| Returns a boolean value depending on whether errors have been registered. |
|`getPaymentData`| Creates a `payload` object with the customer's payment details, used to create orders|

{{< /details >}}

{{< two-buttons

href-1="/payment-components/previous-release" header-1="Back" text-1="Step 1: Add the elements" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/previous-release/step-3" header-2="Next" text-2="Step 3: Create an order" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

