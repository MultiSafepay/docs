---
title: "PrestaShop 1.7"
category: 62962dd7e272a6002ebbbbc5
order: 111
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'prestashop-1-7'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/PrestaShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official/releases/download/5.5.0/Plugin_PrestaShop_5.5.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-official/blob/main/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

> ⚠️ Action required
> If you are still using the [deprecated plugin](https://github.com/MultiSafepay/prestashop), we recommend [upgrading to the latest version](#upgrades) as soon as possible.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- PrestaShop version 1.7.6 or higher
- PHP version 7.2 or higher

> **Tip!** If you're on PrestaShop 1.7.5 or lower, consider updating PrestaShop or use an older version (4.x) of our plugin which can be found in our [PrestaShop GitHub repository](https://github.com/MultiSafepay/prestashop/releases). 

# How to install

> **Tip!** We recommend first installing the plugin in a test environment, following the PrestaShop 1.7 installation procedure. Always make a backup.

1. Sign in to your PrestaShop 1.7 <<glossary:backend>>.
2. Go to **Modules** > **Module Manager** > **Upload a module**.
3. Select the Plugin_PrestaShop.zip file, and then click **Configure**.
4. Clear your cache.

# How to configure

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **MultiSafepay**, and enter your [site API key](/docs/sites/#site-id-api-key-and-security-code).
3. On the **Payment methods** tab, enable the relevant payment methods.
4. Click **Save**.
<br>

---

# User guide

## Backend orders

In the previous release, PrestaShop backend orders were only created for MultiSafepay orders with **Completed** status. 
In the current release, a backend order is created for **every** order attempt, that is for MultiSafepay orders with **Initialized** status.

## Checkouts

The plugin supports the PrestaShop core checkout and is compatible with most premium themes, unless you have a custom checkout.

<details id="supported-third-party-modules">
<summary>Supported third-party modules</summary>
<br>

The following third-party modules are supported:

- [One Page Checkout PS](https://addons.prestashop.com/en/express-checkout-process/8503-one-page-checkout-ps-easy-fast-intuitive.html)
- [The Checkout](https://addons.prestashop.com/en/express-checkout-process/42005-the-checkout.html) – Payment options must be set on separate pages in the plugin settings page.

The Integration Team will do their best to provide support for third-party plugins and premium themes. Email <integration@multisafepay.com>

</details>

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/docs/payment-pages/). This is particularly useful for integrating gift cards. 

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Prestashop 1.7 backend.
2. Go to **Improve** > **MultiSafepay** > **Payment methods** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway icon.


The generic gateway supports:

- All payment methods (filter by country, currency, customer group, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only

**Gift cards**

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and *no* closed-loop gift cards.

**Co-branded credit cards**

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

{{< /details >}}

### Order flows

The plugin supports two flows for creating orders: **before** or **after** the transaction is completed.

{{< details title="Before flow" >}}
 
By default, order confirmation emails are sent before the payment is finalized.  
You can disable this feature. 

The status of abandoned payments changes to **Cancelled**.

{{< /details >}}

{{< details title="After flow" >}}
 
Orders are created via a MultiSafepay notification to PrestaShop using the `cart ID`. After completing payment, the customer is redirected to your order confirmation page.  
If the notification hasn't been processed yet, a waiting page with a loader displays while the order is created.

{{< /details >}}

{{< details title="Switching order flows" >}}

To change the flow you are using, follow these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the **MultiSafepay module**, go to the **General settings** tab.
4. In the **Create order before payment** field, select the flow.
5. Click **Save**.

{{< /details >}}

### Order flows

The plugin supports two flows for creating orders: **before** or **after** the transaction is completed.
{{< details title="Before flow" >}}
 
By default, order confirmation emails are sent before the payment is finalized.  
You can disable this feature. 

The status of abandoned payments changes to **Cancelled**.

{{< /details >}}

{{< details title="After flow" >}}
 
Orders are created via a MultiSafepay notification to PrestaShop using the `cart ID`. After completing payment, the customer is redirected to your order confirmation page.  
If the notification hasn't been processed yet, a waiting page with a loader displays while the order is created.

{{< /details >}}

{{< details title="Switching order flows" >}}

To change the flow you are using, follow these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the **MultiSafepay module**, go to the **General settings** tab.
4. In the **Create order before payment** field, select the flow.
5. Click **Save**.

</details>

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

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the **MultiSafepay module**, go to the **General settings** tab.
4. In the **Create order before payment** field, select the flow.
5. Click **Save**.

</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting credit card payments, email a request to activate them to <sales@multisafepay.com>

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **MultiSafepay module** > **Payment methods** > **Credit card**.
3. Slide the **Enable payment component** radio button to **Enabled**.
4. Click **Save config**.

> **Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/cards/)
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

1. Sign in to your PrestaShop 1.7 backend. 
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the MultiSafepay module, go to the **Payment methods** tab.  
4. Select either the bundled credit cards <<glossary:gateway>>, **or** select specific credit cards. 
5. Set the **Enable tokenization** toggle to **Enabled**.
6. Click **Save**.

</details>

## Refunds

- [Full and partial refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
- [BNPL refunds](/docs/refund-payments#bnpl-refunds) are only supported in your dashboard.
    
<details id="how-to-disable-api-refunds">
<summary>How to disable API refunds</summary>
<br>

By default, refunds initiated in your backend are automatically processed via our API, **except** for voucher refunds.

To disable this, follow these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **MultiSafepay module** > **Manage hooks**.
3. Select **Display non-positionable hooks**.
4. For **actionOrderSlipAdd**, select the three dots, and then click **Unhook**.

</details>

## Shopping carts

If you notice errors in shopping cart calculations, email <integration@multisafepay.com>

As a temporary solution, you can disable sending the shopping cart with the payment request.

❗️ <<glossary:BNPL>> methods do not work if the shopping cart is disabled. 

<details id="how-to-disable-the-shopping-cart">
<summary>How to disable the shopping cart</summary>
<br>

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the MultiSafepay module, go to the **General settings** tab.
4. Set the **Disable Shopping Cart** toggle to **Enabled**.
5. Click **Save**.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.

<details id="how-to-apply-surcharges-with-third-party-add-ons">
<summary>How to apply surcharges with third-party add-ons</summary>
<br>

There are several [third-party add-ons](https://addons.prestashop.com/en/search?search_query=surcharge) available. However, we can't guarantee compatibility with our plugin. Make sure that you test them carefully before installing.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

</details>

## Translation

<details id="how-to-translate-the-multisafepay-module">
<summary>How to translate the MultiSafepay module</summary>
<br>

To translate elements of the MultiSafepay module in the plugin, follow these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Improve** > **International** > **Translations**.
3. On the **Modify translations** tab, from the **Type of translation** list, select **Installed module translations**.
4. Select the **MultiSafepay** module and the **Language**, and then click **Modify**.
5. Enter the required translations, and then click **Save**. 

To translate the names of payment methods:

1. Go to **Improve** > **MultiSafepay** > **Payment methods**.
2. Select the payment method you want to translate.
3. Make sure the **Title** field is empty.

</details>

## Updates

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

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

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)