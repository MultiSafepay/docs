---
title : "Drupal"
category: 62962dd7e272a6002ebbbbc5
order: 110
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugins to integrate MultiSafepay payment solutions with Drupal 7, 8 & 9."
slug: 'drupal'
---
# Drupal 8 & 9

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Drupal_8.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [Changelog](https://github.com/MultiSafepay/drupal-commerce-2/blob/master/CHANGELOG.md) :link:

> [View source code](https://github.com/MultiSafepay/drupal-commerce-2/) :link:

> [Download](https://github.com/MultiSafepay/drupal-commerce-2/releases/download/3.0.0/commerce_multisafepay_payments-3.0.0.zip) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's free plugin for Drupal 8 & 9. 

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

</details>

<details id="support">
<summary>Support</summary>
<br>

Drupal no longer provides support for Drupal 8.9.x.

For how to upgrade to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

## Installation

These instructions are for Composer. You can also install the plugin in your backend. 

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

To install the latest stable version of the Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

## Configuration  
1. Sign in to your Drupal backend.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your [account ID, site ID, and site API key](/websites/#site-id-api-key-and-secure-code). 
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your [MultiSafepay dashboard](https://merchant.multisafepay.com).

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

1. Sign in to your Drupal backend. 
2. Go to **Commerce** > **Configuration** > **Payments** > **Payments gateways** > **Add payment gateway** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.

</details>

### Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Banking methods: [All](/banks/)
- Pay later methods: [All](/pay-later/), **except** in3
- Wallets: [Alipay](/alipay), [Apple Pay](/apple-pay), [PayPal](/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl)

</details>

### Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="updating-in-your-backend">
<summary>Updating in your backend</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation instructions and the Configuration instructions from step 2.

</details>

### Upgrading to Drupal 9

Drupal no longer provides support for Drupal 8.9.x. 

For how to upgrade Drupal 8 to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).

---

# Drupal 7

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Drupal_7.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [Changelog](https://github.com/MultiSafepay/Drupal-Commerce/blob/master/CHANGELOG.md) :link:

> [View source code](https://github.com/MultiSafepay/Drupal-Commerce) :link:

> [Download](https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's free plugin for Drupal 7.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Drupal 7.x
- Tested on PHP 7.0

</details>

<details id="support">
<summary>Support</summary>
<br>

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

## Installation and configuration

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Unpack the content of the .ZIP file in the root of your Drupal 7 webshop.
2. Sign in to your Drupal 7 backend.
3. Go to **Site settings** > **Modules**. 
4. Enable the Commerce MultiSafepay JSON module, and your selected payment method modules. 
5. Click **Save configuration**.
6. Go to **Store settings** > **Advanced store settings** > **Payment methods**.
7. **Enable** the `multisafepay` core module.
8. **Enable** the modules for each payment method.
9. To configure each payment method, under **Actions**, click the **Edit** button.
10. When the main module is installed, two rules are created but disabled by default:  
    - MultiSafepay order paid in full: Order state to `processing`  
This rule sets the order to `processing` when the order is paid in full.  
    - MultiSafepay order complete: Shipped at MultiSafepay  
This rule updates the [transaction status](/payment-statuses/) to **Shipped** at MultiSafepay. For Pay After Delivery, Klarna, and E-Invoicing, this triggers the invoicing process.

## User guide

### Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Banking methods: [All](/banks/), **except** iDEAL QR and Trustly
- Pay later methods: [E-Invoicing](/e-invoicing), [Klarna](/klarna), [Pay After Delivery](/pay-after-delivery)
- Wallets: [Alipay](/alipay), [Apple Pay](/applepay), [PayPal](/paypal)
- Prepaid cards: 
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/paysafecard)
    - Wijn cadeau
    - [Yourgift](https://www.yourgift.nl)

</details>

### Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backed.  
Refunding more than the original amount is **not** supported in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="updating-via-sftp">
<summary>Updating via SFTP</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>