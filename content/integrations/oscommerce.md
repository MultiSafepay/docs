---
title: "OsCommerce"
category: 62962dd7e272a6002ebbbbc5
order: 10
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'oscommerce'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/OsCommerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/OsCommerce/archive/3.0.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/OsCommerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

</div>

# Changelog

<details id="changelog">
<summary>Changelog</summary>
<br>

**3.0.0**
Release date: May 9, 2017

**Changes**
- This plugin now uses the JSON API, rather than the XML API.
- Added all available payment methods as separate <<glossary:gateways>>
- Added all available gift card methods

---

**2.0.3**
Release date: Oct 12, 2016

**Improvements**
- Added Klarna as a payment method.

**Changes**
- Changed MisterCash to Bancontact and replaced the payment method logo.

---

**2.0.2**
Release date: Jun 18, 2015

**Improvements**
- Add check for completed transactions so that the confirmation is only sent once for paid transactions
- Added iDEAL selection to the payment selection page instead before the order confirmation
- Added javascript that will auto select iDEAL as payment method when an <<glossary:issuer>> is selected

**Fixes**
- On extra offline action the status of the order was reset to initialized. This has now been solved
- Zone restriction is now working correct again
- Added extra check for Fee tax. This solves 1027 errors and invalid tax rate for shipping

---

**2.0.1**
Release date: Mar 28, 2014

**Improvements**
- Now compatible with OsCommerce 2.2
- Added NL images
- Added order total language files, untranslated
- Added Multi-Currency support
- Added OSC input validation
- Added American Express Support to the OsCommerce plugin
- Added SOFORT Banking support

**Changes**
- Changed language files. Added option to show only the gateway title, and no images. On request
- Changed default order status to selected initial status
- Updated curl combined files
- Updated Pay After Delivery default order status to the init status
- Disabled updating customer info as this is saved before the transaction

**Fixes**
- Fixed bug with weight-based shipping
- Fixed amount bug
- Fixed bug that caused a Pay After Delivery order not to show before a finished transaction
- Fixed bug for cancel URL, use hardcoded method like nurl script
- Fixed bug with single quotes

[Top of page](#)

---

</details>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- OsCommerce 2.3
- Tested on PHP 7.0

**⚠️ Note:** Version 3.0.0 is tested on PHP 5.6. Previous versions are no longer tested for compatibility. For more information, email <sales@multisafepay.com>

# Installation and configuration

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the OsCommerce installation procedure. Always make a backup.

1. Unpack the content of the .ZIP file in the root of your webshop.
2. Sign in to your OsCommerce <<glossary:backend>>.
3. Go to **Modules** > **Payment**.
4. Click **Install modules** in the top-right corner.
5. Enter your website [API key](/docs/sites#site-id-api-key-and-security-code), and then complete the other fields as required.

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- <<glossary:BNPL>>: [E-Invoicing](/docs/e-invoicing/), [Klarna](/docs/klarna/), [Pay After Delivery](/docs/pay-after-delivery/)
- Wallets: [PayPal](/docs/paypal/)
- Banking methods:
    - [Bancontact](/docs/bancontact/)
    - [Bank transfer](/docs/bank-transfer/)
    - [CBC/KBC](/docs/cbc-kbc/)
    - [Dotpay](/docs/dotpay/)
    - [EPS](/docs/eps/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [Direct debit](/docs/direct-debit/)
    - [Sofort](/docs/sofort/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - [Paysafecard](/docs/paysafecard/)
    - <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Wijncadeau
    - <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.yourgift.nl/" target="_blank">YourGift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
<summary>How to update via SFTP</summary>
<br>

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/OsCommerce/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)