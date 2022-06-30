---
title: "Mijnwebwinkel"
category: 62962dd7e272a6002ebbbbc5
order: 204
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
excerpt: "Technical manual for installing and configuring Mijnwebwinkel's free app for MultiSafepay."
slug: 'mijnwebwinkel'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Mijnwebwinkel.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# How to install and configure

> **Tip!** We recommend first installing the plugin in a test environment, following the Mijnwebwinkel installation procedure. Always make a backup.

1. Sign in to your Mijwebwinkel <<glossary:backend>>.
2. Go to **Online orders** > **Payment method** > **MultiSafepay**.
2. Add your MultiSafepay account ID, [site ID, site security code, and API key](/docs/sites#site-id-api-key-and-security-code).
6. Select the relevant payment methods.
<br>

---

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [Mastercard](/docs/cards/) and [Visa](/docs/cards/)
- <<glossary:BNPL>>: [Klarna](/docs/klarna/)
- Wallets: [PayPal](/docs/paypal/)
- Banking methods: 
    - [Bancontact](/docs/bancontact/)
    - [Bank Transfer](/docs/bank-transfer/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [Maestro](/docs/cards/)
    - [SEPA Direct Debit](/docs/sepa-direct-debit/)
    - [Sofort](/docs/sofort/)
- Prepaid cards:
    - [Baby Cadeaubon](https://www.babycadeaubon.nl)
    - Beauty & Wellness
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashion Cheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Good4fun](https://www.good4fun.nl)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl)

</details>

<details id="how-to-change-payment-method-order-in-checkout">
<summary>How to change payment method order in checkout</summary>
<br>

To change the order of payment methods in your checkout, follow these steps:

1. Go to Mijnwebwinkel - [Sorting](https://www.mijnwebwinkel.nl/beheer/payment/sorting).
2. Select **Sort manually, defined below**.
3. Drag and drop the active payment methods to change the order.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are supported.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>For:</p>\n  <ul>\n    <li>General information about the app, see Mijnwebwinkel – <a href=\"https://www.mijnwebwinkel.nl/partner/multisafepay\">MultiSafepay</a>.</li>\n    <li>Technical queries about the app, see Mijnwebwinkel – <a href=\"https://www.mijnwebwinkel.nl/contactformulier\">Contact form</a>.</li>\n    <li>Support documentation, see Mijnwebwinkel – <a href=\"https://www.mijnwebwinkel.nl/support\">Support</a>.</li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)