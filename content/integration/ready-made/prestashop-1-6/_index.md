---
title : "PrestaShop 1.6 plugin"
download_url : "https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/prestashop-1-6/Plugin_PrestaShop1.6_3.7.1.zip"
changelog_url : "/integration/ready-made/prestashop-1-6/changelog/"
changelog: https://docs.multisafepay.com/integration/ready-made/prestashop-1-6/changelog/
meta_title: "PrestaShop 1.6 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.6"
type: 'Plugin'
layout: 'single'
url: '/prestashop-1-6/'
aliases: 
    - /plugins/prestashop-1-6
    - /integrations/plugins/prestashop-1-6
    - /integrations/prestashop-1-6
    - /plugins/prestashop-1-6/manual
    - /integrations/plugins/prestashop-1-6/manual
    - /integrations/prestashop-1-6/manual
    - /integrations/ecommerce-integrations/prestashop-1-6
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/
    - /ecommerce-platforms/prestashop-1-6/
    - /integrations/prestashop-1-6/faq/payment-fee-surcharges/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/applying-surcharges/
    - /prestashop-1-6/surcharges/
    - /integrations/prestashop-1-6/faq/tokenization-prestashop16/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/enabling-tokenization/
    - /prestashop-1-6/recurring-payments/
    - /integrations/ecommerce-integrations/prestashop-1-6/faq/order-ids-not-matching/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/matching-orders/
    - /prestashop-1-6/matching-orders/
    - /integrations/prestashop-1-6/faq/refunding-prestashop/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/processing-refunds/
    - /prestashop-1-6/refunds/
    - /integrations/prestashop-1-6/faq/extra-confirmation-page/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/skipping-extra-confirmation-page/
    - /prestashop-1-6/skipping-confirmation-page/
    - /integrations/prestashop-1-6/faq/do-you-support-thirty-bees/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/support-for-thirty-bees/
    - /prestashop-1-6/thirty-bees/
    - /integrations/prestashop-1-6/faq/how-can-i-update-the-plugin-for-prestashop-1-6/
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/faq/updating-the-plugin/
    - /prestashop-1-6/updates/
---

{{< alert-notice >}} We are phasing out support for this plugin. We recommend migrating to our [Prestashop 1.7 plugin](/prestashop-1-7/) as soon as possible. {{< /alert-notice >}}

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Prestashop 1.6.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- PrestaShop 1.6
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the PrestaShop 1.6 installation procedure. Always make a backup. {{< /blue-notice >}}

1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directoy, merging the two folders.
2. Sign in to your PrestaShop 1.6 backend.
3. Go to **Modules and services** > **Payments and gateways**.  
    **Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code), and then click **Save**.
6. On the **Payments** tab, enable the relevant payment methods.

## User guide

### Confirmation page

{{< details title="Skipping the confirmation page" >}}

PrestaShop 1.6 version 3.1.7 lets you skip the extra confirmation page so that the customer is redirected straight to the MultiSafepay payment page.

This is no longer supported from version 3.2.0. If you want to skip the extra confirmation page, you can [download version 3.1.7](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/prestashop-1-6/Plugin_PrestaShop1.6_3.7.1.zip). New features might be lost when downgrading.

{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Pay later methods: [All](/payment-methods/pay-later/), except Betaal per Maand
- Wallets: [Alipay](/payment-methods/alipay/), [Apple Pay](/payment-methods/apple-pay/), [PayPal](/payment-methods/paypal/)
- Banking methods: 
    - [Bancontact](/payment-methods/bancontact/)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [Belfius](/payment-methods/belfius/)
    - [CBC/KBC](/payment-methods/cbc-kbc/)
    - [Dotpay](/payment-methods/dotpay/)
    - [EPS](/payment-methods/eps/)
    - [Giropay](/payment-methods/giropay/)
    - [iDEAL](/payment-methods/ideal/)
    - [Request to Pay](/payment-methods/request-to-pay/)
    - [SEPA Direct Debit](/payment-methods/sepa-direct-debit/)
    - [Sofort](/payment-methods/sofort/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - Boekenbon
    - Degrotespeelgoedwinkel
    - Fashioncheque
    - Fashion gift card
    - Fietsenbon
    - Gezondheidsbon
    - Good4fun
    - Parfumcadeaukaart
    - Paysafecard
    - Sport en Fit
    - VVV gift card
    - Webshop gift card
    - Wijncadeau
    - Yourgift

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

### Matching orders

In Prestashop 1.6, the order ID is generated after the payment, which causes a mismatch with the order ID in your MultiSafepay dashboard. You can match orders using the transaction ID. 

{{< details title="Viewing transaction IDs" >}}

1. Sign in to your Prestashop 1.6 backend.
2. Go to **Payment** > **Order details**. 

{{< /details >}}

### Payment links

Payment links generated manually in your MultiSafepay dashboard don't automatically create or update orders in your PrestaShop 1.6 backend.

### Recurring payments

{{< details title="Enabling recurring payments" >}}

To enable [recurring payments](/features/recurring-payments), follow these steps:

1. Sign in to your PrestaShop 1.6 backend. 
2. Go to **Modules and services** > **Modules and services** > **MultiSafepay**.
3. Click **Configure**.
4. Set the **Tokenization** field to **YES**.
5. Click **Save**.

{{< /details >}}

### Refunds

You can process [full and partial refunds](/refunds/full-partial/) from your MultiSafepay dashboard.  
Backend refunds are **not** supported.

### Surcharges

[Surcharges](/surcharges/) are not supported by default.

{{< details title="Applying surcharges with BVK">}}  
To apply a surcharge or payment fee to a payment method, you can use the third-party [BVK](https://www.bvkyazilim.com/cart/prestashop-modules) package.

The Integration Team will do their best to support you with installing BVK, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

**Attention Dutch merchants** 

 We strongly recommend **not** applying surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). 

{{< /details >}}

### Thirty Bees

For support for the Prestashop [Thirty Bees](https://thirtybees.com/blog/what-is-thirty-bees) fork, email <integration@multisafepay.com>

### Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

{{< details title="Updating via SFTP" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Download the plugin again above.
3. Follow the Installation and configuration instructions from step 2.

{{< /details >}}
