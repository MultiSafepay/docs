---
title : "MultiSafepay plugin for Craft Commerce"
title_short: "Craft Commerce"
meta_title: "Craft Commerce plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
github_url : "https://github.com/MultiSafepay/craft-commerce"
changelog_url : "."
logo: "/logo/Integrations/Craft_Commerce.svg"
weight: 21
title_short: "Craft Commerce"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Craft Commerce webshop"
changelog: https://github.com/MultiSafepay/craft-commerce/blob/master/CHANGELOG.md
layout: 'single'
faq: "."
url: '/ecommerce-platforms/craft-commerce/'
aliases: 
    - /plugins/craftcommerce
    - /integrations/plugins/craftcommerce
    - /integrations/craftcommerce
    - /integrations/ecommerce-integrations/craftcommerce
    - /payments/integrations/ecommerce-platforms/craftcommerce/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Craft Commerce 3 webshop via Composer.

You can also install the plugin via the [Craft Plugin Store](https://plugins.craftcms.com/multisafepay).

{{< details title="Features" >}}
&nbsp;  
- Support for separate payment methods, billing suites, and gift cards
- Partial and full refunds for non-billing suite payment methods
- Customizable order statuses
- Shipment notifications for billing suite payment methods

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

**Credit cards**

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) & [Dankort](/payments/methods/credit-and-debit-cards/dankort)

**Banking methods**

- [Bancontact](/payments/methods/banks/bancontact)
- [Bank transfer](/payments/methods/banks/bank-transfer)
- [Belfius](/payments/methods/banks/belfius)
- [Dotpay](/payments/methods/banks/dotpay)
- [EPS](/payments/methods/banks/eps)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)
- [TrustPay](/payments/methods/banks/trustpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [in3](https://docs.multisafepay.com/payment-methods/billing-suite/in3)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
+ [PayPal](/payments/methods/wallet/paypal)

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

{{< /details >}}

## Installation

Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

## Configuration
1. Sign in to the [backend](/getting-started/glossary/#backend) of your Craft Commerce webshop.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure gateways, go to **Commerce** > **System settings** > **Gateways**.  