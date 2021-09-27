---
title: 'Payment Components'
breadcrumb_title: "Payment Components"
layout: 'single'
meta_title: 'Payment Components - MultiSafepay Docs'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: 'Embedded solution: Embed payment methods directly in your ecommerce integration.'
hideMenu : 'true'
weight: 51
aliases:
    - /tools/credit-card-component/
---
Payment Components let you embed payment methods directly into your checkout. 

- Create a seamless checkout experience to increase [conversion](/getting-started/glossary/#conversion-rate).
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay
- Customize the component interface to match your brand's visual identity

{{< screen src="/gifs/credit-card-component.gif" alt="Credit Card Component" align="center" class="medium-img" screen_size="desktop" >}}

## Payment methods

Embed a single payment method or multiple methods, which are automatically sorted by availability in the customer's country. 

The customer completes payment within your checkout or is redirected to the [issuer's](/getting-started/glossary/#issuer) payment page. 

{{< details title="Supported payment methods" >}}

- [Bank Transfer](/payments/methods/banks/bank-transfer/)
- Credit cards:  
    - [American Express](/payments/methods/credit-and-debit-cards/american-express/)
    - [Bancontact](/payments/methods/banks/bancontact/)
    - [Mastercard](/payments/methods/credit-and-debit-cards/mastercard/)
    - [Visa](/payments/methods/credit-and-debit-cards/visa/)
- [iDEAL](/payments/methods/banks/ideal/)
- [PayPal](/payments/methods/wallet/paypal/)
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit/)
- [Sofort](/payments/methods/banks/sofort/)

{{< /details >}}

## Credit card features

Payment Components:

- Bundle all supported credit cards in one gateway
- Detect the credit card brand automatically and display the logo in the card number field
- Validate the card number
- Display error messages for credit card fields, e.g. card not supported, card expired, incorrect [CVC](/credit-and-debit-cards/glossary/#card-verification-code-cvc)
- Support iframe implementation for increased security 
- Support tokenization

## Manuals 
{{< two-buttons href-2="/payments/checkout/payment-components/integration" header-2="Manual" text-2="Integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/payments/checkout/payment-components/using-tokenization" header-2="Manual" text-2="Tokenization" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/payments/checkout/payment-components/customizing-payment-components" header-2="Manual" text-2="Customization" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
