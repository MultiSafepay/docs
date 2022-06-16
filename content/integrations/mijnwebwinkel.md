---
title : "Mijnwebwinkel"
category: 62962dd7e272a6002ebbbbc5
order: 204
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
excerpt: "Free app to integrate MultiSafepay payment solutions with Mijnwebwinkel."
slug: 'mijnwebwinkel'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Mijnwebwinkel.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

This technical manual is for installing and configuring Mijnwebwinkel's free app for MultiSafepay. 

<details id="requirements">
<summary>Requirements</summary>
<br>

You will need a [MultiSafepay account](/getting-started-guide/).

</details>

<details id="support">
<summary>Support</summary>
<br>

See Mijnwebwinkel:

- General information about the plugin - [MultiSafepay](https://www.mijnwebwinkel.nl/partner/multisafepay).
- Technical queries about the plugin - [Contact form](https://www.mijnwebwinkel.nl/contactformulier).
- Support documentation - [Support](https://www.mijnwebwinkel.nl/support).

Contact MultiSafepay:

- Telephone: -31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

# Installation and configuration

:warning: We recommend first installing the plugin in a test environment, following the Mijnwebwinkel installation procedure. Always make a backup.

1. Sign in to your Mijwebwinkel backend.
2. Go to **Online orders** > **Payment method** > **MultiSafepay**.
2. Add your MultiSafepay account ID, [site ID, site security code, and API key](/websites/#site-id-api-key-and-secure-code).
6. Select the relevant payment methods.

# User guide

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [Mastercard](/mastercard) and [Visa](/visa)
- Pay later methods: [Klarna](/klarna)
- Wallets: [PayPal](/paypal)
- Banking methods: 
    - [Bancontact](/bancontact)
    - [Bank Transfer](/bank-transfer)
    - [Giropay](/giropay)
    - [iDEAL](/ideal)
    - [Maestro](/maestro)
    - [SEPA Direct Debit](/sepa-direct-debit)
    - [Sofort](/sofort)
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

<details id="changing-payment-method-order-in-checkout">
<summary>Changing payment method order in checkout</summary>
<br>

To change the order of payment methods in your checkout, follow these steps:

1. Go to Mijnwebwinkel - [Sorting](https://www.mijnwebwinkel.nl/beheer/payment/sorting).
2. Select **Sort manually, defined below**.
3. Drag and drop the active payment methods to change the order.

</details>

## Surcharges

[Surcharges](/surcharges/) are supported.

**Attention Dutch merchants**

We strongly recommend **not** applying surcharges to [pay later methods](/pay-later/). This is now considered providing credit under the Consumer Credit Act (Wet op het consumentenkrediet) and requires a permit from the Authority for Financial Markets (AFM).

