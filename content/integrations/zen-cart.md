---
title: Zen Cart
category:
  uri: Integrations
slug: zen-cart
position: 6
privacy:
  view: public
content:
  excerpt: Technical manual for MultiSafepay's free plugin.
---
> ❗️ Important:
>
> This plugin is at end-of-life. It may contain security vulnerabilities, compatibility issues, and lack the latest features. MultiSafepay provides no support for these plugins.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Zen_Cart.svg" width="50" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<div style={{display: 'flex', flexWrap: 'wrap'}}>
  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#006ba1', color: '#ffffff', textDecoration: 'none'}} href="https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style={{marginLeft: '0.6em'}}> </i></a>

  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/Zencart" target="_blank"><i class="icon-external-link" /> <span>Source code</span></a>

  <a class="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>
</div>

# Prerequisites

* [MultiSafepay account](/docs/getting-started-guide/)
* ZenCart 1.5.5
* Tested on PHP 7.0

# Installation and configuration

  **💡 Tip!** We recommend first installing the plugin in a test environment, following the Zen Cart installation procedure. Always make a backup.

1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart <Glossary>backend</Glossary>.
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/docs/sites#site-id-api-key-and-security-code).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.\ <br />

***

# User guide

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/)
  * Banking methods: All, except iDEAL QR, TrustPay, and Bizum.
  * <Glossary>BNPL</Glossary>: All, except in3 and Billink.
  * Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
  * Prepaid cards:
    * Beauty and Wellness gift card
    * <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Fietsenbon
    * <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Paysafecard](/docs/paysafecard/)
    * <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Wijncadeau
    * <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.\
You cannot refund more than the original amount in your backend.

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
    <li>GitHub: <a href="https://github.com/MultiSafepay/Zencart/issues" target="_blank"> create a technical issue</a></li>
  </ul>
</blockquote>

[Top of page](#)
