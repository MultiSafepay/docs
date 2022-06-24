---
title: "X-Cart"
category: 62962dd7e272a6002ebbbbc5
order: 119
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with X-Cart."
slug: 'x-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/X-Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart/releases/download/2.3.0/Plugin_X-Cart_2.3.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with X-Cart.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/docs/getting-started-guide/)
- X-Cart 5.x        
- Tested on PHP 7.0

</details>

# How to install

:warning: We recommend first installing the plugin in a test environment, following the X-Cart installation procedure. Always make a backup.

1. In the root of your webshop, unzip the content of the .ZIP file.
2. Sign in to your X-Cart <<glossary:backend>>.
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

# How to configure
1. Sign in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your API key in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
9. Enter your account ID, [site ID, secure code, and API key](/docs/sites/#site-id-api-key-and-secure-code 
Make sure you enter the correct API key for the account type you want to use. 
10. Click **Save changes**.  

# User guide

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/docs/cards/)
- Banking methods: All, except Request to Pay
- Pay later methods: All, except in3
- Wallets: [Alipay](/docs/alipay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/docs/paysafecard/)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="updating-in-your-backend">
<summary>Updating in your backend</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 1.

</details>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]
