---
title: "CCV Shop"
category: 62962dd7e272a6002ebbbbc5
order: 100
hidden: true
parentDoc: 62a9a54aba9800011a8bda88
slug: 'ccv-shop-partner'
excerpt: "Technical manual for MultiSafepay's free app."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/CCVShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation and configuration

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Sign in to your CCV Shop <<glossary:backend>> and install the MultiSafepay app from the App Store.
2. Go to **Mijn webshop** > **Instellingen** > **Bestelproces & voorraad** > **Betaalmethoden**.
3. In the **Electronische betalingen** tab, select **MultiSafepay**.
4. Enter your [account ID, website ID and security code](/docs/sites#site-id-api-key-and-security-code).
5. If using your MultiSafepay test account, select **Test mode**.
6. Click **Synchroniseer betaalmethodes met MultiSafepay**, and then click **Save**.
   <br>

___

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Wallets: [PayPal](/docs/paypal/)
- Banking methods:
    - [Bancontact](/docs/bancontact/)
    - [Bank transfer](/docs/bank-transfer/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [Sofort](/docs/sofort/)

</details>

## Refunds

You can process refunds from your MultiSafepay dashboard, but not in your <<glossary:backend>>.
<br>

---

[block:html]
{
"html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <ul>\n    <li>For technical queries about the app, email CCV Shop at <a href=\"mailto:support@ccvshop.nl\">support@ccvshop.nl</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)