---
title: "PrestaShop 1.6"
category: 62962dd7e272a6002ebbbbc5
order: 10
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'prestashop-1-6'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/PrestaShop_new.svg" width="50" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<div style={{display: 'flex', flexWrap: 'wrap'}}>
  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#006ba1', color: '#ffffff', textDecoration: 'none'}} href="https://github.com/MultiSafepay/prestashop-1.6/releases/download/3.15.0/Plugin_PrestaShop_1_6_3.15.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style={{marginLeft: '0.6em'}}> </i></a>

  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/prestashop-1.6" target="_blank"><i class="icon-external-link" /> <span>Source code</span></a>

  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/prestashop-1.6/blob/main/CHANGELOG.md" target="_blank"><span>Changelog</span></a>
</div>

> ⚠️ Action required
>
> We are phasing out support for this plugin. We recommend migrating to our [PrestaShop 1.7 plugin](/docs/prestashop-1-7/) as soon as possible.

# Prerequisites

* [MultiSafepay account](/docs/getting-started-guide/)
* PrestaShop 1.6
* Tested on PHP 5.6

# Installation and configuration

  **💡 Tip!** We recommend first installing the plugin in a test environment, following the PrestaShop 1.6 installation procedure. Always make a backup.

1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directory.\
   **⚠️Note:** When upgrading to a newer version of your plugin, always make sure to remove all outdated plugin files and folders.
2. Sign in to your PrestaShop 1.6 <Glossary>backend</Glossary>.
3. Go to **Modules and services** > **Payments and gateways**.\
   **⚠️ Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your website [API key](/docs/sites#site-id-api-key-and-security-code), and then click **Save**.
6. On the **Payments** tab, enable the relevant payment methods.\ <br />

***

# User guide

## Generic gateways

The plugin supports generic gateways, which let you add payment methods manually. This is particularly useful for integrating gift cards specific to your business.

<details id="how-to-configure-generic-gateways">
  <summary>How to configure generic gateways</summary>

  <br />

  1. Sign in to your PrestaShop 1.6 <Glossary>backend</Glossary>.
  2. Go to **Modules and services**.
  3. Search for "generic gateway", select gateway 1, 2, or 3, and then click **Install**.
  4. In the **Gateway title** field, enter the name of the payment method.
  5. In the **Gateway ID** field, enter the [gateway ID](/reference/gateway-ids).
  6. Optionally:
     * Upload the <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">payment method logo</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
     * Enter minimum and maximum order amounts.
  7. Click **Save**.

  ✅   Success! The payment method is now active.
</details>

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/)
  * <Glossary>BNPL</Glossary>: All
  * Wallets: [Alipay](/docs/alipay/), [Alipay+](/docs/alipay-plus/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
  * Banking methods:
    * [Bancontact](/docs/bancontact/)
    * [Bank transfer](/docs/bank-transfer/)
    * [Belfius](/docs/belfius/)
    * [CBC/KBC](/docs/cbc-kbc/)
    * [Dotpay](/docs/dotpay/)
    * [EPS](/docs/eps/)
    * [Giropay](/docs/giropay/)
    * [Google Pay](/docs/google-pay/)
    * [iDEAL](/docs/ideal/)
    * [MyBank](/docs/mybank/)
    * [Request to Pay](/docs/request-to-pay/)
    * [Direct debit](/docs/direct-debit/)
    * [Sofort](/docs/sofort/)
  * Prepaid cards:
    * Beauty and Wellness gift card
    * Boekenbon
    * Degrotespeelgoedwinkel
    * Fashioncheque
    * Fashion gift card
    * Gezondheidsbon
    * Good4fun
    * Parfumcadeaukaart
    * Paysafecard
    * Sport en Fit
    * VVV gift card
    * Webshop gift card
    * Wijncadeau
    * YourGift
</details>

## Matching orders

In PrestaShop 1.6, the order ID is generated after the payment, which causes a mismatch with the order ID in your MultiSafepay dashboard. You can match orders using the transaction ID.

<details id="how-to-view-transaction-ids">
  <summary>How to view transaction IDs</summary>

  <br />

  1. Sign in to your PrestaShop 1.6 backend.
  2. Go to **Payment** > **Order details**.
</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

* Provide a seamless checkout experience to increase <Glossary>conversion</Glossary>.
* Encrypt customer payment details for secure processing.
* Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: Amex, Maestro, Mastercard, and Visa
  * <Glossary>BNPL</Glossary>: [Pay After Delivery installments](/docs/pay-after-delivery-installments)
</details>

<details id="how-to-activate-payment-components">
  <summary>How to activate payment components</summary>

  <br />

  1. Sign in to your PrestaShop 1.6 backend.
  2. Go to **Modules and services**
  3. Select the relevant payment methods.
  4. Set the **Use Payment component** toggle to **Yes**.
  5. Click **Save**.

  💬 Support: If you're new to accepting card payments, email a request to activate them to [risk@multisafepay.com](mailto:risk@multisafepay.com)
</details>

## Payment links

Payment links generated manually in your MultiSafepay dashboard don't automatically create or update orders in your PrestaShop 1.6 backend.

## Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

<details id="how-to-enable-recurring-payments">
  <summary>How to enable recurring payments</summary>

  <br />

  1. Sign in to your PrestaShop 1.6 backend.
  2. Go to **Modules and services** > **Modules and services**
  3. Select either the bundled card payments <Glossary>gateway</Glossary>, **or** select specific card.
  4. Click **Configure**.
  5. Set the **Tokenization** field to **Yes**.
  6. Click **Save**.
</details>

## Refunds

You can process [full and partial refunds](/docs/refund-payments/) from your MultiSafepay dashboard.\
Backend refunds are **not** supported.

## Shipping orders

When you ship <Glossary>BNPL</Glossary> orders, you need to change the <Glossary>order status</Glossary> from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing.

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.

<details id="applying-surcharges-with-bvk">
  <summary>Applying surcharges with BVK</summary>

  <br />

  To apply a surcharge or payment fee to a payment method, you can use the third-party <a href="https://www.bvkyazilim.com/cart/prestashop-modules" target="_blank">BVK</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> package.

  The Integration Team will do their best to support you with installing BVK, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

  > ⚠️ **Attention Dutch merchants**
  >
  > We strongly recommend **not** applying surcharges to <Glossary>BNPL</Glossary> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).
</details>

## Thirty Bees

For support for the PrestaShop <a href="https://thirtybees.com/blog/what-is-thirty-bees" target="_blank">Thirty Bees</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> fork, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
  <summary>How to update via SFTP</summary>

  <br />

    **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

  1. Download the plugin again above.
  2. Follow the Installation and configuration instructions from step 2.
</details>

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Contact MultiSafepay:</p>

  <ul>
    <li>Telephone: <a href="tel:+310208500500">+31 (0)20 8500 500</a></li>
    <li>Email: <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></li>
    <li>GitHub: <a href="https://github.com/MultiSafepay/prestashop-1.6/issues" target="_blank"> create a technical issue</a></li>
  </ul>
</blockquote>

[Top of page](#)