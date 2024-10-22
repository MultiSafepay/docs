---
title: "Craft Commerce"
category: 62962dd7e272a6002ebbbbc5
order: 2
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'craft-commerce'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Craft_Commerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/craft-commerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Features
 
- Support for separate payment methods, <<glossary:BNPL>>, and gift cards
- Partial and full refunds for all payment methods, except BNPL
- Customizable <<glossary:order statuses>>
- Shipment notifications for BNPL orders 

# Prerequisites

- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

# Installation

These instructions are for installing the plugin via Composer. You can also install via the <a href="https://plugins.craftcms.com/multisafepay" target="_blank">Craft Plugin Store</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

# Configuration
1. Sign in to your Craft Commerce <<glossary:backend>>.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and configure <<glossary:gateways>>, go to **Commerce** > **System settings** > **Gateways**.  
<br>

---

# User guide

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 1.2.0, March 19th 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Craft Commerce backend. 
2. Go to **Commerce** > **System settings** > **Gateways** > **+ New gateway**.
3. From the **Gateway** list, select **Generic gateway**.
4. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway label.

</details>

## Payment methods

Before activating the relevant payment methods in your backend you must first activate them in you MultiSafepay dashboard. See - [How to activate payment methods](/docs/payment-methods#activation).

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/), **except** Postepay and V Pay
- Banking methods: All
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Wijncadeau
    - <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

## Refunds

<details id="refund-rules">
<summary>Refund rules</summary>
<br>

| Platform | Details |
|---|---|
| MultiSafepay dashboard | - [Full and partial refunds](/docs/refund-payments/) <br> - Generic gateway transactions |
| Backend | - Full and partial refunds <br> - You can't refund more than the original amount in your backend <br> - Generic gateway transactions **not** supported |
| API | - [Refund order](/reference/refundorder/) <br> - [BNPL refunds](/docs/refund-payments#bnpl-refunds) **not** supported <br> - Discounts **not** supported |

</details>

<details id="how-to-process-backend-refunds">
<summary>How to process backend refunds</summary>
<br>

To process refunds from the Craft Commerce admin panel:  

1. Go to **Commerce** > **Orders**.
2. Select the order.
3. To see the refund options, go to the **Transactions** tab. 

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/craft-commerce/issues/new\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)