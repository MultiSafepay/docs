---
title : "Zen Cart plugin"
github_url : "https://github.com/MultiSafepay/Zencart"
download_url : "https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip"
changelog_url : "."
meta_title: "ZenCart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Zen_Cart.svg"
weight: 20
title_short: "Zen Cart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md"
url: '/zen-cart/'
aliases: 
    - /plugins/zencart
    - /integrations/plugins/zencart
    - /integrations/zencart
    - /plugins/zencart/manual
    - /integrations/plugins/zencart/manual
    - /integrations/zencart/manual
    - /integrations/ecommerce-integrations/zencart
    - /payments/integrations/ecommerce-platforms/zencart/
    - /ecommerce-platforms/zen-cart/
    - /integrations/zencart/faq/refunding-zen-cart/
    - /payments/integrations/ecommerce-platforms/zencart/faq/processing-refunds/
    - /zencart/refunds/
    - /integrations/zencart/faq/how-can-i-update-the-plugin-for-zen-cart/
    - /payments/integrations/ecommerce-platforms/zencart/faq/updating-the-plugin/
    - /zencart/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Zen Cart.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- ZenCart 1.5.5
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the Zen Cart installation procedure. Always make a backup. {{< /blue-notice >}}

1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart backend.
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.

## User guide

### Payment methods


{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/), except iDEAL QR and TrustPay
- Pay later methods: [All](/payment-methods/pay-later/), except in3
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
    - [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

### Refunds

[Full refunds](/refunds/full-partial/) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

{{< details title="Updating via SFTP" >}}

**Note:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

{{< /details >}}