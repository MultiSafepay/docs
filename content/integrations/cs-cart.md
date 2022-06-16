---
title : "CS-Cart plugin"
category: 62962dd7e272a6002ebbbbc5
order: 109
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions into your CS-Cart webshop."
slug: 'cs-cart'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/CS-Cart.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [Changelog](https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md) :link:

> [View source code](https://github.com/MultiSafepay/CS-Cart) :link:

> [Download](https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's free plugin for CS-Cart.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- CS-Cart 4.x
- Tested on PHP 7.0

</details>

<details id="support">
<summary>Support</summary>
<br>

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

</details>

# Installation

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
3. Delete the `msp_installer.php` file.
4. In your [MultiSafepay account](https://merchant.multisafepay.com), provide your [webhook endpoint](/integrations/self-made/configure-your-webhook/).

# Configuration
1. Sign in to your CS-Cart backend.
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required, and click **Create**.
7. In the **Configure** tab, enter your [account ID, site ID, and site code](/websites/#site-id-api-key-and-secure-code). 

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.

# User guide

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/) except in3
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payment-methods/paysafecard)
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

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backend.   Refunding more than the original amount is **not** supported in your backend.

## Surcharges

You can apply surcharges when configuring the payment method under **Surcharge**. Always enter the amount **including** VAT.

**Attention Dutch merchants**  

We strongly recommend **not** applying surcharges to [pay later methods](/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

You can update the plugin in your CS-Cart backend or the CMS marketplace, or via SFTP.

<details id="updating-via-sftp">
<summary>Updating via SFTP</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation instructions from step 2 and then the Configuration instructions.

</details>