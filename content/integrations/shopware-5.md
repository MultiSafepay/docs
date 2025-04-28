---
title: "Shopware 5"
category: 62962dd7e272a6002ebbbbc5
order: 14
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manuals for MultiSafepay's free plugins."
slug: 'shopware-5'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_5.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Shopware" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Shopware/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Shopware 5.6.x and 5.7.x.
- Tested on Shopware 5.7.11 and PHP 8.0

## Installation and configuration

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the Shopware 5 installation procedure. Always make a backup.

1. Sign in to your Shopware 5 backend.
2. Go to **Configuration** > **Plugin manager**.
3. Search for the MultiSafepay plugin, and then click **Download now**.
4. Go to **Configuration** > **Plugin manager** > **Installed**.
5. Search for the installed MultiSafepay plugin, and then click the **Edit** pencil icon.
6. In the **API key** field, enter your [API key](/docs/sites#site-id-api-key-and-security-code).
7. Fill out the other fields as required.
8. Go to **Configuration** and select the required payment methods.
<br>
---

## User guide

### Enabling and disabling payment methods

Once the plugin is initially installed, reinstalling becomes necessary to manage the listing or delisting of enabled and disabled payment methods.

Please follow the first four steps described in the installation and configuration process, then proceed to the fifth one, where you will find the **Reinstall** icon for clicking.

### Backend orders

To create backend orders in the MultiSafepay Shopware 5 plugin, Shopware uses a third-party plugin. 

See shopwareLabs GitHub – <a href="https://github.com/shopwareLabs/SwagBackendOrder" target="_blank">SwagBackendOrder</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

We support V2.x versions.

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

Orders are created via a MultiSafepay notification to Shopware 5 using the `transaction ID`. After completing payment, the customer is redirected to your order confirmation page.  

</details>

<details id="how-to-switch-order-flows">
<summary>How to switch order flows</summary>
<br>

To change the flow you are using, follow these steps:

1. Sign in to your Shopware 5 backend.
2. Go to **Configuration** > **Plugin manager** > **Installed**.
3. Search for the installed **MultiSafepay** plugin, and then click the **Edit** pencil icon.
4. Click the dropdown icon to select the relevant status in the **Status** fields.
5. Click **Save**.

</details>


### Payment methods

By default, any payment method you activate in your MultiSafepay account will be available for your backend. Newly activated payment methods must be enabled manually in your <<glossary:backend>> settings.

### Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

To [enable recurring payments](/docs/recurring-payments#activate) for your <<glossary:backend>>, email [sales@multisafepay.com](sales@multisafepay.com).
Once activated, the setting will be automatically applied to the supported payment methods at your checkout.

### Refunds

You can process [full refunds](/docs/refund-payments/) for all Shopware 5 payment methods **except** <<glossary:BNPL>> from your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

### Session data

Shopware 5 can remove sessions before the order is created in the backend.
To prevent this, we recommend making the following changes to the <a href="https://developers.shopware.com/developers-guide/shopware-config/" target="_blank">config.php</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

```
'session' => [
    'save_handler' => 'db',
    'gc_probability' => 0,
    'gc_divisor' => 1000
],
```

For more information, see Shopware – <a href="https://developers.shopware.com/sysadmins-guide/sessions/#blocking-transactions" target="_blank">Blocking transactions</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

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

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>

### Upgrading to Shopware 6

<details id="how-to-upgrade-to-shopware-6">
<summary>How to upgrade to Shopware 6</summary>
<br>

**About Shopware 6**  
Shopware 6 is the latest version of the Shopware ecommerce platform. It maintains simplicity, but features a great new interface and functionalities, including:

- Sales Channels function that links to social shopping platforms (e.g. Facebook, Instagram), and supports mobile apps and <<glossary:POS>> systems
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

For instructions, see the <a href="https://docs.shopware.com/en/migration-en" target="_blank">Shopware migration manual</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

For questions, email <integration@multisafepay.com>

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/shopware/issues\" target=\"_blank\"> create a technical issue</a></li>\n    <li>Join the <a href=\"https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ\">official Shopware 6 Slack channel</a></li>\n    <li>Join the private <a href=\"https://shopwarenederland.slack.com/archives/G0146NKFJTT\">MultiSafepay Shopware 6 Slack channel</a></li>\n  </ul>  \n  <p>For support for Shopware 6 Professional/Enterprise, email <a href=\"mailto:sales@multisafepay.com\">sales@multisafepay.com</p>\n</blockquote>"
}
[/block]

[Top of page](#)
