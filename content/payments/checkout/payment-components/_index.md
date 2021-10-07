---
title: 'Payment Components'
breadcrumb_title: "Payment Components"
layout: 'single'
meta_title: 'Payment Components - MultiSafepay Docs'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: '/svgs/Payment pages.svg'
short_description: 'Embedded solution: Embed payment methods directly in your checkout.'
hideMenu : 'true'
logo: '/svgs/API.svg'
weight: 51
url: '/payment-components/'
aliases:
    - /tools/credit-card-component/
---
Payment Components let you embed payment methods directly into your checkout.

- Creates a seamless checkout experience to increase [conversion](/getting-started/glossary/#conversion-rate)
- Encrypts customer payment details for secure processing
<<<<<<< HEAD
- Reduces your [PCI DSS](/payment-regulations/pci-dss/) responsibility, falling only under [Self-Assessment Questionaire A](https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf)
- Supports [tokenization](/payments/features/tokenization/)

{{< screen src="/gifs/credit-card-component.gif" alt="Credit Card Component" align="center" class="medium-img" screen_size="desktop" >}}

## Payment methods

Embed a single or multiple payment methods in your checkout.
=======
- Shifts responsibility for [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay

## Integration
>>>>>>> origin/master

Embed a selected payment method in your checkout. The customer completes payment within your checkout or is redirected to the relevant payment page.

<<<<<<< HEAD
- [Bancontact](/payments/methods/banks/bancontact/)
- [Bank Transfer](/payments/methods/banks/bank-transfer/)
- Credit cards:  
    - [American Express](/payments/methods/credit-and-debit-cards/american-express/)
    - [Mastercard](/payments/methods/credit-and-debit-cards/mastercard/)
    - [Visa](/payments/methods/credit-and-debit-cards/visa/)
- [iDEAL](/payments/methods/banks/ideal/)
- [PayPal](/payments/methods/wallet/paypal/)
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit/)
- [Sofort](/payments/methods/banks/sofort/)

{{< /details >}}

## Credit card features

- Bundles all supported credit cards in one gateway
- Displays the logos of available card brands in the card number field, and then detects the specific brand as the customer enters their card number and displays the relevant logo
- Validates the card number
- Displays error messages for credit card fields, e.g. card not supported, card expired
- Supports tokenization for fast, secure repeat payments

## Manuals 
{{< two-buttons href-2="/payment-components/integration" header-2="Manual" text-2="Integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/payment-components/customization" header-2="Manual" text-2="Customization" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
=======
{{< screen src="/gifs/credit-card-component.gif" alt="Credit Card Component" align="center" class="medium-img" screen_size="desktop" >}}

## Customization

You can customize the look of the component to match your brand's visual identity, and set the display language.

For instructions, see [Customizing payment components](/payments/checkout/payment-components/customizing-payment-components/).

{{< two-buttons href-2="/payments/checkout/payment-components/integrating-single-payment-method" header-2="Integration manual" text-2="Single payment method" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
>>>>>>> origin/master
