---
title: "Drupal 7 plugin"
github_url: "https://github.com/MultiSafepay/Drupal-Commerce"
download_url: "https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip"
changelog: https://github.com/MultiSafepay/Drupal-Commerce/blob/master/CHANGELOG.md
type: 'Plugin'
meta_title: "Drupal 7 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Drupal_7.svg"
weight: 15
title_short: "Drupal 7"
description_short: "Free plugin to integrate MultiSafepay payment solutions with Drupal 7."
layout: 'single'
url: '/drupal-7/'
aliases: 
    - /plugins/drupal7
    - /integrations/plugins/drupal7
    - /integrations/drupal7
    - /integrations/ecommerce-integrations/drupal7
    - /payments/integrations/ecommerce-platforms/drupal7/
    - /ecommerce-platforms/drupal-7/
    - /integrations/drupal7/faq/refunding-drupal/
    - /payments/integrations/ecommerce-platforms/drupal7/faq/processing-refunds/
    - /drupal-7/refunds/
    - /integrations/drupal7/faq/how-can-i-update-the-plugin-for-drupal7/
    - /payments/integrations/ecommerce-platforms/drupal7/faq/updating-the-plugin/
    - /drupal-7/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for Drupal 7.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Drupal 7.x
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} Make sure you have a backup of your production environment, and that you test the plugin in a staging environment. {{< /blue-notice >}}

1. Unpack the content of the .ZIP file in the root of your Drupal 7 webshop.
2. Sign in to your Drupal 7 backend.
3. Go to **Site settings** > **Modules**. 
4. Enable the Commerce MultiSafepay JSON module, and your selected payment method modules. 
5. Click **Save configuration**.
6. Go to **Store settings** > **Advanced store settings** > **Payment methods**.
7. **Enable** the `multisafepay` core module.
8. **Enable** the modules for each payment method.
9. To configure each payment method, under **Actions**, click the **Edit** button.
10. When the main module is installed, two rules are created but disabled by default:  
    - MultiSafepay order paid in full: Order state to `processing`  
This rule sets the order to `processing` when the order is paid in full.  

    - MultiSafepay order complete: Shipped at MultiSafepay  
This rule updates the [transaction status](/about-payments/multisafepay-statuses/) to **Shipped** at MultiSafepay. For Pay After Delivery, Klarna, and E-Invoicing, this triggers the invoicing process.

## User guide

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/), **except** iDEAL QR and Trustly
- Pay later methods: [E-Invoicing](/payment-methods/e-invoicing), [Klarna](/payment-methods/klarna), [Pay After Delivery](/payment-methods/pay-after-delivery)
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/applepay), [PayPal](/payment-methods/paypal)
- Prepaid cards: 
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payment-methods/paysafecard)
    - Wijn cadeau
    - [Yourgift](https://www.yourgift.nl)

{{< /details >}}

### Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and backed.  
Refunding more than the original amount is **not** supported in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

{{< details title="Updating via SFTP" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Download the plugin again above.
3. Follow the Installation and configuration instructions from step 2.

{{< /details >}}