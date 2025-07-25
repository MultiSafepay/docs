---
title: "OpenCart 3"
category: 62962dd7e272a6002ebbbbc5
order: 8
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'opencart-3'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/OpenCart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Opencart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Opencart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

> ℹ More information
>
> For more information about the plugin and a preview, see OpenCart – <a href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960" target="_blank">MultiSafepay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- OpenCart 2.X, 3.X
- PHP version 7.2, 7.3, or 7.4

# Installation

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the OpenCart installation procedure. Always make a backup.

1. Download the `Plugin_OpenCart_3.x.x.ocmod.zip`.
2. Sign in to your OpenCart <<glossary:backend>>.
3. Go to **Extensions** > **Installer**.
4. Click the **Upload** button, and then select the downloaded file.
5. Once installed, click the **Dashboard** menu.
7. To clear both caches, click the blue cog wheel button in the top-right corner, and then click the **Refresh** icon. 
8. Go to **Extensions** > **Modifications**, and then click the **Refresh** button.
9. Go to **Extensions** > **Payments** > **MultiSafepay**, and then click the **Install** button. 

## Configuration

1. Sign in to your OpenCart backend and go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay**.
2. On the **MultiSafepay configuration** page, configure the:  
    - **Payment methods** tab
    - **Order status** tab
    - **Options** tab  

To retrieve your API key, see [Website ID, API key, and security code](/docs/sites#site-id-api-key-and-security-code).
<br>

---

# User guide

## Checkouts

The plugin supports the OpenCart core checkout and is compatible with most premium themes, unless you have a custom checkout.

<details id="patches-for-third-party-themes-and-extensions">
<summary>Patches for third-party themes and extensions</summary>
<br>

The table belows shows the patches available for third-party themes and extensions:

| Patch | Download |
|---|---|
| <a href="https://www.journal-theme.com/" target="_blank">Journal3 Quick Checkout for OpenCart 3.0.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-journal3-opencart-3.0.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.journal-theme.com/" target="_blank">Journal3 Quick Checkout for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-journal3-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://dreamvention.ee/ajax-quick-checkout-one-page-checkout-fast-checkout" target="_blank">AJAX Quick Checkout for OpenCart 3.0.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-ajax-quick-checkout-free-version-7.3.1-opencart-3.0.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://dreamvention.ee/ajax-quick-checkout-one-page-checkout-fast-checkout" target="_blank">AJAX Quick Checkout for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-ajax-quick-checkout-free-version-7.3.1-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.extensionsbazaar.com/opencart-one-page-checkout" target="_blank">OnePage Checkout 4.0.0 for OpenCart 3.0.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-onepage-checkout-4.0.0-opencart-3.0.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.extensionsbazaar.com/opencart-one-page-checkout" target="_blank">OnePage Checkout 4.0.0 for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-onepage-checkout-4.0.0-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.modulepoints.com/quickcheckout" target="_blank">Quick Checkout / Onepage Checkout for OpenCart 3.0.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-quick-checkout-from-module-points-opencart-3.0.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.modulepoints.com/quickcheckout" target="_blank">Quick Checkout / Onepage Checkout for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-quick-checkout-from-module-points-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://shop.openwebcreations.eu/eu-vat-compliant" target="_blank">EU VAT Compliant</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-owc-euvat-reverse-charge-vat-exempt.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=5040" target="_blank">PayCharge Free for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-paycharge-free-version-6.1-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |
| <a href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=7382" target="_blank">Quick Checkout 11.0.0 for OpenCart 2.3.X</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/opencart/multisafepay-patch-for-quick-checkout-11.0.0-from-marketinsg-opencart-2.3.X.ocmod.zip" target="_blank">Download OCMOD</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> |

  <br>
  
The Integration Team will do their best to provide support for third-party plugins and premium themes. Email <integration@multisafepay.com>

</details>

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 3.9.0, March 19th 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

To configure generic gateways, follow these steps:

1. Sign in to your OpenCart backend.
2. Go to **Plugin settings** > **Payment methods** tab.
3. Set the:  
    - Gateway identifier  
    - Gateway logo  
    - Gateway label  
    - Whether to include the shopping cart in refunds (required for <<glossary:BNPL>> gateway IDs)

You can filter payment methods by:

- Geographic zone
- Currency
- Minimum amount
- Maximum amount
- Customer groups

Full and partial refunds (except for BNPL orders), and backend orders are fully supported. You can also set a custom initial <<glossary:order status>>.

</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase conversion.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting card payments, email a request to activate them to <sales@multisafepay.com>

1. Sign in to your OpenCart <<glossary:backend>>.
2. Go to **Extensions** > Type: **Payments** > **MultiSafepay** > **Edit**.
3. Select the **Payment methods** tab and then expand the method of your choice.
4. Enable **Payment Component** and optionally **Tokenization**.

**⚠️ Note:** Tokenization is available only when **Payment Component** is activated.

💬  **Support:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links

<details id="how-to-generate-payment-links-for-backend-orders">
<summary>How to generate payment links for backend orders</summary>
<br>

1. Sign in to your OpenCart backend.
2. Go to **System** > **Localisation** > **Order status**.
3. Enter a custom <<glossary:order status>> for when the payment link is sent.
4. Go to **Extensions** > **Payments** > **MultiSafepay**.
5. Set the **Generate payment links at the admin** field to **Yes**.
6. On the **Options** tab > **Payment request** field, set the **Previously created order status**.
7. To reserve stock units of order items generated by the admin, while the <<glossary:order status>> is still **Pending**, go to **System** > **Settings** > **Store** > **Options** tab. 
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

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/) 
- Banking methods: All, except TrustPay
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - <a href="https://www.babycadeaubon.nl" target="_blank">Baby Cadeaubon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Beauty & Wellness
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashion Cheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
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
    - <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

