---
title : "VirtueMart"
category: 62962dd7e272a6002ebbbbc5
order: 117
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with Virtuemart."
slug: 'virtuemart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/VirtueMart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/VirtueMart/releases/download/2.2.2/Plugin_VirtueMart_2.2.2.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Virtuemart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/VirtueMart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with VirtueMart.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Joomla 2.5 & 3.x + Virtuemart 2.x & 3.x
- Tested on PHP 7.0

</details>

# How to install

:warning: We recommend first installing the plugin in a test environment, following the VirtueMart installation procedure. Always make a backup.

1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Extension manager**.
3. Install the Plugin_VirtueMart_x.x.x.zip file using **Drag and drop** or **Browse for file**. 
4. Click **Upload & install**.

# How to configure
1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**. 
5. Click **Shop** > **Payment methods**. 
6. To install and configure each payment method separately:  
    - Click **New**.
    - Set the payment method to **VirtueMart – Payment, MultiSafepay**.
    - To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
    - Account ID (top-right corner of your dashboard)
    - [Site ID, API key, and secure code](/websites/#site-id-api-key-and-secure-code)
    - [Gateway ID](https://docs-api.multisafepay.com/reference/gateway-ids)

# User guide

## Checkouts

If a customer selects Apple Pay at checkout but isn't on an Apple device, they receive a notification to select another payment method. 

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [All](/payment-methods/wallets/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Edenred](/payment-methods/edenred/)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payment-methods/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Postepay](/payment-methods/postepay/)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

## Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and your backend.  
You cannot refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend and the CMS marketplace, via SFTP.

<details id="updating-in-your-backend">
<summary>Updating in your backend</summary>
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