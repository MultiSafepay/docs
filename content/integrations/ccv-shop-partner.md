---
title: CCV Shop
category:
  uri: Integrations
slug: ccv-shop-partner
position: 100
privacy:
  view: anyone_with_link
parent:
  uri: partner-integrations
content:
  excerpt: Technical manual for MultiSafepay's free app.
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/CCVShop.svg" width="50" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation and configuration

  **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Sign in to your CCV Shop <Glossary>backend</Glossary> and install the MultiSafepay app from the App Store.
2. Go to **Mijn webshop** > **Instellingen** > **Bestelproces & voorraad** > **Betaalmethoden**.
3. In the **Electronische betalingen** tab, select **MultiSafepay**.
4. Enter your [account ID, website ID and security code](/docs/sites#site-id-api-key-and-security-code).
5. If using your MultiSafepay test account, select **Test mode**.
6. Click **Synchroniseer betaalmethodes met MultiSafepay**, and then click **Save**.<br />

***

# User guide

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/)
  * Wallets: [PayPal](/docs/paypal/)
  * Banking methods:
    * [Bancontact](/docs/bancontact/)
    * [Bank transfer](/docs/bank-transfer/)
    * [Giropay](/docs/giropay/)
    * [iDEAL](/docs/ideal/)
    * [Sofort](/docs/sofort/)
</details>

## Refunds

You can process refunds from your MultiSafepay dashboard, but not in your <Glossary>backend</Glossary>.<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <ul>
    <li>For technical queries about the app, email CCV Shop at <a href="mailto:support@ccvshop.nl">support@ccvshop.nl</a></li>
    <li>To contact MultiSafepay, email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></li>
  </ul>
</blockquote>

[Top of page](#)
