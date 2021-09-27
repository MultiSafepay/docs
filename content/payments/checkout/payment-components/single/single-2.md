---
title : "Step 2: Initialize"
breadcrumb_title : "Step 2"
meta_title: "Payment Components - Integrating a single payment method step 2 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
--- 
## Generate an API token
Payment Components require a MultiSafepay API token. See API reference&nbsp;–&nbsp;[Generate an API token](/api/#generate-an-api-token).

**Note:** To keep your API key private, request the token from your own server. 

## Construct the component object

**1.** Initialize an `orderData` object, containing information about the customer's order collected during the checkout process:

```
const orderData = {
    currency: 'EUR',
    amount: 10000,
    customer: {
        locale: 'EN',
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
| currency| Currency of the order. Format: [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217), e.g. `EUR`. **Required**. |
| amount| Value of the order. Format: Number without decimal points, e.g. 100 euro is formatted as `10000`. **Required**. |
| customer.country| Customer's country code. Used to check the availability of the payment method. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. **Required**. |
|customer.locale | Customer's language. Used to set the language of the Payment Component UI. Format: [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), e.g. `NL`. Supported languages: `EN`, `ES`, `FR`, `IT`, `NL`. **Optional**.|
| template.settings.embed_mode| A template designed to blend in seamlessly with your ecommerce platform. Format:&nbsp;Boolean. **Optional**. |
|payment_options.settings.connect.group_cards||


{{< /details >}}

**Note:** We use the `orderData` object to ensure the payment method is enabled and the currency, country, and transaction amount are supported. 

**2.** Construct a `PaymentComponent` object in the `test` environment using the `orderData` object and your API token:

```
PaymentComponent = new MultiSafepay({
    env: 'test',
    apiToken: apiToken,
    order: orderData
});
```

## Initialize the payment component

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
**2.** Replace the `<GATEWAY>` placeholder with the relevant payment gateway code.
{{< details title="View gateway codes" >}}

| Payment method| Gateway code|
|---|---|
| Bank Transfer | `BANKTRANS` |
| Credit cards |`CREDITCARD`|
| iDEAL|`IDEAL`|
| PayPal | `PAYPAL` |
| SEPA Direct Debit | `DIRDEB` |
| Sofort | `DIRECTBANK`|

{{< /details >}}

**3.** Create event handlers for the following events:

{{< details title="View events" >}}

| Event | Event handler |
| ---- | ---- |
|`onError`| Called when an error occurs in the payment component|
|`onLoad`| Called when the Payment Component UI is rendered |

{{< /details >}}

**Note:** The `PaymentComponent` uses the following methods:

{{< details title="View methods" >}}

| Method | Description |
| ---- | ---- |
|`getErrors`| Returns error details, like error messages or codes.|
|`hasErrors`| Returns a boolean value depending on whether errors have been registered. |
|`getPaymentData`| Creates a `payload` object with the customer's payment details, used to create orders|

{{< /details >}}

{{< two-buttons

href-1="/payments/checkout/payment-components/single/single-1" header-1="Back" text-1="Step 1: Install" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/single/single-3" header-2="Next" text-2="Step 3: Redirect to pay" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}


