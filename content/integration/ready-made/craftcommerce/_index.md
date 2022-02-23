---
title : "MultiSafepay plugin for Craft Commerce"
title_short: "Craft Commerce"
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
faq: "."
url: '/craft-commerce/'
aliases: 
    - /plugins/craftcommerce
    - /integrations/plugins/craftcommerce
    - /integrations/craftcommerce
    - /integrations/ecommerce-integrations/craftcommerce
    - /payments/integrations/ecommerce-platforms/craftcommerce/
    - /ecommerce-platforms/craft-commerce/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Craft Commerce 3 webshop via Composer.

You can also install the plugin via the [Craft Plugin Store](https://plugins.craftcms.com/multisafepay).

{{< details title="Features" >}}
&nbsp;  
- Support for separate payment methods, pay later methods, and gift cards
- Partial and full refunds for all payment methods, except pay later
- Customizable order statuses
- Shipment notifications for pay later methods

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Maestro](/payment-methods/maestro)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires) & [Dankort](/payment-methods/dankort)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payment-methods/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

+ [AfterPay](/payment-methods/afterpay)
+ [E-Invoicing](/payment-methods/e-invoicing)
+ [in3](/payment-methods/in3)
+ [Klarna](/payment-methods/klarna)
+ [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

+ [Alipay](/payment-methods/alipay)
+ [PayPal](/payment-methods/paypal)

**Prepaid cards**

+ Beauty and Wellness gift card
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Nationale tuinbon](https://www.nationale-tuinbon.nl)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
+ [Podium](https://www.podiumcadeaukaart.nl)
+ [Sport en Fit](https://www.sportenfitcadeau.nl)
+ [VVV gift card](https://www.vvvcadeaukaarten.nl)
+ [Webshop gift card](https://www.webshopgiftcard.nl)
+ [Wellness gift card](https://www.wellnessgiftcard.nl)
+ Wijncadeau
+ [Winkelcheque](https://www.winkelcheque.nl)
+ [Yourgift](https://www.yourgift.nl/)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

## Configuration
1. Sign in to the [backend](/glossaries/multisafepay-glossary/#backend) of your Craft Commerce webshop.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure gateways, go to **Commerce** > **System settings** > **Gateways**.  