<details id="how-to-process-backend-refunds">
<summary>How to process backend refunds</summary>
<br>

1. Sign in to your OpenCart backend.
2. Go to **Orders** > **Order view button** > **Order history panel**. 
3. Click the **Refund** button.  
This only appears if the <<glossary:order status>> is **Completed** or **Shipped**.

</details>

## Shipping orders

When you ship <<glossary:BNPL>> orders, you need to change the <<glossary:order status>> from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

## Shopping carts

If you notice any errors in shopping cart calculations, email <integration@multisafepay.com>

As a temporary solution, you can disable payments with shopping carts.

<details id="how-to-disable-shopping-carts">
<summary>How to disable shopping carts</summary>
<br>

**⚠️ Note:** This disables all <<glossary:BNPL>> methods.

1. Sign in to your OpenCart backend.
2. Go to **Extensions** > **Payments** > **MultiSafepay**.
3. In the MultiSafepay extension, go to the **Options** tab.
4. From the **Disable Shopping Cart** list, select **Yes**.
5. Click **Save**.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.  

> ⚠️ Attention Dutch merchants
>
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

You can update the plugin using the extension installer tool in your OpenCart backend.

<details id="how-to-update-from-version-3-x-or-higher">
<summary>How to update from version 3.0.0 or higher</summary>
<br>

1. For security, create a backup of your OpenCart application.
2. Follow the [installation](/docs/opencart#installation) instructions above.

</details>

<details id="how-to-update-from-version-2-2-to-3">
<summary>How to update from version 2.2.0 to 3.x.x</summary>
<br>

1. For security, always create a backup of your OpenCart application.
2. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
3. Sign in to your OpenCart backend.
4. Go to **Extensions** > **Installer**.
5. Click the **Upload** button, and then select the downloaded file.
6. Once installed, in the menu go to **Dashboard**.
7. To clear both caches, click the blue cog wheel icon in the top-right corner, and then click the **Refresh** icon. 
8. Go to **Extensions** > **Modifications**, and then click the **Refresh** icon.
9. Go to **Extensions** > **Payments** > **MultiSafepay**.
10. To access the **Settings** page, click the **Edit** button.
11. A warning appears requesting you to delete old plugin files. 
12. In the **Maintenance** tab, click **Delete old plugin files**. 
</details>

<details id="how-to-update-from-version-2-1-or-below">
<summary>How to update from version 2.1.0 or below</summary>
<br>

1. For security, create a backup of your OpenCart application.
2. Manually remove all files from the MultiSafepay extension using an FTP program or server file administration program.
3. Follow the [installation](/docs/opencart#installation) instructions above.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/opencart/issues\" target=\"_blank\"> create a technical issue</a></li> </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)