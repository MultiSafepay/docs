---
title : "Zen Cart"
category: 62962dd7e272a6002ebbbbc5
order: 120
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with Zen Cart."
slug: 'zen-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Zen_Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [Changelog](https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md) :link:

> [Source code](https://github.com/MultiSafepay/Zencart) :link:

> [Download](https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Zen Cart.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- ZenCart 1.5.5
- Tested on PHP 7.0

</details>

# How to install and configure

:warning: We recommend first installing the plugin in a test environment, following the Zen Cart installation procedure. Always make a backup.

1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart backend.
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/websites/#site-id-api-key-and-secure-code).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.

# User guide

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/), except iDEAL QR and TrustPay
- Pay later methods: [All](/payment-methods/pay-later/), except in3
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payment-methods/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

## Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="updating-via-sftp">
<summary>Updating via SFTP</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>

---

> 💬  Support
> Contact MultiSafepay:
> 
> - Telephone: +31 (0)20 8500 500
> - Email: <integration@multisafepay.com>
> - GitHub: Create a technical issue