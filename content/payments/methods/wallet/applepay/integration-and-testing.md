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

{{< two-buttons href-2="/payments/methods/wallet/applepay/redirect-integration" text-2="Apple Pay redirect" description-2="Integrate Apple Pay using MultiSafepay payment pages" img-2="/logo/Payment_methods/Apple.svg" alt-2="Right arrow" >}}

{{< br >}}

| | |
|---|---|
| **Ready-made integrations** | Apple Pay (redirect) is supported in all our [ready-made integrations](/integrations/ready-made/) **except** VirtueMart, OsCommerce, X-Cart, and Zen Cart. {{< br >}} For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. {{< br >}} For our [OpenCart plugin](/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |
| **Apple branding** | When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing). |

## Testing

See [Test payment details](/testing/test-payment-details/).