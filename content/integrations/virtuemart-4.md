---
title: VirtueMart 4
category:
  uri: Integrations
slug: virtuemart-4
position: 15
privacy:
  view: public
parent:
  uri: our-integrations
content:
  excerpt: Technical manual for MultiSafepay's free plugin.
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/VirtueMart.svg" width="50" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<div style={{display: 'flex', flexWrap: 'wrap'}}>
  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#006ba1', color: '#ffffff', textDecoration: 'none'}} href="https://github.com/MultiSafepay/virtuemart-4/releases/download/2.0.2/Plugin_VirtueMart-4_2.0.2.zip" target="_self"><span>Download</span><i className="icon icon-download" style={{marginLeft: '0.6em'}}> </i></a>

  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/virtuemart-4" target="_blank"><i className="icon-external-link" /> <span>Source code</span></a>

  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/virtuemart-4/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>
</div>

# Prerequisites

* [MultiSafepay account](/docs/getting-started-guide/)
* Joomla 4.x and VirtueMart 4.x
* Tested on PHP 8.1

# Installation

  **💡 Tip!** We recommend first installing the plugin in a test environment, following the VirtueMart installation procedure. Always make a backup.

1. Sign in to your VirtueMart <Glossary>backend</Glossary>.
2. Go to **System** > **Install** > **Extensions**.
3. Install the Plugin\_VirtueMart-4\_x.x.x.zip file using **Drag and drop** or **Browse for file**.
4. Click **Upload & install**.

# Configuration

1. Sign in to your VirtueMart backend.
2. Go to **System** > **Manage** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**.
5. Click **Payment methods**.
6. To install and configure each payment method separately:
   * Click **New**.
   * Set the payment method to **VirtueMart Payment - MultiSafepay**.
   * To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
   * **Account ID** (top-right corner of your dashboard)
   * [Website ID, API key, and security code](/docs/sites#website-id-api-key-and-security-code)
   * [Gateway ID](/reference/gateway-ids/)

<br />

***

# User guide

## Checkouts

If a customer selects Apple Pay at checkout but isn't on an Apple device, they receive a notification to select another payment method.

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/)
  * Banking methods: All
  * Wallets: All
  * Prepaid cards:
    * Beauty and Wellness gift card
    * <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Edenred](/docs/edenred/)
    * <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Fietsenbon
    * <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Paysafecard](/docs/paysafecard/)
    * <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Postepay](/docs/card-payments/)
    * <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Sodexo](/docs/sodexo/)
    * <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Wijncadeau
    * <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in both MultiSafepay and VirtueMart dashboards.\
You cannot refund more than the original amount in your dashboard.

## Shipping orders

When you ship <Glossary>BNPL</Glossary> orders, you need to change the <Glossary>order status</Glossary> from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing.

## Updates

You can update the plugin in your backend as described below:

  **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Contact MultiSafepay:</p>

  <ul>
    <li>Telephone: <a href="tel:+310208500500">+31 (0)20 8500 500</a></li>
    <li>Email: <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></li>
    <li>GitHub: <a href="https://github.com/MultiSafepay/virtuemart-4/issues" target="_blank"> create a technical issue</a></li>
  </ul>
</blockquote>

[Top of page](#)