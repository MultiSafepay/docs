---
title : "CS-Cart plugin"
github_url : "https://github.com/MultiSafepay/CS-Cart"
download_url : "https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip"
changelog: "https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md"
meta_title: "CS-Cart plugin - MultiSafepay Docs"
type: 'Plugin'
logo: "/logo/Plugins/CS-Cart.svg"
weight: 13
title_short: "CS-Cart"
layout: 'single'
description_short: "Free plugin to integrate MultiSafepay payment solutions into your CS-Cart webshop."
url: '/cs-cart/'
aliases: 
    - /plugins/cs-cart
    - /integrations/plugins/cs-cart
    - /integrations/cs-cart
    - /integrations/ecommerce-integrations/cs-cart
    - /payments/integrations/ecommerce-platforms/cs-cart/
    - /ecommerce-platforms/cs-cart/
    - /integrations/cs-cart/faq/configure-fee-pay-after-delivery/
    - /payments/integrations/ecommerce-platforms/cs-cart/faq/applying-surcharges/
    - /cs-cart/surcharges/
    - /integrations/cs-cart/faq/refunding-cs-cart/
    - /payments/integrations/ecommerce-platforms/cs-cart/faq/processing-refunds/
    - /cs-cart/refunds/
    - /integrations/cs-cart/faq/how-can-i-update-the-plugin-for-cs-cart/
    - /payments/integrations/ecommerce-platforms/cs-cart/faq/updating-the-plugin/
    - /cs-cart/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for CS-Cart.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- CS-Cart 4.x
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

{{< blue-notice >}} Make sure you have a backup of your production environment, and that you test the plugin in a staging environment. {{< /blue-notice >}}

1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
3. Delete the `msp_installer.php` file.
4. In your [MultiSafepay account](https://merchant.multisafepay.com), provide your [webhook endpoint](/integrations/self-made/configure-your-webhook/).

## Configuration
1. Sign in to your CS-Cart backend.
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required, and click **Create**.
7. In the **Configure** tab, enter your [account ID, site ID, and site code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code). 

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.

## User guide

### Payment methods

{{< details title="Payment methods" >}}

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

{{< /details >}}

### Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backend.   Refunding more than the original amount is **not** supported in your backend.

### Surcharges

You can apply surcharges when configuring the payment method under **Surcharge**. Always enter the amount **including** VAT.

{{< alert-notice >}} **Attention Dutch merchants**  

We strongly recommend **not** applying surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). {{< /alert-notice >}}

### Updates

You can update the plugin in your CS-Cart backend or the CMS marketplace, or via SFTP.

{{< details title="Updating via SFTP" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Download the plugin again above.
3. Follow the Installation instructions from step 2 and then the Configuration instructions.

{{< /details >}}