---
title: "Integrating and testing Apple Pay"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Apple Pay - MultiSafepay Docs"
short_description: "Options for integrating Apple Pay and testing payments"
layout: 'child'
url: '/payment-methods/apple-pay/integration-testing/'
aliases:
    - /payment-methods/wallet/applepay/apple-pay-compatibility-and-testing
    - /payment-methods/wallet/applepay/apple-pay-guidelines
    - /payments/methods/wallet/applepay/integration-and-testing/
---
## Integration

{{< two-buttons href-2="/payments/methods/wallet/applepay/direct-integration" text-2="Apple Pay direct" description-2="Embed Apple Pay in your checkout page for the best user experience" img-2="/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/api/#apple-pay" text-2="Apple Pay redirect" description-2="Integrate Apple Pay using MultiSafepay payment pages" img-2="/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< br >}}

| | |
|---|---|
| **Ready-made integrations** | Apple Pay (redirect) is supported in all our [ready-made integrations](/integrations/ready-made/) **except** VirtueMart, OsCommerce, X-Cart, and Zen Cart. {{< br >}} For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. {{< br >}} For our [OpenCart plugin](/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |
| **Apple branding** | When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing). |

## Testing

### Supported devices

For supported devices, see Apple – [Apple is compatible with these devices](https://support.apple.com/en-us/HT208531).

If you don't own an Apple device, we recommend using the [Appetize.io](https://appetize.io) emulator. When you try to complete a test payment on the MultiSafepay payment page, you get a _This device is not supported_ error. But the emulator creates an order with the Apple Pay gateway preselected to check if there is an existing connection to our server. However, you can't fully complete the test transaction.

### Requirements

- Use a [compatible device](https://support.apple.com/en-us/HT208531).
- Use Safari browser.
- The website uses HTTPS.
- Maestro must be activated for your MultiSafepay account.

If any of these requirements is not met, Apple Pay doesn't appear on the checkout page.

### Test environment

We recommend using an Apple Pay – [Sandbox account](https://developer.apple.com/apple-pay/sandbox-testing).

### Testing 

To test Apple Pay transactions, follow these steps:

1. Click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
2. Complete a payment using [test card data](/testing/test-payment-details/#credit-and-debit-cards).
3. The transaction is completed.



