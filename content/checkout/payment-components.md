---
title: 'Payment components'
category: 62bd999547298d001abc714c
order: 1
hidden: false
slug: 'payment-components'
---
Payment components let you embed payment methods directly into your checkout.

- Creates a seamless payment experience to increase <<glossary:conversion>>
- Encrypts customer payment details for secure processing
- Reduces your [PCI DSS](/docs/pci-dss/) responsibility, falling only under <a href="https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf" target="_blank">Self-Assessment Questionnaire A</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- Supports [recurring payments](/docs/recurring-payments/)

# How it works

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/payment-components.svg" alt="Payment component flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment methods

You can embed a single or multiple payment methods in your checkout.
These are the supported payment methods:

- Banking methods:
  - [Bancontact](/docs/bancontact/)
  - [Bank transfer](/docs/bank-transfer/)
  - [Direct debit](/docs/direct-debit/)
  - [iDEAL](/docs/ideal/)
  - [MyBank](/docs/mybank/)
- <<glossary:BNPL>>:
  - [E-invoicing](/docs/e-invoicing/)
  - [In3](/docs/in3/)
  - [Klarna](/docs/klarna/)
  - [Pay After Delivery](/docs/pay-after-delivery/)
  - [Pay After Delivery installments](/docs/pay-after-delivery-installments/)
  - [Riverty](/docs/riverty/)
  - [Zinia](/docs/zinia/)
- Cards:
  - [American Express](/docs/card-payments/)
  - [Maestro](/docs/card-payments/)
  - [Mastercard](/docs/card-payments/)
  - [Visa](/docs/card-payments/)
- Wallets: [PayPal](/docs/paypal/)

  
**⚠️ Note:** [Prepaid cards](/docs/prepaid-cards/) are not supported.

# Card payment features

- Bundles all supported card payments in one <<glossary:gateway>>
- Displays the logos of available card brands in the card number field, and then detects the specific brand as the customer enters their card number and displays the relevant logo
- Validates the card number
- Displays error messages for card fields, e.g. card not supported, card expired
- Supports tokenization for fast, secure recurring payments

# Integration 

- [Single payment method integration](/docs/payment-component-single/): Embed a single payment method into your site
- [Multiple payment method integration](/docs/payment-component-multiple/): Embed multiple payment methods into your site
- [Payment component customization manual](/docs/payment-component-customization/)
- [Previous release integration manual](/docs/payment-component-previous-release/)
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)