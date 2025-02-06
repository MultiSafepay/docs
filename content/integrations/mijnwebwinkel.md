---
title: "Mijnwebwinkel"
category: 62962dd7e272a6002ebbbbc5
order: 2
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
excerpt: "Technical manual for Mijnwebwinkel's free app."
slug: 'mijnwebwinkel'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Mijnwebwinkel.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation and configuration

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the Mijnwebwinkel installation procedure. Always make a backup.

1. Sign in to your Mijnwebwinkel <<glossary:backend>>.
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

- Cards: [Mastercard](/docs/card-payments/) and [Visa](/docs/card-payments/)
- <<glossary:BNPL>>: [Klarna](/docs/klarna/)
- Wallets: [PayPal](/docs/paypal/)
- Banking methods: 
    - [Bancontact](/docs/bancontact/)
    - [Bank transfer](/docs/bank-transfer/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [Maestro](/docs/card-payments/)
    - [Direct debit](/docs/direct-debit/)
    - [Sofort](/docs/sofort/)
- Prepaid cards:
    - <a href="https://www.babycadeaubon.nl" target="_blank">Baby Cadeaubon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Beauty & Wellness
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashion Cheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.good4fun.nl" target="_blank">Good4fun</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Wijncadeau
    - <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.yourgift.nl" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

<details id="how-to-change-payment-method-order-in-checkout">
<summary>How to change payment method order in checkout</summary>
<br>

To change the order of payment methods in your checkout, follow these steps:

1. Go to Mijnwebwinkel - <a href="https://www.mijnwebwinkel.nl/beheer/payment/sorting" target="_blank">Sorting</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Select **Sort manually, defined below**.
3. Drag and drop the active payment methods to change the order.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are supported.

> ⚠️ Attention Dutch merchants
>
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n   <ul>\n    <li>For technical queries about the app, contact <a href=\"https://www.mijnwebwinkel.nl/contact \">Mijnwebwinkel</a></li>\n    <li>For general information about the app, see Mijnwebwinkel  <a href=\"https://www.mijnwebwinkel.nl/support-resources \">Support</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)