---
title: 'Payment components'
breadcrumb_title: "Payment components"
layout: 'single'
meta_title: 'Payment components - MultiSafepay Docs'
logo: '/svgs/Payment pages.svg'
short_description: 'Embed payment methods directly in your checkout.'
hideMenu : 'true'
logo: '/svgs/API.svg'
weight: 30
url: '/payment-components/'
aliases:
    - /tools/credit-card-component/
    - /payments/checkout/payment-components/
    - /integrations/payment-components/
---
Payment components let you embed payment methods directly into your checkout.

- Creates a seamless checkout experience to increase [conversion](/glossaries/multisafepay-glossary/#conversion-rate)
- Encrypts customer payment details for secure processing
- Reduces your [PCI DSS](/payment-regulations/pci-dss/) responsibility, falling only under [Self-Assessment Questionaire A](https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf)
- Supports [recurring payments](/payments/features/tokenization/)

## Payment methods

Embed a single or multiple payment methods in your checkout.

{{< details title="Supported payment methods">}}

- [Bancontact](/payment-methods/bancontact/)
- [Bank Transfer](/payment-methods/bank-transfer/)
- Credit cards:  
    - [American Express](/payment-methods/amex/)
    - [Mastercard](/payment-methods/mastercard/)
    - [Visa](/payment-methods/visa/)
    - [Maestro](/payment-methods/maestro/)
- [iDEAL](/payment-methods/ideal/)
- [PayPal](/payment-methods/paypal/)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit/)
- [Sofort](/payment-methods/sofort/)

{{< /details >}}

## Credit card features

- Bundles all supported credit cards in one gateway
- Displays the logos of available card brands in the card number field, and then detects the specific brand as the customer enters their card number and displays the relevant logo
- Validates the card number
- Displays error messages for credit card fields, e.g. card not supported, card expired
- Supports tokenization for fast, secure recurring payments

## Manuals 
{{< two-buttons href-2="/payment-components/integration" header-2="Manual" text-2="Integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/payment-components/customization" header-2="Manual" text-2="Customization" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
