---
title : "CCV Shop app"
category: 62962dd7e272a6002ebbbbc5
order: 201
hidden: false
parentDoc: 62a1d780224ed800a4af21d0
excerpt: "Free app to integrate MultiSafepay payment solutions with CCV Shop."
slug: 'ccv-shop'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/CCVShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

This technical manual is for installing and configuring MultiSafepay's free app for integrating with CCV Shop.

<details id="requirements">
<summary>Requirements</summary>
<br>

You will need a [MultiSafepay account](/getting-started/guide/).
</details>

<details id="support">
<summary>Support</summary>
<br>

For technical queries about the app, email CCV Shop at <support@ccvshop.nl>

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

# Installation and configuration

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Sign in to your CCV Shop backend and install the MultiSafepay app from the App Store.
2. Go to **Mijn webshop** > **Instellingen** > **Bestelproces & voorraad** > **Betaalmethoden**.
3. In the **Electronische betalingen** tab, select **MultiSafepay**.
4. Enter your [account ID, site ID and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
5. If using your MultiSafepay test account, select **Test mode**.
6. Click **Synchroniseer betaalmethodes met MultiSafepay**, and then click **Save**.

# User guide

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Pay later methods: [AfterPay](/afterpay/), [Klarna](/klarna/)
- Wallets: [PayPal](/paypal)
- Banking methods:
    - [Bancontact](/bancontact)
    - [Bank Transfer](/bank-transfer)
    - [Giropay](/giropay)
    - [iDEAL](/ideal)
    - [Sofort](/sofort)
    - [Trustly](/trustly)

</details>

## Refunds

You can process refunds from your MultiSafepay dashboard, but not in your backend.
