---
title: "CS-Cart"
category: 62962dd7e272a6002ebbbbc5
order: 109
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for installing and configuring MultiSafepay's free plugin for CS-Cart."
slug: 'cs-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/CS-Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/CS-Cart" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- CS-Cart 4.x
- Tested on PHP 7.0

# How to install

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
3. Delete the `msp_installer.php` file.
4. In your [MultiSafepay account](https://merchant.multisafepay.com), provide your [webhook endpoint](/docs/configure-your-webhook/).

# How to configure

1. Sign in to your CS-Cart <<glossary:backend>>.
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required, and click **Create**.
7. In the **Configure** tab, enter your [account ID, site ID, and site code](/docs/sites#site-id-api-key-and-security-code). 

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.
<br>

---

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/cards/)
- Banking methods: All
- Pay later methods: All, except in3
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
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
    - [Yourgift](https://www.yourgift.nl)

</details>

## Refunds

[Full refunds](/docs/refund-payments/) are supported in your MultiSafepay dashboard and backend.   Refunding more than the original amount is **not** supported in your backend.

## Surcharges

You can apply surcharges when configuring the payment method under **Surcharge**. Always enter the amount **including** VAT.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to pay later methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

You can update the plugin in your CS-Cart backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
<summary>How to update via SFTP</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation instructions from step 2 and then the Configuration instructions.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]
