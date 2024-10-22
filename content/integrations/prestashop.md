---
title: "PrestaShop"
category: 62962dd7e272a6002ebbbbc5
order: 12
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'prestashop'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/PrestaShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official/releases/download/5.14.2/Plugin_PrestaShop_5.14.2.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official/blob/main/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

> ⚠️ Action required
>
> If you are still using the <a href="https://github.com/MultiSafepay/prestashop" target="_blank">deprecated plugin</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, we recommend [upgrading to the latest version](#upgrades) as soon as possible.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- PrestaShop 1.7.6 up to PrestaShop 8.1.x
- PHP version 7.2 or higher

# Installation

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the PrestaShop installation procedure. Always make a backup.

1. Sign in to your PrestaShop Back Office.
2. Go to **Modules** > **Module Manager** > **Upload a module**.
3. Select the Plugin_PrestaShop.zip file, and then click **Configure**.
4. Clear your cache.

# Configuration

1. Sign in to your PrestaShop Back Office.
2. Go to **MultiSafepay**, and enter your [site API key](/docs/sites/#site-id-api-key-and-security-code).
3. On the **Payment methods** tab, enable the relevant payment methods.
4. Click **Save**.

### Additional configuration steps

After completing the configuration, enable specific countries to make the payment methods available.

<details id="how-to-configure-countries">
<summary>How to enable countries</summary>
<br>

1. Go to **Improve** > **Payment** > **Preferences** > **Country restrictions**.
2. Select the checkbox to enable the relevant countries. 
3. Click **Save**.

---
</details>

# User guide

## Order flows

The plugin supports two flows for creating orders: **before** or **after** the transaction is completed.

<details id="before-flow">
<summary>Before flow</summary>
<br>

By default, order confirmation emails are sent before the payment is finalized.  
You can disable this feature. 

The status of abandoned payments changes to **Cancelled**.

</details>

<details id="after-flow">
<summary>After flow</summary>
<br>

Orders are created via a MultiSafepay notification to PrestaShop using the `cart ID`. After completing payment, the customer is redirected to your order confirmation page.  
If the notification hasn't been processed yet, a waiting page with a loader displays while the order is created.

</details>

<details id="how-to-switch-order-flows">
<summary>How to switch order flows</summary>
<br>

To change the flow you are using, follow these steps:

1. Sign in to your  PrestaShop Back Office.
2. Go to **MultiSafepay** > **General settings** tab.
3. In the **Create order before payment** field, select the flow.
4. Click **Save**.

</details>

## Backend orders

In the previous release, PrestaShop Back Office orders were only created for MultiSafepay orders with **Completed** status. 
In the current release, a backend order is created for **every** order attempt, that is for MultiSafepay orders with **Initialized** status.

## Checkouts

The plugin supports the PrestaShop core checkout and is compatible with most premium themes, unless you have a custom checkout.

<details id="supported-third-party-modules">
<summary>Supported third-party modules</summary>
<br>

The following third-party modules are supported:

- <a href="https://addons.prestashop.com/en/express-checkout-process/8503-one-page-checkout-ps-easy-fast-intuitive.html" target="_blank">One Page Checkout PS</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://addons.prestashop.com/en/express-checkout-process/42005-the-checkout.html" target="_blank">The Checkout</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> – Payment options must be set on separate pages in the plugin settings page.

The Integration Team will do their best to provide support for third-party plugins and premium themes. Email <integration@multisafepay.com>

</details>

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 5.0.0-RC-1, Oct 27th 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your PrestaShop Back Office.
2. Go to **MultiSafepay** > **Payment methods** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway icon.

You can filter payment methods by:

- Country
- Currency
- Customer group
- Minimum and maximum amount

</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: Amex, Maestro, Mastercard, and Visa
- <<glossary:BNPL>>: [Pay After Delivery installments](/docs/pay-after-delivery-installments)

</details>

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

1. Sign in to your PrestaShop Back Office.
2. Go to **MultiSafepay** > **Payment methods** tab.
3. Select the relevant payment methods.
4. Set **Enable payment component** toggle to **Enabled**.
5. Click **Save**.

💬 Support: If you're new to accepting card payments, email a request to activate them to <risk@multisafepay.com>

**⚠️ Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links

<details id="how-to-generate-payment-links-for-backend-orders">
<summary>How to generate payment links from back office</summary>
<br>

1. Sign in to your PrestaShop back office.
2. Go to **Orders** > **Orders**.
3. Click on **Add new order** at the top right corner.
4. To add new order, follow all steps in PrestaShop 8 core reference page - see <a href="https://devdocs.prestashop-project.org/8/development/page-reference/back-office/order/add-new-order/" target="_blank"> PrestaShop back office page</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> <br>

> **⚠️ Note:** To successfully generate payment links from the back office, ensure that you have followed the steps below:  
> Under **Summary** section:
>   - Select **MultiSafepay** as **Payment**.
>   - Select **MultiSafepay initialized** as **Order status**.

</details>

## Payment methods

Before activating the relevant payment methods in your <<glossary:backend>>, you must first activate them in your MultiSafepay dashboard. See - [How to activate payment methods](/docs/payment-methods#activation).

<details id="activate-payment-methods">
<summary>How to activate payment methods</summary>
<br>

1. Sign in to your **PrestaShop** Back Office.
2. Go to **MultiSafepay** > **Payment Methods**.
3. Go to the relevant payment method and click **+**. This will show settings for the specific payment method.
4. Click to enable.

**💡 Tip!** You can handle the positioning of payment methods in the checkout by clicking the **left icon** and dragging it up or down.

</details>

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All
- <<glossary:BNPL>>: All
- Wallets: All
- Prepaid cards:
    - Baby Giftcard
    - Beauty and wellness
    - Boekenbon
    - Degrotespeelgoedwinkel
    - Fashioncheque
    - Fashion gift card
    - Fietsenbon
    - Gezondheidsbon
    - Givacard
    - Good4fun
    - Goodcard
    - Nationale tuinbon
    - Parfumcadeaukaart
    - Paysafecard
    - Podium
    - Sport en Fit
    - VVV gift card
    - Webshop gift card
    - Wellness gift card
    - Wijncadeau
    - Winkelcheque
    - Yourgift

</details>

## Recurring payments

The plugin supports [recurring payments](/docs/recurring-payments).

<details id="how-to-enable-recurring-payments">
<summary>How to enable recurring payments</summary>
<br>

1. Sign in to your PrestaShop Back Office. 
2. Go to **MultiSafepay** > **Payment methods** tab.  
3. Select either the bundled card payments <<glossary:gateway>>, **or** select specific card. 
4. Set the **Enable tokenization** toggle to **Enabled**.
5. Click **Save**.

</details>

## Refunds

- [Full and partial refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and PrestaShop <<glossary:backend>>.  
- [BNPL refunds](/docs/refund-payments#bnpl-refunds) are supported in the dashboard only.
- Refunds for orders that include shopping cart rule discounts are supported in the dashboard only.

<details id="how-to-disable-api-refunds">
<summary>How to disable API refunds</summary>
<br>

By default, refunds initiated in your backend are automatically processed via our API, **except** for voucher refunds.

To disable this, follow these steps:

1. Sign in to your PrestaShop Back Office.
2. Go to **MultiSafepay** > **Manage hooks**.
3. Select **Display non-positionable hooks**.
4. For **actionOrderSlipAdd**, select the three dots, and then click **Unhook**.

</details>

For more information, see PrestaShop – <a href="https://docs.prestashop-project.org/v.8-documentation/user-guide/selling/managing-orders/order-page-management/creating-returns-and-refunds" target="_blank">Creating returns and refunds</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Shopping carts

If you notice errors in shopping cart calculations, email <integration@multisafepay.com>

As a temporary solution, you can disable sending the shopping cart with the payment request.

**⚠️ Note:** <<glossary:BNPL>> methods do not work if the shopping cart is disabled. 

<details id="how-to-disable-the-shopping-cart">
<summary>How to disable the shopping cart</summary>
<br>

1. Sign in to your PrestaShop Back Office.
2. Go to **MultiSafepay** > **General settings** tab.
3. Set the **Disable Shopping Cart** toggle to **Enabled**.
4. Click **Save**.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.

<details id="how-to-apply-surcharges-with-third-party-add-ons">
<summary>How to apply surcharges with third-party add-ons</summary>
<br>

There are several <a href="https://addons.prestashop.com/en/search?search_query=surcharge" target="_blank">third-party add-ons</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> available. However, we can't guarantee compatibility with our plugin. Make sure that you test them carefully before installing.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

</details>

## Translation

<details id="how-to-translate-the-multisafepay-module">
<summary>How to translate the MultiSafepay module</summary>
<br>

To translate elements of the MultiSafepay module in the plugin, follow these steps:

1. Sign in to your PrestaShop Back Office.
2. Go to **International** > **Translations**.
3. On the **Modify translations** tab, from the **Type of translation** list, select **Installed module translations**.
4. Select the **MultiSafepay** module and the **Language**, and then click **Modify**.
5. Enter the required translations, and then click **Save**. 

To translate the names of payment methods:

1. Go to **MultiSafepay** > **Payment methods**.
2. Select the payment method you want to translate.
3. Make sure the **Title** field is empty.

</details>

## Updates

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the [Installation](/docs/prestashop-1-7#how-to-install) instructions.

</details>

## Upgrades

<details id="how-to-upgrade-to-version-5">
<summary>How to upgrade to version 5.x</summary>
<br>

We recommend upgrading to version 5.x from older versions.

1. Go to **Modules** > **Module manager** > **MultiSafepay** > **Configure**.
2. On the **Payment methods** tab, set all payment methods to **Off**.
3. On the **Gift cards** tab, set all gift cards to **Off**.
4. Install and configure the new plugin following the instructions below.
5. Only uninstall the older plugin when you're sure that orders created with the new plugin are being processed successfully. 

If upgrading from 5.x to a newer version, see [Updates](/docs/prestashop-1-7#updates).

</details>
<br>

---

## Troubleshooting

<details id="how-to-activate-debug-mode">
<summary>How to activate debug mode</summary>
<br>

1. Sign in to your **PrestaShop** Back Office.
2. Go to **MultiSafepay** > **General Settings** > **Debug mode**.
3. Click to enable.

</details>

<details id="how-to-get-a-system-report">
<summary>How to get a system report</summary>
<br>

1. Sign in to your **PrestaShop** Back Office.
2. Go to **MultiSafepay** > **General Settings** > **System Status**.
3. Click **Get system report**
4. A window will appear with the report. You can copy paste the content. 

</details>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/prestashop-official/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
