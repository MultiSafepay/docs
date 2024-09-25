---
title: "OpenCart 4"
category: 62962dd7e272a6002ebbbbc5
order: 9
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'opencart-4'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/OpenCart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960" target="_blank"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/opencart-4" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/opencart-4/blob/main/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

> ℹ More information
>
> For more information about the plugin and a preview, see OpenCart 4 – <a href="https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960" target="_blank">MultiSafepay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- OpenCart 4.0.2.0 up to 4.0.2.3
- PHP versions supported: 8.0, 8.1

# Installation

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the OpenCart 4 installation procedure. Always make a backup.

1. Download the plugin file: `multisafepay.ocmod.zip`.
2. Sign in to your OpenCart 4 <<glossary:backend>>.
3. Go to **Extensions** > **Installer**.
4. Click on the **Upload** icon, and then select the downloaded file.
5. Click on the **Install** icon of **MultiSafepay** in the list of installed extensions.
6. Once installed, click on the **Extensions** option in the main menu.
7. Select **Extensions** and then **Payments** inside the **Choose the extension type**.
8. In the deployed list of **Payments** below, find **MultiSafepay**, and then click on the **Install** icon.

## Additional installation steps
You need to make two specific extra actions in the **OpenCart 4 Backend** ...

1. Enable **Telephone Display** and **Telephone Required** at **System** > **Settings** > **Edit your Store** > **Option** > **Account**

2. Enable the option **Lax** in **Session Same-Site Cookie** at **System** > **Settings** > **Edit your Store** > **Server**

## Configuration

1. Sign in to your OpenCart 4 <<glossary:backend>>.
2. Go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay** > **Edit Icon**.
3. On the **MultiSafepay configuration** page, configure the:  
    - **Payment methods** tab
    - **Order status** tab
    - **Options** tab  

To retrieve your API key, see [Site ID, API key, and security code](/docs/sites#site-id-api-key-and-security-code).
<br>

---

# User guide

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

To configure generic gateways, follow these steps:

1. Sign in to your OpenCart 4 backend.
2. Go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay** > **Edit Icon**.
3. On the **MultiSafepay configuration** page > **Payment methods** tab.
4. Set the:  
    - Gateway **name**
    - Gateway **code**
    - Whether to include the shopping cart in refunds (required for <<glossary:BNPL>> gateway IDs)

You can filter payment methods by:

- Geographic zone
- Currency
- Minimum total amount
- Maximum total amount
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

If you're new to accepting card payments, email a request to activate them to <risk@multisafepay.com>

1. Sign in to your OpenCart 4 <<glossary:backend>>.
2. Go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay** > **Edit Icon**.
3. Select the **Payment methods** tab and then expand the method of your choice.
4. Enable **Payment Component** and optionally **Tokenization**.

**⚠️ Note:** Tokenization is available only when **Payment Component** is activated.

💬  **Support:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

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

1. Sign in to your OpenCart 4 <<glossary:backend>>.
2. Go to **Orders** > **Order view button** > **Order history panel**. 
3. Click the **Refund** button.  
This only appears if the <<glossary:order status>> is **Completed** or **Shipped**.

</details>

## Shopping carts

If you notice any errors in shopping cart calculations, email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a>

As a temporary solution, you can disable payments with shopping carts.

<details id="how-to-disable-shopping-carts">
<summary>How to disable shopping carts</summary>
<br>

**⚠️ Note:** This disables all <<glossary:BNPL>> methods.

1. Sign in to your OpenCart 4 <glossary:backend>.
2. Go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay** > **Edit Icon**.
3. In the MultiSafepay extension, go to the **Options** tab.
4. From the **Disable Shopping Cart** list, select **Yes**.
5. Click **Save**.

</details>

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.

<details id="applying-surcharges-with-third-party-extensions">
<summary>Applying surcharges with third-party extensions</summary>
<br>

To apply a surcharge or payment fee to a payment method, you can use the <a href="https://www.opencart.com/index.php?route=marketplace/extension" rel="nofollow" target="_blank">third-party extensions</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

The Integration Team will do their best to support you with installing surcharges module, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

> ⚠️ **Attention Dutch merchants**
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

</details>

## Updates

1. **Backup** all the values you used on the previous installation of **MultiSafepay** plugin.
2. **Upgrade** your store to OpenCart 4.x.
3. Install **MultiSafepay** plugin as described before.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/opencart-4/issues\" target=\"_blank\"> create a technical issue</a></li> </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
