---
title: "Shopware"
category: 62962dd7e272a6002ebbbbc5
order: 115
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manuals for MultiSafepay's free plugins."
slug: 'shopware'
---

# Shopware 6

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_6.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/releases/download/2.6.1/Plugin_Shopware6_2.6.1.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Shopware 6.3.x, 6.4.x _([Starter Edition](https://www.shopware.com/en/pricing) supported)_*
- Tested on PHP 7.2.0

## How to install and configure

> **Tip!** We recommend first installing the plugin in a test environment, following the Shopware 6 installation procedure. Always make a backup.

1. Navigate to our [Shopware 6 GitHub repository](https://github.com/MultiSafepay/shopware6/releases).
2. Under **Assets**, download the latest release, which starts with Plugin_Shopware6_x.x.x.zip.
3. Sign in to your Shopware 6 <<glossary:backend>>.
4. Go to **Settings** > **System** on the left hand side.
5. Select **Plugins**.
6. Click **Upload plugin** at the top of the page, and then select the file you downloaded in step 2.
7. When the plugin appears, make sure the **Activated** button is toggled.
8. Click the **...** (more) button, and then select **Config**.
9. In the drop-down menu, select **Test**.
10. In the **API key** field, enter your [API key](/docs/sites#site-id-api-key-and-security-code).
11. Fill out the other fields as required.

### Marketplace installation
Get the free MultiSafepay plugin from the [Shopware 6 marketplace](https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html) and connect your webshop with your Shopware account.

### Composer installation
Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6
```
<br>

---

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/docs/payment-pages/). This is particularly useful for integrating gift cards.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Shopware 6 backend.
2. Go to **MultiSafepay settings**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/).

You can filter generic gateways by country, and minimum and maximum amount.

</details>

### Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All, except iDEAL QR
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/docs/paysafecard/)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

### Recurring payments

You need to [enable recurring payments](/docs/recurring-payments) in your MultiSafepay dashboard and then in the <<glossary:gateway>> settings. 

### Refunds

[Full and partial refunds](/docs/refund-payments/) **except** for <<glossary:BNPL>> methods are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

<details id="how-to-process-backend-refunds">
<summary>How to process backend refunds</summary>
<br>

1. In your Shopware 6 backend, go to the **Order details** page.
2. In the **Refund** field, enter the refund amount. 

</details>

### Updates

You can update the plugin in your backend and the CMS marketplace, or via using SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 3.

</details>

[Top of page](#)
---

# Shopware 5

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_5.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Shopware" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Shopware/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Shopware 5.6.x or 5.5.7 and above.
- Tested on PHP 7.0

## How to install and configure

> **Tip!** We recommend first installing the plugin in a test environment, following the Shopware 5 installation procedure. Always make a backup.

1. Sign in to your Shopware 5 backend.
2. Go to **Configuration** > **Plugin manager**.
3. Search for the MultiSafepay plugin and click **Download now**.
4. Go to **Configuration** > **Plugin manager** > **Installed**.
5. Search for the installed MultiSafepay plugin and click on the pencil icon.
6. In the **API key** field, enter your [API key](/docs/sites#site-id-api-key-and-security-code).
7. Fill out the other fields as required.
8. Go to **Configuration** and select the required payment methods.
<br>

---

## User guide

### Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since releases:
- 2.3.0, March 24th 2021
- 2.6.0, December 7th 2020

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Shopware 5 backend.
2. Go to **MultiSafepay settings**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/).
4. Upload a custom gateway image, if relevant.
5. For <<glossary:BNPL>> orders, specify whether to include a shopping cart.

For support, email <integration@multisafepay.com>

You can filter generic gateways by country, and minimum and maximum amount.

</details>

### Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Good4fun](https://www.good4fun.nl)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/docs/paysafecard/)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

### Refunds

You can process [full refunds](/docs/refund-payments/) for all Shopware 5 payment methods **except** <<glossary:BNPL>> from your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

### Session data

<details id="missing-session-data">
<summary>Missing session data</summary>
<br>

Shopware 5 can remove sessions before the order is created in the backend.
To prevent this, we recommend making the following changes to the [config.php](https://developers.shopware.com/developers-guide/shopware-config/).

```
'session' => [
    'save_handler' => 'db',
    'gc_probability' => 0,
    'gc_divisor' => 1000
],
```

For more information, see Shopware – [Blocking transactions](https://developers.shopware.com/sysadmins-guide/sessions/#blocking-transactions).

</details>

### Shipping orders

For <<glossary:BNPL>> orders, after shipment, you must change the order status from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you change the <<glossary:order status>> to **Delivered** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

### Transaction and order numbers

Shopware 5 generates an order number and a transaction number.

The order number is generated **after** the payment is completed (unlike most ecommerce integrations where it is generated at the beginning of the order). 

The transaction number is generated when the transaction is initialized. MultiSafepay uses this number as the **order ID** in transactions.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>

### Upgrading to Shopware 6

<details id="how-to-upgrade-to-shopware-6">
<summary>How to upgrade to Shopware 6</summary>
<br>

**About Shopware 6**  
Shopware 6 is the latest version of the Shopware ecommerce platform. It maintains simplicity, but features a great new interface and functionalities, including:

- Sales Channels function that links to social shopping platforms (e.g. Facebook, Instagram), and supports mobile apps and POS systems
- Rule Builder that lets you set price rules per country, and supports multi-currency options, VAT rules, and delivery options, e.g. free delivery for orders above a specified amount
- Content management function that uses stylized blocks on Experience and Storytelling pages
- Text editor that is easier and more user-friendly

**Shopware 5 phase out**  

Support for Shopware 5 will be phased out as follows:

1. General support until mid-2024
2. Regular functional releases until mid-2021
3. Bug fixes and small releases until mid-2023
4. Security updates until mid-2024

MultiSafepay will continue to support Shopware 5 as long as it remains in the market.

**Migrating to Shopware 6**  

For instructions, see the [Shopware migration manual](https://docs.shopware.com/en/migration-en).

For questions, email <integration@multisafepay.com>

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: Create a technical issue</li>\n    <li>Join the <a href=\"https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ\">official Shopware 6 Slack channel</a></li>\n    <li>Join the private <a href=\"https://shopwarenederland.slack.com/archives/G0146NKFJTT\">MultiSafepay Shopware 6 Slack channel</a></li>\n  </ul>  \n  <p>For support for Shopware 6 Professional/Enterprise, email <a href=\"mailto:sales@multisafepay.com\">sales@multisafepay.com</p>\n</blockquote>"
}
[/block]

[Top of page](#)