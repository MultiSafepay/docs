---
title: Craft Commerce
category:
  uri: Archived integrations
slug: craft-commerce
position: 0
privacy:
  view: public
content:
  excerpt: Technical manual for MultiSafepay's free plugin.
---
> ❗️ Important:
>
> This plugin is at end-of-life. It may contain security vulnerabilities, compatibility issues, and lack the latest features. MultiSafepay provides no support for these plugins.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Craft_Commerce.svg" width="50" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<div style={{display: 'flex', flexWrap: 'wrap'}}>
  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/craft-commerce" target="_blank"><i className="icon-external-link" /> <span>Source code</span></a>

  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>
</div>

# Features

* Support for separate payment methods, <Glossary>BNPL</Glossary>, and gift cards
* Partial and full refunds for all payment methods, except BNPL
* Customizable <Glossary>order statuses</Glossary>
* Shipment notifications for BNPL orders

# Prerequisites

* Craft CMS version 3.2 or higher
* PHP 7.0 and higher
* Tested with PHP 7.0

# Installation

These instructions are for installing the plugin via Composer. You can also install via the <a href="https://plugins.craftcms.com/multisafepay" target="_blank">Craft Plugin Store</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

# Configuration

1. Sign in to your Craft Commerce <Glossary>backend</Glossary>.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.
3. To add payment methods activated in your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay account</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> and configure <Glossary>gateways</Glossary>, go to **Commerce** > **System settings** > **Gateways**.<br />


***

# User guide

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business.

Supported since release: 1.2.0, March 19th 2021.

<details id="how-to-configure-generic-gateways">
  <summary>How to configure generic gateways</summary>

  <br />

  1. Sign in to your Craft Commerce backend.
  2. Go to **Commerce** > **System settings** > **Gateways** > **+ New gateway**.
  3. From the **Gateway** list, select **Generic gateway**.
  4. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway label.
</details>

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/), **except** Postepay and V Pay
  * Banking methods: All, except Bizum.
  * <Glossary>BNPL</Glossary>: All, except Billink.
  * Wallets: [Alipay](/docs/alipay/), [PayPal](/docs/paypal/)
  * Prepaid cards:
    * Beauty and Wellness gift card
    * <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Fietsenbon
    * <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Wijncadeau
    * <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
</details>

## Refunds

<details id="refund-rules">
  <summary>Refund rules</summary>

  <br />

  | Platform               | Details                                                                                                                                                      |
  | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | MultiSafepay dashboard | - [Full and partial refunds](/docs/refund-payments/) <br /> - Generic gateway transactions                                                                   |
  | Backend                | - Full and partial refunds <br /> - You can't refund more than the original amount in your backend <br /> - Generic gateway transactions **not** supported   |
  | API                    | - [Refund order](/reference/refundorder/) <br /> - [BNPL refunds](/docs/refund-payments#bnpl-refunds) **not** supported <br /> - Discounts **not** supported |
</details>

<details id="how-to-process-backend-refunds">
  <summary>How to process backend refunds</summary>

  <br />

  To process refunds from the Craft Commerce admin panel:

  1. Go to **Commerce** > **Orders**.
  2. Select the order.
  3. To see the refund options, go to the **Transactions** tab.
</details>

<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Contact MultiSafepay:</p>

  <ul>
    <li>Telephone: <a href="tel:+310208500500">+31 (0)20 8500 500</a></li>
    <li>Email: <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></li>
    <li>GitHub: <a href="https://github.com/MultiSafepay/craft-commerce/issues/new" target="_blank"> create a technical issue</a></li>
  </ul>
</blockquote>

[Top of page](#)