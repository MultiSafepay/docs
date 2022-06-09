---
title : "OsCommerce plugin"
category: 62962dd7e272a6002ebbbbc5
order: 114
hidden: false
parentDoc: 62a1d773f96fe80056354d84
excerpt: "Free plugin to integrate MultiSafepay payment solutions with OsCommerce."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/OsCommerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<details id="changelog">
<summary>Changelog</summary>
<br>

**3.0.0**
Release date: May 9, 2017

**Changes**
- This plugin now uses the JSON API, rather than the XML API.
- Added all available payment methods as separate gateways
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
- Added javascript that will auto select iDEAL as payment method when an issuer is selected

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

---
</details>

> [View source code](https://github.com/MultiSafepay/OsCommerce) :link:

> [Download](https://github.com/MultiSafepay/OsCommerce/archive/3.0.0.zip) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with OsCommerce.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- OsCommerce 2.3
- Tested on PHP 7.0

**Note:** Version 3.0.0 is tested on PHP 5.6. Previous versions are no longer tested for compatibility. For more information, email <sales@multisafepay.com>

</details>

<details id="support">
<summary>Support</summary>
<br>

For support, contact OsCommerce.

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

# Installation and configuration

:warning: We recommend first installing the plugin in a test environment, following the OsCommerce installation procedure. Always make a backup.

1. Unpack the content of the .ZIP file in the root of your webshop.
2. Sign in to your OsCommerce backend.
3. Go to **Modules** > **Payment**.
4. Click **Install modules** in the top-right corner.
5. Enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code), and then complete the other fields as required.

# User guide

## Payment methods

<details id="payment-methods" >
<summary>Payment methods</summary>
<br>

- Cards: [All](/payment-methods/credit-debit-cards/)
- Pay later methods: [E-Invoicing](/payment-methods/e-invoicing), [Klarna](/payment-methods/klarna), [Pay After Delivery](/payment-methods/pay-after-delivery)
- Wallets: [PayPal](/payment-methods/paypal)
- Banking methods:
    - [Bancontact](/payment-methods/bancontact)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [CBC/KBC](/payment-methods/cbc-kbc)
    - [Dotpay](/payment-methods/dotpay)
    - [EPS](/payment-methods/eps)
    - [Giropay](/payment-methods/giropay)
    - [iDEAL](/payment-methods/ideal)
    - [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
    - [Sofort](/payment-methods/sofort)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payments/methods/prepaid-cards/paysafecard)
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
You can't refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="updating-via-sftp">
<summary>Updating via SFTP</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>