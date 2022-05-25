---
title : "Craft Commerce plugin"
title_short: "Craft Commerce plugin"
meta_title: "Craft Commerce plugin - MultiSafepay Docs"
github_url : "https://github.com/MultiSafepay/craft-commerce"
type: 'Plugin'
changelog_url : "."
logo: "/logo/Integrations/Craft_Commerce.svg"
weight: 21
title_short: "Craft Commerce"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Craft Commerce webshop."
changelog: https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md
layout: 'single'
url: '/craft-commerce/'
aliases: 
    - /plugins/craftcommerce
    - /integrations/plugins/craftcommerce
    - /integrations/craftcommerce
    - /integrations/ecommerce-integrations/craftcommerce
    - /payments/integrations/ecommerce-platforms/craftcommerce/
    - /ecommerce-platforms/craft-commerce/
    - /payments/integrations/ecommerce-platforms/craftcommerce/faq/generic-gateways/
    - /ecommerce-platforms/craft-commerce/generic-gateways/
    - /craft-commerce/configuring-generic-gateways/
    - /integrations/ecommerce-integrations/craftcommerce/faq/refunding-craft-commerce/
    - /payments/integrations/ecommerce-platforms/craftcommerce/faq/processing-refunds/
    - /craft-commerce/refunds/
    - /integrations/ecommerce-integrations/craftcommerce/faq/craft-commerce-2-support/
    - /payments/integrations/ecommerce-platforms/craftcommerce/faq/support-for-craft-commerce-2/
    - /craft-commerce/craft-commerce-2/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for Craft Commerce 3.

### Features
 
- Support for separate payment methods, pay later methods, and gift cards
- Partial and full refunds for all payment methods, except pay later
- Customizable order statuses
- Shipment notifications for pay later methods 

{{< details title="Requirements" >}}
 
- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

{{< /details >}}

{{< details title="Support" >}}

For support for Craft Commerce 2, email <integration@multisafepay.com> 
 
Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

These instructions are for installing the plugin via Composer. You can also install via the [Craft Plugin Store](https://plugins.craftcms.com/multisafepay).

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

## Configuration
1. Sign in to your Craft Commerce backend.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure gateways, go to **Commerce** > **System settings** > **Gateways**.  

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Craft Commerce backend. 
2. Go to **Commerce** > **System settings** > **Gateways** > **+ New gateway**.
3. From the **Gateway** list, select **Generic gateway**.
4. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.

{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/), **except** Postepay and V Pay
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/)
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

| | |
|---|---|
| MultiSafepay dashboard | - [Full and partial refunds](/refunds/full-partial/) <br> - Generic gateway transactions |
| Backend | - Full and partial refunds <br> - You can't refund more than the original amount in your backend <br> - Generic gateway transactions **not** supported |
| API | - [Refund order](https://docs-api.multisafepay.com/reference/refundorder) <br> - [Pay later refunds](/payment-methods/pay-later) **not** supported <br> - Discounts **not** supported |

{{< details title="Processing backend refunds" >}}

To process refunds from the Craft Commerce admin panel:  

1. Go to **Commerce** > **Orders**.
2. Select the order.
3. To see the refund options, go to the **Transactions** tab. 

{{< /details >}}