---
title: "Odoo"
category: 62962dd7e272a6002ebbbbc5
order: 112
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with Odoo."
slug: 'odoo'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Odoo.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration/archive/13.0-develop.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration/blob/13.0-develop/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Odoo. 

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Odoo 13.0
- Tested on Python 3.6

</details>

# How to install

:warning: We recommend first installing the plugin in a test environment, following the Odoo installation procedure. Always make a backup.

1. Download the ZIP archive with module.
2. Unpack the content of the .ZIP file.
3. In your Odoo server (`/mnt/extra-addons/`), under **Custom apps**, add the **payment_multisafepay_official** folder. 
4. Install the required Python dependencies:
    ```
    pip3 install -r requirements.txt
    ```
    Alternatively, you can install them manually:
    ```
    pip3 install multisafepay==0.2.0
    ```
    For more information about dependencies, see Python - [MultiSafepay](https://pypi.org/project/multisafepay).
5. Restart your Odoo server.
6. In your Odoo <<glossary:backend>>, activate developer mode.
7. Go to the **Apps menu** > **Update apps list**.
8. Search for and open the MultiSafepay payments module `payment_multisafepay_official`.
9. Click **Install**.

# How to configure
1. Sign in to your Odoo backend. 
2. Go to the **Invoicing** or **Website** menu > **Configuration** > **Payment acquirers**.
3. Select **MultiSafepay** payment acquirer. 
4. Go to **Edit** mode. 
5. To change the <<glossary:acquirer>> state, click **Enabled** or **Test**. (Default: Disabled)
6. Enter **Live** and/or **Test** **API key**.
7. On the **Configuration tab**, set **Journal**, and then click **Save**.
9. To get payment methods from your MultiSafepay account, go the **Configuration** tab, click **Pull payment methods**.  
    Make sure the relevant payment methods are activated for your account.
10. Configure each payment method separately

<details id="payment-methods-settings">
<summary>Payment methods settings</summary>
<br>

- Name  
- State  
- Country: Disabled for some payment methods  
- Customer group  
- Order amount: Disabled for some payment methods  
- Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.

</details>

# User guide

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

1. Sign in to your Odoo backend. 
2. Go to **Invoicing** > **Payment method** > **Other payment acquirer** > **MultiSafepay**.
3. In the **Title** field, set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids). 
4. Set the gateway logo and name.

</details>

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Pay later methods: [All](/pay-later/)
- Wallets: [Alipay](/alipay), [Apple Pay](/apple-pay), [PayPal](/paypal)
- Banking methods:
    - [Bancontact](/bancontact)
    - [Bank Transfer](/bank-transfer)
    - [Belfius](/belfius)
    - [CBC/KBC](/cbc-kbc)
    - [Dotpay](/dotpay)
    - [EPS](/eps)
    - [Giropay](/giropay)
    - [iDEAL](/ideal)
    - [SEPA Direct Debit](/sepa-direct-debit)
    - [Sofort](/sofort)
    - [Trustly](/trustly)

</details>

## Updates

<details id="updating-the-plugin">
<summary>Updating the plugin</summary>
<br>

1. Sign in to your Odoo backend. 
2. Go to the **Apps** menu.
3. Search for and open the **MultiSafepay payments** module.
4. Click **Upgrade**.

</details>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]