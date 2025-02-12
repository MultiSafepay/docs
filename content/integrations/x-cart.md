---
title: "X-Cart"
category: 62962dd7e272a6002ebbbbc5
order: 23
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'x-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/X-Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart/releases/download/2.3.0/Plugin_X-Cart_2.3.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/X-Cart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- X-Cart 5.x        
- Tested on PHP 7.0

# Installation

✅ &nbsp; **Tip!** We recommend first installing the plugin in a test environment, following the X-Cart installation procedure. Always make a backup.

1. In the root of your webshop, unzip the content of the .ZIP file.
2. Sign in to your X-Cart <<glossary:backend>>.
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

# Configuration

1. Sign in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your API key in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
9. Enter your account ID, [website ID, security code, and API key](/docs/sites/#site-id-api-key-and-security-code). 
Make sure you enter the correct API key for the account type you want to use. 
10. Click **Save changes**.  
<br>

---

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All, except Request to Pay
- <<glossary:BNPL>>: All, except in3
- Wallets: [Alipay](/docs/alipay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - [Paysafecard](/docs/paysafecard/)
    - <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Wijncadeau
    - <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

## Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

✅ &nbsp; **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 1.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/X-Cart/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)