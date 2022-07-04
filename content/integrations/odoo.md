---
title: "Odoo"
category: 62962dd7e272a6002ebbbbc5
order: 107
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'odoo'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Odoo.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration/archive/13.0-develop.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/official-odoo-integration/blob/13.0-develop/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Odoo 13.0
- Tested on Python 3.6

# How to install

> **Tip!** We recommend first installing the plugin in a test environment, following the Odoo installation procedure. Always make a backup.

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
10. Configure each payment method separately:

    <details id="payment-method-settings">
    <summary>Payment method settings</summary>
    <br>

    - Name  
    - State  
    - Country: Disabled for some payment methods  
    - Customer group  
    - Order amount: Disabled for some payment methods  
    - Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.

    </details>

    <br>

---

# User guide

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/docs/payment-pages/). This is particularly useful for integrating gift cards.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Odoo backend. 
2. Go to **Invoicing** > **Payment method** > **Other payment acquirer** > **MultiSafepay**.
3. In the **Title** field, set the relevant [payment method gateway IDs](/reference/gateway-ids/). 
4. Set the gateway logo and name.

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/cards/)
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Banking methods:
    - [Bancontact](/docs/bancontact/)
    - [Bank Transfer](/docs/bank-transfer/)
    - [Belfius](/docs/belfius/)
    - [CBC/KBC](/docs/cbc-kbc/)
    - [Dotpay](/docs/dotpay/)
    - [EPS](/docs/eps/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [SEPA Direct Debit](/docs/sepa-direct-debit/)
    - [Sofort](/docs/sofort/)
    - [Trustly](/docs/trustly/)

</details>

## Updates

You can update in your <<glossary:backend>>.

<details id="how-to-update-the-plugin">
<summary>How to update the plugin</summary>
<br>

1. Sign in to your Odoo backend. 
2. Go to the **Apps** menu.
3. Search for and open the **MultiSafepay payments** module.
4. Click **Upgrade**.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
