---
title: "OpenCart"
category: 62962dd7e272a6002ebbbbc5
order: 113
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with OpenCart."
slug: 'opencart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/OpenCart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Opencart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Opencart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with OpenCart.

For more information about the plugin and a preview, see Opencart – [MultiSafepay](https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960).

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- OpenCart 2.X, 3.X
- PHP version 7.2, 7.3, or 7.4

</details>

# How to install

:warning: We recommend first installing the plugin in a test environment, following the OpenCart installation procedure. Always make a backup.

1. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
2. Sign in to your OpenCart <<glossary:backend>>.
3. Go to **Extensions** > **Installer**.
4. Click the **Upload** button, and then select the downloaded file.
5. Once installed, click the **Dashboard** menu.
7. To clear both caches, click the blue cog wheel button in the top-right corner, and then click the **Refresh** icon. 
8. Go to **Extensions** > **Modifications**, and then click the **Refresh** button.
9. Go to **Extensions** > **Payments** > **MultiSafepay**, and then click the **Install** button. 

## How to configure
1. Sign in to your OpenCart backend and go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay**.
2. On the **MultiSafepay configuration** page, configure the:  
    - **Payment methods** tab
    - **Order status** tab
    - **Options** tab  

To retrieve your API key, see [Viewing the site ID, API key, and secure code](/sites/#site-id-api-key-and-secure-code).

# User guide

## Checkouts

The plugin supports the OpenCart core checkout and is compatible with most premium themes, unless you have a custom checkout.

<details id="patches-for-third-party-themes-and-extensions">
<summary>Patches for third-party themes and extensions</summary>
<br>

The following patches for third-party themes and extensions are available:

| | |
|---|---|
| [Journal3 Quick Checkout for OpenCart 3.0.X](https://www.journal-theme.com/) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-journal3-opencart-3.0.X.ocmod.zip) |
| [Journal3 Quick Checkout for OpenCart 2.3.X](https://www.journal-theme.com/) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-journal3-opencart-2.3.X.ocmod.zip) |
| [AJAX Quick Checkout for OpenCart 3.0.X](https://dreamvention.ee/ajax-quick-checkout-one-page-checkout-fast-checkout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-ajax-quick-checkout-free-version-7.3.1-opencart-3.0.X.ocmod.zip) |
| [AJAX Quick Checkout for OpenCart 2.3.X](https://dreamvention.ee/ajax-quick-checkout-one-page-checkout-fast-checkout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-ajax-quick-checkout-free-version-7.3.1-opencart-2.3.X.ocmod.zip) |
| [OnePage Checkout 4.0.0 for OpenCart 3.0.X](https://www.extensionsbazaar.com/opencart-one-page-checkout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-onepage-checkout-4.0.0-opencart-3.0.X.ocmod.zip) |
| [OnePage Checkout 4.0.0 for OpenCart 2.3.X](https://www.extensionsbazaar.com/opencart-one-page-checkout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-onepage-checkout-4.0.0-opencart-2.3.X.ocmod.zip) |
| [Quick Checkout / Onepage Checkout for OpenCart 3.0.X](https://www.modulepoints.com/quickcheckout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-quick-checkout-from-module-points-opencart-3.0.X.ocmod.zip) |
| [Quick Checkout / Onepage Checkout for OpenCart 2.3.X](https://www.modulepoints.com/quickcheckout) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-quick-checkout-from-module-points-opencart-2.3.X.ocmod.zip) |
| [EU VAT Compliant](https://shop.openwebcreations.eu/eu-vat-compliant) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-owc-euvat-reverse-charge-vat-exempt.ocmod.zip) |
| [PayCharge Free for OpenCart 2.3.X](https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=5040) | [Download OCMOD](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-paycharge-free-version-6.1-opencart-2.3.X.ocmod.zip) |

The Integration Team will do their best to provide support for third-party plugins and premium themes. Email <integration@multisafepay.com>

</details>

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). You can use them to integrate custom gift cards, or co-branded credit cards. 

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

To configure generic gateways, follow these steps:

1. Sign in to your OpenCart backend.
2. Go to **Plugin settings** > **Payment methods** tab.
3. Set the:  
    - Gateway identifier  
    - Gateway logo  
    - Gateway label  
    - Whether to include the shopping cart in refunds (required for pay later gateway IDs)

Generic gateways support:

- All payment methods (filter by country, currency, customer group, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only
- Full and partial refunds (except for [pay later](/payment-methods/pay-later/) methods) 
- Backend orders (set a custom initial order status)

Full and partial refunds (except for [pay later](/pay-later/) methods), and backend orders are fully supported. You can also set a custom initial order status.

</details>

## Payment links

<details id="generating-payment-links-for-backend-orders">
<summary>Generating payment links for backend orders</summary>
<br>

1. Sign in to your OpenCart backend.
2. Go to **System** > **Localisation** > **Order status**.
3. Enter a custom order status for when the payment link is sent.
4. Go to **Extensions** > **Payments** > **MultiSafepay**.
5. Set the **Generate payment links at the admin** field to **Yes**.
6. On the **Options** tab > **Payment request** field, set the **Previously created order status**.
7. To reserve stock units of order items generated by the admin, while the order status is still **Pending**, go to **System** > **Settings** > **Store** > **Options** tab. 
8. In the **Processing order status** field, set the order status previously registered as **Payment request**.
9. Go to **Sales** > **Orders** > **Add new order**.
10. Enter all the order details in the following tabs:  
    - **Customer details**  
    - **Products**  
    - **Payment details**  
    - **Shipping details** 
11. At the fifth step **Totals**, in the **Payment method** field, select a MultiSafepay payment method.
12. In the **Order status** field, select the order status previously registered as **Payment request**.
13. To process the order, click **Save**.

The customer receives the payment link in the email sent by OpenCart containing the order details. The payment link is also added to the order history details. 

</details>

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/) 
- Banking methods: [All](/banks/), except TrustPay
- Pay later methods: [All](/pay-later/)
- Wallets: [Alipay](/alipay), [Apple Pay](/apple-pay), [PayPal](/paypal)
- Prepaid cards:
    - [Baby Cadeaubon](https://www.babycadeaubon.nl)
    - Beauty & Wellness
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashion Cheque](https://www.fashioncheque.com/nl)
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
    - [Yourgift](https://www.yourgift.nl/)

</details>

## Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

<details id="processing-backend-refunds">
<summary>Processing backend refunds</summary>
<br>

1. Sign in to your OpenCart backend.
2. Go to **Orders** > **Order view button** > **Order history panel**. 
3. Click the **Refund** button.  
This only appears if the order status is **Completed** or **Shipped**.

</details>

## Shopping carts

If you notice any errors in shopping cart calculations, email <integration@multisafepay.com>

As a temporary solution, you can disable payments with shopping carts.
<details id="disabling-shopping-carts">
<summary>Disabling shopping carts</summary>
<br>

**Alert:** This disables all [pay later methods](/pay-later/).

1. Sign in to your OpenCart backend.
2. Go to **Extensions** > **Payments** > **MultiSafepay**.
3. In the MultiSafepay extension, go to the **Options** tab.
4. From the **Disable Shopping Cart** list, select **Yes**.
5. Click **Save**.

</details>

## Surcharges

[Surcharges](/surcharges/) are no longer supported, but you can request a patch.  
Email <integration@multisafepay.com> 

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to [pay later methods](/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

<details id="updating-version-2-2-to-3">
<summary>Updating version 2.2.0 to 3.x.x</summary>
<br>

To update the plugin using the extension installer tool in your OpenCart backend:

1. For security, always create a backup of your OpenCart application.
2. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
3. Sign in to your OpenCart backend.
4. Go to **Extensions** > **Installer**.
5. Click the **Upload** button, and then select the downloaded file.
6. Once installed, in the menu go to **Dashboard**.
7. To clear both caches, click the blue cog wheel icon in the top-right corner, and then click on the **Refresh** icon. 
8. Go to **Extensions** > **Modifications**, and then click the **Refresh** icon.
9. Go to **Extensions** > **Payments** > **MultiSafepay**.
10. To access the **Settings** page, click the **Edit** button.
11. A warning appears requesting you to delete old plugin files. 
12. In the **Maintenance** tab, click **Delete old plugin files**. 
</details>

<details id="updating-from-version-2-1-or-below">
<summary>Updating from version 2.1.0 or below</summary>
<br>

1. For security, create a backup of your OpenCart application.
2. Manually remove all files from the MultiSafepay extension using an FTP program or server file administration program.
3. Follow the [installation](/opencart/#installation) instructions above.

</details>

---

> 💬  Support
> Contact MultiSafepay:
> 
> - Telephone: +31 (0)20 8500 500
> - Email: <integration@multisafepay.com>
> - GitHub: Create a technical issue
