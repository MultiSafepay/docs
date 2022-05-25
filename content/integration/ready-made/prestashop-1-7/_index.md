---
title : "MultiSafepay plugin for PrestaShop 1.7"
github_url : "https://github.com/MultiSafepay/prestashop-official"
meta_title: "PrestaShop 1.7 plugin - MultiSafepay Docs"
download_url : "https://github.com/MultiSafepay/prestashop-official/releases/download/5.5.0/Plugin_PrestaShop_5.5.0.zip"
changelog_url : "."
faq: "."
logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.7"
type: 'Plugin'
layout: 'single'
layout: 'single'
changelog: https://github.com/MultiSafepay/prestashop-official/blob/main/CHANGELOG.md
url: '/prestashop-1-7/'
aliases: 
    - /plugins/prestashop-1-7
    - /integrations/plugins/prestashop-1-7
    - /integrations/prestashop-1-7
    - /plugins/prestashop-1-7/manual
    - /integrations/plugins/prestashop-1-7/manual
    - /integrations/prestashop-1-7/manual
    - /integrations/ecommerce-integrations/prestashop-1-7
    - /payments/integrations/ecommerce-platforms/prestashop-1-7/
    - /ecommerce-platforms/prestashop-1-7/
    - /prestashop/
---
This technical manual is for installing and configuring our latest free plugin for integrating MultiSafepay payment solutions into your Prestashop 1.7 webshop.

{{< alert-notice>}} If you are still using the [deprecated plugin](https://github.com/MultiSafepay/prestashop), we recommend migrating to this new version as soon as possible. {{< /alert-notice >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- PrestaShop version 1.7.6 or higher
- PHP version 7.2 or higher

If you're on PrestaShop 1.7.5 or lower, consider updating PrestaShop or use an older version (4.x) of our plugin which can be found in our [PrestaShop GitHub repository](https://github.com/MultiSafepay/prestashop/releases). 

{{< /details >}}

{{< details title="Supported versions" >}}

- 1.7.6
- 1.7.7
- 1.7.8

To use an older version of the plugin, see MultiSafepay GitHub – [PrestaShop releases](https://github.com/MultiSafepay/prestashop/releases).

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/amex)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

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

- [AfterPay](/payment-methods/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay/)
- [Google Pay](/payment-methods/google-pay/)
- [WeChat Pay](/payment-methods/wechat-pay/)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

- Baby Giftcard
- Beauty and wellness
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Degrotespeelgoedwinkel](https://www.degrotespeelgoedwinkel.nl/cadeaukaart)
- [Fashioncheque](https://www.fashioncheque.com/nl)
- [Fashion gift card](https://www.fashion-giftcard.nl)
- Fietsenbon
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
- Givacard
- [Good4fun](https://www.good4fun.nl)
- Goodcard
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

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended PrestaShop 1.7 installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Sign in to your PrestaShop 1.7 [backend](/glossaries/multisafepay-glossary/#backend).
2. Go to **Modules** > **Module Manager**.
3. Click **Upload a module**.
4. Select the Plugin_PrestaShop.zip file, and then click **Configure**.
5. Clear your cache.


## Configuration
1. Sign in to your PrestaShop 1.7 backend.
2. Go to **IMPROVE** > **MultiSafepay**.
3. Enter your [API key](/glossaries/multisafepay-glossary/#api-key). {{% account_info %}}
4. On the **Payment methods** tab, enable the relevant payment methods.
5. Click **Save**.

## Upgrading from 4.x or lower

To upgrade to version 5.x from an older version, follow these steps:

1. Go to **Modules** > **Module manager** > **MultiSafepay** > **Configure**.
2. On the **Payment methods** tab, set all payment methods to **Off**.
3. On the **Gift cards** tab, set all gift cards to **Off**.
4. Install and configure the new plugin following the instructions below.
5. Only uninstall the older plugin when you're sure that orders created with the new plugin are being processed successfully. 

If upgrading from 5.x to a newer version, see [Updating the plugin](/prestashop-1-7/updates).
