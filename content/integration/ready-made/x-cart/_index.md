---
title : "X-Cart plugin"
github_url : "https://github.com/MultiSafepay/X-Cart"
download_url : "https://github.com/MultiSafepay/X-Cart/releases/download/2.3.0/Plugin_X-Cart_2.3.0.zip"
changelog_url : "."
meta_title: "X-Cart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/X-Cart.svg"
weight: 14
title_short: "X-Cart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/X-Cart/blob/master/CHANGELOG.md"
url: '/x-cart/'
aliases:
    - /integrations/x-cart/
    - /plugins/x-cart
    - /integrations/plugins/x-cart
    - /integrations/x-cart
    - /plugins/x-cart/manual
    - /integrations/plugins/x-cart/manual
    - /integrations/x-cart/manual
    - /integrations/ecommerce-integrations/x-cart
    - /payments/integrations/ecommerce-platforms/x-cart/
    - /ecommerce-platforms/x-cart/
    - /integrations/x-cart/faq/refunding-x-cart/
    - /payments/integrations/ecommerce-platforms/x-cart/faq/processing-refunds/
    - /x-cart/refunds/
    - /integrations/x-cart/faq/how-can-i-update-the-plugin-for-x-cart/
    - /payments/integrations/ecommerce-platforms/x-cart/faq/updating-the-plugin/
    - /x-cart/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with X-Cart.

{{< details title="Requirements" >}}
&nbsp;  
- [MultiSafepay account](/getting-started/guide/)
- X-Cart 5.x        
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

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the X-Cart installation procedure. Always make a backup. {{< /blue-notice >}}

1. In the root of your webshop, unzip the content of the .ZIP file.
2. Sign in to your X-Cart backend.
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

## Configuration
1. Sign in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your API key in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
9. Enter your account ID, [site ID, secure code, and API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).  
Make sure you enter the correct API key for the account type you want to use. 
10. Click **Save changes**.  

## User guide

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/cards/)
- Banking methods: [All](/payment-methods/banks/), except Request to Pay
- Pay later methods: [All](/payment-methods/pay-later/), except in3
- Wallets: [Alipay](/payment-methods/alipay), [PayPal](/payment-methods/paypal)
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

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

### Refunds

[Full refunds](/refunds/full-partial/) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

{{< details title="Updating in your backend" >}}
**Note:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 1.

{{< /details >}}