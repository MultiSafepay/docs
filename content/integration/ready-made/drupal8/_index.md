---
title : "Drupal 8 & 9 plugin"
github_url : "https://github.com/MultiSafepay/drupal-commerce-2/"
download_url : "https://github.com/MultiSafepay/drupal-commerce-2/releases/download/3.0.0/commerce_multisafepay_payments-3.0.0.zip"
changelog: https://github.com/MultiSafepay/drupal-commerce-2/blob/master/CHANGELOG.md
type: 'Plugin'
layout: 'single'
meta_title: "Drupal 8 & 9 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Drupal_8.svg"
weight: 16
title_short: "Drupal 8 & 9"
description_short: "Free plugin to integrate MultiSafepay payment solutions with Drupal 8 & 9."
url: '/drupal-8-9/'
aliases: 
    - /plugins/drupal8
    - /integrations/plugins/drupal8
    - /integrations/drupal8
    - /integrations/ecommerce-integrations/drupal8
    - /payments/integrations/ecommerce-platforms/drupal8/
    - /ecommerce-platforms/drupal-8-9/
    - /integrations/drupal8/faq/refunding-drupal/
    - /payments/integrations/ecommerce-platforms/drupal8/faq/processing-refunds/
    - /drupal-8-9/refunds/
    - /payments/integrations/ecommerce-platforms/drupal8/faq/configuring-generic-gateways/
    - /drupal-8-9/configuring-generic-gateways/
    - /integrations/drupal8/faq/how-can-i-update-the-plugin-for-drupal8/
    - /payments/integrations/ecommerce-platforms/drupal8/faq/updating-the-plugin/
    - /drupal-8-9/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for Drupal 8 & 9. 

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

{{< /details >}}

{{< details title="Support" >}}

Drupal no longer provides support for Drupal 8.9.x.

For how to upgrade to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

These instructions are for Composer. You can also install the plugin in your backend. 

{{< blue-notice >}} Make sure you have a backup of your production environment, and that you test the plugin in a staging environment. {{< /blue-notice >}}

To install the latest stable version of the Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

## Configuration  
1. Sign in to your Drupal backend.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your [account ID, site ID, and site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code). 
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your [MultiSafepay dashboard](https://merchant.multisafepay.com).

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). 

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Drupal backend. 
2. Go to **Commerce** > **Configuration** > **Payments** > **Payments gateways** > **Add payment gateway** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.

Generic gateways support:

- All payment methods (filter by country, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only

**Gift cards**

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and *no* closed-loop gift cards.

**Co-branded credit cards**

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/), **except** in3
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

[Full refunds](/refunds/full-partial/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

{{< details title="Updating the plugin in your backend" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Download the plugin again above.
3. Follow the Installation instructions and the Configuration instructions from step 2.

{{< /details >}}

### Upgrading to Drupal 9

Drupal no longer provides support for Drupal 8.9.x. 

For how to upgrade Drupal 8 to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).