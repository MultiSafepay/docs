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

- Creates a seamless checkout experience to increase [conversion](/getting-started/glossary/#conversion-rate)
- Encrypts customer payment details for secure processing
- Shifts responsibility for [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay
- Supports [tokenization](/payments/features/tokenization/)

{{< screen src="/gifs/credit-card-component.gif" alt="Credit Card Component" align="center" class="medium-img" screen_size="desktop" >}}

## Payment methods

Embed a single or multiple payment methods automatically detected as available in the customer's country. 

The customer completes payment in your checkout or is redirected to a [payment page](/getting-started/glossary/#payment-page). 

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

## PCI DSS compliance

Reduce your responsibility for [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss). With the Payment Compononent, you only fall under [Self-Assessment Questionaire A](https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf).

## Credit card features

- Bundles all supported credit cards in one gateway
- Detects the credit card brand automatically and displays the logo in the card number field
- Validates the card number
- Displays error messages for credit card fields, e.g. card not supported, card expired, incorrect [CVC](/credit-and-debit-cards/glossary/#card-verification-code-cvc)
- Supports tokenization for fast, secure repeat payments

## Manuals 
{{< two-buttons href-2="/payments/checkout/payment-components/integration" header-2="Manual" text-2="Integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/payments/checkout/payment-components/customizing-payment-components" header-2="Manual" text-2="Customization" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
