---
title: "Shopware 6"
category: 62962dd7e272a6002ebbbbc5
order: 13
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manuals for MultiSafepay's free plugins."
slug: 'shopware-6'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_6.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Shopware 6.6.x.x
- Tested on Shopware 6.6.3.0 and PHP 8.1–8.2

## Installation and configuration

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the Shopware 6 installation procedure. Always make a backup.

### Marketplace installation
Get the free MultiSafepay plugin from the <a href="https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html" target="_blank">Shopware 6 marketplace</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and connect your webshop with your Shopware account.

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

### Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting card payments, email a request to activate them to <risk@multisafepay.com>

1. Sign in to your Shopware backend.
2. Go to **Settings** > **Payment**.
3. Select each payment method, and then enable the **Component** toggle.

For questions, email <integration@multisafepay.com>

**⚠️ Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

### Payment methods

By default, any payment method you activate in your MultiSafepay account will be available for your backend. Newly activated payment methods must be enabled manually in your <<glossary:backend>> settings.

### Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

<details id="how-to-enable-recurring-payments">
<summary>How to enable recurring payments</summary>
<br>

To [enable recurring payments](/docs/recurring-payments#activate) for your <<glossary:backend>>, email [sales@multisafepay.com](sales@multisafepay.com). Then:
1. Sign in to your Shopware backend.
2. Go to **Settings** > **Payment**.
3. Select each payment method, and then enable the **Tokenization** toggle.

</details>

### Refunds

[Full and partial refunds](/docs/refund-payments/) **except** for <<glossary:BNPL>> methods are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

<details id="how-to-process-backend-refunds">
<summary>How to process backend refunds</summary>
<br>

1. In your Shopware 6 backend, go to the **Order details** page.
2. In the **Refund** field, enter the refund amount. 

</details>

### Shipping orders

For <<glossary:BNPL>> orders, once shipped, the delivery status must be manually updated from **Open** to **Shipped**. This change will then automatically reflect in your MultiSafepay dashboard.

## Updates

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

### Marketplace update
Following the steps described in the installation process from <a href="https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html" target="_blank">Shopware 6 marketplace</a>.

### Composer update
By executing the following command within the root directory of Shopware 6:

```
composer update multisafepay/shopware6
```

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/shopware6/issues\" target=\"_blank\"> create a technical issue</a></li>\n    <li>Join the <a href=\"https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ\">official Shopware 6 Slack channel</a></li>\n    <li>Join the private <a href=\"https://shopwarenederland.slack.com/archives/G0146NKFJTT\">MultiSafepay Shopware 6 Slack channel</a></li>\n  </ul>  \n  <p>For support for Shopware 6 Professional/Enterprise, email <a href=\"mailto:sales@multisafepay.com\">sales@multisafepay.com</p>\n</blockquote>"
}
[/block]

[Top of page](#)
