---
title: "Zen Cart"
category: 62962dd7e272a6002ebbbbc5
order: 120
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for installing and configuring MultiSafepay's free plugin for Zen Cart."
slug: 'zen-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Zen_Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Zencart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- ZenCart 1.5.5
- Tested on PHP 7.0

# How to install and configure

> **Tip!** We recommend first installing the plugin in a test environment, following the Zen Cart installation procedure. Always make a backup.

1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart <<glossary:backend>>.
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/docs/sites#site-id-api-key-and-security-code).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.
<br>

---

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/cards/)
- Banking methods: All, except iDEAL QR and TrustPay
- Pay later methods: All, except in3
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/docs/paysafecard/)
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

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
<summary>How to update via SFTP</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)