---
title: "Craft Commerce"
category: 62962dd7e272a6002ebbbbc5
order: 108
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions into your Craft Commerce webshop."
slug: 'craft-commerce'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Craft_Commerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/craft-commerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

This technical manual is for installing and configuring MultiSafepay's free plugin for Craft Commerce 3.

# Features
 
- Support for separate payment methods, pay later methods, and gift cards
- Partial and full refunds for all payment methods, except pay later
- Customizable order statuses
- Shipment notifications for pay later methods 

<details id="requirements">
<summary>Requirements</summary>
<br>

- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

</details>

# How to install

These instructions are for installing the plugin via Composer. You can also install via the [Craft Plugin Store](https://plugins.craftcms.com/multisafepay).

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

# How to configure
1. Sign in to your Craft Commerce <<glossary:backend>>.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure <<glossary:gateways>>, go to **Commerce** > **System settings** > **Gateways**.  

# User guide

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

1. Sign in to your Craft Commerce backend. 
2. Go to **Commerce** > **System settings** > **Gateways** > **+ New gateway**.
3. From the **Gateway** list, select **Generic gateway**.
4. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.

</details>

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/payment-methods/credit-debit-cards/), **except** Postepay and V Pay
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [Alipay](/payment-methods/alipay), [PayPal](/payment-methods/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
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

| | |
|---|---|
| MultiSafepay dashboard | - [Full and partial refunds](/refunds/) <br> - Generic gateway transactions |
| Backend | - Full and partial refunds <br> - You can't refund more than the original amount in your backend <br> - Generic gateway transactions **not** supported |
| API | - [Refund order](https://docs-api.multisafepay.com/reference/refundorder) <br> - [Pay later refunds](/payment-methods/pay-later) **not** supported <br> - Discounts **not** supported |

<details id="processing-backend-refunds">
<summary>Processing backend refunds</summary>
<br>

To process refunds from the Craft Commerce admin panel:  

1. Go to **Commerce** > **Orders**.
2. Select the order.
3. To see the refund options, go to the **Transactions** tab. 

</details>

---

> 💬  Support
> Contact MultiSafepay:
> 
> - Telephone: +31 (0)20 8500 500
> - Email: <integration@multisafepay.com>
> - GitHub: Create a technical issue