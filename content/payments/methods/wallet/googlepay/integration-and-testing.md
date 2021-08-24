---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Apple Pay - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing Apple Pay in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/wallet/applepay/apple-pay-compatibility-and-testing
    - /payment-methods/wallet/applepay/apple-pay-guidelines
---
## Integration

{{< two-buttons href-2="/payments/methods/wallet/applepay/direct-integration" text-2="Apple Pay direct" description-2="Integrate Apple Pay directly in your checkout page" img-2="/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/api/#apple-pay" text-2="Apple Pay redirect" description-2="Integrate Apple Pay using MultiSafepay payment pages" img-2="/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< br >}}

When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing).

For the Apple Pay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

## Testing

{{< details title="Supported devices" >}}

For supported devices, see Apple – [Apple is compatible with these devices](https://support.apple.com/en-us/HT208531).

If you don't own an Apple device, we recommend using the [Appetize.io](https://appetize.io) emulator. When you try to complete a test payment on the MultiSafepay payment page, you get a "This device is not supported" error. But the emulator creates a pretransaction with Apple Pay as a gateway to check if there is an existing connection to our server. However, you can't fully complete the test transaction.

{{< /details >}}

{{< details title="Requirements" >}}

- Use a [compatible device](https://support.apple.com/en-us/HT208531).
- Use Safari browser.
- The website uses HTTPS.
- Maestro must be activated in your MultiSafepay account.

If any of these requirements is not met, Apple Pay doesn't appear on the checkout page.

{{< /details >}}

To test Apple Pay transactions, follow these steps:

1. Click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
2. Complete a payment using [test card data](/getting-started/test-your-integration/test-payment-details/#credit-and-debit-cards).
3. The transaction is completed.

### Test environment

We recommend using an Apple Pay – [Sandbox account](https://developer.apple.com/apple-pay/sandbox-testing).

