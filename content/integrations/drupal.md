---
title: "Drupal"
category: 62962dd7e272a6002ebbbbc5
order: 3
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'drupal'
---
# Drupal 8, 9 & 10

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Drupal_10.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/drupal-commerce-2/releases/download/4.0.0/commerce_multisafepay_payments-4.0.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/drupal-commerce-2/" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/drupal-commerce-2/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Drupal 8.9 and above, Drupal 9.x and 10.x
- Drupal Commerce 2.x

## Installation

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

These instructions are for Composer. You can also install the plugin in your <<glossary:backend>>. 

To install the latest stable version of the Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

## Configuration  

1. Sign in to your Drupal backend.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your [account ID, site ID, and site API key](/docs/sites#site-id-api-key-and-security-code). 
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
<br>

---
## User guide

### Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 3.0.0, March 19th 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Drupal backend. 
2. Go to **Commerce** > **Configuration** > **Payments** > **Payments gateways** > **Add payment gateway** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway label.

</details>

### Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All
- <<glossary:BNPL>>: All, **except** in3
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
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
    - <a href="https://www.yourgift.nl" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

### Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation instructions and the Configuration instructions from step 2.

</details>

### Upgrades

**⚠️ Note:** Drupal no longer provides support for Drupal 8.9.x. 

For how to upgrade Drupal 8 to Drupal 9, see Drupal - <a href="https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher" target="_blank">Upgrading from Drupal 8 to Drupal 9 or higher</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
<br>

[Top of page](#)

---

# Drupal 7

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Drupal_7.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Drupal-Commerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Drupal-Commerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Drupal 7.x
- Tested on PHP 7.0

## Installation and configuration

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

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
    This rule updates the <<glossary:transaction status>> to **Shipped** at MultiSafepay. For Pay After Delivery, Klarna, and E-Invoicing, this triggers the invoicing process.

<br>

---
## User guide

### Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All, **except** iDEAL QR and Trustly
- <<glossary:BNPL>>: [E-Invoicing](/docs/e-invoicing/), [Klarna](/docs/klarna/), [Pay After Delivery](/docs/pay-after-delivery/)
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards: 
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - [Paysafecard](/docs/paysafecard/)
    - Wijn cadeau
    - <a href="https://www.yourgift.nl" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

### Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backed.  
Refunding more than the original amount is **not** supported in your backend.

### Updates

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
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/drupal-commerce-2/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)