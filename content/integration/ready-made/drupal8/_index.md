---
title : "MultiSafepay plugin for Drupal 8 and 9"
github_url : "https://github.com/MultiSafepay/drupal-commerce-2/"
download_url : "https://github.com/MultiSafepay/drupal-commerce-2/releases/download/3.0.0/commerce_multisafepay_payments-3.0.0.zip"
changelog: https://github.com/MultiSafepay/drupal-commerce-2/blob/master/CHANGELOG.md
faq: "."
type: 'Plugin'
layout: 'single'
meta_title: "Drupal 8 & 9 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Drupal_8.svg"
weight: 16
title_short: "Drupal 8 & 9"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Drupal 8 webshop."
url: '/drupal-8-9/'
aliases: 
    - /plugins/drupal8
    - /integrations/plugins/drupal8
    - /integrations/drupal8
    - /integrations/ecommerce-integrations/drupal8
    - /payments/integrations/ecommerce-platforms/drupal8/
    - /ecommerce-platforms/drupal-8-9/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Drupal 8 webshop via Composer.

You can also install the plugin via your Drupal 8 & 9 [backend](/glossaries/multisafepay-glossary/#backend). 

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Versions" >}}
&nbsp;  
Drupal no longer provides security updates for Drupal 8.9.x, and will only provide bugfix support until early 2021 and security fixes until November 2021. 

For more information about upgrading from Drupal 8 to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
- MultiSafepay account – See [Getting started](/getting-started/).
- Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Maestro](/payment-methods/maestro)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payments/methods/credit-and-debit-cards/dankort), and [V Pay](/payment-methods/vpay)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

- [AfterPay](/payments/methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payments/methods/wallet/applepay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

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

## Installation
To install the latest stable version of our Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

The latest stable release is downloaded and installed in your Drupal Commerce 2.x webshop.

## Configuration  
1. Sign in to the [backend](/glossaries/multisafepay-glossary/#backend) of your webshop.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your account ID, site ID, site code or API key. {{% account_info %}}
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com).

